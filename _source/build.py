# -*- coding: utf-8 -*-
"""Static site generator for torsten-kai-jachmann's homepage.

Usage (from the repository root):   python3 _source/build.py
Writes plain HTML pages into the repository root (English) and /de/ (German).
No dependencies beyond the Python standard library.
"""
import html, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from content import *  # noqa
from ja import JA  # English text -> Japanese
MISSING = []
LANGS = ("en", "de", "ja")
LANG_NAMES = {"en": "English", "de": "Deutsch", "ja": "日本語"}
LANG_SHORT = {"en": "EN", "de": "DE", "ja": "日本語"}
ME_JA = "トーステン・カイ・ヤッハマン"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE_URL = ""          # e.g. "https://username.github.io" – optional, used for canonical links
YEAR = datetime.date.today().year
e = html.escape

# Original pixel sizes of photos (ratio only matters). Files: assets/img/<name>-{640,1200}.jpg
PHOTOS = {
    "portrait": (1152, 1536), "japan-lake": (1536, 1152), "japan-university-gate": (1536, 1152),
    "japan-garden": (1536, 1536), "brazil-coast": (1536, 1152), "japan-plum-blossoms": (1400, 1050),
    "japan-torii": (1400, 1050), "japan-osaka-castle": (825, 1100), "berlin-reichstag": (1500, 1125),
    "london-eye": (1500, 1125), "boston-mit": (1500, 1125), "san-francisco": (1400, 1050),
    "knit-sweater": (931, 1536), "knit-grey": (1536, 1152), "knit-lace-blue": (1152, 1536),
    "knit-cable": (1152, 1536), "cake-berry": (1152, 1536), "cake-slice": (1536, 1152),
    "cake-flowers": (1536, 1527), "cake-layers": (1152, 1536),
}

PAGES = ["index", "research", "publications", "teaching", "cv", "personal", "contact"]
NAV = {
    "research":     {"en": "Research", "de": "Forschung", "ja": "研究"},
    "publications": {"en": "Publications", "de": "Publikationen", "ja": "業績"},
    "teaching":     {"en": "Teaching", "de": "Lehre", "ja": "教育"},
    "cv":           {"en": "CV", "de": "Lebenslauf", "ja": "経歴"},
    "personal":     {"en": "Beyond the lab", "de": "Persönliches", "ja": "プライベート"},
    "contact":      {"en": "Contact", "de": "Kontakt", "ja": "連絡先"},
}


class Ctx:
    def __init__(self, lang, slug):
        self.lang, self.slug = lang, slug
        self.pre = "" if lang == "en" else "../"

    def t(self, en, de, ja=None):
        if self.lang == "en":
            return en
        if self.lang == "de":
            return de
        if ja is not None:
            return ja
        if en not in JA:
            MISSING.append(en)
            return en
        return JA[en]

    def url(self, u):
        return u if re.match(r"^(https?:|mailto:|#)", u) else self.pre + u

    def page(self, slug, anchor=""):
        return ("index.html" if slug == "index" else slug + ".html") + anchor


# ---------------------------------------------------------------- helpers
def img(c, name, alt, sizes="(min-width: 900px) 50vw, 100vw", eager=False, cls=""):
    w, h = PHOTOS[name]
    H = round(1200 * h / w) if w >= h else 1200
    W = 1200 if w >= h else round(1200 * w / h)
    base = c.pre + "assets/img/" + name
    return (f'<img{" class=%s" % cls if cls else ""} src="{base}-1200.jpg" '
            f'srcset="{base}-640.jpg 640w, {base}-1200.jpg 1200w" sizes="{sizes}" '
            f'width="{W}" height="{H}" alt="{e(alt)}" '
            f'{"" if eager else "loading=" + chr(34) + "lazy" + chr(34) + " "}decoding="async">')


def ext(u):
    return ' target="_blank" rel="noopener"' if (u.startswith("http") or u.endswith(".pdf")) else ""


def authors(a):
    return e(a).replace(e(ME), f"<strong>{e(ME)}</strong>")


def pub_item(c, p, show_year=True):
    venue = p["venue"]
    if p["type"] == "thesis":
        venue = DEGREE[p["degree"]][c.lang] + " · " + venue
    note = ""
    if p.get("note") == "slam":
        note = f' <span class="pub-note">{c.t("Selected for the poster slam", "Für den Poster-Slam ausgewählt")}</span>'
    links = "".join(
        f'<a class="res" href="{e(c.url(u))}"{ext(u)}>{LINK_LABELS[k][c.lang]}<span aria-hidden="true"> ↗</span></a>'
        for k, u in p["links"])
    yr = f'<span class="pub-year">{p["year"]}</span>' if show_year else ""
    return (f'<li class="pub">{yr}<div class="pub-body">'
            f'<p class="pub-title">{e(p["title"])}</p>'
            f'<p class="pub-authors">{authors(p["authors"])}</p>'
            f'<p class="pub-venue">{e(venue)}{note}</p>'
            f'<p class="pub-links">{links}</p></div></li>')


def layout(c, title, desc, body):
    def href_for(l):
        return c.pre + ("" if l == "en" else l + "/") + c.page(c.slug)
    switch = "".join(
        f'<a href="{href_for(l)}" hreflang="{l}" lang="{l}"{" aria-current=" + chr(34) + "true" + chr(34) if l == c.lang else ""}><span class="ln-long">{LANG_NAMES[l]}</span><span class="ln-short" aria-hidden="true">{LANG_SHORT[l]}</span></a>'
        for l in LANGS)
    nav = "".join(
        f'<a href="{c.page(s)}"{" aria-current=" + chr(34) + "page" + chr(34) if s == c.slug else ""}>{NAV[s][c.lang]}</a>'
        for s in PAGES if s != "index")
    full_title = ME if c.slug == "index" else f"{title} · {ME}"
    return f"""<!doctype html>
<html lang="{c.lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="{ME}">
<meta name="theme-color" content="#003153">
{"".join(f'<link rel="alternate" hreflang="{l}" href="{href_for(l)}">' for l in LANGS)}
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<link rel="icon" href="{c.pre}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{c.pre}assets/css/style.css">
</head>
<body class="page-{c.slug}">
<a class="skip" href="#main">{c.t("Skip to content", "Zum Inhalt springen")}</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">TKJ</span><span class="brand-name">{ME}</span></a>
    <nav class="site-nav" aria-label="{c.t("Main", "Hauptnavigation")}">{nav}</nav>
    <nav class="lang-switch" aria-label="{c.t("Language", "Sprache")}">{switch}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <p class="footer-name">{ME}</p>
      <p>{c.t("Postdoctoral researcher · Psycholinguistics", "Wissenschaftlicher Mitarbeiter (Postdoc) · Psycholinguistik")}<br>{c.t("Saarland University, Saarbrücken", "Universität des Saarlandes, Saarbrücken")}</p>
    </div>
    <div>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="mailto:{EMAIL_PRIVATE}">{EMAIL_PRIVATE}</a></p>
      <p><a href="{c.page('contact')}#legal">{c.t("Legal notice &amp; privacy", "Impressum &amp; Datenschutz")}</a></p>
    </div>
    <p class="footer-copy">© {YEAR} {ME}</p>
  </div>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------- pages
def page_index(c):
    feat = [p for p in PUBLICATIONS if p.get("featured")]
    hsp = PUBLICATIONS[[p["year"] for p in PUBLICATIONS].index(2026)]
    poster = c.url(dict(hsp["links"])["poster"])
    abstract = c.url(dict(hsp["links"])["abstract"])
    body = f"""
<section class="hero wrap">
  <div class="hero-text">
    <p class="eyebrow">{c.t("Psycholinguistics · Saarland University", "Psycholinguistik · Universität des Saarlandes")}</p>
    <h1>{ME}</h1>{'<p class="name-kana">' + ME_JA + '</p>' if c.lang == "ja" else ""}
    <p class="lead">{c.t(
        "I study how people build expectations while they understand language – from a speaker’s glance at an object to the order in which words arrive and what is already known in the conversation.",
        "Ich erforsche, wie Menschen beim Sprachverstehen Erwartungen aufbauen – vom Blick eines Sprechers auf ein Objekt bis zur Reihenfolge, in der Wörter eintreffen, und dem, was im Gespräch bereits bekannt ist.")}</p>
    <p class="hero-meta">{c.t("Postdoctoral researcher, Psycholinguistics Group, Department of Language Science and Technology", "Wissenschaftlicher Mitarbeiter (Postdoc), Arbeitsgruppe Psycholinguistik, Fachrichtung Sprachwissenschaft und Sprachtechnologie")}</p>
    <p class="actions"><a class="btn" href="{c.page('research')}">{c.t("Research", "Forschung")}</a><a class="btn btn-ghost" href="{c.page('publications')}">{c.t("Publications", "Publikationen")}</a></p>
  </div>
  <figure class="hero-portrait">{img(c, "portrait", c.t("Portrait of Torsten Kai Jachmann", "Porträt von Torsten Kai Jachmann"), "(min-width: 900px) 380px, 70vw", eager=True)}</figure>
</section>

<section class="band band-blue">
  <div class="wrap feature">
    <div class="feature-text">
      <p class="eyebrow eyebrow-light">{c.t("Latest work · HSP 2026, MIT", "Aktuell · HSP 2026, MIT")}</p>
      <h2>{c.t("Word order and givenness in German and Korean", "Wortstellung und Gegebenheit im Deutschen und Koreanischen")}</h2>
      <p>{c.t(
        "Two self-paced reading studies test an <em>expected-first</em> account: readers slow down when the first noun phrase departs from what discourse and grammar lead them to expect. German shows a graded pattern (given &lt; implied &lt; new); in Korean, implied referents pattern with new ones and word-order costs appear later.",
        "Zwei Self-Paced-Reading-Studien prüfen einen <em>Expected-first</em>-Ansatz: Leser werden langsamer, wenn die erste Nominalphrase von dem abweicht, was Diskurs und Grammatik erwarten lassen. Im Deutschen zeigt sich eine Abstufung (gegeben &lt; impliziert &lt; neu); im Koreanischen verhalten sich implizierte Referenten wie neue, und Wortstellungseffekte treten später auf.")}</p>
      <p class="feature-links"><a class="res res-light" href="{poster}" target="_blank" rel="noopener">{LINK_LABELS["poster"][c.lang]} ↗</a><a class="res res-light" href="{abstract}" target="_blank" rel="noopener">{LINK_LABELS["abstract"][c.lang]} ↗</a></p>
    </div>
    <a class="feature-figure" href="{poster}" target="_blank" rel="noopener" aria-label="{c.t("Open the HSP 2026 poster (PDF)", "HSP-2026-Poster öffnen (PDF)")}">
      <img src="{c.pre}assets/fig/hsp2026-reading-times.png" width="1400" height="849" alt="{c.t("Interaction plot of reading times by givenness, word order and region for German and Korean", "Interaktionsdiagramm der Lesezeiten nach Gegebenheit, Wortstellung und Region für Deutsch und Koreanisch")}" loading="lazy">
    </a>
  </div>
</section>

<section class="wrap section">
  <p class="eyebrow">{c.t("Research", "Forschung")}</p>
  <h2 class="section-title">{c.t("Three lines of work", "Drei Forschungslinien")}</h2>
  <div class="cards">
    <a class="card" href="{c.page('research', '#gaze')}"><span class="card-num">01</span><h3>{c.t("Speaker gaze and prediction", "Sprecherblick und Vorhersage")}</h3><p>{c.t("How listeners use where a speaker looks to anticipate what comes next – measured with ERPs.", "Wie Hörer den Blick eines Sprechers nutzen, um das Kommende vorherzusagen – gemessen mit EKPs.")}</p></a>
    <a class="card" href="{c.page('research', '#word-order')}"><span class="card-num">02</span><h3>{c.t("Word order and information structure", "Wortstellung und Informationsstruktur")}</h3><p>{c.t("How givenness and constituent order jointly shape reading in German and Korean.", "Wie Gegebenheit und Konstituentenreihenfolge gemeinsam das Lesen im Deutschen und Koreanischen prägen.")}</p></a>
    <a class="card" href="{c.page('research', '#beyond')}"><span class="card-num">03</span><h3>{c.t("Collaborations and earlier work", "Kooperationen und frühere Arbeiten")}</h3><p>{c.t("Discourse expectations, word learning, turn-taking and English–Japanese machine translation.", "Diskurserwartungen, Wortlernen, Sprecherwechsel und maschinelle Übersetzung Englisch–Japanisch.")}</p></a>
  </div>
</section>

<section class="wrap section section-tight">
  <div class="section-head"><div><p class="eyebrow">{c.t("Selected publications", "Ausgewählte Publikationen")}</p><h2 class="section-title">{c.t("Journal articles", "Zeitschriftenartikel")}</h2></div><a class="more" href="{c.page('publications')}">{c.t("All publications", "Alle Publikationen")} →</a></div>
  <ol class="pub-list">{"".join(pub_item(c, p) for p in feat)}</ol>
</section>

<section class="band band-tint">
  <div class="wrap teaser">
    <div class="teaser-photos">
      <figure>{img(c, "japan-lake", c.t("At a lake in Japan", "An einem See in Japan"), "(min-width: 900px) 30vw, 60vw")}</figure>
      <figure>{img(c, "knit-sweater", c.t("Hand-knitted three-colour sweater", "Selbst gestrickter dreifarbiger Pullover"), "(min-width: 900px) 15vw, 30vw")}</figure>
      <figure>{img(c, "cake-berry", c.t("Berry cream cake", "Beerentorte"), "(min-width: 900px) 15vw, 30vw")}</figure>
    </div>
    <div class="teaser-text">
      <p class="eyebrow">{c.t("Beyond the lab", "Persönliches")}</p>
      <h2>{c.t("Japan, yarn and cake", "Japan, Wolle und Torten")}</h2>
      <p>{c.t("Away from the lab I travel – to Japan above all – knit, cook and bake.", "Abseits der Forschung reise ich – vor allem nach Japan –, stricke, koche und backe.")}</p>
      <a class="btn" href="{c.page('personal')}">{c.t("A little more about me", "Mehr über mich")}</a>
    </div>
  </div>
</section>
"""
    return layout(c, "", c.t(
        "Torsten Kai Jachmann – postdoctoral researcher in psycholinguistics at Saarland University: speaker gaze, ERPs, word order and information structure.",
        "Torsten Kai Jachmann – Postdoc in der Psycholinguistik an der Universität des Saarlandes: Sprecherblick, EKPs, Wortstellung und Informationsstruktur."), body)


def related(c, theme):
    items = [p for p in PUBLICATIONS if p["theme"] == theme]
    items.sort(key=lambda p: -p["year"])
    return f'<details class="related"><summary>{c.t("Related publications", "Zugehörige Publikationen")} ({len(items)})</summary><ol class="pub-list pub-list-compact">{"".join(pub_item(c, p) for p in items)}</ol></details>'


def page_research(c):
    cog_poster = c.url("assets/pdf/Jachmann-CogSci2017-poster.pdf")
    hsp_poster = c.url("assets/pdf/Jachmann-HSP2026-poster.pdf")
    body = f"""
<section class="wrap page-intro">
  <p class="eyebrow">{c.t("Research", "Forschung")}</p>
  <h1>{c.t("Understanding language in context", "Sprache im Kontext verstehen")}</h1>
  <p class="lead">{c.t(
    "Comprehension is not a passive decoding of words. Listeners and readers continuously predict what comes next, drawing on the visual scene, the speaker, the discourse and the grammar of their language. My work asks which cues feed these expectations, when they are used, and what happens when they are confirmed or violated.",
    "Sprachverstehen ist kein passives Entschlüsseln von Wörtern. Hörer und Leser sagen fortlaufend voraus, was als Nächstes kommt – auf Grundlage der visuellen Szene, des Sprechers, des Diskurses und der Grammatik ihrer Sprache. Meine Arbeit fragt, welche Hinweise diese Erwartungen speisen, wann sie genutzt werden und was geschieht, wenn sie bestätigt oder verletzt werden.")}</p>
  <nav class="toc" aria-label="{c.t("On this page", "Auf dieser Seite")}"><a href="#gaze">01 {c.t("Speaker gaze", "Sprecherblick")}</a><a href="#word-order">02 {c.t("Word order &amp; givenness", "Wortstellung &amp; Gegebenheit")}</a><a href="#beyond">03 {c.t("Collaborations &amp; earlier work", "Kooperationen &amp; frühere Arbeiten")}</a><a href="#methods">{c.t("Methods", "Methoden")}</a></nav>
</section>

<section class="wrap theme" id="gaze">
  <div class="theme-head"><span class="theme-num">01</span><h2>{c.t("Speaker gaze and referential expectations", "Sprecherblick und referenzielle Erwartungen")}</h2></div>
  <div class="theme-body">
    <div class="prose">
      <p>{c.t(
        "In face-to-face conversation, speakers tend to look at an object shortly before they name it. Listeners can exploit this: a glance towards the house makes <em>house</em> the expected next word. In a series of EEG experiments, a virtual speaker looked at one of several objects while a sentence unfolded; the gaze either matched the noun that followed, contradicted it, or was absent.",
        "Im Gespräch blicken Sprecher meist kurz auf ein Objekt, bevor sie es benennen. Hörer können das nutzen: Ein Blick zum Haus macht <em>Haus</em> zum erwarteten nächsten Wort. In einer Reihe von EEG-Experimenten blickte ein virtueller Sprecher auf eines von mehreren Objekten, während ein Satz ablief; der Blick passte zum folgenden Nomen, widersprach ihm oder fehlte.")}</p>
      <p>{c.t(
        "Event-related potentials show that listeners use the gaze cue immediately: incongruent gaze changes the brain’s response to the noun within a few hundred milliseconds, and later components suggest that listeners update their model of the situation. The 2023 <em>Cognition</em> article shows that when gaze points to an unexpected object, the brain responds to the gaze cue itself (N400, P300) and the effects on the following noun are attenuated: listeners treat speaker gaze as an integral part of the communicative signal.",
        "Ereigniskorrelierte Potenziale zeigen, dass Hörer den Blickhinweis sofort nutzen: Ein inkongruenter Blick verändert die Hirnantwort auf das Nomen innerhalb weniger hundert Millisekunden, und spätere Komponenten deuten darauf hin, dass Hörer ihr Situationsmodell aktualisieren. Der <em>Cognition</em>-Artikel von 2023 zeigt: Weist der Blick auf ein unerwartetes Objekt, reagiert das Gehirn bereits auf den Blickhinweis selbst (N400, P300), und die Effekte auf das folgende Nomen fallen schwächer aus – Hörer behandeln den Sprecherblick als festen Bestandteil des kommunikativen Signals.")}</p>
    </div>
    <figure class="fig fig-wide">
      <img src="{c.pre}assets/fig/cogsci2017-procedure.png" width="2000" height="336" alt="{c.t("Trial procedure: a schematic face between a shirt, a house and a car; the face looks at an object 800 ms before it is named", "Ablauf eines Durchgangs: ein schematisches Gesicht zwischen Hemd, Haus und Auto; das Gesicht blickt 800 ms vor der Nennung auf ein Objekt")}" loading="lazy">
      <figcaption>{c.t(
        "Procedure. The speaker’s gaze shift 800 ms before the second noun (red box) was manipulated: congruent, incongruent or neutral. Example: “Compared to the car, the <em>house</em> is relatively small, I think.”",
        "Ablauf. Manipuliert wurde der Blickwechsel des Sprechers 800 ms vor dem zweiten Nomen (roter Rahmen): kongruent, inkongruent oder neutral. Beispiel: „Verglichen mit dem Auto ist das <em>Haus</em> verhältnismäßig klein, denke ich.“")}
        <span class="fig-source">Jachmann, Drenhaus, Staudte &amp; Crocker (CogSci 2017) · <a href="{cog_poster}" target="_blank" rel="noopener">{LINK_LABELS["poster"][c.lang]} ↗</a></span></figcaption>
    </figure>
    <figure class="fig fig-erp">
      <img src="{c.pre}assets/fig/cogsci2017-erp.png" width="1100" height="1170" alt="{c.t("ERP waveforms at electrodes Fz and Pz for congruent, incongruent and neutral gaze, with N2, N4 and late positivity windows marked", "EKP-Verläufe an den Elektroden Fz und Pz für kongruenten, inkongruenten und neutralen Blick; N2-, N4- und Late-Positivity-Fenster markiert")}" loading="lazy">
      <figcaption>{c.t(
        "Grand-average ERPs at the second noun (electrodes Fz and Pz), time in ms from noun onset; negative is plotted upwards. Congruent (black), incongruent (red), neutral (blue). Shaded windows mark the N2, N4 and late positivity analyses.",
        "Gemittelte EKPs am zweiten Nomen (Elektroden Fz und Pz), Zeit in ms ab Nomenbeginn; negativ ist nach oben aufgetragen. Kongruent (schwarz), inkongruent (rot), neutral (blau). Markierte Fenster: N2, N4 und späte Positivierung.")}
        <span class="fig-source">Jachmann, Drenhaus, Staudte &amp; Crocker (CogSci 2017)</span></figcaption>
    </figure>
    {related(c, "gaze")}
  </div>
</section>

<section class="wrap theme" id="word-order">
  <div class="theme-head"><span class="theme-num">02</span><h2>{c.t("Word order, givenness and the expected-first principle", "Wortstellung, Gegebenheit und das Expected-first-Prinzip")}</h2></div>
  <div class="theme-body">
    <div class="prose">
      <p>{c.t(
        "Languages with flexible word order make object-first sentences harder to process, and readers prefer given information before new. Expectation-based accounts explain both: canonical orders and given-before-new are simply more predictable. My current work, part of SFB 1102 project C3, tests a stronger claim – that comprehenders rely heavily on expectations about the <em>first</em> noun phrase, and that costs arise whenever it diverges from them.",
        "In Sprachen mit freier Wortstellung sind Objekt-zuerst-Sätze schwerer zu verarbeiten, und Leser bevorzugen Gegebenes vor Neuem. Erwartungsbasierte Ansätze erklären beides: Kanonische Abfolgen und Gegebenes-vor-Neuem sind schlicht vorhersagbarer. Meine aktuelle Arbeit im SFB 1102, Projekt C3, prüft eine stärkere These: dass Verstehende sich vor allem auf Erwartungen an die <em>erste</em> Nominalphrase stützen und Kosten immer dann entstehen, wenn diese abweicht.")}</p>
      <p>{c.t(
        "Self-paced reading studies in German (HSP 2024) manipulated word order and three grades of givenness – given, implied (inferable from context) and new. A parallel study in Korean, a language with productive topic and subject drop, shows that the same expectation system surfaces differently depending on case marking and argument drop.",
        "Self-Paced-Reading-Studien im Deutschen (HSP 2024) variierten Wortstellung und drei Grade von Gegebenheit – gegeben, impliziert (aus dem Kontext erschließbar) und neu. Eine parallele Studie im Koreanischen, einer Sprache mit produktivem Topik- und Subjekt-Drop, zeigt, dass sich dasselbe Erwartungssystem je nach Kasusmarkierung und Argumentauslassung unterschiedlich äußert.")}</p>
    </div>
    <figure class="fig fig-plot">
      <img src="{c.pre}assets/fig/hsp2026-reading-times.png" width="1400" height="849" alt="{c.t("Reading times for given, implied and new first referents in SOV and OSV sentences, at NP1 and NP2, for German (top) and Korean (bottom)", "Lesezeiten für gegebene, implizierte und neue erste Referenten in SOV- und OSV-Sätzen, an NP1 und NP2, für Deutsch (oben) und Koreanisch (unten)")}" loading="lazy">
      <figcaption>{c.t(
        "Reading times (ms) at the first and second noun phrase for SOV and OSV sentences, by whether the first referent was given, implied or new. German (top): graded costs at NP1. Korean (bottom): given vs. the rest at NP1, word-order effects at NP2.",
        "Lesezeiten (ms) an der ersten und zweiten Nominalphrase für SOV- und OSV-Sätze, je nachdem, ob der erste Referent gegeben, impliziert oder neu war. Deutsch (oben): abgestufte Kosten an NP1. Koreanisch (unten): gegeben vs. Rest an NP1, Wortstellungseffekte an NP2.")}
        <span class="fig-source">Jachmann, Drenhaus, Delogu, Lee &amp; Crocker (HSP 2026) · <a href="{hsp_poster}" target="_blank" rel="noopener">{LINK_LABELS["poster"][c.lang]} ↗</a></span></figcaption>
    </figure>
    {related(c, "infostruct")}
  </div>
</section>

<section class="wrap theme" id="beyond">
  <div class="theme-head"><span class="theme-num">03</span><h2>{c.t("Collaborations and earlier work", "Kooperationen und frühere Arbeiten")}</h2></div>
  <div class="theme-body">
    <div class="prose">
      <p>{c.t(
        "With colleagues I have worked on how the question under discussion shapes discourse expectations (ERPs), on age-related differences in learning new words from expectations, and on how informativity affects the order in which speakers mention referents.",
        "Gemeinsam mit Kolleginnen und Kollegen habe ich untersucht, wie die Question under Discussion Diskurserwartungen prägt (EKPs), wie sich das erwartungsbasierte Lernen neuer Wörter mit dem Alter verändert und wie Informativität die Reihenfolge beeinflusst, in der Sprecher Referenten nennen.")}</p>
      <p>{c.t(
        "My MSc thesis asked whether prosody works as a turn-taking cue across German, English and Japanese, building on joint work on prosody and gaze in turn-end anticipation. My BSc thesis and a paper at NLP2014 dealt with pre-editing rules for machine-translating English forum posts into Japanese.",
        "Meine Masterarbeit fragte, ob Prosodie sprachübergreifend – im Deutschen, Englischen und Japanischen – als Hinweis für den Sprecherwechsel dient, aufbauend auf gemeinsamer Arbeit zu Prosodie und Blick bei der Antizipation von Turn-Enden. Meine Bachelorarbeit und ein Beitrag auf der NLP2014 befassten sich mit Pre-Editing-Regeln für die maschinelle Übersetzung englischer Forenbeiträge ins Japanische.")}</p>
    </div>
    {related(c, "other")}
  </div>
</section>

<section class="band band-tint" id="methods">
  <div class="wrap methods">
    <div><p class="eyebrow">{c.t("Methods", "Methoden")}</p><h2 class="section-title">{c.t("How I work", "Wie ich arbeite")}</h2></div>
    <ul class="method-list">
      <li><strong>{c.t("EEG / event-related potentials", "EEG / ereigniskorrelierte Potenziale")}</strong><span>{c.t("Time-locked brain responses to words in visual and spoken contexts.", "Zeitlich gekoppelte Hirnantworten auf Wörter in visuellen und gesprochenen Kontexten.")}</span></li>
      <li><strong>{c.t("Self-paced reading and reaction times", "Self-Paced Reading und Reaktionszeiten")}</strong><span>{c.t("Word-by-word processing costs in carefully controlled designs.", "Wortweise Verarbeitungskosten in kontrollierten Designs.")}</span></li>
      <li><strong>{c.t("Cross-linguistic comparison", "Sprachvergleich")}</strong><span>{c.t("Parallel experiments in German, Korean, English and Japanese.", "Parallele Experimente im Deutschen, Koreanischen, Englischen und Japanischen.")}</span></li>
      <li><strong>{c.t("Mixed-effects modelling", "Gemischte Modelle")}</strong><span>{c.t("Linear mixed-effects models in Julia and R; open data on OSF.", "Lineare gemischte Modelle in Julia und R; offene Daten auf OSF.")}</span></li>
    </ul>
  </div>
</section>
"""
    return layout(c, c.t("Research", "Forschung"), c.t(
        "Research by Torsten Kai Jachmann: speaker gaze and ERPs, word order and givenness in German and Korean, and expectation-based comprehension.",
        "Forschung von Torsten Kai Jachmann: Sprecherblick und EKPs, Wortstellung und Gegebenheit im Deutschen und Koreanischen, erwartungsbasiertes Sprachverstehen."), body)


def page_publications(c):
    toc, secs = [], []
    for key, label in PUB_SECTIONS:
        items = sorted([p for p in PUBLICATIONS if p["type"] == key], key=lambda p: -p["year"])
        toc.append(f'<a href="#{key}">{label[c.lang]} <span>{len(items)}</span></a>')
        secs.append(f'<section class="pub-section" id="{key}"><h2>{label[c.lang]}</h2><ol class="pub-list">{"".join(pub_item(c, p) for p in items)}</ol></section>')
    body = f"""
<section class="wrap page-intro">
  <p class="eyebrow">{c.t("Publications", "Publikationen")}</p>
  <h1>{c.t("Publications &amp; presentations", "Publikationen &amp; Vorträge")}</h1>
  <p class="lead">{c.t("Every entry links to the resource itself – the article, the PDF of the paper, poster or slides, and where available the research data on OSF.", "Jeder Eintrag verweist direkt auf die Ressource – den Artikel, das PDF von Beitrag, Poster oder Folien und, wo vorhanden, die Forschungsdaten auf OSF.")}</p>
  <nav class="toc" aria-label="{c.t("Sections", "Abschnitte")}">{"".join(toc)}</nav>
</section>
<div class="wrap pubs">{"".join(secs)}</div>
"""
    return layout(c, c.t("Publications", "Publikationen"), c.t(
        "Journal articles, conference papers, talks, posters and theses by Torsten Kai Jachmann, with PDFs, DOIs and research data.",
        "Zeitschriftenartikel, Konferenzbeiträge, Vorträge, Poster und Abschlussarbeiten von Torsten Kai Jachmann mit PDFs, DOIs und Forschungsdaten."), body)


def term_label(c, term):
    if c.lang == "de":
        return term
    if c.lang == "ja":
        kind, yr = term.split(" ")
        return yr + "年 " + ("冬学期" if kind == "WS" else "夏学期")
    return term.replace("WS ", "Winter ").replace("SS ", "Summer ")


def course_rows(c, courses):
    return "".join(
        f'<li class="course"><span class="course-title">{e(t[c.lang])}</span><span class="course-terms">{" · ".join(term_label(c, x) for x in terms)}</span></li>'
        for t, terms in courses)


def page_teaching(c):
    body = f"""
<section class="wrap page-intro">
  <p class="eyebrow">{c.t("Teaching", "Lehre")}</p>
  <h1>{c.t("Teaching", "Lehre")}</h1>
  <p class="lead">{c.t(
    "I teach empirical and experimental methods in the Language Science and Technology programmes, and Japanese as a foreign language.",
    "Ich unterrichte empirische und experimentelle Methoden in den Studiengängen der Language Science and Technology sowie Japanisch als Fremdsprache.")}</p>
</section>
<section class="wrap section section-tight">
  <div class="current">
    <p class="eyebrow">{c.t("This semester", "Aktuelles Semester")} · {CURRENT_TERM[c.lang]}</p>
    {"".join(f"<h2>{e(x[c.lang])}</h2>" for x in CURRENT_COURSES)}
  </div>
  <div class="course-groups">
    <div>
      <h2 class="group-title">{c.t("Psycholinguistics and methods", "Psycholinguistik und Methoden")}</h2>
      <ul class="course-list">{course_rows(c, COURSES_ACADEMIC)}</ul>
    </div>
    <div>
      <h2 class="group-title">{c.t("Japanese language courses", "Japanischkurse")}</h2>
      <ul class="course-list">{course_rows(c, COURSES_JAPANESE)}</ul>
      <p class="small">{c.t("Earlier: Japanese A1–A2 at the Volkshochschule Sulzbach (Saar), 2013–2015.", "Früher: Japanisch A1–A2 an der Volkshochschule Sulzbach (Saar), 2013–2015.")}</p>
    </div>
  </div>
</section>
"""
    return layout(c, c.t("Teaching", "Lehre"), c.t(
        "Courses taught by Torsten Kai Jachmann at Saarland University: empirical methods, experimental psycholinguistics and Japanese.",
        "Lehrveranstaltungen von Torsten Kai Jachmann an der Universität des Saarlandes: empirische Methoden, experimentelle Psycholinguistik und Japanisch."), body)


def timeline(c, rows, with_thesis=False):
    out = []
    for r in rows:
        when, title, desc = r[0], r[1][c.lang], r[2][c.lang]
        thesis = f'<p class="tl-thesis">{c.t("Thesis", "Arbeit")}: <em>{e(r[3])}</em></p>' if with_thesis else ""
        out.append(f'<li><span class="tl-when">{e(when)}</span><div><h3>{e(title)}</h3><p>{e(desc)}</p>{thesis}</div></li>')
    return '<ol class="timeline">' + "".join(out) + "</ol>"


def page_cv(c):
    body = f"""
<section class="wrap page-intro">
  <p class="eyebrow">{c.t("Curriculum vitae", "Lebenslauf")}</p>
  <h1>{c.t("Academic CV", "Akademischer Lebenslauf")}</h1>
</section>
<section class="wrap cv">
  <div><h2 class="group-title">{c.t("Positions", "Stationen")}</h2>{timeline(c, POSITIONS)}</div>
  <div><h2 class="group-title">{c.t("Education", "Ausbildung")}</h2>{timeline(c, EDUCATION, True)}  </div>
</section>
"""
    return layout(c, c.t("CV", "Lebenslauf"), c.t(
        "Academic CV of Torsten Kai Jachmann: positions and education at Saarland University.",
        "Akademischer Lebenslauf von Torsten Kai Jachmann: Stationen und Ausbildung an der Universität des Saarlandes."), body)


def jfig(c, name, en, de):
    w, h = PHOTOS[name]
    ar = round(w / h, 4)
    cap = c.t(en, de)
    return f'<figure style="--ar:{ar}">{img(c, name, cap, "(min-width: 900px) 33vw, 50vw")}<figcaption>{e(cap)}</figcaption></figure>'


def stagger(c, col1, col2):
    def col(items):
        return "".join(f'<figure>{img(c, n, c.t(en, de), "(min-width: 900px) 30vw, 50vw")}</figure>' for n, en, de in items)
    return f'<div class="stagger"><div class="stagger-col">{col(col1)}</div><div class="stagger-col stagger-offset">{col(col2)}</div></div>'


def page_personal(c):
    body = f"""
<section class="wrap page-intro">
  <p class="eyebrow">{c.t("Beyond the lab", "Persönliches")}</p>
  <h1>{c.t("Beyond the lab", "Abseits der Forschung")}</h1>
  <p class="lead">{c.t("A few things that bring me joy outside academia: travelling, knitting, cooking and baking.", "Ein paar Dinge, die mir außerhalb der Wissenschaft Freude machen: Reisen, Stricken, Kochen und Backen.")}</p>
</section>

<section class="wrap hobby" id="japan">
  <div class="hobby-head">
    <span class="theme-num">01</span>
    <h2>{c.t("Travels in Japan", "Reisen in Japan")}</h2>
    <p>{c.t("Japan is my favourite destination for private travel.", "Privat zieht es mich besonders häufig nach Japan.")}</p>
  </div>
  <div class="mosaic">
    <figure class="mosaic-main">{img(c, "japan-lake", c.t("At a lake in Japan", "An einem See in Japan"), "(min-width: 900px) 65vw, 100vw")}<figcaption>{c.t("Lakeside, Japan", "Am See, Japan")}</figcaption></figure>
    <div class="mosaic-side">
      <figure class="mosaic-a">{img(c, "japan-university-gate", c.t("At a university gate in Tokyo", "Vor einem Universitätstor in Tokio"), "(min-width: 900px) 30vw, 55vw")}<figcaption>{c.t("University gate, Tokyo", "Universitätstor, Tokio")}</figcaption></figure>
      <figure class="mosaic-b">{img(c, "japan-garden", c.t("Selfie in a Japanese garden", "Selfie in einem japanischen Garten"), "(min-width: 900px) 30vw, 45vw")}<figcaption>{c.t("Japanese garden", "Japanischer Garten")}</figcaption></figure>
    </div>
  </div>
  <div class="jrow jrow-after">
    {jfig(c, "japan-plum-blossoms", "Plum blossoms at a shrine", "Pflaumenblüte an einem Schrein")}
    {jfig(c, "japan-torii", "Path of torii gates", "Weg aus Torii-Toren")}
    {jfig(c, "japan-osaka-castle", "Osaka Castle", "Burg Osaka")}
  </div>
</section>

<section class="wrap hobby" id="travel">
  <div class="hobby-head">
    <span class="theme-num">02</span>
    <h2>{c.t("Other journeys", "Weitere Reisen")}</h2>
    <p>{c.t("A few places from conference trips and holidays.", "Einige Orte von Konferenzreisen und Urlauben.")}</p>
  </div>
  <div class="journeys">
    <div class="region"><h3>{c.t("Europe", "Europa")}</h3><div class="jrow">
      {jfig(c, "berlin-reichstag", "Reichstag building, Berlin", "Reichstagsgebäude, Berlin")}
      {jfig(c, "london-eye", "London Eye and the Thames", "London Eye an der Themse")}
    </div></div>
    <div class="region"><h3>{c.t("Americas", "Amerika")}</h3><div class="jrow">
      {jfig(c, "boston-mit", "MIT, Cambridge, Massachusetts", "MIT, Cambridge, Massachusetts")}
      {jfig(c, "san-francisco", "San Francisco", "San Francisco")}
      {jfig(c, "brazil-coast", "Coastline, Brazil", "Küste, Brasilien")}
    </div></div>
  </div>
</section>

<section class="wrap hobby hobby-split" id="knitting">
  <div class="hobby-head sticky">
    <span class="theme-num">03</span>
    <h2>{c.t("Knitting", "Stricken")}</h2>
    <p>{c.t("I like making things by hand – exploring textures, intricate lace and cable patterns and different yarns. The three-colour sweater is one of my own projects.", "Ich stricke gern und probiere unterschiedliche Garne, Strukturen sowie anspruchsvolle Lochmuster und Zöpfe aus. Der dreifarbige Pullover ist eines meiner eigenen Projekte.")}</p>
  </div>
  {stagger(c, [("knit-sweater", "Hand-knitted three-colour sweater", "Selbst gestrickter dreifarbiger Pullover"), ("knit-grey", "Grey textured knitting on the needles", "Graues Strukturmuster auf der Nadel")],
              [("knit-lace-blue", "Blue lace knitting in progress", "Blaues Lochmuster in Arbeit"), ("knit-cable", "Navy cable knitting", "Dunkelblaues Zopfmuster")])}
</section>

<section class="wrap hobby hobby-split" id="baking">
  <div class="hobby-head sticky">
    <span class="theme-num">04</span>
    <h2>{c.t("Cooking &amp; baking", "Kochen &amp; Backen")}</h2>
    <p>{c.t("I love cooking and baking – above all the creative part of building and decorating cakes.", "Ich koche und backe sehr gern – besonders das Gestalten und Dekorieren von Torten macht mir Freude.")}</p>
  </div>
  {stagger(c, [("cake-berry", "Berry cream cake decorated with fresh berries", "Beerentorte mit frischen Beeren"), ("cake-slice", "Slice of the berry cake", "Stück der Beerentorte")],
              [("cake-flowers", "Cake with handmade fondant roses", "Torte mit selbst modellierten Rosen"), ("cake-layers", "Cut cake showing its layers", "Angeschnittene Torte mit ihren Schichten")])}
</section>
"""
    return layout(c, c.t("Beyond the lab", "Persönliches"), c.t(
        "Travel in Japan and elsewhere, knitting, cooking and baking – Torsten Kai Jachmann outside the lab.",
        "Reisen nach Japan und anderswohin, Stricken, Kochen und Backen – Torsten Kai Jachmann abseits der Forschung."), body)


def page_contact(c):
    lc = Ctx("en", c.slug) if c.lang == "ja" else c   # the Impressum stays in English on the Japanese page
    body = f"""
<section class="wrap page-intro">
  <p class="eyebrow">{c.t("Contact", "Kontakt")}</p>
  <h1>{c.t("Get in touch", "Kontakt")}</h1>
  <p class="lead">{c.t("For research collaborations, questions about teaching or anything else, email is the best way to reach me.", "Für Forschungskooperationen, Fragen zur Lehre und alles Weitere erreichen Sie mich am besten per E-Mail.")}</p>
</section>
<section class="wrap contact">
  <div class="contact-card">
    <p class="eyebrow">{c.t("University email", "Dienstliche E-Mail")}</p>
    <a class="contact-email" href="mailto:{EMAIL}">{EMAIL}</a>
    <p class="eyebrow contact-gap">{c.t("Personal email", "Private E-Mail")}</p>
    <a class="contact-email" href="mailto:{EMAIL_PRIVATE}">{EMAIL_PRIVATE}</a>
  </div>
  <div class="contact-card contact-card-blue">
    <p class="eyebrow eyebrow-light">{c.t("Office", "Büro")}</p>
    <address>{c.t("Saarland University", "Universität des Saarlandes")}<br>{c.t("Department of Language Science and Technology", "Fachrichtung Sprachwissenschaft und Sprachtechnologie")}<br>{c.t("Campus C7 1, Room 1.13", "Campus C7 1, Raum 1.13", "Campus C7 1, 1.13号室")}<br>66123 Saarbrücken, {c.t("Germany", "Deutschland")}</address>
  </div>
</section>
<section class="wrap legal" id="legal">
  <div{' lang="en"' if c.lang == "ja" else ""}>
    <h2 class="group-title">{lc.t("Legal notice (Impressum)", "Impressum")}</h2>
    <p>{lc.t("Responsible for the content of this website:", "Verantwortlich für den Inhalt dieser Website:")}<br>{ME}<br>{lc.t("Saarland University", "Universität des Saarlandes")}, Campus C7 1<br>66123 Saarbrücken, {lc.t("Germany", "Deutschland")}<br>E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p class="small">{lc.t("This is a personal website. It is not an official publication of Saarland University.", "Dies ist eine private Website und keine offizielle Veröffentlichung der Universität des Saarlandes.")}</p>
  </div>
  <div>
    <h2 class="group-title">{c.t("Privacy", "Datenschutz")}</h2>
    <p>{c.t(
      "This website uses no cookies, analytics, tracking or embedded third-party content. Fonts are served from this site. The site is hosted on GitHub Pages; when you visit it, GitHub processes technical data such as your IP address to deliver the pages (see GitHub’s privacy statement). Links to publishers, OSF and other sites are subject to those providers’ privacy policies.",
      "Diese Website verwendet keine Cookies, keine Analyse- oder Tracking-Werkzeuge und keine eingebetteten Inhalte Dritter. Schriften werden von dieser Website selbst ausgeliefert. Gehostet wird die Website über GitHub Pages; beim Aufruf verarbeitet GitHub technische Daten wie Ihre IP-Adresse, um die Seiten auszuliefern (siehe Datenschutzerklärung von GitHub). Für verlinkte Seiten von Verlagen, OSF und anderen gelten deren Datenschutzbestimmungen.")}</p>
  </div>
</section>
"""
    return layout(c, c.t("Contact", "Kontakt"), c.t(
        "Contact Torsten Kai Jachmann, Saarland University.", "Kontakt zu Torsten Kai Jachmann, Universität des Saarlandes."), body)


RENDER = dict(index=page_index, research=page_research, publications=page_publications, teaching=page_teaching,
              cv=page_cv, personal=page_personal, contact=page_contact)

if __name__ == "__main__":
    for lang in LANGS:
        outdir = ROOT if lang == "en" else os.path.join(ROOT, lang)
        os.makedirs(outdir, exist_ok=True)
        for slug in PAGES:
            c = Ctx(lang, slug)
            with open(os.path.join(outdir, c.page(slug)), "w", encoding="utf-8") as f:
                f.write(RENDER[slug](c))
    if MISSING:
        print("Missing Japanese translations:")
        for m in dict.fromkeys(MISSING):
            print(repr(m))
        sys.exit(1)
    print("Built", len(LANGS) * len(PAGES), "pages.")
