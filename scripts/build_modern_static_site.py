from __future__ import annotations

import csv
import html
import json
import shutil
from pathlib import Path


DOMAIN = "https://donau-ries-haustechnik.de"
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
STATIC = ROOT / "static-site"
ASSETS = STATIC / "assets"
IMG_DIR = ASSETS / "placeholder-images"


PAGES = [
    {
        "path": "/",
        "label": "Start",
        "title": "Donau-Ries Haustechnik | Bad, Heizung, Solar, Lueftung",
        "description": "Moderner SHK-Fachbetrieb fuer Bad, Heizung, Solar, Lueftung und Haustechnik in Donau-Ries.",
        "h1": "Haustechnik, die modern aussieht und im Alltag funktioniert.",
        "kicker": "SHK-Fachbetrieb fuer Donau-Ries",
        "lead": "Ein klarer, schneller und vertrauensvoller Relaunch fuer Kunden, die ein neues Bad, eine effiziente Heizung oder verlaessliche Haustechnik suchen.",
        "image": "placeholder-02.jpg",
        "cluster": "home",
    },
    {
        "path": "/bad/",
        "label": "Bad",
        "title": "Badplanung und Badsanierung | Donau-Ries Haustechnik",
        "description": "Badplanung, Badsanierung und barrierearme Badloesungen aus einer Hand in Donau-Ries.",
        "h1": "Ihr neues Bad: geplant, koordiniert und sauber umgesetzt.",
        "kicker": "Badplanung und Sanierung",
        "lead": "Von der ersten Idee bis zur fertigen Uebergabe entsteht eine Badseite, die Beratung, Stil, Budget und Umsetzung deutlich besser fuehrt.",
        "image": "placeholder-02.jpg",
        "cluster": "bad",
    },
    {
        "path": "/heizung/",
        "label": "Heizung",
        "title": "Heizung modernisieren | Donau-Ries Haustechnik",
        "description": "Heizungsmodernisierung, Waermepumpe, Gas, Holz und Foerderberatung fuer Donau-Ries.",
        "h1": "Effizient heizen, sauber planen, Foerderung mitdenken.",
        "kicker": "Heizung und Modernisierung",
        "lead": "Die neue Heizungsseite fuehrt Nutzer von der Systemwahl bis zur Anfrage und bleibt stark fuer lokale Suchbegriffe.",
        "image": "placeholder-03.jpg",
        "cluster": "heizung",
    },
    {
        "path": "/solar/",
        "label": "Solar",
        "title": "Solar und Energie | Donau-Ries Haustechnik",
        "description": "Solartechnik und erneuerbare Energie als Teil moderner Haustechnik in Donau-Ries.",
        "h1": "Solartechnik als sinnvoller Baustein fuer Ihr Gebaeude.",
        "kicker": "Solar und Energie",
        "lead": "Die Solar-Seite ergaenzt die Heizungs- und Haustechnikthemen mit klarer Beratung und regionalem Bezug.",
        "image": "placeholder-03.jpg",
        "cluster": "solar",
    },
    {
        "path": "/lueftung/",
        "label": "Lueftung",
        "title": "Lueftung und Raumluft | Donau-Ries Haustechnik",
        "description": "Kontrollierte Lueftung und dezentrale Wohnraumlueftung fuer moderne Gebaeude.",
        "h1": "Frische Raumluft, bessere Effizienz und mehr Komfort.",
        "kicker": "Lueftung",
        "lead": "Eine moderne Lueftungsseite erklaert Nutzen, Einsatzbereiche und den Weg zur passenden Loesung.",
        "image": "placeholder-04.jpg",
        "cluster": "lueftung",
    },
    {
        "path": "/haustechnik/",
        "label": "Haustechnik",
        "title": "Haustechnik und Installation | Donau-Ries Haustechnik",
        "description": "Installation, Wassertechnik, Entkalkung und technische Gebaeudeloesungen in Donau-Ries.",
        "h1": "Technik im Haus, die einfach verlaesslich laeuft.",
        "kicker": "Haustechnik",
        "lead": "Die Haustechnikseite sammelt Leistungen rund um Installation, Wasser, Entkalkung und technische Betreuung.",
        "image": "placeholder-05.jpg",
        "cluster": "haustechnik",
    },
    {
        "path": "/leistungen-gewerbekunden/",
        "label": "Gewerbe",
        "title": "Haustechnik fuer Gewerbekunden | Donau-Ries",
        "description": "Objekt- und Anlagenbau, Sanitaer, Heizung und Betreuung fuer Gewerbekunden.",
        "h1": "Gebaeudetechnik fuer Gewerbe, Objekte und Verwaltungen.",
        "kicker": "Gewerbekunden",
        "lead": "Ein eigener Bereich fuer gewerbliche Kunden macht Leistungen, Reaktionswege und Kompetenz schneller erfassbar.",
        "image": "placeholder-05.jpg",
        "cluster": "gewerbe",
    },
    {
        "path": "/unternehmen/",
        "label": "Unternehmen",
        "title": "Unternehmen | Donau-Ries Haustechnik GmbH",
        "description": "Regionale Naehe, Erfahrung und Arbeitsweise der Donau-Ries Haustechnik GmbH.",
        "h1": "Regional verwurzelt. Technisch erfahren. Persoenlich erreichbar.",
        "kicker": "Unternehmen",
        "lead": "Diese Seite wird spaeter mit echten Teamfotos, Partnern, Zertifikaten und Firmenfakten zum Vertrauensanker.",
        "image": "placeholder-06.png",
        "cluster": "unternehmen",
    },
    {
        "path": "/jobs/",
        "label": "Jobs",
        "title": "Jobs und Ausbildung | Donau-Ries Haustechnik",
        "description": "Jobs, Ausbildung und Karriere im SHK-Handwerk bei Donau-Ries Haustechnik.",
        "h1": "Arbeiten im SHK-Handwerk mit Perspektive.",
        "kicker": "Jobs und Ausbildung",
        "lead": "Der Jobs-Bereich bleibt als eigener URL erhalten und kann spaeter Bewerber gezielt ansprechen.",
        "image": "placeholder-06.png",
        "cluster": "jobs",
    },
    {
        "path": "/kontaktformular/",
        "label": "Kontakt",
        "title": "Kontakt aufnehmen | Donau-Ries Haustechnik",
        "description": "Kontakt zu Donau-Ries Haustechnik fuer Beratung, Angebot und Rueckruf.",
        "h1": "Sprechen wir ueber Ihr Projekt.",
        "kicker": "Kontakt",
        "lead": "Die lokale Praesentation sendet keine Daten. Fuer den Livegang wird das Formular sauber angebunden.",
        "image": "placeholder-01.png",
        "cluster": "kontakt",
    },
]


NAV = [
    ("/", "Home"),
    ("/bad/", "Bad"),
    ("/heizung/", "Heizung"),
    ("/solar/", "Solar"),
    ("/lueftung/", "Lueftung"),
    ("/haustechnik/", "Haustechnik"),
    ("/leistungen-gewerbekunden/", "Gewerbe"),
    ("/unternehmen/", "Unternehmen"),
]


def read_redirect_rows() -> list[dict[str, str]]:
    path = DATA / "redirect-map.csv"
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def rel(from_file: Path, target: str) -> str:
    depth = len(from_file.parent.relative_to(STATIC).parts)
    return ("../" * depth) + target.lstrip("/")


def url_to_file(path: str) -> Path:
    if path == "/":
        return STATIC / "index.html"
    return STATIC / path.strip("/") / "index.html"


def page_url(path: str) -> str:
    return f"{DOMAIN}{path}"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def available_image(filename: str) -> str:
    if (IMG_DIR / filename).exists():
        return f"/assets/placeholder-images/{filename}"
    return "/assets/placeholder.svg"


def write_assets() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "placeholder.svg").write_text(
        """<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="900" viewBox="0 0 1400 900">
<rect width="1400" height="900" fill="#edf3f5"/>
<path d="M0 670 C230 570 420 760 680 625 C920 500 1080 540 1400 430 V900 H0 Z" fill="#d8e5ea"/>
<circle cx="1120" cy="170" r="88" fill="#d8a73d"/>
<text x="90" y="150" font-family="Arial, sans-serif" font-size="48" font-weight="700" fill="#113340">Placeholder</text>
<text x="90" y="212" font-family="Arial, sans-serif" font-size="26" fill="#51646b">Replace image before publication</text>
</svg>""",
        encoding="utf-8",
    )
    (ASSETS / "site-modern.js").write_text(
        """
document.querySelectorAll('[data-demo-form]').forEach((form) => {
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const notice = form.querySelector('[data-form-notice]');
    if (notice) notice.textContent = 'Demo: Diese lokale Praesentation sendet keine Daten.';
  });
});
""".strip()
        + "\n",
        encoding="utf-8",
    )
    (ASSETS / "styles-modern.css").write_text(CSS.strip() + "\n", encoding="utf-8")


def layout(page: dict[str, str], body: str, *, noindex: bool = False) -> str:
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large"
    path = page["path"]
    schema = schema_for(page)
    return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(page['title'])}</title>
  <meta name="description" content="{esc(page['description'])}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{page_url(path)}">
  <link rel="stylesheet" href="{rel(url_to_file(path), '/assets/styles-modern.css')}">
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=True)}</script>
</head>
<body>
  {header(path)}
  <main>{body}</main>
  {footer(path)}
  <script src="{rel(url_to_file(path), '/assets/site-modern.js')}"></script>
</body>
</html>
"""


def header(current_path: str) -> str:
    links = []
    for path, label in NAV:
        active = ' aria-current="page"' if path == current_path else ""
        links.append(f'<a href="{rel(url_to_file(current_path), path)}"{active}>{label}</a>')
    return f"""
<div class="utility">
  <span>Interne Relaunch-Praesentation</span>
  <a href="{rel(url_to_file(current_path), '/kontaktformular/')}">Rueckruf planen</a>
</div>
<header class="site-header">
  <a class="brand" href="{rel(url_to_file(current_path), '/')}">
    <span class="brand-mark">DR</span>
    <span><strong>Donau-Ries</strong><small>Haustechnik GmbH</small></span>
  </a>
  <nav class="main-nav" aria-label="Hauptnavigation">{''.join(links)}</nav>
  <a class="nav-cta" href="{rel(url_to_file(current_path), '/kontaktformular/')}">Anfrage starten</a>
</header>
"""


def footer(current_path: str) -> str:
    return f"""
<footer class="footer">
  <div class="footer-grid">
    <div>
      <strong>Donau-Ries Haustechnik</strong>
      <p>Moderner statischer Relaunch mit sicherer URL-Migration, klaren Leistungsseiten und lokaler SEO-Struktur.</p>
    </div>
    <div>
      <span>Leistungen</span>
      <a href="{rel(url_to_file(current_path), '/bad/')}">Bad</a>
      <a href="{rel(url_to_file(current_path), '/heizung/')}">Heizung</a>
      <a href="{rel(url_to_file(current_path), '/lueftung/')}">Lueftung</a>
    </div>
    <div>
      <span>Kontakt</span>
      <a href="{rel(url_to_file(current_path), '/kontaktformular/')}">Kontaktformular</a>
      <a href="{rel(url_to_file(current_path), '/impressum/')}">Impressum</a>
      <a href="{rel(url_to_file(current_path), '/datenschutz/')}">Datenschutz</a>
    </div>
  </div>
</footer>
<a class="mobile-action" href="{rel(url_to_file(current_path), '/kontaktformular/')}">Projekt anfragen</a>
"""


def home_body(page: dict[str, str]) -> str:
    img = rel(url_to_file(page["path"]), available_image(page["image"]))
    return f"""
<section class="hero">
  <div class="hero-copy">
    <span class="kicker">{esc(page['kicker'])}</span>
    <h1>{esc(page['h1'])}</h1>
    <p>{esc(page['lead'])}</p>
    <div class="hero-actions">
      <a class="button primary" href="{rel(url_to_file(page['path']), '/kontaktformular/')}">Kostenlose Erstberatung</a>
      <a class="button ghost" href="{rel(url_to_file(page['path']), '/bad/')}">Leistungen ansehen</a>
    </div>
    <div class="trust-row">
      <span>Bad</span><span>Heizung</span><span>Solar</span><span>Lueftung</span>
    </div>
  </div>
  <div class="hero-media">
    <img src="{img}" alt="Moderne Haustechnik und Badplanung als Placeholder">
    <div class="floating-card"><strong>SEO bleibt stabil</strong><span>URLs, Canonicals, Sitemap und Redirects sind mitgedacht.</span></div>
  </div>
</section>
<section class="section intro-grid">
  <div>
    <span class="kicker">Warum neu?</span>
    <h2>Mehr Vertrauen, weniger Reibung, bessere Anfragewege.</h2>
  </div>
  <p>Die alte Seite hatte viele Inhalte, aber zu wenig Fokus. Der neue Aufbau macht Leistungen schneller verstaendlich, setzt klare Kontaktpunkte und bewahrt die wichtigen URL-Signale der bestehenden Website.</p>
</section>
{service_grid(page['path'])}
<section class="section process">
  <span class="kicker">Ablauf</span>
  <h2>Von der Idee zur Anfrage in drei klaren Schritten.</h2>
  <div class="steps">
    <div><b>01</b><h3>Orientieren</h3><p>Nutzer finden schnell Bad, Heizung, Solar, Lueftung oder Gewerbe.</p></div>
    <div><b>02</b><h3>Verstehen</h3><p>Jede Seite erklaert Nutzen, Ablauf und naechste Entscheidung.</p></div>
    <div><b>03</b><h3>Anfragen</h3><p>Wiederkehrende CTA-Bloecke fuehren zur Kontaktaufnahme.</p></div>
  </div>
</section>
<section class="cta-band">
  <div>
    <span class="kicker">Lokaler Relaunch</span>
    <h2>Bereit fuer eine moderne Website ohne SEO-Verlust.</h2>
  </div>
  <a class="button light" href="{rel(url_to_file(page['path']), '/kontaktformular/')}">Kontaktseite ansehen</a>
</section>
"""


def service_body(page: dict[str, str]) -> str:
    img = rel(url_to_file(page["path"]), available_image(page["image"]))
    related = related_links(page)
    contact_form = contact_block(page["path"]) if page["path"] == "/kontaktformular/" else ""
    return f"""
<section class="sub-hero">
  <div>
    <span class="kicker">{esc(page['kicker'])}</span>
    <h1>{esc(page['h1'])}</h1>
    <p>{esc(page['lead'])}</p>
    <div class="hero-actions">
      <a class="button primary" href="{rel(url_to_file(page['path']), '/kontaktformular/')}">Anfrage starten</a>
      <a class="button ghost" href="{rel(url_to_file(page['path']), '/')}">Zur Startseite</a>
    </div>
  </div>
  <img src="{img}" alt="{esc(page['kicker'])} Placeholder Bild">
</section>
<section class="proof-strip" aria-label="Projektvorteile">
  <div><strong>01</strong><span>Klare Beratung statt Standardpaket</span></div>
  <div><strong>02</strong><span>Koordination aus einer Hand</span></div>
  <div><strong>03</strong><span>Regionale Naehe in Donau-Ries</span></div>
</section>
<section class="section feature-layout">
  <div>
    <span class="kicker">Funktion der Seite</span>
    <h2>Eine Seite, die nicht nur gut aussieht, sondern Anfragen fuehrt.</h2>
    <p>Die neue Struktur kombiniert moderne Gestaltung mit SEO-Sicherheit: ein eindeutiger H1, klare Nutzenargumente, logische interne Links, CTA-Bloecke und ein sauberer Canonical auf die bestehende URL.</p>
  </div>
  <div class="feature-panel">
    <h3>Was diese Seite leisten muss</h3>
    <ul>
      <li>Besucher innerhalb weniger Sekunden orientieren.</li>
      <li>Leistung, Ablauf und Kontaktweg sichtbar machen.</li>
      <li>Alte URL-Signale und interne Verlinkung erhalten.</li>
      <li>Finale Texte und Bilder vor Livegang ersetzen.</li>
    </ul>
  </div>
</section>
<section class="section detail-cards">
  <article>
    <span>Beratung</span>
    <h3>Verstehen, was wirklich gebraucht wird.</h3>
    <p>Statt langer Textbloecke fuehrt die Seite mit klaren Fragen, Nutzenpunkten und Kontaktwegen.</p>
  </article>
  <article>
    <span>Planung</span>
    <h3>Von Budget bis Umsetzung strukturiert bleiben.</h3>
    <p>Jede Leistungsseite bekommt eine logische Informationsfolge und passende interne Verlinkung.</p>
  </article>
  <article>
    <span>Umsetzung</span>
    <h3>Vertrauen schaffen, bevor der Nutzer anfragt.</h3>
    <p>Platz fuer echte Referenzen, Teamfotos, Partner, Zertifikate und regionale Nachweise ist vorgesehen.</p>
  </article>
</section>
{related}
{contact_form}
<section class="cta-band">
  <div>
    <span class="kicker">Naechster Schritt</span>
    <h2>Die Seite fuehrt direkt zur passenden Anfrage.</h2>
  </div>
  <a class="button light" href="{rel(url_to_file(page['path']), '/kontaktformular/')}">Projekt besprechen</a>
</section>
"""


def service_grid(current_path: str) -> str:
    cards = []
    for page in PAGES[1:7]:
        cards.append(
            f"""<a class="service-card" href="{rel(url_to_file(current_path), page['path'])}">
  <span>{esc(page['kicker'])}</span>
  <h3>{esc(page['label'])}</h3>
  <p>{esc(page['description'])}</p>
</a>"""
        )
    return f"""
<section class="section">
  <span class="kicker">Leistungen</span>
  <h2>Alles schnell erreichbar, ohne Suchmaschinen-Signale zu verlieren.</h2>
  <div class="service-grid">{''.join(cards)}</div>
</section>
"""


def related_links(page: dict[str, str]) -> str:
    if page["cluster"] == "bad":
        items = [("/badplanung/", "Badplanung"), ("/barrierefreies-bad/", "Barrierefreies Bad"), ("/foerderung-bad/", "Foerderung Bad")]
    elif page["cluster"] == "heizung":
        items = [("/waermepumpe/", "Waermepumpe"), ("/oel-gasheizung/", "Oel- und Gasheizung"), ("/foerderung/", "Foerderung")]
    elif page["cluster"] == "lueftung":
        items = [("/dezentrale-wohnraumlueftung/", "Dezentrale Wohnraumlueftung"), ("/haustechnik/", "Haustechnik")]
    elif page["cluster"] == "gewerbe":
        items = [("/objekt-u-anlagenbau/", "Objekt- und Anlagenbau"), ("/sanitaeranlagen/", "Sanitaeranlagen")]
    else:
        items = [("/bad/", "Bad"), ("/heizung/", "Heizung"), ("/kontaktformular/", "Kontakt")]
    links = "".join(f'<a href="{rel(url_to_file(page["path"]), path)}">{esc(label)}</a>' for path, label in items)
    return f"""
<section class="section related">
  <span class="kicker">URL-Struktur</span>
  <h2>Verwandte alte URLs bleiben erreichbar.</h2>
  <div>{links}</div>
</section>
"""


def contact_block(current_path: str) -> str:
    return f"""
<section class="section contact-section">
  <div>
    <span class="kicker">Demo-Formular</span>
    <h2>Kontakt ohne externe Uebertragung.</h2>
    <p>Diese lokale Version zeigt nur die Funktion. Beim Livegang werden Empfaenger, Datenschutz und Spam-Schutz final eingerichtet.</p>
  </div>
  <form data-demo-form>
    <label>Name<input name="name" autocomplete="name" placeholder="Max Mustermann"></label>
    <label>E-Mail<input name="email" autocomplete="email" placeholder="name@example.de"></label>
    <label>Projekt<textarea name="message" placeholder="Bad, Heizung, Solar oder Haustechnik?"></textarea></label>
    <button class="button primary" type="submit">Demo-Anfrage testen</button>
    <p class="form-notice" data-form-notice></p>
  </form>
</section>
"""


def legal_body(title: str, text: str) -> str:
    return f"""
<section class="section legal">
  <span class="kicker">Vor Livegang finalisieren</span>
  <h1>{esc(title)}</h1>
  <p>{esc(text)}</p>
</section>
"""


def schema_for(page: dict[str, str]) -> dict[str, object]:
    base = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness" if page["path"] in {"/", "/unternehmen/", "/kontaktformular/"} else "Service",
        "name": page["h1"],
        "description": page["description"],
        "url": page_url(page["path"]),
        "areaServed": "Donau-Ries",
    }
    if base["@type"] == "Service":
        base["provider"] = {"@type": "LocalBusiness", "name": "Donau-Ries Haustechnik GmbH", "url": DOMAIN}
    return base


def write_page(page: dict[str, str]) -> None:
    target = url_to_file(page["path"])
    target.parent.mkdir(parents=True, exist_ok=True)
    body = home_body(page) if page["path"] == "/" else service_body(page)
    target.write_text(layout(page, body), encoding="utf-8")


def write_legal_pages() -> None:
    legal_pages = [
        {
            "path": "/impressum/",
            "title": "Impressum | Donau-Ries Haustechnik",
            "description": "Impressum der Donau-Ries Haustechnik GmbH. Platzhalter fuer die lokale Relaunch-Praesentation.",
            "h1": "Impressum",
            "kicker": "Rechtliches",
            "lead": "",
            "image": "placeholder-01.png",
            "cluster": "legal",
        },
        {
            "path": "/datenschutz/",
            "title": "Datenschutz | Donau-Ries Haustechnik",
            "description": "Datenschutz der Donau-Ries Haustechnik GmbH. Platzhalter fuer die lokale Relaunch-Praesentation.",
            "h1": "Datenschutz",
            "kicker": "Rechtliches",
            "lead": "",
            "image": "placeholder-01.png",
            "cluster": "legal",
        },
    ]
    for page in legal_pages:
        text = "Diese Seite ist ein Platzhalter. Vor Veroeffentlichung muessen Anbieterkennzeichnung, Datenschutz, Hosting, Formularverarbeitung, Cookies und Tracking rechtlich final geprueft werden."
        url_to_file(page["path"]).parent.mkdir(parents=True, exist_ok=True)
        url_to_file(page["path"]).write_text(layout(page, legal_body(page["h1"], text)), encoding="utf-8")


def write_alias_pages(redirect_rows: list[dict[str, str]]) -> None:
    public_paths = {page["path"] for page in PAGES} | {"/impressum/", "/datenschutz/"}
    for row in redirect_rows:
        old_path = row.get("old_path", "")
        new_path = row.get("new_path", "/")
        if not old_path or old_path in public_paths:
            continue
        target = url_to_file(old_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target_rel = rel(target, new_path)
        page = {
            "path": old_path,
            "title": "Weiterleitung | Donau-Ries Haustechnik",
            "description": f"Diese alte URL bleibt erhalten und wird im Livebetrieb per 301 auf {new_path} weitergeleitet.",
            "h1": "Diese URL bleibt erhalten.",
            "kicker": "URL-Schutz",
            "lead": "",
            "image": "placeholder-01.png",
            "cluster": "alias",
        }
        body = f"""
<section class="section alias">
  <span class="kicker">URL-Schutz</span>
  <h1>Diese alte URL bleibt erhalten.</h1>
  <p>Im Livebetrieb wird diese Adresse per 301 auf die passende neue Seite weitergeleitet. Lokal zeigen wir diese Hinweis-Seite, damit keine alte Adresse als 404 endet.</p>
  <a class="button primary" href="{target_rel}">Zur neuen passenden Seite</a>
</section>
"""
        target.write_text(layout(page, body, noindex=True), encoding="utf-8")


def write_seo_files(redirect_rows: list[dict[str, str]]) -> None:
    sitemap_paths = [page["path"] for page in PAGES] + ["/impressum/", "/datenschutz/"]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in sitemap_paths:
        lines.append(f"  <url><loc>{page_url(path)}</loc></url>")
    lines.append("</urlset>")
    (STATIC / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (STATIC / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: https://donau-ries-haustechnik.de/sitemap.xml\n",
        encoding="utf-8",
    )
    htaccess = ["# Donau-Ries static migration redirects", "RewriteEngine On"]
    for row in redirect_rows:
        if row.get("redirect_type") != "301":
            continue
        old_path = row.get("old_path", "").strip("/")
        new_path = row.get("new_path", "/")
        if old_path:
            htaccess.append(f"Redirect 301 /{old_path}/ {new_path}")
    (STATIC / ".htaccess").write_text("\n".join(htaccess) + "\n", encoding="utf-8")


def write_url_report(redirect_rows: list[dict[str, str]]) -> None:
    kept = sum(1 for row in redirect_rows if row.get("redirect_type") == "keep 200")
    redirects = sum(1 for row in redirect_rows if row.get("redirect_type") == "301")
    report = f"""# URL Preservation Report

- Old URLs inventoried: {len(redirect_rows)}
- Canonical pages kept as 200: {kept}
- Old URLs mapped to 301 redirects: {redirects}
- Local preview alias pages generated for old URLs: {redirects}

The public launch should use `.htaccess` redirects from `static-site/.htaccess`.
Alias pages exist only so local preview URLs do not show 404 while designing.
"""
    (ROOT / "URL-PRESERVATION-REPORT.md").write_text(report, encoding="utf-8")


def build() -> None:
    redirect_rows = read_redirect_rows()
    preserved_images = IMG_DIR if IMG_DIR.exists() else None
    temp_images = ROOT / ".tmp-placeholder-images"
    if preserved_images and preserved_images.exists():
        if temp_images.exists():
            shutil.rmtree(temp_images)
        shutil.copytree(preserved_images, temp_images)
    if STATIC.exists():
        shutil.rmtree(STATIC)
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    if temp_images.exists():
        for item in temp_images.iterdir():
            shutil.copy2(item, IMG_DIR / item.name)
        shutil.rmtree(temp_images)
    write_assets()
    for page in PAGES:
        write_page(page)
    write_legal_pages()
    write_alias_pages(redirect_rows)
    write_seo_files(redirect_rows)
    write_url_report(redirect_rows)


CSS = """
:root {
  --ink: #10252b;
  --muted: #5f7075;
  --bg: #f4f8f9;
  --paper: #ffffff;
  --line: #dce7ea;
  --teal: #056b73;
  --teal-dark: #0d3e47;
  --gold: #d6a334;
  --soft: #eaf3f4;
  --shadow: 0 22px 60px rgba(16, 37, 43, .13);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  color: var(--ink);
  background: var(--bg);
  line-height: 1.55;
}
a { color: inherit; }
.utility {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  padding: 8px clamp(18px, 4vw, 54px);
  background: var(--teal-dark);
  color: #e9f5f6;
  font-size: 14px;
}
.utility a { color: #fff; font-weight: 700; text-decoration: none; }
.site-header {
  position: sticky;
  top: 0;
  z-index: 10;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  align-items: center;
  gap: 22px;
  padding: 16px clamp(18px, 4vw, 54px);
  background: rgba(255, 255, 255, .92);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(220, 231, 234, .9);
}
.brand {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  min-width: 218px;
  text-decoration: none;
}
.brand-mark {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 8px;
  background: var(--teal);
  color: #fff;
  font-weight: 900;
}
.brand strong, .brand small { display: block; }
.brand small { color: var(--muted); font-size: 13px; }
.main-nav {
  display: flex;
  justify-content: center;
  gap: 3px;
  flex: 1;
  flex-wrap: nowrap;
  min-width: 0;
}
.main-nav a {
  padding: 9px 10px;
  border-radius: 8px;
  color: #20383f;
  font-size: 14px;
  text-decoration: none;
  white-space: nowrap;
}
.main-nav a:hover, .main-nav a[aria-current="page"] { background: var(--soft); color: var(--teal); }
.nav-cta, .button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 0 18px;
  border-radius: 8px;
  border: 1px solid transparent;
  font-weight: 800;
  text-decoration: none;
  cursor: pointer;
}
.nav-cta, .button.primary { background: var(--gold); color: #17252a; }
.button.ghost { background: #fff; border-color: var(--line); color: var(--teal-dark); }
.button.light { background: #fff; color: var(--teal-dark); }
.hero, .sub-hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(360px, .86fr);
  align-items: center;
  gap: clamp(28px, 5vw, 70px);
  max-width: 1240px;
  margin: 0 auto;
  padding: clamp(44px, 7vw, 92px) clamp(18px, 4vw, 54px);
}
.hero-copy { max-width: 720px; }
.kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--teal);
  font-size: 13px;
  font-weight: 900;
  letter-spacing: .08em;
  text-transform: uppercase;
}
h1, h2, h3, p { margin-top: 0; }
h1 {
  margin-bottom: 20px;
  font-size: clamp(42px, 6vw, 76px);
  line-height: .98;
  letter-spacing: 0;
}
.sub-hero {
  grid-template-columns: minmax(0, .9fr) minmax(340px, .78fr);
  padding-top: clamp(52px, 6vw, 78px);
  padding-bottom: clamp(42px, 5vw, 68px);
}
.sub-hero h1 {
  max-width: 680px;
  font-size: clamp(40px, 5vw, 62px);
  line-height: 1.02;
}
.sub-hero p {
  max-width: 620px;
}
h2 { margin-bottom: 18px; font-size: clamp(30px, 4vw, 48px); line-height: 1.08; letter-spacing: 0; }
h3 { font-size: 22px; line-height: 1.18; }
p { color: var(--muted); font-size: 18px; }
.hero-actions { display: flex; flex-wrap: wrap; gap: 12px; margin: 28px 0; }
.trust-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.trust-row span {
  padding: 8px 12px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: #fff;
  color: var(--muted);
  font-size: 14px;
  font-weight: 700;
}
.hero-media, .sub-hero > img {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: var(--shadow);
  background: #dfe9ec;
}
.hero-media img, .sub-hero > img {
  display: block;
  width: 100%;
  aspect-ratio: 4 / 3.1;
  object-fit: cover;
}
.floating-card {
  position: absolute;
  right: 18px;
  bottom: 18px;
  max-width: 270px;
  padding: 16px;
  border-radius: 8px;
  background: rgba(255, 255, 255, .94);
  box-shadow: 0 14px 34px rgba(16, 37, 43, .16);
}
.floating-card strong, .floating-card span { display: block; }
.floating-card span { color: var(--muted); font-size: 14px; margin-top: 4px; }
.section {
  max-width: 1240px;
  margin: 0 auto;
  padding: clamp(44px, 7vw, 82px) clamp(18px, 4vw, 54px);
}
.proof-strip {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1px;
  max-width: 1240px;
  margin: -20px auto 0;
  padding: 0 clamp(18px, 4vw, 54px);
}
.proof-strip div {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 86px;
  padding: 18px 22px;
  background: #fff;
  border: 1px solid var(--line);
}
.proof-strip div:first-child { border-radius: 8px 0 0 8px; }
.proof-strip div:last-child { border-radius: 0 8px 8px 0; }
.proof-strip strong {
  color: var(--gold);
  font-size: 26px;
}
.proof-strip span {
  color: var(--teal-dark);
  font-weight: 800;
}
.intro-grid, .feature-layout, .contact-section {
  display: grid;
  grid-template-columns: minmax(0, .9fr) minmax(320px, 1.1fr);
  gap: 44px;
  align-items: start;
}
.service-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  margin-top: 26px;
}
.service-card {
  min-height: 230px;
  padding: 24px;
  border-radius: 8px;
  background: var(--paper);
  border: 1px solid var(--line);
  text-decoration: none;
  transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
.service-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow);
  border-color: rgba(5, 107, 115, .35);
}
.service-card span {
  color: var(--teal);
  font-size: 13px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: .08em;
}
.service-card p { font-size: 16px; }
.process { background: var(--paper); border-radius: 8px; box-shadow: 0 1px 0 var(--line); }
.steps {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  margin-top: 24px;
}
.steps > div, .feature-panel {
  padding: 24px;
  border-radius: 8px;
  background: var(--soft);
  border: 1px solid var(--line);
}
.steps b { color: var(--gold); font-size: 30px; }
.feature-panel ul { margin: 0; padding-left: 20px; color: var(--muted); }
.detail-cards {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  padding-top: 16px;
}
.detail-cards article {
  min-height: 250px;
  padding: 26px;
  border-radius: 8px;
  background: #fff;
  border: 1px solid var(--line);
  box-shadow: 0 14px 36px rgba(16, 37, 43, .08);
}
.detail-cards span {
  display: inline-flex;
  margin-bottom: 18px;
  color: var(--teal);
  font-size: 13px;
  font-weight: 900;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.related {
  padding-top: 22px;
}
.related div {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 18px;
}
.related a {
  padding: 12px 15px;
  border-radius: 8px;
  background: #fff;
  border: 1px solid var(--line);
  text-decoration: none;
  font-weight: 800;
}
.cta-band {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  max-width: 1240px;
  margin: 34px auto 76px;
  padding: 36px clamp(18px, 4vw, 54px);
  border-radius: 8px;
  background: var(--teal);
  color: #fff;
}
.cta-band h2 { margin: 6px 0 0; color: #fff; }
.cta-band .kicker, .cta-band p { color: #e5f2f3; }
form {
  display: grid;
  gap: 14px;
  padding: 24px;
  border-radius: 8px;
  background: #fff;
  border: 1px solid var(--line);
  box-shadow: var(--shadow);
}
label { display: grid; gap: 7px; color: var(--teal-dark); font-weight: 800; }
input, textarea {
  width: 100%;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 13px 14px;
  font: inherit;
}
textarea { min-height: 130px; resize: vertical; }
.form-notice { min-height: 24px; margin: 0; color: var(--teal); font-weight: 800; }
.legal, .alias { min-height: 52vh; }
.footer {
  background: var(--teal-dark);
  color: #e8f4f5;
  padding: 42px clamp(18px, 4vw, 54px);
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.2fr .6fr .6fr;
  gap: 28px;
  max-width: 1240px;
  margin: 0 auto;
}
.footer p { color: #cfe0e3; }
.footer span, .footer strong { display: block; margin-bottom: 10px; color: #fff; }
.footer a { display: block; color: #e8f4f5; text-decoration: none; margin: 7px 0; }
.mobile-action { display: none; }
@media (max-width: 980px) {
  .site-header { display: flex; align-items: flex-start; flex-direction: column; }
  .main-nav { justify-content: flex-start; flex-wrap: wrap; }
  .hero, .sub-hero, .intro-grid, .feature-layout, .contact-section { grid-template-columns: 1fr; }
  .service-grid, .steps, .footer-grid, .proof-strip, .detail-cards { grid-template-columns: 1fr; }
  .proof-strip { margin-top: 0; }
  .proof-strip div, .proof-strip div:first-child, .proof-strip div:last-child { border-radius: 8px; }
  .nav-cta { display: none; }
}
@media (max-width: 640px) {
  .utility { display: none; }
  h1 { font-size: 40px; }
  .hero, .sub-hero, .section { padding-left: 16px; padding-right: 16px; }
  .cta-band { margin-left: 16px; margin-right: 16px; flex-direction: column; align-items: flex-start; }
  .mobile-action {
    position: fixed;
    left: 14px;
    right: 14px;
    bottom: 14px;
    z-index: 20;
    display: flex;
    justify-content: center;
    padding: 14px;
    border-radius: 8px;
    background: var(--gold);
    color: #17252a;
    font-weight: 900;
    text-decoration: none;
    box-shadow: 0 14px 34px rgba(16, 37, 43, .2);
  }
}
"""


if __name__ == "__main__":
    build()
