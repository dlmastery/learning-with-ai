/* Theme persistence, shared by every page on the site.

   Each page owns its own toggle button; this file only remembers the choice
   and re-applies it on the next page. It runs render-blocking in <head> so
   the stored theme is set before first paint — a flash of the wrong scheme
   is the cheapest kind of incoherence and the most visible.

   No preference stored means no attribute set, so prefers-color-scheme wins.
   That is the intended default. */
(function () {
  var R = document.documentElement;
  try {
    var t = localStorage.getItem('theme');
    if (t === 'dark' || t === 'light') R.setAttribute('data-theme', t);
  } catch (e) { /* private mode; fall through to the media query */ }

  if (!window.MutationObserver) return;
  new MutationObserver(function () {
    try {
      var v = R.getAttribute('data-theme');
      if (v) localStorage.setItem('theme', v);
    } catch (e) { }
  }).observe(R, { attributes: true, attributeFilter: ['data-theme'] });
})();
