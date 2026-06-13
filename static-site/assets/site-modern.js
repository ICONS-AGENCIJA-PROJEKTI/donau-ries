document.querySelectorAll('[data-demo-form]').forEach((form) => {
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const notice = form.querySelector('[data-form-notice]');
    if (notice) notice.textContent = 'Demo: Diese lokale Praesentation sendet keine Daten.';
  });
});
