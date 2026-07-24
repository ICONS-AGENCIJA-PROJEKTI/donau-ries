import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

// Supabase = Backup/Speicherung (funktioniert überall, auch auf der Vercel-Vorschau).
// send-mail.php = E-Mail-Versand auf dem Produktions-Host (Checkdomain, mit PHP).
const supabase = (window.SUPABASE_URL && window.SUPABASE_ANON_KEY)
  ? createClient(window.SUPABASE_URL, window.SUPABASE_ANON_KEY)
  : null;

document.querySelectorAll("[data-supabase-form]").forEach((form) => {
  const roleField = form.querySelector('[name="rolle"]');
  const firmaField = form.querySelector('[name="firma"]');
  const firmaLabel = form.querySelector('[data-firma-label]');
  const firmaRequired = form.querySelector('[data-firma-required]');

  const syncFirmaRequirement = () => {
    const isPrivate = roleField?.value === "Privatperson / Eigentümer";
    const isBusiness = Boolean(roleField?.value) && !isPrivate;
    if (firmaField) {
      firmaField.required = isBusiness;
      if (isPrivate) firmaField.value = "";
    }
    if (firmaLabel) firmaLabel.hidden = isPrivate;
    if (firmaRequired) firmaRequired.hidden = !isBusiness;
  };

  roleField?.addEventListener("change", syncFirmaRequirement);
  syncFirmaRequirement();

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const notice = form.querySelector("[data-form-notice]");
    const button = form.querySelector('button[type="submit"]');

    // Honeypot: von Bots ausgefülltes Feld -> stillschweigend ignorieren
    if (form.website && form.website.value) {
      form.reset();
      syncFirmaRequirement();
      if (notice) notice.textContent = "Vielen Dank!";
      return;
    }

    const firma = form.firma?.value.trim() || "";
    const email = form.email?.value.trim() || "";
    const isPrivate = form.rolle?.value === "Privatperson / Eigentümer";
    if ((!isPrivate && !firma) || !email) {
      if (notice) notice.textContent = "Bitte füllen Sie die Pflichtfelder aus.";
      return;
    }

    if (button) button.disabled = true;
    if (notice) notice.textContent = "Wird gesendet …";

    const fd = new FormData(form);
    let ok = false;

    // 1) E-Mail über send-mail.php (nur strenge JSON-Antwort {success:true} zählt als versendet;
    //    auf der Vercel-Vorschau ohne PHP schlägt das fehl -> Supabase greift als Backup).
    try {
      const res = await fetch("/send-mail.php", { method: "POST", body: fd });
      if (res.ok) {
        const data = await res.json();
        if (data && data.success) ok = true;
      }
    } catch (_) { /* kein PHP (Vorschau) oder Netzwerkfehler */ }

    // 2) Backup: Anfrage in Supabase speichern (B2B-Felder in message gebündelt).
    if (supabase) {
      try {
        const parts = [];
        [["Firma", "firma"], ["Rolle", "rolle"], ["Projekttyp", "projekttyp"], ["Umfang/Volumen", "umfang"], ["Telefon", "telefon"]]
          .forEach(([label, n]) => { const v = form[n]?.value.trim(); if (v) parts.push(label + ": " + v); });
        const message = (parts.length ? parts.join("\n") + "\n\n" : "") + (form.message?.value.trim() || "");
        const { error } = await supabase.from("kontakt_anfragen").insert({
          name: form.ansprechpartner?.value.trim() || null,
          email,
          message: message || null,
          source_page: location.pathname,
        });
        if (!error) ok = true;
      } catch (_) { /* Speicherung optional */ }
    }

    if (ok) {
      form.reset();
      syncFirmaRequirement();
      if (notice) notice.textContent = "Vielen Dank! Ihre Anfrage ist bei uns eingegangen – wir melden uns zeitnah.";
    } else {
      if (notice) notice.textContent = "Es gab ein Problem beim Senden. Bitte rufen Sie uns an: 09080 4317.";
    }
    if (button) button.disabled = false;
  });
});
