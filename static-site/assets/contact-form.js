import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const supabase = createClient(window.SUPABASE_URL, window.SUPABASE_ANON_KEY);

document.querySelectorAll("[data-supabase-form]").forEach((form) => {
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const notice = form.querySelector("[data-form-notice]");
    const button = form.querySelector('button[type="submit"]');

    const payload = {
      name: form.name?.value.trim() || null,
      email: form.email?.value.trim() || null,
      message: form.message?.value.trim() || null,
      source_page: location.pathname,
    };

    if (!payload.email && !payload.message) {
      if (notice) notice.textContent = "Bitte fuellen Sie das Formular aus.";
      return;
    }

    if (button) button.disabled = true;
    if (notice) notice.textContent = "Wird gesendet …";

    const { error } = await supabase.from("kontakt_anfragen").insert(payload);

    if (error) {
      if (notice) notice.textContent = "Es gab ein Problem. Bitte versuchen Sie es spaeter erneut.";
      if (button) button.disabled = false;
      return;
    }

    form.reset();
    if (notice) notice.textContent = "Vielen Dank! Ihre Anfrage wurde gesendet.";
    if (button) button.disabled = false;
  });
});
