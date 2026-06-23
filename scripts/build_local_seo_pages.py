from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "static-site"
DOMAIN = "https://donau-ries-haustechnik.de"


CITIES = [
    {
        "slug": "haustechnik-donauwoerth",
        "name": "Donauwörth",
        "title": "SHK-Fachbetrieb Donauwörth | Bad, Heizung & Wärmepumpe",
        "description": "Bad, Heizung, Wärmepumpe, Solar und Haustechnik für Donauwörth. Persönliche Beratung und saubere Umsetzung durch Donau-Ries Haustechnik aus Harburg.",
        "h1": "Haustechnik für Donauwörth – zuverlässig aus einer Hand.",
        "lead": "Ob neues Bad, Heizungsmodernisierung oder Wärmepumpe: Wir begleiten Eigentümer in Donauwörth von der Beratung bis zur fertigen Übergabe – mit einem festen Ansprechpartner.",
        "focus": "Modernisierung für Haus und Wohnung",
        "intro": "In Donauwörth treffen gewachsene Wohngebiete, sanierte Bestandsimmobilien und Neubauten aufeinander. Entsprechend unterschiedlich sind die Anforderungen an Bad, Heizung und Haustechnik. Wir planen nicht nach Schema F, sondern passend zu Gebäude, Budget und Alltag.",
        "benefit": "Kurze Abstimmung, klare Planung und ein regionaler Fachbetrieb aus dem Landkreis Donau-Ries.",
        "faq": [
            ("Kommt Donau-Ries Haustechnik für Projekte nach Donauwörth?", "Ja. Unser Firmensitz ist in Harburg und Donauwörth gehört zu unserem regionalen Einsatzgebiet. Den genauen Umfang klären wir bei der ersten Anfrage."),
            ("Welche Leistungen bieten Sie in Donauwörth an?", "Wir beraten und realisieren Badsanierungen, Heizungsmodernisierungen, Wärmepumpen, Solar, Lüftung und Sanitärinstallationen."),
            ("Ist eine Vor-Ort-Beratung möglich?", "Ja. Nach einem ersten Gespräch vereinbaren wir für passende Projekte einen Termin am Objekt und erstellen anschließend eine konkrete Planung."),
        ],
    },
    {
        "slug": "haustechnik-noerdlingen",
        "name": "Nördlingen",
        "title": "SHK-Fachbetrieb Nördlingen | Bad & Heizung modernisieren",
        "description": "Badsanierung, Heizung, Wärmepumpe und Haustechnik für Nördlingen. Regional geplant und umgesetzt von Donau-Ries Haustechnik in Harburg.",
        "h1": "Bad und Heizung für Nördlingen – durchdacht modernisiert.",
        "lead": "Für Bestandsgebäude und moderne Wohnhäuser in Nördlingen entwickeln wir Lösungen, die technisch passen, sauber aussehen und langfristig zuverlässig funktionieren.",
        "focus": "Sensible Lösungen für den Bestand",
        "intro": "Bei Modernisierungen in Nördlingen kommt es oft auf eine sorgfältige Bestandsaufnahme an: Welche Leitungen können bleiben, wie lässt sich der Grundriss sinnvoll nutzen und welches Heizsystem passt wirklich zum Gebäude? Wir verbinden ehrliche Beratung mit einer koordinierten Umsetzung.",
        "benefit": "Bestehende Bausubstanz respektieren, Technik sinnvoll erneuern und Kosten früh transparent machen.",
        "faq": [
            ("Betreuen Sie auch ältere Gebäude in Nördlingen?", "Ja. Gerade bei Bestandsgebäuden prüfen wir die vorhandene Technik sorgfältig und entwickeln eine Lösung, die zum Haus und zum geplanten Budget passt."),
            ("Übernehmen Sie komplette Badsanierungen?", "Ja. Wir koordinieren die Badsanierung von der Planung bis zur Übergabe und bündeln die beteiligten Gewerke über einen Ansprechpartner."),
            ("Beraten Sie zur passenden neuen Heizung?", "Ja. Wir betrachten Gebäude, Wärmebedarf und Nutzung, vergleichen geeignete Systeme und beziehen mögliche Förderungen in die Planung ein."),
        ],
    },
    {
        "slug": "haustechnik-dillingen",
        "name": "Dillingen an der Donau",
        "title": "Haustechnik Dillingen | Heizung, Wärmepumpe, Bad & Solar",
        "description": "Heizung, Wärmepumpe, Bad, Solar und Sanitär für Dillingen an der Donau. Beratung und Umsetzung aus einer Hand vom SHK-Fachbetrieb aus Harburg.",
        "h1": "Effiziente Haustechnik für Dillingen an der Donau.",
        "lead": "Wir unterstützen Hausbesitzer in Dillingen bei der energetischen Modernisierung, beim neuen Bad und bei zuverlässiger Sanitärtechnik – persönlich, strukturiert und regional.",
        "focus": "Energie und Wohnkomfort zusammendenken",
        "intro": "Eine neue Heizung wirkt sich auf mehr aus als den Energieverbrauch. Wärmeverteilung, Warmwasser, Lüftung und bei Bedarf Solar sollten als Gesamtsystem betrachtet werden. Für Projekte in Dillingen planen wir deshalb vom Gebäude aus – nicht vom einzelnen Gerät.",
        "benefit": "Heizung, Warmwasser, Solar und Sanitär technisch aufeinander abstimmen, statt Einzellösungen zu sammeln.",
        "faq": [
            ("Liegt Dillingen in Ihrem Einsatzgebiet?", "Dillingen an der Donau betreuen wir projektabhängig von unserem Firmensitz in Harburg aus. Fragen Sie Ihr Vorhaben kurz an, damit wir Termin und Umfang direkt prüfen können."),
            ("Planen Sie Wärmepumpen auch für Bestandsgebäude?", "Ja. Entscheidend sind Gebäudezustand, Heizflächen, Wärmebedarf und die gewünschte Nutzung. Diese Punkte prüfen wir vor einer Empfehlung gemeinsam."),
            ("Kann Solar mit der Heizung kombiniert werden?", "Je nach Gebäude und Ziel kann eine Kombination sinnvoll sein. Wir betrachten Erzeugung, Warmwasser und Verbrauch im Zusammenhang und erklären die passenden Varianten."),
        ],
    },
    {
        "slug": "haustechnik-neuburg-donau",
        "name": "Neuburg an der Donau",
        "title": "SHK-Fachbetrieb Neuburg an der Donau | Bad & Heizung",
        "description": "Badsanierung, Heizung, Wärmepumpe, Lüftung und Haustechnik für Neuburg an der Donau. Regionaler SHK-Service mit Sitz in Harburg.",
        "h1": "Moderne Haustechnik für Neuburg an der Donau.",
        "lead": "Vom komfortablen Bad bis zur effizienten Heizungsanlage: Wir planen technische Lösungen für Wohngebäude in Neuburg mit klaren Abläufen und einem Ansprechpartner.",
        "focus": "Komfort, Effizienz und saubere Umsetzung",
        "intro": "Ob umfassende Sanierung oder gezielte Modernisierung: Gute Haustechnik beginnt mit den richtigen Fragen. Wie wird das Gebäude genutzt, welche Technik ist vorhanden und welche Investition zahlt sich langfristig aus? Daraus entsteht eine belastbare Lösung für Ihr Projekt in Neuburg.",
        "benefit": "Beratung ohne Standardpaket, nachvollziehbare Entscheidungen und koordinierte Umsetzung bis zur Übergabe.",
        "faq": [
            ("Übernehmen Sie Projekte in Neuburg an der Donau?", "Wir betreuen Neuburg projektabhängig aus Harburg. Nach Ihrer Anfrage prüfen wir kurzfristig, ob Umfang und Termin zu unserem regionalen Einsatzplan passen."),
            ("Kann ich Bad und Heizung gemeinsam planen lassen?", "Ja. Bei einer größeren Modernisierung kann die gemeinsame Planung Schnittstellen reduzieren und den Bauablauf deutlich übersichtlicher machen."),
            ("Bieten Sie auch Lüftungs- und Sanitärtechnik an?", "Ja. Neben Bad und Heizung gehören kontrollierte Wohnraumlüftung, Sanitärinstallation, Wassertechnik und weitere Haustechnik zu unserem Angebot."),
        ],
    },
    {
        "slug": "haustechnik-rain",
        "name": "Rain",
        "region": "Bayern",
        "title": "SHK-Fachbetrieb Rain | Heizung, Wärmepumpe & Bad",
        "description": "Heizung, Wärmepumpe, Bad, Solar und Sanitär für Rain am Lech. Regionaler SHK-Fachbetrieb mit Sitz in Harburg im Landkreis Donau-Ries.",
        "h1": "Haustechnik für Rain – effizient und regional umgesetzt.",
        "lead": "Von der Heizungsmodernisierung bis zum neuen Bad planen und realisieren wir Haustechnik für Wohngebäude in Rain – mit kurzen Wegen und einem festen Ansprechpartner.",
        "focus": "Modernisieren mit Plan",
        "intro": "Rain verbindet gewachsene Ortskerne mit neuen Wohngebieten. Damit Heizung, Bad und Sanitärtechnik dauerhaft funktionieren, betrachten wir jedes Projekt vom Gebäude aus und stimmen die Gewerke sauber aufeinander ab.",
        "benefit": "Kurze Wege aus dem Landkreis Donau-Ries, klare Planung und ein fester Ansprechpartner für Ihr Projekt.",
        "faq": [
            ("Ist Rain Teil Ihres Einsatzgebiets?", "Ja. Rain liegt nahe unserem Firmensitz in Harburg und gehört zu unserem regionalen Einsatzgebiet. Den genauen Umfang klären wir bei Ihrer Anfrage."),
            ("Lohnt sich eine Wärmepumpe in meinem Haus?", "Das hängt von Gebäudezustand, Heizflächen und Wärmebedarf ab. Wir prüfen diese Punkte vor Ort und rechnen Ihnen die passende Lösung transparent durch."),
            ("Übernehmen Sie die komplette Badsanierung?", "Ja. Wir koordinieren alle Gewerke von der Demontage bis zur Übergabe – Sie haben einen Ansprechpartner und einen Festpreis."),
        ],
    },
    {
        "slug": "haustechnik-oettingen",
        "name": "Oettingen in Bayern",
        "region": "Bayern",
        "title": "Haustechnik Oettingen i. Bay. | Bad, Heizung & Solar",
        "description": "Bad, Heizung, Wärmepumpe, Solar und Sanitär für Oettingen in Bayern. Persönliche Beratung vom SHK-Fachbetrieb aus Harburg im Landkreis Donau-Ries.",
        "h1": "Bad und Heizung für Oettingen – sorgfältig modernisiert.",
        "lead": "Für die historisch geprägten Wohngebäude und modernen Häuser in Oettingen entwickeln wir Haustechnik-Lösungen, die technisch passen und langfristig zuverlässig funktionieren.",
        "focus": "Sorgfalt im Bestand",
        "intro": "Gerade in Oettingen mit seinem charakteristischen Altstadtkern lohnt sich eine sorgfältige Bestandsaufnahme: Welche Leitungen bleiben, wie wird der Grundriss sinnvoll genutzt und welche Heizung passt zum Gebäude? Wir verbinden ehrliche Beratung mit sauberer Umsetzung.",
        "benefit": "Bausubstanz respektieren, Technik sinnvoll erneuern und Kosten früh transparent machen.",
        "faq": [
            ("Betreuen Sie auch ältere Gebäude in Oettingen?", "Ja. Bei Bestandsgebäuden prüfen wir die vorhandene Technik genau und entwickeln eine Lösung, die zum Haus und zum Budget passt."),
            ("Beraten Sie zur Förderung einer neuen Heizung?", "Ja. Wir kennen die aktuellen Förderprogramme und beziehen mögliche Zuschüsse von Anfang an in die Planung ein."),
            ("Wie schnell bekomme ich einen Termin?", "Nach Ihrer Anfrage melden wir uns zeitnah und stimmen für passende Projekte einen Vor-Ort-Termin ab."),
        ],
    },
    {
        "slug": "haustechnik-augsburg",
        "name": "Augsburg",
        "region": "Bayern",
        "title": "SHK-Fachbetrieb für Augsburg | Bad, Heizung & Wärmepumpe",
        "description": "Badsanierung, Heizung, Wärmepumpe, Solar und Haustechnik für Augsburg und Umgebung. Geplant und umgesetzt von Donau-Ries Haustechnik aus Harburg.",
        "h1": "Moderne Haustechnik für Augsburg und Umgebung.",
        "lead": "Ob Stadthaus, Reihenhaus oder Wohnung: Wir planen Bad, Heizung und Haustechnik für Projekte in Augsburg strukturiert, sauber und mit einem festen Ansprechpartner.",
        "focus": "Stadt und Umland zuverlässig betreut",
        "intro": "In Augsburg und im Umland reichen die Anforderungen vom sanierten Altbau bis zum modernen Neubau. Wir planen nicht nach Schema F, sondern passend zu Gebäude, Nutzung und Budget – und koordinieren alle Gewerke über einen Ansprechpartner.",
        "benefit": "Ein regionaler Fachbetrieb, der Planung und Umsetzung aus einer Hand übernimmt.",
        "faq": [
            ("Fahren Sie für Projekte nach Augsburg?", "Augsburg betreuen wir projektabhängig von unserem Firmensitz in Harburg aus. Senden Sie uns Ort und Vorhaben, dann prüfen wir Umfang und Termin direkt."),
            ("Welche Leistungen bieten Sie in Augsburg an?", "Badsanierung, Heizungsmodernisierung, Wärmepumpe, Solar, Lüftung sowie Sanitär- und Haustechnik – auf Wunsch gemeinsam geplant."),
            ("Kann ich Bad und Heizung zusammen modernisieren?", "Ja. Eine gemeinsame Planung reduziert Schnittstellen und macht den Bauablauf deutlich übersichtlicher."),
        ],
    },
    {
        "slug": "haustechnik-aalen",
        "name": "Aalen",
        "region": "Baden-Württemberg",
        "title": "Haustechnik Aalen | Heizung, Wärmepumpe, Bad & Solar",
        "description": "Heizung, Wärmepumpe, Badsanierung, Solar und Sanitär für Aalen in Baden-Württemberg. Regionaler SHK-Service vom Fachbetrieb aus Harburg.",
        "h1": "Effiziente Haustechnik für Aalen.",
        "lead": "Wir unterstützen Hausbesitzer in Aalen bei der energetischen Modernisierung, beim neuen Bad und bei zuverlässiger Sanitärtechnik – persönlich, strukturiert und regional.",
        "focus": "Energie und Wohnkomfort zusammendenken",
        "intro": "Eine neue Heizung wirkt sich auf mehr aus als den Energieverbrauch. Wärmeverteilung, Warmwasser, Lüftung und bei Bedarf Solar gehören als Gesamtsystem betrachtet. Für Projekte in Aalen planen wir deshalb vom Gebäude aus – nicht vom einzelnen Gerät.",
        "benefit": "Heizung, Warmwasser, Solar und Sanitär technisch aufeinander abstimmen statt Einzellösungen zu sammeln.",
        "faq": [
            ("Liegt Aalen in Ihrem Einsatzgebiet?", "Aalen in Baden-Württemberg betreuen wir projektabhängig von Harburg aus. Fragen Sie Ihr Vorhaben kurz an, damit wir Termin und Umfang prüfen können."),
            ("Planen Sie Wärmepumpen auch für Bestandsgebäude?", "Ja. Entscheidend sind Gebäudezustand, Heizflächen, Wärmebedarf und Nutzung – diese Punkte prüfen wir vor einer Empfehlung gemeinsam."),
            ("Bieten Sie auch komplette Badsanierungen an?", "Ja. Wir planen und realisieren Badsanierungen aus einer Hand, inklusive Koordination aller Gewerke und transparentem Festpreis."),
        ],
    },
    {
        "slug": "haustechnik-heidenheim",
        "name": "Heidenheim an der Brenz",
        "region": "Baden-Württemberg",
        "title": "SHK-Fachbetrieb Heidenheim | Bad, Heizung & Wärmepumpe",
        "description": "Badsanierung, Heizung, Wärmepumpe, Lüftung und Haustechnik für Heidenheim an der Brenz. Regionaler SHK-Service mit Sitz in Harburg.",
        "h1": "Haustechnik für Heidenheim – durchdacht und zuverlässig.",
        "lead": "Vom komfortablen Bad bis zur effizienten Heizungsanlage planen wir technische Lösungen für Wohngebäude in Heidenheim mit klaren Abläufen und einem Ansprechpartner.",
        "focus": "Komfort, Effizienz und saubere Umsetzung",
        "intro": "Ob umfassende Sanierung oder gezielte Modernisierung – gute Haustechnik beginnt mit den richtigen Fragen: Wie wird das Gebäude genutzt, welche Technik ist vorhanden und welche Investition zahlt sich langfristig aus? Daraus entsteht eine belastbare Lösung für Ihr Projekt in Heidenheim.",
        "benefit": "Beratung ohne Standardpaket, nachvollziehbare Entscheidungen und koordinierte Umsetzung bis zur Übergabe.",
        "faq": [
            ("Übernehmen Sie Projekte in Heidenheim?", "Heidenheim an der Brenz betreuen wir projektabhängig aus Harburg. Nach Ihrer Anfrage prüfen wir kurzfristig Umfang und Termin."),
            ("Kann ich Bad und Heizung gemeinsam planen lassen?", "Ja. Bei einer größeren Modernisierung reduziert die gemeinsame Planung Schnittstellen und macht den Ablauf übersichtlicher."),
            ("Bieten Sie auch Lüftungs- und Sanitärtechnik an?", "Ja. Neben Bad und Heizung gehören Wohnraumlüftung, Sanitärinstallation und weitere Haustechnik zu unserem Angebot."),
        ],
    },
    {
        "slug": "haustechnik-bopfingen",
        "name": "Bopfingen",
        "region": "Baden-Württemberg",
        "title": "Haustechnik Bopfingen | Heizung, Bad, Wärmepumpe & Solar",
        "description": "Heizung, Wärmepumpe, Bad, Solar und Sanitär für Bopfingen in Baden-Württemberg. Persönliche Beratung vom SHK-Fachbetrieb aus Harburg.",
        "h1": "Haustechnik für Bopfingen – nah an der Region.",
        "lead": "Direkt an der Grenze zu Bayern gelegen, ist Bopfingen für uns gut erreichbar. Wir planen Bad, Heizung und Haustechnik mit kurzen Wegen und einem festen Ansprechpartner.",
        "focus": "Nah, persönlich, planbar",
        "intro": "Bopfingen liegt unweit von Nördlingen und damit gut in unserem Einsatzbereich. Für Bestandsgebäude und moderne Wohnhäuser entwickeln wir Lösungen, die technisch passen, sauber aussehen und langfristig zuverlässig funktionieren.",
        "benefit": "Gute Erreichbarkeit, ehrliche Beratung und eine koordinierte Umsetzung aus einer Hand.",
        "faq": [
            ("Ist Bopfingen Teil Ihres Einsatzgebiets?", "Ja. Bopfingen liegt nah an Nördlingen und ist für uns gut erreichbar. Den genauen Umfang klären wir bei Ihrer Anfrage."),
            ("Beraten Sie zur passenden neuen Heizung?", "Ja. Wir betrachten Gebäude, Wärmebedarf und Nutzung, vergleichen geeignete Systeme und beziehen mögliche Förderungen ein."),
            ("Ist eine Vor-Ort-Beratung möglich?", "Ja. Für passende Projekte vereinbaren wir einen Termin am Objekt und erstellen anschließend eine konkrete Planung."),
        ],
    },
]


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def schema(city: dict[str, object]) -> dict[str, object]:
    questions = [
        {
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {"@type": "Answer", "text": answer},
        }
        for question, answer in city["faq"]
    ]
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "name": f"SHK- und Haustechnik-Leistungen in {city['name']}",
                "serviceType": "Badsanierung, Heizung, Wärmepumpe, Solar, Lüftung und Sanitär",
                "url": f"{DOMAIN}/{city['slug']}/",
                "areaServed": {"@type": "City", "name": city["name"]},
                "provider": {
                    "@type": ["LocalBusiness", "HVACBusiness", "PlumbingBusiness"],
                    "name": "Donau-Ries Haustechnik GmbH",
                    "url": f"{DOMAIN}/",
                    "telephone": "+49 9080 4317",
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": "Goethestraße 1",
                        "postalCode": "86655",
                        "addressLocality": "Harburg",
                        "addressRegion": "Bayern",
                        "addressCountry": "DE",
                    },
                },
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Start", "item": f"{DOMAIN}/"},
                    {"@type": "ListItem", "position": 2, "name": "Einsatzgebiet", "item": f"{DOMAIN}/einsatzgebiet/"},
                    {"@type": "ListItem", "position": 3, "name": city["name"], "item": f"{DOMAIN}/{city['slug']}/"},
                ],
            },
            {"@type": "FAQPage", "mainEntity": questions},
        ],
    }


def header() -> str:
    return """
<div class="utility">
  <span>SHK-Fachbetrieb in Harburg · <a href="tel:+4990804317">09080 4317</a> · <a href="mailto:info@donau-ries-haustechnik.de">info@donau-ries-haustechnik.de</a></span>
  <a href="../kontaktformular/">Rückruf anfragen</a>
</div>
<header class="site-header">
  <a class="brand" href="../"><img class="brand-logo" src="../assets/logo-hero.webp" alt="Donau-Ries Haustechnik"></a>
  <nav class="main-nav" aria-label="Hauptnavigation"><a href="../">Home</a><div class="nav-dropdown"><button class="nav-dropdown-toggle" type="button" aria-expanded="false">Leistungen</button><div class="nav-dropdown-menu"><a href="../bad/">Bad</a><a href="../heizung/">Heizung</a><a href="../solar/">Solar</a><a href="../lueftung/">Lüftung</a><a href="../haustechnik/">Haustechnik</a></div></div><a href="../leistungen-gewerbekunden/">Gewerbe</a><a href="../unternehmen/">Unternehmen</a><a href="../blog/">Blog</a><a href="../kontaktformular/">Kontakt</a></nav>
  <div class="header-actions"><a class="header-phone" href="tel:+4990804317">09080 4317</a><a class="nav-cta" href="../kontaktformular/">Anfrage starten</a></div>
  <button class="nav-toggle" type="button" aria-label="Menü öffnen" aria-expanded="false"><span></span><span></span><span></span></button>
</header>
"""


def footer() -> str:
    return """
<section class="leistungen-band" aria-label="Unsere Leistungen im Überblick">
  <span class="kicker">Leistungen im Überblick</span><h2>Wählen Sie Ihren Bereich.</h2>
  <div class="leistungen-grid">
    <a href="../bad/"><strong>Bad</strong><span>Sanierung &amp; Planung</span></a>
    <a href="../heizung/"><strong>Heizung</strong><span>Modernisierung</span></a>
    <a href="../solar/"><strong>Solar</strong><span>Photovoltaik</span></a>
    <a href="../lueftung/"><strong>Lüftung</strong><span>Wohnraumlüftung</span></a>
    <a href="../haustechnik/"><strong>Haustechnik</strong><span>Installation</span></a>
    <a href="../einsatzgebiet/"><strong>Region</strong><span>Einsatzgebiet</span></a>
  </div>
</section>
<footer class="footer">
  <div class="footer-grid">
    <div><img class="footer-logo" src="../assets/logo-white.png" alt="Donau-Ries Haustechnik"><p>Ihr SHK-Fachbetrieb für Bad, Heizung, Solar und Lüftung mit Sitz in Harburg – in Bayern und Baden-Württemberg im Einsatz.</p></div>
    <div><span>Leistungen</span><a href="../bad/">Bad</a><a href="../heizung/">Heizung</a><a href="../solar/">Solar</a><a href="../haustechnik/">Haustechnik</a><a href="../einsatzgebiet/">Einsatzgebiet</a></div>
    <div><span>Kontakt</span><a href="tel:+4990804317">09080 4317</a><a href="mailto:info@donau-ries-haustechnik.de">info@donau-ries-haustechnik.de</a><a href="https://maps.google.com/?q=Goethestra%C3%9Fe+1,+86655+Harburg" rel="noopener" target="_blank">Goethestraße 1, 86655 Harburg</a></div>
    <div><span>Rechtliches</span><a href="../kontaktformular/">Kontakt</a><a href="../impressum/">Impressum</a><a href="../datenschutz/">Datenschutz</a></div>
  </div>
  <div class="footer-bottom"><span>© 2026 Donau-Ries Haustechnik GmbH · Alle Rechte vorbehalten</span><span>Mo–Fr nach Vereinbarung · <a href="tel:+4990804317">09080 4317</a></span></div>
</footer>
<a class="mobile-action" href="../kontaktformular/">Projekt anfragen</a>
<script src="../assets/site-modern.js"></script>
<div class="contact-fab" data-contact-fab><div class="contact-fab-options" hidden><a class="cfab-opt" href="tel:+4990804317">Anrufen</a><a class="cfab-opt" href="mailto:info@donau-ries-haustechnik.de">E-Mail</a><a class="cfab-opt" href="../kontaktformular/">Nachricht</a></div><button class="contact-fab-toggle" type="button" aria-label="Kontakt aufnehmen" aria-expanded="false">☎</button></div>
"""


def page_shell(title: str, description: str, canonical: str, body: str, page_schema: dict[str, object]) -> str:
    return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{canonical}">
  <link rel="stylesheet" href="../assets/styles-modern.css">
  <script type="application/ld+json">{json.dumps(page_schema, ensure_ascii=False)}</script>
</head>
<body>{header()}<main>{body}</main>{footer()}</body>
</html>
"""


def city_page(city: dict[str, object]) -> str:
    faq_html = "".join(f'<div class="faq-item"><h3>{esc(q)}</h3><p>{esc(a)}</p></div>' for q, a in city["faq"])
    other_cities = "".join(
        f'<a href="../{item["slug"]}/">{esc(item["name"])}</a>'
        for item in CITIES
        if item["slug"] != city["slug"]
    )
    body = f"""
<nav class="breadcrumbs" aria-label="Brotkrümelnavigation"><a href="../">Start</a><span>›</span><a href="../einsatzgebiet/">Einsatzgebiet</a><span>›</span><span>{esc(city['name'])}</span></nav>
<section class="page-hero local-hero" style="background-image:linear-gradient(90deg, rgba(37,60,140,.92) 0%, rgba(37,60,140,.62) 50%, rgba(37,60,140,.28) 100%), url('../assets/images/hero-heizung.jpg')">
  <div class="hero-copy"><span class="kicker">SHK-Fachbetrieb für {esc(city['name'])}</span><h1>{esc(city['h1'])}</h1><p>{esc(city['lead'])}</p><div class="hero-actions"><a class="button primary" href="../kontaktformular/">Kostenlose Erstberatung</a><a class="button ghost" href="tel:+4990804317">09080 4317</a></div></div>
</section>
<section class="proof-strip" aria-label="Ihre Vorteile"><div><strong>01</strong><span>Firmensitz in Harburg</span></div><div><strong>02</strong><span>Ein fester Ansprechpartner</span></div><div><strong>03</strong><span>Planung und Umsetzung aus einer Hand</span></div></section>
<section class="section intro-grid"><div><span class="kicker">{esc(city['focus'])}</span><h2>Technik, die zum Gebäude und zu Ihrem Alltag passt.</h2></div><div><p>{esc(city['intro'])}</p><p><strong>{esc(city['benefit'])}</strong></p></div></section>
<section class="section"><span class="kicker">Leistungen in {esc(city['name'])}</span><h2>Was wir für Ihr Zuhause planen und umsetzen.</h2><div class="service-grid">
  <a class="service-card" href="../bad/"><span>Komplett aus einer Hand</span><h3>Badsanierung</h3><p>Individuelle Badplanung, Komplettbad und barrierearme Lösungen mit klarer Koordination.</p></a>
  <a class="service-card" href="../heizung/"><span>Effizient modernisieren</span><h3>Heizung</h3><p>Passende Heiztechnik für Bestand und Neubau – inklusive Systemvergleich und Planung.</p></a>
  <a class="service-card" href="../heizung/"><span>Gebäude richtig prüfen</span><h3>Wärmepumpe</h3><p>Auslegung von Wärmequelle, Heizflächen und Warmwasser passend zu Ihrem Gebäude.</p></a>
  <a class="service-card" href="../solar/"><span>Energie sinnvoll nutzen</span><h3>Solar</h3><p>Photovoltaik und Solar als durchdachter Baustein Ihrer Energie- und Haustechnik.</p></a>
  <a class="service-card" href="../lueftung/"><span>Gesundes Raumklima</span><h3>Lüftung</h3><p>Kontrollierte Wohnraumlüftung für Komfort, Feuchteschutz und Energieeffizienz.</p></a>
  <a class="service-card" href="../haustechnik/"><span>Zuverlässige Installation</span><h3>Sanitär &amp; Haustechnik</h3><p>Wassertechnik, Sanitärinstallation und technische Gebäudelösungen vom Fachbetrieb.</p></a>
</div></section>
<section class="section process"><span class="kicker">So starten wir</span><h2>Vom ersten Gespräch zur passenden Lösung.</h2><div class="steps"><div><b>01</b><h3>Projekt anfragen</h3><p>Sie schildern kurz Gebäude, Standort und gewünschte Leistung.</p></div><div><b>02</b><h3>Vor Ort prüfen</h3><p>Bei passenden Projekten nehmen wir Bestand und Anforderungen am Objekt auf.</p></div><div><b>03</b><h3>Klar planen</h3><p>Sie erhalten eine nachvollziehbare Lösung mit abgestimmtem Ablauf.</p></div></div></section>
<section class="section faq"><span class="kicker">Häufige Fragen</span><h2>Haustechnik in {esc(city['name'])}: kurz beantwortet.</h2><div class="faq-list">{faq_html}</div></section>
<section class="section related"><span class="kicker">Weitere Orte</span><h2>Unser regionales Einsatzgebiet.</h2><div>{other_cities}<a href="../einsatzgebiet/">Alle Orte ansehen</a></div></section>
<section class="cta-band"><div><span class="kicker">Kostenlose Erstberatung</span><h2>Planen Sie ein Projekt in {esc(city['name'])}?</h2></div><a class="button light" href="../kontaktformular/">Jetzt Projekt anfragen</a></section>
"""
    return page_shell(city["title"], city["description"], f"{DOMAIN}/{city['slug']}/", body, schema(city))


def hub_page() -> str:
    def cards_for(region: str) -> str:
        return "".join(
            f'<a class="service-card city-card" href="../{city["slug"]}/"><span>Bad · Heizung · Haustechnik</span><h3>{esc(city["name"])}</h3><p>{esc(city["benefit"])}</p></a>'
            for city in CITIES
            if city.get("region", "Bayern") == region
        )
    cards_bayern = cards_for("Bayern")
    cards_bw = cards_for("Baden-Württemberg")
    hub_schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "name": "Einsatzgebiet Donau-Ries Haustechnik",
                "url": f"{DOMAIN}/einsatzgebiet/",
                "description": "Einsatzgebiet für Bad, Heizung, Wärmepumpe, Solar und Haustechnik in Bayern und Baden-Württemberg, mit Firmensitz in Harburg.",
                "about": [
                    {"@type": "AdministrativeArea", "name": "Bayern"},
                    {"@type": "AdministrativeArea", "name": "Baden-Württemberg"},
                ],
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Start", "item": f"{DOMAIN}/"},
                    {"@type": "ListItem", "position": 2, "name": "Einsatzgebiet", "item": f"{DOMAIN}/einsatzgebiet/"},
                ],
            },
        ],
    }
    body = f"""
<nav class="breadcrumbs" aria-label="Brotkrümelnavigation"><a href="../">Start</a><span>›</span><span>Einsatzgebiet</span></nav>
<section class="page-hero local-hero" style="background-image:linear-gradient(90deg, rgba(37,60,140,.92) 0%, rgba(37,60,140,.62) 50%, rgba(37,60,140,.28) 100%), url('../assets/images/hero-haustechnik.jpg')"><div class="hero-copy"><span class="kicker">Regionaler SHK-Fachbetrieb</span><h1>Haustechnik in Bayern &amp; Baden-Württemberg.</h1><p>Mit Firmensitz in Harburg (Schwaben) sind wir in Bayern und Baden-Württemberg weit im Einsatz – von der Region Donau-Ries bis nach Ostwürttemberg, persönlich und aus einer Hand.</p><div class="hero-actions"><a class="button primary" href="../kontaktformular/">Einsatzort anfragen</a><a class="button ghost" href="tel:+4990804317">09080 4317</a></div></div></section>
<section class="section intro-grid"><div><span class="kicker">Unser Einsatzgebiet</span><h2>In Bayern und Baden-Württemberg unterwegs.</h2></div><p>Unser Firmensitz ist in Harburg (Schwaben). Von dort sind wir in ganz Bayern und Baden-Württemberg im Einsatz – von der Region Donau-Ries über das schwäbische Umland bis nach Ostwürttemberg. Ob Ihr konkretes Projekt in unseren Einsatzplan passt, klären wir schnell und persönlich.</p></section>
<section class="section"><span class="kicker">Standorte in Bayern</span><h2>Im Raum Donau-Ries und Schwaben.</h2><div class="service-grid local-city-grid">{cards_bayern}</div></section>
<section class="section"><span class="kicker">Standorte in Baden-Württemberg</span><h2>In Ostwürttemberg und Umgebung.</h2><div class="service-grid local-city-grid">{cards_bw}</div></section>
<section class="section feature-layout"><div><span class="kicker">Projektabhängige Anfahrt</span><h2>Die richtige Lösung beginnt mit einer kurzen Anfrage.</h2><p>Entfernung allein entscheidet nicht. Projektumfang, Leistung und Termin müssen sinnvoll zusammenpassen. Senden Sie uns deshalb Ort und Vorhaben – wir sagen Ihnen offen, ob und wann wir helfen können.</p></div><div class="feature-panel"><h3>Bitte direkt mitsenden</h3><ul><li>Ort und Postleitzahl des Projekts</li><li>Gewünschte Leistung: Bad, Heizung, Solar oder Haustechnik</li><li>Bestand, Neubau oder geplante Sanierung</li><li>Gewünschter Zeitraum</li></ul></div></section>
<section class="cta-band"><div><span class="kicker">Schnelle Standortprüfung</span><h2>Ist Ihr Ort nicht aufgeführt?</h2><p>Fragen Sie trotzdem kurz an – wir prüfen den Einsatz projektabhängig.</p></div><a class="button light" href="../kontaktformular/">Projekt und Ort senden</a></section>
"""
    return page_shell(
        "Einsatzgebiet | SHK-Fachbetrieb in Bayern & Baden-Württemberg",
        "Unser Einsatzgebiet für Bad, Heizung, Wärmepumpe, Solar und Haustechnik: Harburg, Donauwörth, Nördlingen, Augsburg, Aalen, Heidenheim und weitere Orte in Bayern und Baden-Württemberg.",
        f"{DOMAIN}/einsatzgebiet/",
        body,
        hub_schema,
    )


def write(path: str, content: str) -> None:
    target = STATIC / path / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def main() -> None:
    write("einsatzgebiet", hub_page())
    for city in CITIES:
        write(city["slug"], city_page(city))


if __name__ == "__main__":
    main()
