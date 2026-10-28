// Mobile menu toggle for templates/partials/navbar.html
(
    function () {
  var btn = document.getElementById('menu-toggle');
  var menu = document.getElementById('mobile-menu');
  if (!btn || !menu) return;

  function setOpen(open) {
    btn.setAttribute('aria-expanded', String(open));
    btn.textContent = open ? 'Close' : 'Menu';
    menu.classList.toggle('is-open', open);
    document.body.classList.toggle('menu-open', open);
  }

  btn.addEventListener('click', function () {
    setOpen(btn.getAttribute('aria-expanded') !== 'true');
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') setOpen(false);
  });

  // Close the menu if the window is resized up to desktop width
  window.matchMedia('(min-width: 861px)').addEventListener('change', function (e) {
    if (e.matches) setOpen(false);
  });
})();