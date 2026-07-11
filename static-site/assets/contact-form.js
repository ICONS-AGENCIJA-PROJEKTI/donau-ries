import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const supabase = createClient(window.SUPABASE_URL, window.SUPABASE_ANON_KEY);

document.querySelectorAll("[data-supabase-form]").forEach((form) => {
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const notice = form.querySelector("[data-form-notice]");
    const button = form.querySelector('button[type="submit"]');

    // B2B-Felder sauber in die vorhandenen Spalten packen (name/email/message):
    // Ansprechpartner -> name, die Qualifizierungsfelder in message vorangestellt.
    const parts = [];
    const add = (label, el) => {
      const v = el?.value.trim();
      if (v) parts.push(label + ": " + v);
    };
    add("Firma", form.firma);
    add("Rolle", form.rolle);
    add("Projekttyp", form.projekttyp);
    add("Umfang/Volumen", form.umfang);
    add("Telefon", form.telefon);
    const beschreibung = form.message?.value.trim() || "";
    const message = (parts.length ? parts.join("\n") + "\n\n" : "") + beschreibung;

    const payload = {
      name: form.ansprechpartner?.value.trim() || null,
      email: form.email?.value.trim() || null,
      message: message || null,
      source_page: location.pathname,
    };

    if (!payload.email || !form.firma?.value.trim()) {
      if (notice) notice.textContent = "Bitte fuellen Sie die Pflichtfelder aus.";
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
