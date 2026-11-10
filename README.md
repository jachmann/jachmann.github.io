# Torsten Kai Jachmann – personal website

Static trilingual site: English at the root, German in `/de/`, Japanese in `/ja/`. Plain HTML and CSS, no JavaScript, no external requests.

## Put it online with GitHub Pages

1. Create a repository on GitHub – for the address `https://<username>.github.io`, name it exactly `<username>.github.io`.
2. Upload the *contents* of this folder (so `index.html` sits at the top level of the repository).
3. Repository → **Settings → Pages** → Source: *Deploy from a branch*, Branch: `main`, folder `/ (root)` → Save.
4. After a minute the site is live. Open the contact page and check the legal notice.

## Change content

All text that changes over time lives in `_source/content.py` (publications, teaching, CV).
Page texts are in `_source/build.py` (English and German side by side); Japanese texts are in `_source/ja.py`, keyed by the English text. If an English text has no Japanese counterpart, the build stops and lists it. After editing, regenerate the pages:

```
python3 _source/build.py
```

Then commit and push the changed files. No packages need to be installed.

To add a publication, copy an entry in `PUBLICATIONS`, put its PDF into `assets/pdf/` and link it as e.g. `("poster", "assets/pdf/Name.pdf")`.
Link kinds and their labels are listed in `LINK_LABELS`.

## Folder structure

```
index.html, research.html, …   English pages (generated)
de/                            German pages (generated)
ja/                            Japanese pages (generated; Japanese text uses the visitor's system fonts)
assets/css/style.css           design – colours: Prussian blue #003153, Ritsumeikan red #8c2332
assets/fonts/                  self-hosted Source Serif 4 and Inter (SIL Open Font License)
assets/img/                    photos, 640 px and 1200 px versions
assets/fig/                    figures cropped from the HSP 2026 and CogSci 2017 posters
assets/pdf/                    papers, posters, slides, abstracts, theses
_source/                       content and generator (not linked from the site)
```

The BSc and MSc thesis PDFs have the title-page lines with date of birth and matriculation number removed.
