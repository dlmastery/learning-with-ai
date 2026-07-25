#!/usr/bin/env bash
# Hardened DGX Spark headless Sunshine configuration.
#
# Derived from eelbaz/dgx-spark-headless-sunshine, with three changes:
#   1. Every file this script touches is backed up unconditionally, timestamped,
#      before modification — including files the upstream script overwrote blind.
#   2. Passwordless autologin is OFF by default and must be opted into with
#      --enable-autologin. Upstream enables it silently.
#   3. A matching rollback.sh is generated in the backup directory that restores
#      the exact prior state of every file, and regenerates GRUB.
#
# Also: the Sunshine release is resolvable/pinnable rather than "whatever the
# GitHub API returns first" (upstream's `head -1` can select a pre-release).
#
# Usage:
#   sudo ./configure_headless_sunshine_hardened.sh [options]
#
# Run with --dry-run first. It prints every change without touching the system.

set -euo pipefail

# ------------------------------------------------------------------ defaults
ENABLE_AUTOLOGIN=0
DRY_RUN=0
SKIP_SUNSHINE=0
SKIP_GRUB=0
SKIP_XORG=0
SKIP_GDM=0
SKIP_AUTOSTART=0
SUNSHINE_TAG=""
ALLOW_PRERELEASE=0

TS="$(date +%Y%m%d-%H%M%S)"
BACKUP_DIR="/var/backups/dgx-sunshine-${TS}"

GRUB_FILE="/etc/default/grub"
XORG_FILE="/etc/X11/xorg.conf"
GDM_FILE="/etc/gdm3/custom.conf"

usage() {
    cat <<'EOF'
Usage: sudo ./configure_headless_sunshine_hardened.sh [options]

Options:
  --enable-autologin      Enable passwordless GDM autologin for the target user.
                          OFF by default. Without this, you log in normally at
                          the GDM greeter and Sunshine starts with your session.
  --dry-run               Print every action; change nothing.
  --sunshine-tag <tag>    Pin a specific Sunshine release tag.
  --allow-prerelease      Permit a pre-release when auto-resolving the tag.
  --skip-sunshine         Do not install the Sunshine package.
  --skip-grub             Do not modify /etc/default/grub.
  --skip-xorg             Do not write /etc/X11/xorg.conf.
  --skip-gdm              Do not modify /etc/gdm3/custom.conf.
  --skip-autostart        Do not install the GNOME autostart entry.
  --backup-dir <path>     Override the backup directory.
  -h, --help              This message.

Environment:
  TARGET_USER   Non-root user to configure. Defaults to $SUDO_USER.

Every modified file is backed up to /var/backups/dgx-sunshine-<timestamp>/ and a
rollback.sh is written there. To undo everything: sudo <backup-dir>/rollback.sh
EOF
}

while [ "$#" -gt 0 ]; do
    case "$1" in
        --enable-autologin) ENABLE_AUTOLOGIN=1; shift ;;
        --dry-run)          DRY_RUN=1; shift ;;
        --sunshine-tag)     SUNSHINE_TAG="${2:?missing tag}"; shift 2 ;;
        --allow-prerelease) ALLOW_PRERELEASE=1; shift ;;
        --skip-sunshine)    SKIP_SUNSHINE=1; shift ;;
        --skip-grub)        SKIP_GRUB=1; shift ;;
        --skip-xorg)        SKIP_XORG=1; shift ;;
        --skip-gdm)         SKIP_GDM=1; shift ;;
        --skip-autostart)   SKIP_AUTOSTART=1; shift ;;
        --backup-dir)       BACKUP_DIR="${2:?missing path}"; shift 2 ;;
        -h|--help)          usage; exit 0 ;;
        *) echo "[ERROR] Unknown argument: $1" >&2; usage; exit 1 ;;
    esac
done

say()  { printf '  %s\n' "$*"; }
step() { printf '\n==> %s\n' "$*"; }
run()  {
    if [ "$DRY_RUN" -eq 1 ]; then
        printf '  [dry-run] %s\n' "$*"
    else
        eval "$@"
    fi
}

require_root() {
    if [ "${EUID}" -ne 0 ]; then
        echo "[ERROR] Must run as root: sudo $0" >&2
        exit 1
    fi
}

determine_target_user() {
    local user="${TARGET_USER:-${SUDO_USER:-}}"
    if [ -z "$user" ]; then
        echo "[ERROR] Cannot determine the non-root user. Set TARGET_USER=username." >&2
        exit 1
    fi
    id "$user" >/dev/null 2>&1 || { echo "[ERROR] No such user: $user" >&2; exit 1; }
    TARGET_USER="$user"
    TARGET_HOME="$(getent passwd "$TARGET_USER" | cut -d: -f6)"
    TARGET_UID="$(id -u "$TARGET_USER")"
    [ -n "$TARGET_HOME" ] || { echo "[ERROR] No home directory for $TARGET_USER" >&2; exit 1; }
}

preflight() {
    step "Preflight"
    local model="unknown"
    [ -f /sys/devices/virtual/dmi/id/product_name ] && model="$(cat /sys/devices/virtual/dmi/id/product_name)"
    say "System:      $model"
    say "OS:          $(. /etc/os-release && echo "$PRETTY_NAME")"
    say "Arch:        $(uname -m)"
    say "Target user: $TARGET_USER (uid $TARGET_UID, home $TARGET_HOME)"
    say "Autologin:   $([ "$ENABLE_AUTOLOGIN" -eq 1 ] && echo 'ENABLED (--enable-autologin)' || echo 'disabled (default)')"
    say "Backups:     $BACKUP_DIR"

    case "$model" in
        *DGX*Spark*) ;;
        *) echo "[WARN] This does not look like a DGX Spark. The Xorg config hardcodes NVIDIA GB10." >&2 ;;
    esac
    if [ "$(uname -m)" != "aarch64" ]; then
        echo "[WARN] Expected aarch64; the Sunshine .deb is arm64-only." >&2
    fi
}

# Back up a file unconditionally, recording it for rollback. Records absent
# files too, so rollback can delete something this script created.
backup_file() {
    local f="$1"
    if [ "$DRY_RUN" -eq 1 ]; then
        printf '  [dry-run] backup %s\n' "$f"
        return 0
    fi
    mkdir -p "$BACKUP_DIR/files"
    if [ -f "$f" ]; then
        local dest="$BACKUP_DIR/files/$(echo "$f" | sed 's|/|_|g')"
        cp -a "$f" "$dest"
        printf '%s\t%s\tEXISTED\n' "$f" "$dest" >> "$BACKUP_DIR/manifest.tsv"
        say "backed up $f"
    else
        printf '%s\t-\tABSENT\n' "$f" >> "$BACKUP_DIR/manifest.tsv"
        say "recorded $f as absent (rollback will remove it)"
    fi
}

resolve_sunshine_tag() {
    if [ -n "$SUNSHINE_TAG" ]; then
        echo "$SUNSHINE_TAG"
        return 0
    fi
    local api tag
    if [ "$ALLOW_PRERELEASE" -eq 1 ]; then
        api="https://api.github.com/repos/LizardByte/Sunshine/releases"
        tag="$(curl -fsSL --max-time 30 "$api" 2>/dev/null | grep '"tag_name"' | head -1 | cut -d'"' -f4 || true)"
    else
        api="https://api.github.com/repos/LizardByte/Sunshine/releases/latest"
        tag="$(curl -fsSL --max-time 30 "$api" 2>/dev/null | grep '"tag_name"' | head -1 | cut -d'"' -f4 || true)"
    fi
    if [ -z "$tag" ]; then
        echo "[ERROR] Could not resolve a Sunshine release tag. GitHub's API rate limit is 60 req/hr unauthenticated." >&2
        echo "[ERROR] Re-run with --sunshine-tag <tag>, e.g. --sunshine-tag v2025.1014.193231" >&2
        exit 1
    fi
    echo "$tag"
}

install_sunshine() {
    step "Sunshine package"
    if command -v sunshine >/dev/null 2>&1; then
        say "already installed: $(sunshine --version 2>/dev/null || echo 'version unknown')"
        return 0
    fi

    local tag deb url
    tag="$(resolve_sunshine_tag)"
    deb="/tmp/sunshine-ubuntu-24.04-arm64-${tag}.deb"
    url="https://github.com/LizardByte/Sunshine/releases/download/${tag}/sunshine-ubuntu-24.04-arm64.deb"
    say "release: $tag"
    say "url:     $url"

    run "wget -q --show-progress -O '$deb' '$url'"
    run "apt-get update -qq"
    run "apt-get install -y -qq \
        libavcodec-dev libavformat-dev libavutil-dev libswscale-dev \
        libevdev-dev libpulse-dev libopus-dev libxtst-dev libx11-dev \
        libxrandr-dev libxfixes-dev libxcb1-dev libxcb-shm0-dev \
        libxcb-xfixes0-dev libdrm-dev libcap-dev libudev-dev \
        libwayland-dev libinput-dev libcurl4-openssl-dev libssl-dev || true"
    run "dpkg -i '$deb' || apt-get --fix-broken install -y -qq"
    run "rm -f '$deb'"

    if [ "$DRY_RUN" -eq 0 ]; then
        if command -v sunshine >/dev/null 2>&1; then
            say "installed: $(sunshine --version 2>/dev/null || echo ok)"
        else
            echo "[WARN] Sunshine does not appear on PATH after install." >&2
        fi
    fi
}

update_grub_cmdline() {
    step "GRUB kernel command line"
    [ -f "$GRUB_FILE" ] || { echo "[ERROR] $GRUB_FILE not found" >&2; exit 1; }
    backup_file "$GRUB_FILE"

    if [ "$DRY_RUN" -eq 1 ]; then
        say "[dry-run] would append nvidia-drm.modeset=1 nvidia.NVreg_UsePageAttributeTable=1"
        say "[dry-run] would run update-grub"
        return 0
    fi

    python3 - <<'PY'
import re, shlex
from pathlib import Path

p = Path("/etc/default/grub")
text = p.read_text()
m = re.search(r'^GRUB_CMDLINE_LINUX_DEFAULT="([^"]*)"', text, re.MULTILINE)
if not m:
    raise SystemExit("Unable to find GRUB_CMDLINE_LINUX_DEFAULT in /etc/default/grub")

existing = shlex.split(m.group(1))
added = []
for flag in ("nvidia-drm.modeset=1", "nvidia.NVreg_UsePageAttributeTable=1"):
    if flag not in existing:
        existing.append(flag)
        added.append(flag)

if added:
    repl = f'GRUB_CMDLINE_LINUX_DEFAULT="{" ".join(existing)}"'
    s, e = m.span()
    p.write_text(text[:s] + repl + text[e:])
    print("  added: " + " ".join(added))
else:
    print("  already present; no change")
PY

    run "update-grub"
}

write_xorg_config() {
    step "Xorg headless configuration"
    backup_file "$XORG_FILE"

    if [ "$DRY_RUN" -eq 1 ]; then
        say "[dry-run] would write $XORG_FILE (NVIDIA GB10, virtual 1920x1080, HDMI-0 1600x900)"
        return 0
    fi

    mkdir -p "$(dirname "$XORG_FILE")"
    cat <<'EOF' > "$XORG_FILE"
# Headless Xorg configuration for NVIDIA GB10 on DGX Spark
Section "ServerLayout"
    Identifier     "Layout0"
    Screen      0  "Screen0" 0 0
    InputDevice    "Keyboard0" "CoreKeyboard"
    InputDevice    "Mouse0" "CorePointer"
EndSection

Section "Files"
EndSection

Section "InputDevice"
    Identifier     "Mouse0"
    Driver         "mouse"
    Option         "Protocol" "auto"
    Option         "Device" "/dev/psaux"
    Option         "Emulate3Buttons" "no"
    Option         "ZAxisMapping" "4 5"
EndSection

Section "InputDevice"
    Identifier     "Keyboard0"
    Driver         "kbd"
EndSection

Section "Monitor"
    Identifier     "Monitor0"
    VendorName     "Virtual"
    ModelName      "Headless"
    Option         "DPMS"
EndSection

Section "Device"
    Identifier     "Device0"
    Driver         "nvidia"
    VendorName     "NVIDIA Corporation"
    BoardName      "NVIDIA GB10"
    Option         "AllowEmptyInitialConfiguration" "True"
    Option         "VirtualHeads" "1"
    Option         "ConnectedMonitor" "DFP-0"
    Option         "Coolbits" "28"
EndSection

Section "Screen"
    Identifier     "Screen0"
    Device         "Device0"
    Monitor        "Monitor0"
    DefaultDepth    24
    Option         "MetaModes" "HDMI-0: 1600x900 +0+0"
    SubSection     "Display"
        Virtual     1920 1080
        Depth       24
    EndSubSection
EndSection
EOF
    say "wrote $XORG_FILE"
}

configure_gdm() {
    step "GDM session configuration"
    [ -f "$GDM_FILE" ] || { echo "[WARN] $GDM_FILE not found; skipping GDM step." >&2; return 0; }
    backup_file "$GDM_FILE"

    if [ "$DRY_RUN" -eq 1 ]; then
        say "[dry-run] would set WaylandEnable=false, DefaultSession=gnome-xorg.desktop"
        if [ "$ENABLE_AUTOLOGIN" -eq 1 ]; then
            say "[dry-run] would ENABLE passwordless autologin for $TARGET_USER"
        else
            say "[dry-run] autologin left untouched (pass --enable-autologin to change it)"
        fi
        return 0
    fi

    AUTOLOGIN_USER="$TARGET_USER" ENABLE_AUTOLOGIN="$ENABLE_AUTOLOGIN" python3 - <<'PY'
from pathlib import Path
from configparser import ConfigParser
import os

path = Path("/etc/gdm3/custom.conf")
parser = ConfigParser(strict=False, allow_no_value=True)
parser.optionxform = str
parser.read(path)

if "daemon" not in parser:
    parser["daemon"] = {}
daemon = parser["daemon"]

# Xorg session is required for the NVIDIA virtual-display path; Sunshine's
# X11 capture cannot attach to a Wayland compositor session.
for key in list(daemon.keys()):
    if key.lower() in {"waylandenable", "defaultsession"}:
        daemon.pop(key)
daemon["WaylandEnable"] = "false"
daemon["DefaultSession"] = "gnome-xorg.desktop"
changes = ["WaylandEnable=false", "DefaultSession=gnome-xorg.desktop"]

if os.environ.get("ENABLE_AUTOLOGIN") == "1":
    for key in list(daemon.keys()):
        if key.lower() in {"automaticloginenable", "automaticlogin"}:
            daemon.pop(key)
    daemon["AutomaticLoginEnable"] = "true"
    daemon["AutomaticLogin"] = os.environ["AUTOLOGIN_USER"]
    changes.append("AutomaticLoginEnable=true")
    changes.append("AutomaticLogin=" + os.environ["AUTOLOGIN_USER"])

with path.open("w") as fh:
    parser.write(fh, space_around_delimiters=False)

for c in changes:
    print("  set " + c)
PY

    if [ "$ENABLE_AUTOLOGIN" -eq 0 ]; then
        say "autologin NOT enabled — you will log in at the GDM greeter as usual"
    fi
}

install_autostart() {
    step "GNOME autostart entry"
    local autostart_dir="${TARGET_HOME}/.config/autostart"
    local desktop_file="${autostart_dir}/headless-xrandr.desktop"
    local xauth="/run/user/${TARGET_UID}/gdm/Xauthority"
    local runtime_dir="/run/user/${TARGET_UID}"

    backup_file "$desktop_file"

    if [ "$DRY_RUN" -eq 1 ]; then
        say "[dry-run] would write $desktop_file"
        return 0
    fi

    install -d -m 755 -o "$TARGET_USER" -g "$TARGET_USER" "$autostart_dir"
    cat <<EOF > "$desktop_file"
[Desktop Entry]
Type=Application
Exec=/bin/sh -c '/usr/bin/xrandr --output HDMI-0 --mode 1600x900; sleep 5; if ! pgrep -x sunshine >/dev/null 2>&1; then DISPLAY=:0 XAUTHORITY=${xauth} XDG_RUNTIME_DIR=${runtime_dir} /usr/bin/sunshine & fi'
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Headless Display Mode
EOF
    chown "$TARGET_USER:$TARGET_USER" "$desktop_file"
    chmod 644 "$desktop_file"
    say "wrote $desktop_file"
}

write_rollback() {
    [ "$DRY_RUN" -eq 1 ] && return 0
    local rb="$BACKUP_DIR/rollback.sh"
    cat <<'ROLLBACK' > "$rb"
#!/usr/bin/env bash
# Restore every file this run modified, to its exact prior state.
set -euo pipefail
[ "${EUID}" -eq 0 ] || { echo "Run as root: sudo $0" >&2; exit 1; }

DIR="$(cd "$(dirname "$0")" && pwd)"
MANIFEST="$DIR/manifest.tsv"
[ -f "$MANIFEST" ] || { echo "No manifest at $MANIFEST" >&2; exit 1; }

regen_grub=0
while IFS=$'\t' read -r target saved state; do
    [ -n "${target:-}" ] || continue
    case "$state" in
        EXISTED)
            cp -a "$saved" "$target"
            echo "restored $target"
            ;;
        ABSENT)
            if [ -e "$target" ]; then
                rm -f "$target"
                echo "removed  $target (did not exist before)"
            fi
            ;;
    esac
    [ "$target" = "/etc/default/grub" ] && regen_grub=1
done < "$MANIFEST"

if [ "$regen_grub" -eq 1 ]; then
    echo "regenerating GRUB..."
    update-grub
fi

echo
echo "Rollback complete. Reboot for kernel/Xorg changes to fully revert."
echo "Note: this does NOT uninstall the Sunshine package. To remove it:"
echo "  sudo apt-get remove --purge sunshine"
ROLLBACK
    chmod +x "$rb"
    say "rollback script: $rb"
}

main() {
    require_root
    determine_target_user
    preflight

    if [ "$DRY_RUN" -eq 0 ]; then
        mkdir -p "$BACKUP_DIR/files"
        : > "$BACKUP_DIR/manifest.tsv"
    fi

    [ "$SKIP_SUNSHINE"  -eq 1 ] || install_sunshine
    [ "$SKIP_GRUB"      -eq 1 ] || update_grub_cmdline
    [ "$SKIP_XORG"      -eq 1 ] || write_xorg_config
    [ "$SKIP_GDM"       -eq 1 ] || configure_gdm
    [ "$SKIP_AUTOSTART" -eq 1 ] || install_autostart

    write_rollback

    if [ "$DRY_RUN" -eq 1 ]; then
        printf '\nDry run complete. Nothing was changed.\n'
        return 0
    fi

    cat <<EOM

============================================================
Configuration complete.

Backups:  $BACKUP_DIR
Undo:     sudo $BACKUP_DIR/rollback.sh

Next steps:
  1. Reboot so the GRUB command line and Xorg config take effect.
  2. Log in at the GDM greeter$([ "$ENABLE_AUTOLOGIN" -eq 1 ] && echo " (autologin is ENABLED — it will log in for you)").
     The autostart entry sets 1600x900 and launches Sunshine.
  3. Sunshine web UI:  https://$(hostname):47990/
     Use HTTPS and accept the self-signed certificate.
  4. Set your Sunshine username and password on first access.
  5. Pair Moonlight using the PIN page at https://$(hostname):47990/pin

Security notes:
  - Sunshine listens on the network from boot. Restrict it at the firewall
    if this host is reachable from untrusted networks.
  - Autologin is $([ "$ENABLE_AUTOLOGIN" -eq 1 ] && echo "ENABLED — anyone with console access reaches your desktop" || echo "DISABLED — you log in normally").
============================================================
EOM
}

main "$@"
