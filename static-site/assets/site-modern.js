document.querySelectorAll('[data-demo-form]').forEach((form) => {
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const notice = form.querySelector('[data-form-notice]');
    if (notice) notice.textContent = 'Demo: Diese lokale Praesentation sendet keine Daten.';
  });
});

// Floating contact widget (event delegation – works regardless of script order)
document.addEventListener('click', (event) => {
  const toggle = event.target.closest('.contact-fab-toggle');
  if (toggle) {
    const fab = toggle.closest('.contact-fab');
    const options = fab.querySelector('.contact-fab-options');
    const isOpen = fab.hasAttribute('data-open');
    if (isOpen) {
      fab.removeAttribute('data-open');
      if (options) options.hidden = true;
      toggle.setAttribute('aria-expanded', 'false');
    } else {
      fab.setAttribute('data-open', '');
      if (options) options.hidden = false;
      toggle.setAttribute('aria-expanded', 'true');
    }
    return;
  }
  // Close when clicking outside an open widget
  const openFab = document.querySelector('.contact-fab[data-open]');
  if (openFab && !event.target.closest('.contact-fab')) {
    openFab.removeAttribute('data-open');
    const opts = openFab.querySelector('.contact-fab-options');
    if (opts) opts.hidden = true;
    const t = openFab.querySelector('.contact-fab-toggle');
    if (t) t.setAttribute('aria-expanded', 'false');
  }
});

// Mobile hamburger menu (event delegation)
document.addEventListener('click', (event) => {
  const toggle = event.target.closest('.nav-toggle');
  if (!toggle) return;
  const header = toggle.closest('.site-header');
  if (!header) return;
  const isOpen = header.toggleAttribute('data-nav-open');
  toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
});
