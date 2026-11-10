# -*- coding: utf-8 -*-
"""All website content. Edit this file, then run:  python3 _source/build.py

Two languages: "en" (site root) and "de" (/de/).
Bibliographic data (titles, authors, venues) stay in the original language.
"""

ME = "Torsten Kai Jachmann"
EMAIL = "jachmann@uni-saarland.de"
EMAIL_PRIVATE = "tkjachmann@gmail.com"

# ---------------------------------------------------------------------------
# Publications
# type: journal | proceedings | talk | poster | thesis
# theme: gaze | infostruct | other   (used to list related work on the research page)
# links: list of (kind, url). kinds are labelled in LINK_LABELS below.
# ---------------------------------------------------------------------------
PUBLICATIONS = [
    # ----- Journal articles -----
    dict(year=2023, type="journal", theme="gaze", featured=True,
         title="When a look is enough: Neurophysiological correlates of referential speaker gaze in situated comprehension",
         authors="Torsten Kai Jachmann, Heiner Drenhaus, Maria Staudte, Matthew W. Crocker",
         venue="Cognition, 236, 105449",
         links=[("article", "https://doi.org/10.1016/j.cognition.2023.105449"),
                ("data", "https://osf.io/uzktp/")]),
    dict(year=2022, type="journal", theme="other", featured=True,
         title="Age-related differences in expectation-based novel word learning",
         authors="Yoana Vergilova, Torsten Kai Jachmann, Nivedita Mani, Jutta Kray",
         venue="Psychophysiology, e14030",
         links=[("article", "https://doi.org/10.1111/psyp.14030"),
                ("data", "https://osf.io/2cfjd/")]),
    dict(year=2019, type="journal", theme="gaze", featured=True,
         title="Influence of speakers’ gaze on situated language comprehension: Evidence from Event-Related Potentials",
         authors="Torsten Kai Jachmann, Heiner Drenhaus, Maria Staudte, Matthew W. Crocker",
         venue="Brain and Cognition",
         links=[("article", "https://doi.org/10.1016/j.bandc.2019.05.009"),
                ("data", "https://osf.io/q367s/?view_only=be366104c9d54cd3a058b496cdbdf5a4")]),
    dict(year=2019, type="journal", theme="other",
         title="Discourse Expectations Are Sensitive to the Question Under Discussion: Evidence From ERPs",
         authors="Francesca Delogu, Torsten Kai Jachmann, Maria Staudte, Francesco Vespignani, Nicola Molinaro",
         venue="Discourse Processes",
         links=[("article", "https://doi.org/10.1080/0163853X.2019.1575140")]),

    # ----- Peer-reviewed conference papers -----
    dict(year=2023, type="proceedings", theme="infostruct",
         title="Does informativity modulate linearization preferences in reference production?",
         authors="Muqing Li, Noortje J. Venhuizen, Torsten Kai Jachmann, Heiner Drenhaus, Matthew W. Crocker",
         venue="Proceedings of the 45th Annual Meeting of the Cognitive Science Society · Sydney, Australia",
         links=[("paper", "assets/pdf/Li-CogSci2023-paper.pdf")]),
    dict(year=2017, type="proceedings", theme="gaze",
         title="The Influence of Speaker’s Gaze on Sentence Comprehension: An ERP Investigation",
         authors="Torsten Kai Jachmann, Heiner Drenhaus, Maria Staudte, Matthew W. Crocker",
         venue="Proceedings of the 39th Annual Conference of the Cognitive Science Society, pp. 2261–2266 · London, UK",
         links=[("paper", "assets/pdf/Jachmann-CogSci2017-paper.pdf"),
                ("poster", "assets/pdf/Jachmann-CogSci2017-poster.pdf")]),
    dict(year=2015, type="proceedings", theme="other",
         title="The role of prosody and gaze in turn-end anticipation",
         authors="Chiara Gambi, Torsten Kai Jachmann, Maria Staudte",
         venue="Proceedings of the 37th Annual Conference of the Cognitive Science Society · Pasadena, USA",
         links=[("paper", "assets/pdf/Gambi-CogSci2015-paper.pdf")]),
    dict(year=2014, type="proceedings", theme="other",
         title="Machine-Translating English Forum Posts to Japanese: On Pre-editing Rules as Part of Domain Adaptation",
         authors="Torsten Kai Jachmann, Robert Grabowski, Mayo Kudo",
         venue="Proceedings of the 20th Annual Meeting of the Association for Natural Language Processing (NLP2014), pp. 808–811 · Hokkaido University, Japan",
         links=[("paper", "assets/pdf/Jachmann-NLP2014-paper.pdf")]),

    # ----- Talks -----
    dict(year=2024, type="talk", theme="infostruct",
         title="Investigating Word Order and Givenness Effects as Part of Expected-first Strategies in Information Structure",
         authors="Torsten Kai Jachmann, Heiner Drenhaus, Francesca Delogu, Matthew W. Crocker",
         venue="37th Annual Conference on Human Sentence Processing (HSP 2024) · University of Michigan, Ann Arbor, USA",
         links=[("slides", "assets/pdf/Jachmann-HSP2024-slides.pdf"),
                ("abstract", "assets/pdf/Jachmann-HSP2024-abstract.pdf")]),

    # ----- Posters (with peer-reviewed abstracts) -----
    dict(year=2026, type="poster", theme="infostruct",
         title="The interplay of constituent order and givenness in German and Korean: An Expectation-based account",
         authors="Torsten Kai Jachmann, Heiner Drenhaus, Francesca Delogu, Myeongju Lee, Matthew W. Crocker",
         venue="39th Annual Conference on Human Sentence Processing (HSP 2026) · MIT, Cambridge, USA",
         links=[("poster", "assets/pdf/Jachmann-HSP2026-poster.pdf"),
                ("abstract", "assets/pdf/Jachmann-HSP2026-abstract.pdf")]),
    dict(year=2018, type="poster", theme="gaze", note="slam",
         title="(Dis)Confirmation of Linguistic Prediction by Non-Linguistic Cues",
         authors="Torsten Kai Jachmann, Heiner Drenhaus, Maria Staudte, Matthew W. Crocker",
         venue="AMLaP 2018 · Berlin, Germany",
         links=[("poster", "assets/pdf/Jachmann-AMLaP2018-poster.pdf"),
                ("abstract", "assets/pdf/Jachmann-AMLaP2018-abstract.pdf")]),
    dict(year=2017, type="poster", theme="gaze",
         title="Congruency effects of speaker’s gaze on listeners’ sentence comprehension",
         authors="Torsten Kai Jachmann, Heiner Drenhaus, Maria Staudte, Matthew W. Crocker",
         venue="Society for the Neurobiology of Language (SNL 2017) · Baltimore, USA",
         links=[("poster", "assets/pdf/Jachmann-SNL2017-poster.pdf"),
                ("supplement", "assets/pdf/Jachmann-SNL2017-poster-supplement.pdf"),
                ("abstract", "assets/pdf/Jachmann-SNL2017-abstract.pdf")]),
    dict(year=2017, type="poster", theme="gaze",
         title="Congruency effects of speaker’s gaze on listeners’ sentence comprehension",
         authors="Torsten Kai Jachmann, Heiner Drenhaus, Maria Staudte, Matthew W. Crocker",
         venue="30th Annual CUNY Conference on Human Sentence Processing (CUNY 2017) · Boston, USA",
         links=[("poster", "assets/pdf/Jachmann-CUNY2017-poster.pdf"),
                ("abstract", "assets/pdf/Jachmann-CUNY2017-abstract.pdf")]),
    dict(year=2017, type="poster", theme="gaze",
         title="Influence of Speakers’ Gaze on Listeners’ Comprehension: Evidence from Event Related Potentials (ERP)",
         authors="Torsten Kai Jachmann, Heiner Drenhaus, Maria Staudte, Matthew W. Crocker",
         venue="Cognitive Neuroscience Society (CNS 2017) · San Francisco, USA",
         links=[("poster", "assets/pdf/Jachmann-CNS2017-poster.pdf"),
                ("abstract", "assets/pdf/Jachmann-CNS2017-abstract.pdf")]),

    # ----- Theses -----
    dict(year=2020, type="thesis", theme="gaze", degree="phd",
         title="The Immediate Influence of Speaker Gaze on Situated Speech Comprehension: Evidence from Multiple ERP Components",
         authors="Torsten Kai Jachmann",
         venue="Saarland University",
         links=[("dissertation", "https://doi.org/10.22028/D291-31309"),
                ("data_exp12", "https://osf.io/q367s/?view_only=be366104c9d54cd3a058b496cdbdf5a4")]),
    dict(year=2015, type="thesis", theme="other", degree="msc",
         title="On Universality of Prosody as a Turn-Taking Cue Across Languages",
         authors="Torsten Kai Jachmann",
         venue="Saarland University",
         links=[("thesis", "assets/pdf/Jachmann-2015-MSc-thesis.pdf")]),
    dict(year=2013, type="thesis", theme="other", degree="bsc",
         title="Exploring Domain Adaptation in Machine Translation for English to Japanese",
         authors="Torsten Kai Jachmann",
         venue="Saarland University",
         links=[("thesis", "assets/pdf/Jachmann-2013-BSc-thesis.pdf")]),
]

LINK_LABELS = {
    "article": {"en": "Article", "de": "Artikel", "ja": "論文"},
    "data": {"en": "Research data (OSF)", "de": "Forschungsdaten (OSF)", "ja": "研究データ（OSF）"},
    "data_exp12": {"en": "Research data, Exp. 1–2 (OSF)", "de": "Forschungsdaten, Exp. 1–2 (OSF)", "ja": "研究データ・実験1–2（OSF）"},
    "paper": {"en": "Conference paper (PDF)", "de": "Konferenzbeitrag (PDF)", "ja": "会議論文（PDF）"},
    "poster": {"en": "Poster (PDF)", "de": "Poster (PDF)", "ja": "ポスター（PDF）"},
    "supplement": {"en": "Poster supplement (PDF)", "de": "Poster-Ergänzung (PDF)", "ja": "ポスター補足資料（PDF）"},
    "abstract": {"en": "Abstract (PDF)", "de": "Abstract (PDF)", "ja": "要旨（PDF）"},
    "slides": {"en": "Slides (PDF)", "de": "Folien (PDF)", "ja": "スライド（PDF）"},
    "dissertation": {"en": "Dissertation", "de": "Dissertation", "ja": "博士論文"},
    "thesis": {"en": "Thesis (PDF)", "de": "Abschlussarbeit (PDF)", "ja": "学位論文（PDF）"},
}

PUB_SECTIONS = [
    ("journal", {"en": "Journal articles", "de": "Zeitschriftenartikel", "ja": "学術誌論文"}),
    ("proceedings", {"en": "Peer-reviewed conference papers", "de": "Begutachtete Konferenzbeiträge", "ja": "査読付き会議論文"}),
    ("talk", {"en": "Conference talks", "de": "Konferenzvorträge", "ja": "学会口頭発表"}),
    ("poster", {"en": "Conference posters", "de": "Konferenzposter", "ja": "学会ポスター発表"}),
    ("thesis", {"en": "Theses", "de": "Abschlussarbeiten", "ja": "学位論文"}),
]

DEGREE = {
    "phd": {"en": "PhD dissertation", "de": "Dissertation", "ja": "博士論文"},
    "msc": {"en": "MSc thesis · Language Science and Technology", "de": "Masterarbeit · Language Science and Technology", "ja": "修士論文 · Language Science and Technology"},
    "bsc": {"en": "BSc thesis · Computational Linguistics", "de": "Bachelorarbeit · Computerlinguistik", "ja": "学士論文 · 計算言語学"},
}

# ---------------------------------------------------------------------------
# Teaching  – titles per language; romanised Japanese level names (Shokyû …)
# stay as they are in EN/DE and are written in kanji in the Japanese version.
# ---------------------------------------------------------------------------
CURRENT_TERM = {"en": "Winter 2026/27", "de": "WS 2026/27", "ja": "2026/27年 冬学期"}

# Official course titles – identical in all languages
FOEM = {"en": "Foundations of Empirical Methods", "de": "Foundations of Empirical Methods", "ja": "Foundations of Empirical Methods"}
CURRENT_COURSES = [FOEM]

COURSES_ACADEMIC = [
    (FOEM, ["WS 2020/21", "WS 2021/22", "WS 2022/23", "WS 2023/24", "WS 2024/25", "WS 2025/26", "WS 2026/27"]),
    ({"en": "Experimental Methods in Psycholinguistic Research",
      "de": "Experimental Methods in Psycholinguistic Research",
      "ja": "Experimental Methods in Psycholinguistic Research"},
     ["SS 2021", "SS 2022", "SS 2023", "SS 2024", "SS 2025"]),
    ({"en": "(Linguistic) Expectations in Language Comprehension",
      "de": "(Linguistic) Expectations in Language Comprehension",
      "ja": "(Linguistic) Expectations in Language Comprehension"}, ["WS 2022/23"]),
]
COURSES_JAPANESE = [
    ({"en": "Japanese Foundation Course – Shokyû 1", "de": "Japanisch Grundlagenkurs – Shokyû 1", "ja": "日本語基礎講座 – 初級1"},
     ["WS 2022/23", "WS 2023/24"]),
    ({"en": "Japanese Elementary Course – Shokyû 2", "de": "Japanisch Elementarkurs – Shokyû 2", "ja": "日本語初歩講座 – 初級2"},
     ["WS 2023/24"]),
    ({"en": "Japanese Advanced Course – Sho-chûkyû 1", "de": "Japanisch Vertiefungskurs – Sho-chûkyû 1", "ja": "日本語発展講座 – 初中級1"},
     ["SS 2024"]),
    ({"en": "Japanese A2, parts 1 + 2", "de": "Japanisch A2, Teil 1 + 2", "ja": "日本語 A2（パート1・2）"}, ["WS 2024/25"]),
    ({"en": "Japanese B1.1, parts 1 + 2", "de": "Japanisch B1.1, Teil 1 + 2", "ja": "日本語 B1.1（パート1・2）"}, ["SS 2025"]),
    ({"en": "Japanese B1.2, parts 1 + 2", "de": "Japanisch B1.2, Teil 1 + 2", "ja": "日本語 B1.2（パート1・2）"}, ["WS 2025/26"]),
]

# ---------------------------------------------------------------------------
# CV
# ---------------------------------------------------------------------------
POSITIONS = [
    ("2020 –", {"en": "Postdoctoral researcher", "de": "Wissenschaftlicher Mitarbeiter (Postdoc)", "ja": "ポスドク研究員"},
     {"en": "Psycholinguistics Group, Department of Language Science and Technology, Saarland University · SFB 1102 “Information Density and Linguistic Encoding”, project C3",
      "de": "Arbeitsgruppe Psycholinguistik, Fachrichtung Sprachwissenschaft und Sprachtechnologie, Universität des Saarlandes · SFB 1102 „Information Density and Linguistic Encoding“, Projekt C3",
      "ja": "ザールラント大学 言語科学・言語技術学科 心理言語学研究グループ · 共同研究センター SFB 1102「Information Density and Linguistic Encoding」C3プロジェクト"}),
    ("2015 – 2020", {"en": "Doctoral researcher", "de": "Doktorand", "ja": "博士課程研究員"},
     {"en": "Saarland University · Cluster of Excellence MMCI (until 2018), SFB 1102 (from 2018)",
      "de": "Universität des Saarlandes · Exzellenzcluster MMCI (bis 2018), SFB 1102 (ab 2018)",
      "ja": "ザールラント大学 · エクセレンス・クラスター MMCI（2018年まで）、SFB 1102（2018年から）"}),
    ("2014 – 2015", {"en": "Research assistant, Psycholinguistics Group", "de": "Studentische Hilfskraft, Arbeitsgruppe Psycholinguistik", "ja": "研究補助員（心理言語学研究グループ）"},
     {"en": "Saarland University · ERP experiments and stimulus construction",
      "de": "Universität des Saarlandes · EKP-Experimente und Stimuluserstellung",
      "ja": "ザールラント大学 · ERP実験の実施と刺激の作成"}),
    ("2013 – 2015", {"en": "Research assistant, Embodied Spoken Interaction", "de": "Studentische Hilfskraft, Embodied Spoken Interaction", "ja": "研究補助員（Embodied Spoken Interaction）"},
     {"en": "Cluster of Excellence MMCI, Saarland University · reaction-time and ERP experiments, stimulus construction",
      "de": "Exzellenzcluster MMCI, Universität des Saarlandes · Reaktionszeit- und EKP-Experimente, Stimuluserstellung",
      "ja": "ザールラント大学 エクセレンス・クラスター MMCI · 反応時間実験とERP実験の実施、刺激の作成"}),
    ("2013 – 2015", {"en": "Freelancer, acrolinx (Berlin)", "de": "Freier Mitarbeiter, acrolinx (Berlin)", "ja": "フリーランス、acrolinx（ベルリン）"},
     {"en": "Writing and testing pre-editing rules; evaluation",
      "de": "Erstellung und Test von Pre-Editing-Regeln; Evaluation",
      "ja": "前編集ルールの作成・検証と評価"}),
    ("2013 – 2015", {"en": "Japanese teacher, Volkshochschule Sulzbach (Saar)", "de": "Japanischlehrer, Volkshochschule Sulzbach (Saar)", "ja": "日本語講師、Volkshochschule Sulzbach (Saar)（市民大学）"},
     {"en": "Courses at levels A1 and A2", "de": "Kurse auf den Niveaus A1 und A2", "ja": "A1・A2レベルの講座を担当"}),
]

EDUCATION = [
    ("2015 – 2020", {"en": "PhD, Psycholinguistics", "de": "Promotion, Psycholinguistik", "ja": "博士（心理言語学）"},
     {"en": "Saarland University · magna cum laude · Supervisor: Prof. Dr. Matthew W. Crocker; advisors: Dr. Maria Staudte, Dr. Heiner Drenhaus",
      "de": "Universität des Saarlandes · magna cum laude · Betreuer: Prof. Dr. Matthew W. Crocker; Mitbetreuung: Dr. Maria Staudte, Dr. Heiner Drenhaus",
      "ja": "ザールラント大学 · magna cum laude · 指導教員：Prof. Dr. Matthew W. Crocker、副指導：Dr. Maria Staudte、Dr. Heiner Drenhaus"},
     "The Immediate Influence of Speaker Gaze on Situated Speech Comprehension: Evidence from Multiple ERP Components"),
    ("2013 – 2015", {"en": "MSc, Language Science and Technology", "de": "M.Sc. Language Science and Technology", "ja": "修士（Language Science and Technology）"},
     {"en": "Saarland University · Supervisors: Dr. Maria Staudte, Dr. Chiara Gambi",
      "de": "Universität des Saarlandes · Betreuung: Dr. Maria Staudte, Dr. Chiara Gambi",
      "ja": "ザールラント大学 · 指導教員：Dr. Maria Staudte、Dr. Chiara Gambi"},
     "On Universality of Prosody as a Turn-Taking Cue Across Languages"),
    ("2008 – 2013", {"en": "BSc, Computational Linguistics", "de": "B.Sc. Computerlinguistik", "ja": "学士（計算言語学）"},
     {"en": "Saarland University · Supervisors: Prof. Dr. Hans Uszkoreit, Dr. Robert Grabowski",
      "de": "Universität des Saarlandes · Betreuung: Prof. Dr. Hans Uszkoreit, Dr. Robert Grabowski",
      "ja": "ザールラント大学 · 指導教員：Prof. Dr. Hans Uszkoreit、Dr. Robert Grabowski"},
     "Exploring Domain Adaptation in Machine Translation for English to Japanese"),
]
