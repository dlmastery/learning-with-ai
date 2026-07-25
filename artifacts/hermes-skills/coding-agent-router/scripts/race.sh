#!/usr/bin/env bash
# race.sh — run several CLI coding agents in parallel on isolated git worktrees.
#
#   race.sh -r <repo> -a claude,codex,grok -t "task prompt" [-b base-ref] [-T timeout-secs]
#   race.sh --cleanup /tmp/agent-race-<ts> -r <repo>
#
# Each agent gets its own worktree + branch. Diffs, logs and a summary land in
# an output directory under /tmp for comparison. Nothing is merged automatically.

set -uo pipefail

REPO=""
AGENTS="claude,codex,grok"
TASK=""
BASE=""
TIMEOUT=1800
CLEANUP_DIR=""

usage() {
    cat <<'EOF'
Usage:
  race.sh -r <repo> -t "<task>" [-a claude,codex,grok,agy] [-b <base-ref>] [-T <seconds>]
  race.sh --cleanup <race-dir> -r <repo>

Options:
  -r, --repo <path>     Git repository to work in (required)
  -t, --task "<text>"   Task prompt handed to every agent (required)
  -a, --agents <list>   Comma-separated: claude, codex, grok, agy  (default: claude,codex,grok)
  -b, --base <ref>      Base ref for the worktrees (default: current HEAD)
  -T, --timeout <secs>  Per-agent timeout (default: 1800)
      --cleanup <dir>   Remove the worktrees and branches from a previous race
  -h, --help            This message
EOF
}

while [ "$#" -gt 0 ]; do
    case "$1" in
        -r|--repo)    REPO="${2:?missing value for $1}"; shift 2 ;;
        -a|--agents)  AGENTS="${2:?missing value for $1}"; shift 2 ;;
        -t|--task)    TASK="${2:?missing value for $1}"; shift 2 ;;
        -b|--base)    BASE="${2:?missing value for $1}"; shift 2 ;;
        -T|--timeout) TIMEOUT="${2:?missing value for $1}"; shift 2 ;;
        --cleanup)    CLEANUP_DIR="${2:?missing value for $1}"; shift 2 ;;
        -h|--help)    usage; exit 0 ;;
        *) echo "[ERROR] Unknown argument: $1" >&2; usage; exit 1 ;;
    esac
done

[ -n "$REPO" ] || { echo "[ERROR] -r/--repo is required" >&2; exit 1; }
REPO="$(cd "$REPO" 2>/dev/null && pwd)" || { echo "[ERROR] No such directory: $REPO" >&2; exit 1; }
git -C "$REPO" rev-parse --git-dir >/dev/null 2>&1 || { echo "[ERROR] Not a git repository: $REPO" >&2; exit 1; }

# ---------------------------------------------------------------- cleanup mode
if [ -n "$CLEANUP_DIR" ]; then
    [ -d "$CLEANUP_DIR" ] || { echo "[ERROR] No such race directory: $CLEANUP_DIR" >&2; exit 1; }
    for wt in "$CLEANUP_DIR"/*/; do
        [ -d "$wt" ] || continue
        git -C "$REPO" worktree remove --force "$wt" 2>/dev/null \
            && echo "removed worktree $wt"
    done
    if [ -f "$CLEANUP_DIR/.branches" ]; then
        while IFS= read -r br; do
            [ -n "$br" ] || continue
            git -C "$REPO" branch -D "$br" >/dev/null 2>&1 && echo "deleted branch $br"
        done < "$CLEANUP_DIR/.branches"
    fi
    git -C "$REPO" worktree prune
    rm -rf "$CLEANUP_DIR"
    echo "Cleaned up $CLEANUP_DIR"
    exit 0
fi

# ------------------------------------------------------------------ race mode
[ -n "$TASK" ] || { echo "[ERROR] -t/--task is required" >&2; exit 1; }

if [ -n "$(git -C "$REPO" status --porcelain)" ]; then
    echo "[ERROR] Working tree is dirty. Commit or stash first — worktrees branch from HEAD." >&2
    exit 1
fi

[ -n "$BASE" ] || BASE="$(git -C "$REPO" rev-parse HEAD)"

# Build the headless command for an agent. Each writes into $PWD (the worktree).
agent_cmd() {
    case "$1" in
        claude) printf 'claude --dangerously-skip-permissions -p %q' "$TASK" ;;
        codex)  printf 'codex exec --sandbox danger-full-access %q' "$TASK" ;;
        grok)   printf 'grok --directory . -p %q' "$TASK" ;;
        agy)    printf 'agy --dangerously-skip-permissions --print-timeout %ds -p %q' "$TIMEOUT" "$TASK" ;;
        *)      return 1 ;;
    esac
}

# Cheap auth/availability probe — skip agents that clearly cannot run.
agent_available() {
    command -v "$1" >/dev/null 2>&1 || { echo "not installed"; return 1; }
    case "$1" in
        agy) agy models >/dev/null 2>&1 || { echo "not signed in (run bare 'agy')"; return 1; } ;;
    esac
    return 0
}

TS="$(date +%Y%m%d-%H%M%S)"
OUT="/tmp/agent-race-$TS"
mkdir -p "$OUT"
: > "$OUT/.branches"

echo "Repo:    $REPO"
echo "Base:    $BASE"
echo "Task:    $TASK"
echo "Output:  $OUT"
echo

declare -a RUNNING=()
IFS=',' read -ra AGENT_LIST <<< "$AGENTS"

for agent in "${AGENT_LIST[@]}"; do
    agent="$(echo "$agent" | tr -d '[:space:]')"
    [ -n "$agent" ] || continue

    if ! reason="$(agent_available "$agent")"; then
        echo "SKIP  $agent — ${reason:-unavailable}"
        echo "$agent: SKIPPED (${reason:-unavailable})" >> "$OUT/SUMMARY.txt"
        continue
    fi

    cmd="$(agent_cmd "$agent")" || {
        echo "SKIP  $agent — unknown agent"
        echo "$agent: SKIPPED (unknown agent)" >> "$OUT/SUMMARY.txt"
        continue
    }

    branch="race/$TS/$agent"
    wt="$OUT/$agent"

    if ! git -C "$REPO" worktree add -b "$branch" "$wt" "$BASE" >>"$OUT/$agent.log" 2>&1; then
        echo "SKIP  $agent — worktree creation failed (see $OUT/$agent.log)"
        echo "$agent: SKIPPED (worktree failed)" >> "$OUT/SUMMARY.txt"
        continue
    fi
    echo "$branch" >> "$OUT/.branches"

    echo "START $agent  →  $wt  ($branch)"
    (
        start=$(date +%s)
        cd "$wt" || exit 1
        timeout "$TIMEOUT" bash -lc "$cmd" >>"$OUT/$agent.log" 2>&1
        rc=$?
        end=$(date +%s)
        git -C "$wt" add -A >/dev/null 2>&1
        git -C "$wt" diff --cached > "$OUT/$agent.diff" 2>/dev/null
        stat_line="$(git -C "$wt" diff --cached --shortstat 2>/dev/null)"
        [ -n "$stat_line" ] || stat_line="no changes"
        case $rc in
            0)   status="ok" ;;
            124) status="TIMEOUT after ${TIMEOUT}s" ;;
            *)   status="exit $rc" ;;
        esac
        # Several agents exit 0 even when the run failed (auth rejected, API
        # error, quota). Scan the transcript for error markers so a clean exit
        # code alone never gets read as success.
        if grep -qiE 'I encountered an error|API error: [0-9]{3}|invalid api key|unauthorized|rate.?limit|quota exceeded|authentication failed' \
                "$OUT/$agent.log" 2>/dev/null; then
            marker="$(grep -oiE 'I encountered an error[^"]{0,120}|API error: [0-9]{3}[^"]{0,120}|invalid api key|unauthorized|quota exceeded' \
                "$OUT/$agent.log" 2>/dev/null | head -1)"
            status="$status BUT LOG SHOWS ERROR: ${marker:-see log}"
        fi
        printf '%s: %s | %ds | %s\n' "$agent" "$status" "$((end-start))" "$stat_line" >> "$OUT/SUMMARY.txt"
    ) &
    RUNNING+=("$!")
done

if [ "${#RUNNING[@]}" -eq 0 ]; then
    echo
    echo "[ERROR] No agents could be started. See $OUT/SUMMARY.txt" >&2
    exit 1
fi

echo
echo "Waiting for ${#RUNNING[@]} agent(s)…"
for pid in "${RUNNING[@]}"; do wait "$pid"; done

echo
echo "===== SUMMARY ====="
cat "$OUT/SUMMARY.txt" 2>/dev/null
echo
echo "Diffs:    $OUT/*.diff"
echo "Logs:     $OUT/*.log"
echo "Merge:    git -C $REPO merge --squash race/$TS/<agent>"
echo "Cleanup:  race.sh --cleanup $OUT -r $REPO"
