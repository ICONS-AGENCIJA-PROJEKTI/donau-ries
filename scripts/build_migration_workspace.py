from __future__ import annotations

import csv
import html
import json
import re
import shutil
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path


DOMAIN = "https://donau-ries-haustechnik.de"
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ARCHIVE = ROOT / "placeholder-archive"
STATIC = ROOT / "static-site"
ASSETS = STATIC / "assets"
PLACEHOLDER_ASSETS = ASSETS / "placeholder-images"

KEY_PATHS = [
    "/",
    "/bad/",
    "/badsanierung/",
    "/badplanung/",
    "/barrierefreies-bad/",
    "/heizung/",
    "/waermepumpe/",
    "/solar/",
    "/lueftung/",
    "/haustechnik/",
    "/installation/",
    "/leistungen-gewerbekunden/",
    "/unternehmen/",
    "/kontaktformular/",
    "/jobs/",
    "/impressum/",
    "/datenschutz/",
]

PUBLIC_PAGES = [
    {
        "path": "/",
        "title": "Haustechnik in Donau-Ries | Heizung, Bad, Solar",
        "description": "Donau-Ries Haustechnik plant und modernisiert Bad, Heizung, Lueftung und Solar fuer Privat- und Gewerbekunden in der Region.",
        "h1": "Haustechnik fuer Donau-Ries: Bad, Heizung, Lueftung und Solar",
        "lead": "Ein moderner Auftritt fuer einen regionalen SHK-Fachbetrieb: klar, schnell, vertrauensbildend und vorbereitet fuer eine sichere SEO-Migration.",
        "section": "Die Startseite fuehrt Besucher schnell zu den wichtigsten Leistungen und staerkt lokale Suchsignale fuer Donau-Ries, Noerdlingen und Umgebung.",
        "image": "homepage-hero",
    },
    {
        "path": "/bad/",
        "title": "Badplanung und Badsanierung | Donau-Ries Haustechnik",
        "description": "Neue Baeder, Badmodernisierung und barrierearme Loesungen aus einer Hand fuer Kunden in Donau-Ries.",
        "h1": "Badplanung und Badsanierung aus einer Hand",
        "lead": "Von der ersten Idee bis zur fertigen Umsetzung: die Bad-Seite wird als klare Leistungsseite mit Beratung, Planung und Ausfuehrung aufgebaut.",
        "section": "Wichtig fuer SEO: ein eindeutiger H1, klare Unterthemen, interne Links zu Badplanung, barrierefreiem Bad und Kontakt.",
        "image": "bad",
    },
    {
        "path": "/heizung/",
        "title": "Heizung modernisieren | Donau-Ries Haustechnik",
        "description": "Heizungsmodernisierung, Waermepumpe, Gas, Holz und Foerderberatung fuer Gebaeude in Donau-Ries.",
        "h1": "Heizung planen, modernisieren und effizient betreiben",
        "lead": "Die Heizungsseite buendelt die wichtigsten Systeme und fuehrt Nutzer zu Beratung, Foerderung und konkreten Modernisierungsanfragen.",
        "section": "Bestehende Unterseiten wie Waermepumpe, Oel-/Gasheizung, Holz und Foerderung bleiben per URL oder Redirect erreichbar.",
        "image": "heizung",
    },
    {
        "path": "/solar/",
        "title": "Solar und erneuerbare Energie | Donau-Ries Haustechnik",
        "description": "Solartechnik als Baustein moderner Haustechnik: Beratung, Planung und Integration mit Heizungssystemen.",
        "h1": "Solartechnik sinnvoll in die Haustechnik integrieren",
        "lead": "Die Solar-Seite wird als schlanke, lokale Landingpage fuer Energieeffizienz und Systemberatung aufgebaut.",
        "section": "Copy und Bilder werden neu erstellt; die URL bleibt erhalten, damit bestehende Signale nicht verloren gehen.",
        "image": "solar",
    },
    {
        "path": "/lueftung/",
        "title": "Lueftung und Wohnraumlueftung | Donau-Ries Haustechnik",
        "description": "Kontrollierte Lueftung, dezentrale Wohnraumlueftung und Luftqualitaet fuer moderne Gebaeude.",
        "h1": "Lueftung fuer gesunde Raumluft und effiziente Gebaeude",
        "lead": "Die Lueftungsseite erklaert Nutzen, Einsatzbereiche und naechste Schritte fuer Privat- und Gewerbekunden.",
        "section": "Interne Links fuehren zu dezentraler Wohnraumlueftung, Haustechnik und Kontakt.",
        "image": "lueftung",
    },
    {
        "path": "/haustechnik/",
        "title": "Haustechnik Service | Donau-Ries Haustechnik",
        "description": "Installation, Wassertechnik, Entkalkung und technische Loesungen fuer Haus und Gewerbe.",
        "h1": "Haustechnik, die im Alltag verlaesslich funktioniert",
        "lead": "Diese Seite verbindet technische Dienstleistungen mit klaren Anfragewegen und lokaler Kompetenz.",
        "section": "Bestehende Themen wie Installation, Entkalkung und Regen-/Grauwassernutzung werden sauber verlinkt.",
        "image": "haustechnik",
    },
    {
        "path": "/leistungen-gewerbekunden/",
        "title": "Haustechnik fuer Gewerbekunden | Donau-Ries",
        "description": "Objekt- und Anlagenbau, Sanitaer, Heizung und technische Betreuung fuer gewerbliche Kunden.",
        "h1": "Loesungen fuer Gewerbekunden und Objekte",
        "lead": "Die Gewerbeseite wird als eigener Conversion-Pfad fuer Unternehmen, Verwaltungen und Objektbetreiber geplant.",
        "section": "Die bestehende URL bleibt erhalten, weil sie fuer interne und externe Verweise wichtig sein kann.",
        "image": "gewerbe",
    },
    {
        "path": "/unternehmen/",
        "title": "Unternehmen | Donau-Ries Haustechnik GmbH",
        "description": "Informationen ueber Donau-Ries Haustechnik, regionale Naehe, Team und Arbeitsweise.",
        "h1": "Regional verwurzelt, technisch erfahren",
        "lead": "Die Unternehmensseite staerkt Vertrauen mit echter Firmeninformation, Teambezug und Nachweisen.",
        "section": "Hier sollten spaeter echte Fotos, Zertifikate, Partner und Firmenfakten ergaenzt werden.",
        "image": "unternehmen",
    },
    {
        "path": "/kontaktformular/",
        "title": "Kontakt aufnehmen | Donau-Ries Haustechnik",
        "description": "Kontakt zu Donau-Ries Haustechnik fuer Beratung, Angebot und Rueckruf zu Bad, Heizung, Lueftung und Solar.",
        "h1": "Kontakt aufnehmen",
        "lead": "Die lokale Praesentation zeigt das Formular nur als Demo. Vor Livegang wird es an den echten Empfaenger und Datenschutztext angebunden.",
        "section": "Keine externen Daten werden aus dieser lokalen Version gesendet.",
        "image": "kontakt",
    },
]


@dataclass
class PageInfo:
    url: str
    path: str
    status: int = 0
    title: str = ""
    description: str = ""
    canonical: str = ""
    robots: str = ""
    h1: list[str] = field(default_factory=list)
    h2: list[str] = field(default_factory=list)
    images: list[dict[str, str]] = field(default_factory=list)
    links: list[str] = field(default_factory=list)
    schema_count: int = 0
    body_text: str = ""


class PageParser(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.title = ""
        self.description = ""
        self.canonical = ""
        self.robots = ""
        self.h1: list[str] = []
        self.h2: list[str] = []
        self.images: list[dict[str, str]] = []
        self.links: list[str] = []
        self.schema_count = 0
        self._capture: str | None = None
        self._text_parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        attr = {k.lower(): v or "" for k, v in attrs}
        tag = tag.lower()
        if tag in {"script", "style", "noscript"}:
            self._skip_depth += 1
        if tag == "title":
            self._capture = "title"
        elif tag in {"h1", "h2"}:
            self._capture = tag
        elif tag == "meta":
            name = attr.get("name", "").lower()
            if name == "description":
                self.description = attr.get("content", "").strip()
            elif name == "robots":
                self.robots = attr.get("content", "").strip()
        elif tag == "link" and attr.get("rel", "").lower() == "canonical":
            self.canonical = urllib.parse.urljoin(self.base_url, attr.get("href", ""))
        elif tag == "script" and attr.get("type", "").lower() == "application/ld+json":
            self.schema_count += 1
        elif tag == "img":
            src = attr.get("src") or attr.get("data-src") or attr.get("data-lazy-src") or ""
            if src:
                self.images.append(
                    {
                        "src": urllib.parse.urljoin(self.base_url, src),
                        "alt": attr.get("alt", ""),
                    }
                )
        elif tag == "a" and attr.get("href"):
            self.links.append(urllib.parse.urljoin(self.base_url, attr["href"]))

    def handle_endtag(self, tag: str):
        tag = tag.lower()
        if tag in {"script", "style", "noscript"} and self._skip_depth:
            self._skip_depth -= 1
        if self._capture == tag:
            self._capture = None

    def handle_data(self, data: str):
        text = re.sub(r"\s+", " ", data).strip()
        if not text:
            return
        if self._capture == "title":
            self.title += text
        elif self._capture == "h1":
            self.h1.append(text)
        elif self._capture == "h2":
            self.h2.append(text)
        if self._skip_depth == 0:
            self._text_parts.append(text)

    @property
    def body_text(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self._text_parts)).strip()


def fetch(url: str, timeout: int = 12) -> tuple[int, bytes, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; DonauRiesMigrationAudit/1.0; internal placeholder archive)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, response.read(), response.headers.get("content-type", "")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read(), exc.headers.get("content-type", "")
    except Exception as exc:
        return 0, str(exc).encode("utf-8"), "text/plain"


def slug_for_path(path: str) -> str:
    if path == "/":
        return "index"
    return path.strip("/").replace("/", "__") or "index"


def parse_sitemap_urls() -> list[str]:
    urls: set[str] = set()
    for sitemap in [f"{DOMAIN}/sitemap_index.xml", f"{DOMAIN}/page-sitemap.xml"]:
        status, content, _ = fetch(sitemap)
        if status != 200:
            continue
        try:
            root = ET.fromstring(content)
        except ET.ParseError:
            continue
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        for loc in root.findall(".//sm:loc", ns):
            if loc.text and loc.text.startswith(DOMAIN):
                if loc.text.endswith(".xml"):
                    child_status, child_content, _ = fetch(loc.text)
                    if child_status == 200:
                        try:
                            child_root = ET.fromstring(child_content)
                            for child_loc in child_root.findall(".//sm:loc", ns):
                                if child_loc.text and child_loc.text.startswith(DOMAIN):
                                    urls.add(child_loc.text)
                        except ET.ParseError:
                            pass
                else:
                    urls.add(loc.text)
    for path in KEY_PATHS:
        urls.add(urllib.parse.urljoin(DOMAIN, path))
    return sorted(urls, key=lambda item: (urllib.parse.urlparse(item).path.count("/"), item))


def crawl_pages(urls: list[str]) -> list[PageInfo]:
    pages: list[PageInfo] = []
    raw_dir = ARCHIVE / "source-html"
    text_dir = ARCHIVE / "source-text"
    raw_dir.mkdir(parents=True, exist_ok=True)
    text_dir.mkdir(parents=True, exist_ok=True)
    for url in urls:
        path = urllib.parse.urlparse(url).path or "/"
        slug = slug_for_path(path)
        cached_html = raw_dir / f"{slug}.html"
        if cached_html.exists():
            status = 200
            content = cached_html.read_bytes()
            content_type = "text/html"
        else:
            status, content, content_type = fetch(url)
        info = PageInfo(url=url, path=path, status=status)
        if "html" in content_type and content:
            text = content.decode("utf-8", errors="replace")
            parser = PageParser(url)
            parser.feed(text)
            info.title = parser.title.strip()
            info.description = parser.description
            info.canonical = parser.canonical
            info.robots = parser.robots
            info.h1 = parser.h1
            info.h2 = parser.h2
            info.images = parser.images
            info.links = [
                link
                for link in parser.links
                if link.startswith(DOMAIN) and "#" not in link
            ]
            info.schema_count = parser.schema_count
            info.body_text = parser.body_text[:5000]
            (raw_dir / f"{slug}.html").write_text(text, encoding="utf-8")
            (text_dir / f"{slug}.txt").write_text(
                "INTERNAL PLACEHOLDER/REFERENCE ONLY - DO NOT PUBLISH COPIED COPY\n\n"
                + info.body_text,
                encoding="utf-8",
            )
        pages.append(info)
        time.sleep(0.03)
    return pages


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def inventory_exports(pages: list[PageInfo]) -> None:
    write_csv(
        DATA / "url-inventory.csv",
        [
            {
                "url": p.url,
                "path": p.path,
                "status": p.status,
                "title": p.title,
                "meta_description": p.description,
                "canonical": p.canonical,
                "robots": p.robots,
                "h1_count": len(p.h1),
                "h1": " | ".join(p.h1),
                "h2_sample": " | ".join(p.h2[:5]),
                "schema_count": p.schema_count,
                "image_count": len(p.images),
                "internal_link_count": len(set(p.links)),
            }
            for p in pages
        ],
        [
            "url",
            "path",
            "status",
            "title",
            "meta_description",
            "canonical",
            "robots",
            "h1_count",
            "h1",
            "h2_sample",
            "schema_count",
            "image_count",
            "internal_link_count",
        ],
    )
    image_rows = []
    for p in pages:
        for image in p.images:
            image_rows.append(
                {
                    "page_url": p.url,
                    "image_url": image["src"],
                    "alt": image.get("alt", ""),
                    "placeholder_only": "yes",
                    "publish_allowed": "unknown - replace or verify license",
                }
            )
    write_csv(
        DATA / "image-inventory.csv",
        image_rows,
        ["page_url", "image_url", "alt", "placeholder_only", "publish_allowed"],
    )
    redirect_rows = []
    public_paths = {page["path"] for page in PUBLIC_PAGES}
    for p in pages:
        target = p.path if p.path in public_paths else closest_target(p.path)
        redirect_rows.append(
            {
                "old_url": p.url,
                "old_path": p.path,
                "new_path": target,
                "redirect_type": "keep 200" if target == p.path else "301",
                "notes": "Indexable public page" if target == p.path else "Map to closest relevant static page before launch",
            }
        )
    write_csv(
        DATA / "redirect-map.csv",
        redirect_rows,
        ["old_url", "old_path", "new_path", "redirect_type", "notes"],
    )
    issues = []
    for p in pages:
        if p.status != 200:
            issues.append({"url": p.url, "issue": f"Status {p.status}", "priority": "High"})
        if not p.title:
            issues.append({"url": p.url, "issue": "Missing title", "priority": "High"})
        if p.title.lower().startswith("home"):
            issues.append({"url": p.url, "issue": "Generic title starts with Home", "priority": "Medium"})
        if not p.description:
            issues.append({"url": p.url, "issue": "Missing meta description", "priority": "High"})
        if len(p.h1) != 1:
            issues.append({"url": p.url, "issue": f"H1 count is {len(p.h1)}", "priority": "Medium"})
        if not p.canonical:
            issues.append({"url": p.url, "issue": "Missing canonical", "priority": "Medium"})
        missing_alt = sum(1 for img in p.images if not img.get("alt"))
        if missing_alt:
            issues.append({"url": p.url, "issue": f"{missing_alt} image(s) missing alt text", "priority": "Medium"})
    write_csv(DATA / "seo-issues.csv", issues, ["url", "issue", "priority"])


def closest_target(path: str) -> str:
    rules = [
        ("bad", "/bad/"),
        ("dusch", "/bad/"),
        ("heizung", "/heizung/"),
        ("waermepumpe", "/heizung/"),
        ("gas", "/heizung/"),
        ("pellet", "/heizung/"),
        ("foerder", "/heizung/"),
        ("solar", "/solar/"),
        ("lueft", "/lueftung/"),
        ("gewerbe", "/leistungen-gewerbekunden/"),
        ("objekt", "/leistungen-gewerbekunden/"),
        ("anlage", "/leistungen-gewerbekunden/"),
        ("kontakt", "/kontaktformular/"),
        ("danke", "/kontaktformular/"),
        ("job", "/jobs/"),
        ("unternehmen", "/unternehmen/"),
        ("impressum", "/impressum/"),
        ("datenschutz", "/datenschutz/"),
    ]
    lower = path.lower()
    for needle, target in rules:
        if needle in lower:
            return target
    return "/"


def download_placeholder_images(pages: list[PageInfo]) -> dict[str, str]:
    PLACEHOLDER_ASSETS.mkdir(parents=True, exist_ok=True)
    picked: list[str] = []
    for page in pages:
        if page.path in {p["path"] for p in PUBLIC_PAGES}:
            for img in page.images:
                src = img.get("src", "")
                if src.startswith(DOMAIN) and src not in picked and not src.startswith("data:"):
                    picked.append(src)
                if len(picked) >= 10:
                    break
        if len(picked) >= 10:
            break
    mapping: dict[str, str] = {}
    fallback_keys = ["homepage-hero", "bad", "heizung", "lueftung", "haustechnik", "unternehmen", "kontakt"]
    for index, url in enumerate(picked):
        parsed = urllib.parse.urlparse(url)
        ext = Path(parsed.path).suffix.lower() or ".jpg"
        filename = f"placeholder-{index + 1:02d}{ext}"
        status, content, content_type = fetch(url, timeout=8)
        if status == 200 and content and ("image" in content_type or ext in {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}):
            (PLACEHOLDER_ASSETS / filename).write_bytes(content)
            if index < len(fallback_keys):
                mapping[fallback_keys[index]] = f"assets/placeholder-images/{filename}"
    for key in ["solar", "gewerbe"]:
        mapping.setdefault(key, mapping.get("heizung", "assets/placeholder.svg"))
    return mapping


def write_static_site(image_map: dict[str, str]) -> None:
    STATIC.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "placeholder.svg").write_text(
        """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720">
<rect width="1200" height="720" fill="#e9eef2"/>
<path d="M0 560 C220 470 380 650 600 540 S960 420 1200 520 V720 H0 Z" fill="#cad7df"/>
<circle cx="930" cy="180" r="82" fill="#d6b25e"/>
<text x="80" y="130" font-family="Arial, sans-serif" font-size="42" font-weight="700" fill="#18313f">Placeholder image</text>
<text x="80" y="188" font-family="Arial, sans-serif" font-size="24" fill="#455a64">Replace before publication</text>
</svg>""",
        encoding="utf-8",
    )
    css = """
:root {
  --ink: #15242e;
  --muted: #5e6b73;
  --line: #d9e1e6;
  --brand: #0d5b78;
  --brand-2: #d8a841;
  --bg: #f7f9fa;
  --white: #fff;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: Arial, Helvetica, sans-serif; color: var(--ink); background: var(--bg); line-height: 1.55; }
a { color: inherit; }
.topbar { background: #0b3345; color: #fff; font-size: 14px; padding: 8px 24px; }
.nav { display: flex; align-items: center; justify-content: space-between; gap: 24px; padding: 18px 24px; background: #fff; border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 5; }
.brand { font-weight: 800; letter-spacing: .02em; color: var(--brand); text-decoration: none; }
.links { display: flex; gap: 18px; flex-wrap: wrap; font-size: 15px; }
.links a { text-decoration: none; color: var(--ink); }
.hero { display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(320px, .95fr); gap: 36px; align-items: center; max-width: 1180px; margin: 0 auto; padding: 56px 24px; }
.eyebrow { color: var(--brand); font-weight: 800; text-transform: uppercase; font-size: 13px; letter-spacing: .08em; }
h1 { font-size: clamp(34px, 5vw, 58px); line-height: 1.05; margin: 12px 0 18px; letter-spacing: 0; }
h2 { font-size: 28px; margin: 0 0 14px; }
p { color: var(--muted); font-size: 18px; }
.hero img, .page-hero img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; border-radius: 8px; display: block; }
.notice { background: #fff5d8; border: 1px solid #e6ca7b; color: #5f4700; padding: 12px 24px; font-size: 14px; }
.actions { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 26px; }
.btn { display: inline-flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 18px; border-radius: 6px; background: var(--brand); color: #fff; text-decoration: none; font-weight: 700; }
.btn.secondary { background: #fff; color: var(--brand); border: 1px solid var(--brand); }
.band { background: #fff; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
.section { max-width: 1180px; margin: 0 auto; padding: 48px 24px; }
.grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; }
.card { background: #fff; border: 1px solid var(--line); border-radius: 8px; padding: 22px; min-height: 170px; }
.card h3 { margin: 0 0 8px; font-size: 21px; }
.card p { margin: 0; font-size: 16px; }
.page-hero { max-width: 1180px; margin: 0 auto; padding: 42px 24px; display: grid; grid-template-columns: 1fr 380px; gap: 32px; align-items: center; }
.checklist { display: grid; gap: 12px; margin-top: 22px; }
.check { padding: 16px; background: #fff; border: 1px solid var(--line); border-radius: 8px; }
.footer { padding: 36px 24px; background: #0b3345; color: #dbe6eb; }
.footer-inner { max-width: 1180px; margin: 0 auto; display: flex; justify-content: space-between; gap: 20px; flex-wrap: wrap; }
.footer a { color: #fff; }
form { display: grid; gap: 12px; max-width: 640px; }
input, textarea { width: 100%; padding: 13px 14px; border: 1px solid var(--line); border-radius: 6px; font: inherit; }
textarea { min-height: 130px; }
@media (max-width: 860px) {
  .hero, .page-hero { grid-template-columns: 1fr; padding-top: 34px; }
  .grid { grid-template-columns: 1fr; }
  .nav { align-items: flex-start; flex-direction: column; }
}
"""
    (ASSETS / "styles.css").write_text(css.strip() + "\n", encoding="utf-8")
    nav = """
<div class="topbar">Interne lokale Praesentation - kopierte Inhalte/Bilder sind Placeholder und nicht fuer Veroeffentlichung freigegeben.</div>
<nav class="nav">
  <a class="brand" href="/index.html">Donau-Ries Haustechnik</a>
  <div class="links">
    <a href="/bad/index.html">Bad</a>
    <a href="/heizung/index.html">Heizung</a>
    <a href="/solar/index.html">Solar</a>
    <a href="/lueftung/index.html">Lueftung</a>
    <a href="/haustechnik/index.html">Haustechnik</a>
    <a href="/leistungen-gewerbekunden/index.html">Gewerbe</a>
    <a href="/kontaktformular/index.html">Kontakt</a>
  </div>
</nav>
"""
    footer = """
<footer class="footer">
  <div class="footer-inner">
    <div>Donau-Ries Haustechnik GmbH<br>Statische Relaunch-Praesentation</div>
    <div><a href="/impressum/index.html">Impressum</a> · <a href="/datenschutz/index.html">Datenschutz</a></div>
  </div>
</footer>
"""
    service_cards = """
<section class="band">
  <div class="section">
    <h2>Leistungsbereiche</h2>
    <div class="grid">
      <a class="card" href="/bad/index.html"><h3>Bad</h3><p>Planung, Sanierung und barrierearme Badloesungen.</p></a>
      <a class="card" href="/heizung/index.html"><h3>Heizung</h3><p>Modernisierung, Waermepumpe und effiziente Systeme.</p></a>
      <a class="card" href="/lueftung/index.html"><h3>Lueftung</h3><p>Raumluft, Komfort und Technik fuer moderne Gebaeude.</p></a>
    </div>
  </div>
</section>
"""
    for page in PUBLIC_PAGES:
        local = path_to_output(page["path"])
        local.parent.mkdir(parents=True, exist_ok=True)
        image = image_map.get(page["image"], "assets/placeholder.svg")
        image_path = relative_asset_path(local, image)
        canonical = f"{DOMAIN}{page['path']}"
        schema = schema_json(page)
        body = home_body(page, image_path) if page["path"] == "/" else subpage_body(page, image_path)
        content = f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(page['title'])}</title>
  <meta name="description" content="{html.escape(page['description'])}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="{relative_asset_path(local, 'assets/styles.css')}">
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
{nav}
<main>
{body}
</main>
{footer}
</body>
</html>
"""
        local.write_text(content, encoding="utf-8")
    write_legal_page("impressum", "Impressum", "Impressum", "Placeholder fuer die spaetere rechtlich gepruefte Anbieterkennzeichnung. Vor Livegang mit echten Firmendaten abgleichen.")
    write_legal_page("datenschutz", "Datenschutz", "Datenschutz", "Placeholder fuer die spaetere Datenschutzseite. Vor Livegang an Hosting, Formulare, Analytics und Cookie-Setup anpassen.")
    write_static_seo_files()


def path_to_output(path: str) -> Path:
    if path == "/":
        return STATIC / "index.html"
    return STATIC / path.strip("/") / "index.html"


def relative_asset_path(from_file: Path, asset: str) -> str:
    depth = len(from_file.parent.relative_to(STATIC).parts)
    prefix = "" if depth == 0 else "../" * depth
    return prefix + asset


def home_body(page: dict[str, str], image_path: str) -> str:
    return f"""
<section class="hero">
  <div>
    <div class="eyebrow">SEO-sicherer Relaunch · lokale Praesentation</div>
    <h1>{html.escape(page['h1'])}</h1>
    <p>{html.escape(page['lead'])}</p>
    <div class="actions">
      <a class="btn" href="/kontaktformular/index.html">Beratung anfragen</a>
      <a class="btn secondary" href="/heizung/index.html">Leistungen ansehen</a>
    </div>
  </div>
  <img src="{image_path}" alt="Placeholder fuer Haustechnik Startseitenmotiv">
</section>
<div class="notice">Diese lokale Version dient nur der Praesentation. Bilder und alte Textreferenzen muessen vor Veroeffentlichung ersetzt oder lizenziert werden.</div>
{service_cards_block()}
<section class="section">
  <h2>SEO-Migration im Blick</h2>
  <div class="checklist">
    <div class="check">Bestehende URLs werden erhalten oder per 301 weitergeleitet.</div>
    <div class="check">Jede Hauptseite bekommt eigenen Title, Description, Canonical, H1 und Schema.</div>
    <div class="check">Sitemap und robots.txt werden fuer die statische Hostinger-Version neu erstellt.</div>
  </div>
</section>
"""


def subpage_body(page: dict[str, str], image_path: str) -> str:
    form = ""
    if page["path"] == "/kontaktformular/":
        form = """
<form onsubmit="event.preventDefault(); alert('Demo: Diese lokale Praesentation sendet keine Daten.');">
  <input name="name" placeholder="Name" autocomplete="name">
  <input name="email" placeholder="E-Mail" autocomplete="email">
  <textarea name="message" placeholder="Worum geht es?"></textarea>
  <button class="btn" type="submit">Demo-Anfrage nicht senden</button>
</form>
"""
    return f"""
<section class="page-hero">
  <div>
    <div class="eyebrow">Statische Relaunch-Seite</div>
    <h1>{html.escape(page['h1'])}</h1>
    <p>{html.escape(page['lead'])}</p>
    <div class="actions">
      <a class="btn" href="/kontaktformular/index.html">Kontakt aufnehmen</a>
      <a class="btn secondary" href="/index.html">Zur Startseite</a>
    </div>
  </div>
  <img src="{image_path}" alt="Placeholder fuer {html.escape(page['h1'])}">
</section>
<section class="band">
  <div class="section">
    <h2>Geplanter Inhalt</h2>
    <p>{html.escape(page['section'])}</p>
    {form}
  </div>
</section>
<section class="section">
  <h2>Vor Livegang ersetzen</h2>
  <div class="checklist">
    <div class="check">Finale, einzigartige deutsche Copy ohne kopierte Agenturtexte.</div>
    <div class="check">Eigene oder lizenzierte Bilder mit passenden ALT-Texten.</div>
    <div class="check">Pruefung der alten URL im Redirect-Map-Export.</div>
  </div>
</section>
"""


def service_cards_block() -> str:
    return """
<section class="band">
  <div class="section">
    <h2>Direkt zu den wichtigsten Themen</h2>
    <div class="grid">
      <a class="card" href="/bad/index.html"><h3>Bad</h3><p>Badplanung, Sanierung und Modernisierung.</p></a>
      <a class="card" href="/heizung/index.html"><h3>Heizung</h3><p>Heizsysteme, Modernisierung und Foerderung.</p></a>
      <a class="card" href="/leistungen-gewerbekunden/index.html"><h3>Gewerbe</h3><p>Objekt- und Anlagenbau fuer Unternehmen.</p></a>
    </div>
  </div>
</section>
"""


def schema_json(page: dict[str, str]) -> dict[str, object]:
    url = f"{DOMAIN}{page['path']}"
    return {
        "@context": "https://schema.org",
        "@type": "Service" if page["path"] not in {"/", "/unternehmen/", "/kontaktformular/"} else "LocalBusiness",
        "name": page["h1"],
        "description": page["description"],
        "url": url,
        "areaServed": "Donau-Ries",
        "provider": {
            "@type": "LocalBusiness",
            "name": "Donau-Ries Haustechnik GmbH",
            "url": DOMAIN,
        },
    }


def write_legal_page(slug: str, title: str, h1: str, text: str) -> None:
    target = STATIC / slug / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | Donau-Ries Haustechnik</title>
  <meta name="description" content="{html.escape(text[:150])}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{DOMAIN}/{slug}/">
  <link rel="stylesheet" href="../assets/styles.css">
</head>
<body>
<div class="topbar">Interne lokale Praesentation - rechtliche Inhalte vor Livegang finalisieren.</div>
<nav class="nav"><a class="brand" href="/index.html">Donau-Ries Haustechnik</a><div class="links"><a href="/index.html">Start</a><a href="/kontaktformular/index.html">Kontakt</a></div></nav>
<main><section class="section"><h1>{html.escape(h1)}</h1><p>{html.escape(text)}</p></section></main>
<footer class="footer"><div class="footer-inner">Donau-Ries Haustechnik GmbH</div></footer>
</body>
</html>
""",
        encoding="utf-8",
    )


def write_static_seo_files() -> None:
    urls = [f"{DOMAIN}{page['path']}" for page in PUBLIC_PAGES] + [f"{DOMAIN}/impressum/", f"{DOMAIN}/datenschutz/"]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        sitemap.append(f"  <url><loc>{html.escape(url)}</loc></url>")
    sitemap.append("</urlset>")
    (STATIC / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    (STATIC / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: https://donau-ries-haustechnik.de/sitemap.xml\n",
        encoding="utf-8",
    )
    htaccess_lines = ["# Donau-Ries static migration redirects", "RewriteEngine On"]
    if (DATA / "redirect-map.csv").exists():
        with (DATA / "redirect-map.csv").open(encoding="utf-8-sig") as handle:
            for row in csv.DictReader(handle):
                if row["redirect_type"] == "301":
                    old = row["old_path"].strip("/")
                    new = row["new_path"]
                    if old:
                        htaccess_lines.append(f"Redirect 301 /{old}/ {new}")
    (STATIC / ".htaccess").write_text("\n".join(htaccess_lines) + "\n", encoding="utf-8")


def write_report(pages: list[PageInfo]) -> None:
    report = f"""# Donau-Ries Migration Implementation Report

Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}

## What was created

- Local static presentation in `website-migration/static-site/`
- Placeholder/reference archive in `website-migration/placeholder-archive/`
- URL inventory in `website-migration/data/url-inventory.csv`
- Redirect map in `website-migration/data/redirect-map.csv`
- Image inventory in `website-migration/data/image-inventory.csv`
- SEO issue export in `website-migration/data/seo-issues.csv`

## Important legal note

Downloaded source HTML/text/images are only for internal reference and presentation placeholders. Do not publish copied agency content or downloaded images without rights confirmation.

## Crawl summary

- Crawled URLs: {len(pages)}
- 200 responses: {sum(1 for p in pages if p.status == 200)}
- Non-200 responses: {sum(1 for p in pages if p.status != 200)}
- Pages missing meta description: {sum(1 for p in pages if not p.description)}
- Pages with H1 count not equal to 1: {sum(1 for p in pages if len(p.h1) != 1)}

## Next live migration tasks

1. Replace every placeholder image and all archived copy before publication.
2. Confirm real company NAP data, phone, email and legal pages.
3. Upload static files to Hostinger.
4. Enable `.htaccess` redirects or configure equivalent Hostinger redirect rules.
5. Submit `https://donau-ries-haustechnik.de/sitemap.xml` in Google Search Console.
6. Monitor 404s and ranking changes for at least 2-4 weeks.
"""
    (ROOT / "IMPLEMENTATION-REPORT.md").write_text(report, encoding="utf-8")


def main() -> None:
    for directory in [DATA, ARCHIVE, STATIC]:
        directory.mkdir(parents=True, exist_ok=True)
    urls = parse_sitemap_urls()
    pages = crawl_pages(urls)
    inventory_exports(pages)
    image_map = download_placeholder_images(pages)
    write_static_site(image_map)
    write_report(pages)


if __name__ == "__main__":
    main()
