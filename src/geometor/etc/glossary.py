"""Glossary, biographical (persons), and bibliographic (citations) extraction and apparatus generation for ETC."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup, NavigableString, Tag


def apparatus_slug(key: str) -> str:
    """Create a deterministic anchor slug matching photon-platform/publish."""
    return re.sub(r"[^a-z0-9]+", "-", (key or "").lower()).strip("-")


# Single-word primitive nouns in the Glossary that are too generic to auto-wrap in every sentence
SKIP_AUTO_WRAP_TERMS = {
    "center",
    "line",
    "point",
    "polar",
    "perspective",
    "cubic",
    "homologous images: similarity image, trilinear image, barycentric image, and functional image",
}

# Classical named triangles defined inside "cevian triangle", "anticevian triangle", and "central triangle"
CLASSICAL_TRIANGLE_ALIASES: dict[str, dict[str, str]] = {
    "incentral triangle": {
        "target_slug": "cevian-triangle",
        "definition": "The cevian triangle of the incenter X(1) = 1 : 1 : 1, whose vertices are the points where the interior angle bisectors of ABC meet the opposite sidelines.",
    },
    "medial triangle": {
        "target_slug": "cevian-triangle",
        "definition": "The cevian triangle of the centroid X(2) = 1/a : 1/b : 1/c, whose vertices are the midpoints of sides BC, CA, AB.",
    },
    "orthic triangle": {
        "target_slug": "cevian-triangle",
        "definition": "The cevian (and pedal) triangle of the orthocenter X(4) = sec A : sec B : sec C, whose vertices are the feet of the altitudes of ABC.",
    },
    "intouch triangle": {
        "target_slug": "cevian-triangle",
        "definition": "The cevian triangle of the Gergonne point X(7) (also the pedal triangle of the incenter X(1)), whose vertices are the points of tangency of the incircle with the sides of ABC.",
    },
    "extouch triangle": {
        "target_slug": "cevian-triangle",
        "definition": "The cevian triangle of the Nagel point X(8), whose vertices are the points of tangency of the A-, B-, C-excircles with sides BC, CA, AB.",
    },
    "excentral triangle": {
        "target_slug": "anticevian-triangle",
        "definition": "The anticevian triangle of the incenter X(1) = 1 : 1 : 1, whose vertices are the three excenters of ABC.",
    },
    "tangential triangle": {
        "target_slug": "anticevian-triangle",
        "definition": "The anticevian triangle of the symmedian point X(6) = a : b : c, formed by the lines tangent to the circumcircle of ABC at vertices A, B, C.",
    },
    "pedal triangle": {
        "target_slug": "central-triangle",
        "definition": "For a point P, the triangle A'B'C' whose vertices are the orthogonal projections (feet of perpendiculars) of P onto the sidelines BC, CA, AB.",
    },
    "antipedal triangle": {
        "target_slug": "central-triangle",
        "definition": "For a point P, the triangle A'B'C' formed by the lines through A, B, C perpendicular to AP, BP, CP respectively.",
    },
}


# Curated biographical registry for :person: role and resources/persons.json
PERSONS_REGISTRY: dict[str, dict[str, str]] = {
    "clark-kimberling": {
        "name": "Clark Kimberling",
        "dates": "b. 1942",
        "role": "Mathematician at the University of Evansville; founder and creator of the Encyclopedia of Triangle Centers (ETC).",
        "aliases": ["Clark Kimberling", "C. Kimberling", "Kimberling"],
    },
    "peter-moses": {
        "name": "Peter J. C. Moses",
        "dates": "fl. 2000–present",
        "role": "Computational geometer and principal collaborator on the ETC, discoverer of thousands of barycentric combinations, coordinates, and circle/cubic properties.",
        "aliases": ["Peter Moses", "P. Moses"],
    },
    "randy-hutson": {
        "name": "Randy Hutson",
        "dates": "fl. 2011–present",
        "role": "Prolific contributor to the ETC, specializing in synthetic constructions, perspective triangles, radical centers, and conjugate relationships.",
        "aliases": ["Randy Hutson"],
    },
    "cesar-lozada": {
        "name": "César Eliud Lozada",
        "dates": "fl. 2012–present",
        "role": "Author of the Extended Glossary, Alphabetical Index of Terms, and Index of Triangles Referenced in ETC; contributor of thousands of triangle centers.",
        "aliases": ["César Eliud Lozada", "César Lozada", "César E. Lozada"],
    },
    "bernard-gibert": {
        "name": "Bernard Gibert",
        "dates": "fl. 1998–present",
        "role": "Creator of Cubics in the Triangle Plane (CTC), cataloging and analyzing over 1,200 triangle cubics (K001–K1200+) referenced throughout the ETC.",
        "aliases": ["Bernard Gibert"],
    },
    "paul-yiu": {
        "name": "Paul Yiu",
        "dates": "b. 1952",
        "role": "Professor of Mathematics at Florida Atlantic University, founder of Forum Geometricorum, and pioneer of modern barycentric triangle geometry.",
        "aliases": ["Paul Yiu"],
    },
    "floor-van-lamoen": {
        "name": "Floor van Lamoen",
        "dates": "b. 1966",
        "role": "Dutch mathematician and triangle geometer, discoverer of the van Lamoen circle and numerous cevapoint and perspectivity constructions in the ETC.",
        "aliases": ["Floor van Lamoen", "Floor Van Lamoen", "Floor Lamoen"],
    },
    "darij-grinberg": {
        "name": "Darij Grinberg",
        "dates": "b. 1988",
        "role": "Mathematician and early contributor to Hyacinthos and the ETC on barycentric coordinates, pedal triangles, and circle power identities.",
        "aliases": ["Darij Grinberg"],
    },
    "antreas-hatzipolakis": {
        "name": "Antreas P. Hatzipolakis",
        "dates": "fl. 1998–present",
        "role": "Founder of the Hyacinthos, Anopolis, and Euclid geometry research forums; proposer of hundreds of geometric configurations in the ETC.",
        "aliases": ["Antreas Hatzipolakis"],
    },
    "angel-montesdeoca": {
        "name": "Angel Montesdeoca",
        "dates": "fl. 2010–present",
        "role": "Spanish geometer and contributor of numerous triangle centers, perspectors, and conic constructions in the ETC.",
        "aliases": ["Angel Montesdeoca"],
    },
    "dan-reznik": {
        "name": "Dan Reznik",
        "dates": "fl. 2018–present",
        "role": "Researcher on Poncelet porisms, locus invariants, and dynamic triangle center loci in the ETC.",
        "aliases": ["Dan Reznik", "Dan Reznick"],
    },
    "dao-thanh-oai": {
        "name": "Dao Thanh Oai",
        "dates": "fl. 2013–present",
        "role": "Geometer and discoverer of generalizations of the Simson line, Napoleon configuration, and perspective triangles in the ETC.",
        "aliases": ["Dao Thanh Oai", "Thanh Oai Dao"],
    },
    "dasari-naga-vijay-krishna": {
        "name": "Dasari Naga Vijay Krishna",
        "dates": "fl. 2018–present",
        "role": "Indian mathematician contributing synthetic reflection and circle constructions in the ETC.",
        "aliases": ["Dasari Naga Vijay Krishna", "Vijay Krishna"],
    },
    "kiminari-shinagawa": {
        "name": "Kiminari Shinagawa",
        "dates": "fl. 2015–present",
        "role": "Geometer who introduced the Shinagawa coefficients (G, H) for triangle centers on the Euler line.",
        "aliases": ["Kiminari Shinagawa"],
    },
    "stanley-rabinowitz": {
        "name": "Stanley Rabinowitz",
        "dates": "b. 1947",
        "role": "Mathematician and author of 'Location of Triangle Centers Relative to the Incircle and Circumcircle' in the ETC.",
        "aliases": ["Stanley Rabinowitz"],
    },
    "eric-weisstein": {
        "name": "Eric W. Weisstein",
        "dates": "b. 1969",
        "role": "Creator of MathWorld, providing extensive cross-linked articles and illustrations for triangle centers and central circles.",
        "aliases": ["Eric Weisstein"],
    },
    "john-horton-conway": {
        "name": "John Horton Conway",
        "dates": "1937–2020",
        "role": "Mathematician who introduced Conway triangle notation (S, S_A, S_B, S_C, S_ω) and the Conway circle in triangle geometry.",
        "aliases": ["John H. Conway"],
    },
    "leonhard-euler": {
        "name": "Leonhard Euler",
        "dates": "1707–1783",
        "role": "Swiss mathematician who proved in 1765 that the orthocenter X(4), circumcenter X(3), centroid X(2), and nine-point center X(5) are collinear on the Euler line.",
        "aliases": ["Leonhard Euler"],
    },
    "karl-wilhelm-feuerbach": {
        "name": "Karl Wilhelm Feuerbach",
        "dates": "1800–1834",
        "role": "German geometer who proved in 1822 that the nine-point circle is tangent to the incircle at the Feuerbach point X(11) and to the three excircles.",
        "aliases": ["Karl Wilhelm Feuerbach"],
    },
    "emile-lemoine": {
        "name": "Émile Michel Hyacinthe Lemoine",
        "dates": "1840–1912",
        "role": "French mathematician and co-founder of modern triangle geometry; studied the symmedian point X(6) (Lemoine point) and Lemoine circles.",
        "aliases": ["Émile Lemoine", "Emile Lemoine"],
    },
    "ernst-wilhelm-grebe": {
        "name": "Ernst Wilhelm Grebe",
        "dates": "1804–1874",
        "role": "German mathematician who investigated the symmedian point X(6) (Grebe point) in 1847.",
        "aliases": ["Ernst Wilhelm Grebe"],
    },
    "joseph-diaz-gergonne": {
        "name": "Joseph Diaz Gergonne",
        "dates": "1771–1859",
        "role": "French geometer after whom the Gergonne point X(7) (perspector of the intouch triangle) and Gergonne line are named.",
        "aliases": ["Joseph Diaz Gergonne"],
    },
    "christian-heinrich-von-nagel": {
        "name": "Christian Heinrich von Nagel",
        "dates": "1803–1882",
        "role": "German geometer who studied the Nagel point X(8) (perspector of the extouch triangle) and Nagel line in 1836.",
        "aliases": ["Christian Heinrich von Nagel"],
    },
    "theodor-spieker": {
        "name": "Theodor Spieker",
        "dates": "1823–1913",
        "role": "German geometer who discovered the Spieker center X(10) (incenter of the medial triangle and center of mass of the perimeter of ABC).",
        "aliases": ["Theodor Spieker"],
    },
    "pierre-de-fermat": {
        "name": "Pierre de Fermat",
        "dates": "1607–1665",
        "role": "French mathematician who posed the problem of finding the point X(13) minimizing the sum of distances |AX| + |BX| + |CX| to the vertices of ABC.",
        "aliases": ["Pierre de Fermat"],
    },
    "evangelista-torricelli": {
        "name": "Evangelista Torricelli",
        "dates": "1608–1647",
        "role": "Italian physicist and mathematician who solved Fermat's problem via equilateral triangles erected on the sides of ABC, locating X(13) and X(14).",
        "aliases": ["Evangelista Torricelli"],
    },
    "henri-brocard": {
        "name": "Henri Brocard",
        "dates": "1845–1922",
        "role": "French mathematician and co-founder of modern triangle geometry; namesake of the Brocard points, Brocard angle ω, Brocard axis, Brocard circle, and Brocard triangles.",
        "aliases": ["Henri Brocard"],
    },
    "joseph-neuberg": {
        "name": "Joseph Jean Baptiste Neuberg",
        "dates": "1840–1926",
        "role": "Luxembourger-Belgian mathematician, co-founder of modern triangle geometry, discoverer of the Neuberg cubic (K001) and Neuberg circles.",
        "aliases": ["Joseph Neuberg"],
    },
    "gaston-darboux": {
        "name": "Jean-Gaston Darboux",
        "dates": "1842–1917",
        "role": "French geometer after whom the Darboux cubic (K004) and Darboux point X(20) (with De Longchamps) are named.",
        "aliases": ["Gaston Darboux"],
    },
    "gohier-de-longchamps": {
        "name": "Gaston Albert Gohier de Longchamps",
        "dates": "1842–1906",
        "role": "French mathematician who studied the De Longchamps point X(20) (reflection of the orthocenter in the circumcenter) and De Longchamps line.",
        "aliases": ["De Longchamps"],
    },
    "kurt-hofstadter": {
        "name": "Douglas Richard Hofstadter",
        "dates": "b. 1945",
        "role": "Cognitive scientist and geometer who discovered the Hofstadter points, including the Hofstadter zero point X(359) and one point X(360).",
        "aliases": ["Douglas Hofstadter"],
    },
    "cyril-parry": {
        "name": "Cyril F. Parry",
        "dates": "1915–1999",
        "role": "British geometer who discovered the Parry point X(111), the Parry circle, and the Parry reflection property.",
        "aliases": ["Cyril Parry", "C. F. Parry"],
    },
    "peter-yff": {
        "name": "Peter Yff",
        "dates": "1924–2016",
        "role": "Geometer who discovered the Yff center of congruence X(174), Yff parabolic point X(190), and Yff central triangles.",
        "aliases": ["Peter Yff"],
    },
}


# Curated bibliographic registry for :cite: role and resources/citations.json
CITATIONS_REGISTRY: dict[str, dict[str, str]] = {
    "tcct": {
        "author": "Clark Kimberling",
        "work": "Triangle Centers and Central Triangles (TCCT)",
        "locus": "Congressus Numerantium 129 (1998), i–295",
        "notes": "Foundational monograph establishing the formal theory of triangle centers, central lines, central triangles, and the initial 400 centers of the ETC.",
    },
    "kimberling-1994": {
        "author": "Clark Kimberling",
        "work": "Central Points and Central Lines in the Plane of a Triangle",
        "locus": "Mathematics Magazine 67 (1994), 163–187",
        "notes": "Landmark paper introducing the systematic indexing of triangle centers X(n) and central lines L(n).",
    },
    "kimberling-2002-fg": {
        "author": "Clark Kimberling",
        "work": "Collineations, Conjugacies, and Cubics",
        "locus": "Forum Geometricorum 2 (2002), 21–32",
        "notes": "Introduces the Hebrew-letter conjugacies (aleph, beth, gimel, daleth, he, waw, zayin) and their cubic loci.",
    },
    "gibert-ctc": {
        "author": "Bernard Gibert",
        "work": "Cubics in the Triangle Plane (CTC)",
        "locus": "Online Encyclopedia of Triangle Cubics (K001–K1200+)",
        "notes": "Comprehensive catalog of pivotal, isogonal, isotomic, and general curves in the plane of a triangle, referenced via K-indices across the ETC.",
    },
    "forum-geometricorum": {
        "author": "Paul Yiu (Ed.)",
        "work": "Forum Geometricorum",
        "locus": "Florida Atlantic University, Vols. 1–20 (2001–2020)",
        "notes": "Peer-reviewed journal dedicated to classical Euclidean and modern triangle geometry.",
    },
    "hyacinthos": {
        "author": "Antreas P. Hatzipolakis (Founder)",
        "work": "Hyacinthos — Triangle Geometry Forum",
        "locus": "Messages #1–#28000+ (1999–2018)",
        "notes": "The primary international research mailing list where thousands of triangle centers and theorems in the ETC were discovered and proved.",
    },
    "adgeom": {
        "author": "Antreas P. Hatzipolakis (Founder)",
        "work": "ADGEOM / Euclid / Anopolis Geometry Forums",
        "locus": "Research postings (2014–present)",
        "notes": "Research groups succeeding Hyacinthos as primary sources for new configurations and centers in the ETC.",
    },
    "mathworld": {
        "author": "Eric W. Weisstein",
        "work": "MathWorld — A Wolfram Web Resource",
        "locus": "https://mathworld.wolfram.com/",
        "notes": "Comprehensive online mathematical encyclopedia with interactive illustrations and cross-references for Kimberling centers.",
    },
    "court-1952": {
        "author": "Nathan Altshiller-Court",
        "work": "College Geometry: An Introduction to the Modern Geometry of the Triangle and the Circle",
        "locus": "2nd ed., Barnes & Noble, New York (1952)",
        "notes": "Classic treatise on synthetic triangle geometry cited throughout the ETC for historical priority and constructions.",
    },
    "johnson-1929": {
        "author": "Roger A. Johnson",
        "work": "Modern Geometry (Advanced Euclidean Geometry)",
        "locus": "Houghton Mifflin (1929); Dover reprint (1960)",
        "notes": "Standard reference on the geometry of the triangle, Miquel and Johnson circles, Brocard geometry, and Tucker circles.",
    },
    "rabinowitz-2021": {
        "author": "Stanley Rabinowitz",
        "work": "Location of Triangle Centers Relative to the Incircle and Circumcircle",
        "locus": "International Journal of Computer Discovered Mathematics (IJCDM) 6 (2021)",
        "notes": "Systematic classification of which triangle centers lie strictly inside, on, or outside the incircle and circumcircle.",
    },
}


def clean_html_entities(text: str) -> str:
    """Fix common entity typos in ETC HTML and unescape all HTML entities to UTF-8."""
    if not text:
        return ""
    text = (
        text.replace("&cajp;", "&cap;")
        .replace("&nbnbsp;", " ")
        .replace("&nbsnbsp;", " ")
        .replace("&nnbsp;", " ")
        .replace("&nbsp;", " ")
        .replace("&srarr;", "&rarr;")
        .replace("&Sum;", "&Sigma;")
        .replace("AA'&Prime;", "AA'A&Prime;")
        .replace("lines A&Prime;, BB&Prime;", "lines AA&Prime;, BB&Prime;")
    )
    return html.unescape(text)


def _remove_html_tags(text: str) -> str:
    """Remove HTML tags from text."""
    return re.sub(r"<[^>]+>", "", text)


def _replace_balanced_func(text: str, func_name: str, latex_cmd: str) -> str:
    """Replace `func_name(...)` with `latex_cmd{...}` handling nested parentheses."""
    pat = re.compile(rf"\b{func_name}\(", re.IGNORECASE)
    while True:
        m = pat.search(text)
        if not m:
            break
        start_paren = m.end() - 1
        depth = 0
        end_paren = -1
        for idx in range(start_paren, len(text)):
            ch = text[idx]
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    end_paren = idx
                    break
        if end_paren == -1:
            break
        inner = text[start_paren + 1 : end_paren]
        text = f"{text[:m.start()]}{latex_cmd}{{{inner}}}{text[end_paren + 1:]}"
    return text


def formula_html_to_latex(formula_html: str) -> str:
    """Convert an HTML coordinate or algebraic formula into clean LaTeX suitable for `:math:`."""
    s = clean_html_entities(formula_html)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.DOTALL)

    # Escape literal $ used for Shinagawa cyclic sums ($aS_A$)
    s = re.sub(r"(?<!\\)\$", r"\\$", s)

    # Convert <sup>...</sup> and <sub>...</sub> to LaTeX ^{...} and _{...}
    s = re.sub(
        r"<sup>(.*?)</sup>",
        lambda m: f"^{{{_remove_html_tags(m.group(1)).strip()}}}",
        s,
        flags=re.DOTALL | re.IGNORECASE,
    )
    s = re.sub(
        r"<sub>(.*?)</sub>",
        lambda m: f"_{{{_remove_html_tags(m.group(1)).strip()}}}",
        s,
        flags=re.DOTALL | re.IGNORECASE,
    )

    s = _remove_html_tags(s)
    s = " ".join(s.split())

    # Brace caret exponents like a^10, a^-2, a^2, or a^(n+1)
    s = re.sub(r"\^(-?\d+|\([0-9a-zA-Z+\-*/ ]+\))", r"^{\1}", s)

    # Normalize sqr(...) -> sqrt(...) and convert Sqrt[...] / sqrt(...) to \sqrt{...}
    s = re.sub(r"\bsqr\(", "sqrt(", s, flags=re.IGNORECASE)
    while re.search(r"\bSqrt\[([^\[\]]+)\]", s):
        s = re.sub(r"\bSqrt\[([^\[\]]+)\]", r"\\sqrt{\1}", s)
    s = _replace_balanced_func(s, "sqrt", r"\sqrt")

    # Convert area(ABC) and standalone area to \operatorname{area}
    s = re.sub(r"\b[Aa]rea\b", r"\\operatorname{area}", s)

    # Normalize Conway symbols (SA, SB, SC, SW, SBSC, SAa, etc.)
    s = s.replace("SBSC", "S_{B}S_{C}").replace("SCSA", "S_{C}S_{A}").replace("SASB", "S_{A}S_{B}")
    s = re.sub(r"\bSA(?=[a-c]\b|\^)", "S_{A}", s)
    s = re.sub(r"\bSB(?=[a-c]\b|\^)", "S_{B}", s)
    s = re.sub(r"\bSC(?=[a-c]\b|\^)", "S_{C}", s)
    s = re.sub(r"\bSA\b", "S_{A}", s)
    s = re.sub(r"\bSB\b", "S_{B}", s)
    s = re.sub(r"\bSC\b", "S_{C}", s)
    s = re.sub(r"\bSW\b", r"S_{\\omega}", s)

    # Normalize common unsubscripted radii / symmetric polynomials in formulas
    s = re.sub(r"\bR([abcs])\b", r"R_{\1}", s)
    s = re.sub(r"\br([abc])\b", r"r_{\1}", s)
    s = re.sub(r"\be([123])\b", r"e_{\1}", s)

    # Replace Unicode Greek and math symbols with LaTeX commands
    replacements = {
        "ω": r"\omega ",
        "Ω": r"\Omega ",
        "π": r"\pi ",
        "α": r"\alpha ",
        "β": r"\beta ",
        "γ": r"\gamma ",
        "θ": r"\theta ",
        "λ": r"\lambda ",
        "μ": r"\mu ",
        "φ": r"\phi ",
        "Φ": r"\Phi ",
        "ψ": r"\psi ",
        "Ψ": r"\Psi ",
        "σ": r"\sigma ",
        "Δ": r"\Delta ",
        "Γ": r"\Gamma ",
        "Λ": r"\Lambda ",
        "Σ": r"\Sigma ",
        "∩": r"\cap ",
        "∪": r"\cup ",
        "≠": r"\neq ",
        "≤": r"\leq ",
        "≥": r"\geq ",
        "±": r"\pm ",
        "·": r"\cdot ",
        "→": r"\to ",
        "′": "'",
        "″": "''",
    }
    for k, v in replacements.items():
        s = s.replace(k, v)

    # Standard trig functions (including sin^2, sinB, cos2A, etc.)
    s = re.sub(
        r"(?<!\\)\b(sin|cos|tan|cot|sec|csc)(?=\^|\s|\(|[A-Z0-9]|\\|\b)",
        r"\\\1",
        s,
    )
    s = re.sub(
        r"(\\(?:sin|cos|tan|cot|sec|csc)(?:\^\{[^}]+\})?)(?=[A-Za-z0-9])",
        r"\1 ",
        s,
    )

    # Clean up multiplication *
    s = re.sub(r"(?<=\d)\s*\*\s*(?=\d)", r" \\cdot ", s)
    s = re.sub(r"\)\s*\*\s*\(", r") \\cdot (", s)
    s = re.sub(r"(?<=[0-9a-zA-Z\}\)\]])\s*\*\s*(?=[0-9a-zA-Z\\\(\[])", " ", s)

    return " ".join(s.split()).rstrip("\\").strip()


def convert_inline_html_to_rst(
    fragment: str, valid_centers: set[int] | None = None
) -> str:
    """Convert inline HTML tags (sup, sub, b, i, a, br) to clean ReStructuredText."""
    if not fragment:
        return ""

    text = clean_html_entities(fragment)

    # Strip HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    # Store generated RST links/roles in placeholders so HTML tag stripping and * / | escaping never touch them
    placeholders: list[str] = []

    def _stash(rst_str: str) -> str:
        idx = len(placeholders)
        placeholders.append(rst_str)
        return f"\x00PH{idx}PH\x00"

    def _stash_math_html(math_html: str) -> str:
        ltx = formula_html_to_latex(math_html)
        if not ltx:
            return math_html
        return _stash(f":math:`{ltx}`")

    # Convert <a href="...">label</a>
    def _replace_anchor(match: re.Match) -> str:
        attrs = match.group(1)
        inner = match.group(2)
        inner_clean = " ".join(re.sub(r"<[^>]+>", "", inner).split()).strip()
        inner_escaped = inner_clean.replace("*", r"\*").replace("|", r"\|")
        href_m = re.search(r'href=["\']?([^"\'\s>]+)["\']?', attrs, re.IGNORECASE)
        if not href_m:
            return inner_escaped
        href = href_m.group(1).strip()
        if not inner_clean:
            inner_clean = href
            inner_escaped = href

        # Internal center anchor (#X15 or ETC.html#X15)
        xm = re.search(r"#X(\d+)$", href, re.IGNORECASE)
        if xm:
            xnum = int(xm.group(1))
            if valid_centers is None or xnum in valid_centers:
                return _stash(f":ref:`{inner_clean} <X({xnum})>`")
            return _stash(f"**{inner_escaped}**")

        # Internal glossary anchor (#term)
        if "glossary.html#" in href.lower() or href.startswith("#"):
            frag = href.split("#", 1)[-1].strip()
            if frag:
                slug = apparatus_slug(frag)
                return _stash(f":term:`{inner_clean} <{slug}>`")

        # External http/https link
        if href.startswith(("http://", "https://")):
            return _stash(f"`{inner_clean} <{href}>`__")

        # Local relative file link (.gsp, .ggb, .html, .pdf)
        return _stash(f"**{inner_escaped}** (``{href}``)")

    text = re.sub(
        r"<a\b([^>]*)>(.*?)</a>",
        _replace_anchor,
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    # Normalize known HTML typo in X(442): N<sub>A</sub>&cap;<sub>B</sub>&cap;<sub>C</sub>
    text = text.replace("N<sub>A</sub>∩<sub>B</sub>∩<sub>C</sub>", "N<sub>A</sub>N<sub>B</sub>N<sub>C</sub>")

    # 1. Stash Shinagawa coefficients `( ... )` as :math:
    def _repl_shinagawa(m: re.Match) -> str:
        prefix = m.group(1)
        shin_expr = m.group(2).strip()
        if "\x00PH" in shin_expr:
            return m.group(0)
        return f"{prefix}{_stash_math_html(shin_expr)}"

    text = re.sub(
        r"(\bShinagawa\s+coefficients\s+)(\(.+?)(?=(?:\.\s*(?:\([A-Z][^()]+\)\.?\s*)?$|\s*$))",
        _repl_shinagawa,
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    # 2. Stash subscripted geometric elements (triangles, segments, points/lines/circles) as :g: roles
    _v_html_unit = r"[A-QT-Zℓ]['′″]*(?:<sub>[^<]+</sub>)?['′″]*"
    _v_html_item_re = re.compile(
        r"([A-QT-Zℓ])(['′″]*)(?:<sub>([^<]+)</sub>)?(['′″]*)"
    )

    def _parse_html_vertex(v_str: str) -> tuple[str, str]:
        vm = _v_html_item_re.fullmatch(v_str)
        if not vm:
            return v_str, v_str
        base = vm.group(1)
        pr1 = (vm.group(2) or "").replace("′", "'").replace("''", "″")
        sub = _remove_html_tags(vm.group(3) or "").strip()
        pr2 = (vm.group(4) or "").replace("′", "'").replace("''", "″")
        if sub:
            return f"{base}{pr1}_{{{sub}}}{pr2}", f"{base}{pr1}_{sub}{pr2}"
        return f"{base}{pr1}{pr2}", f"{base}{pr1}{pr2}"

    def _repl_sub_seq(m: re.Match) -> str:
        full = m.group(0)
        if "<sub" not in full.lower() or "\x00PH" in full:
            return full
        units = [u.group(0) for u in _v_html_item_re.finditer(full) if u.group(0)]
        if len(units) == 3:
            (d1, t1), (d2, t2), (d3, t3) = (
                _parse_html_vertex(units[0]),
                _parse_html_vertex(units[1]),
                _parse_html_vertex(units[2]),
            )
            return _stash(f":g:`{d1}{d2}{d3} << {t1} {t2} {t3} >>`")
        if len(units) == 2:
            (d1, t1), (d2, t2) = (
                _parse_html_vertex(units[0]),
                _parse_html_vertex(units[1]),
            )
            return _stash(f":g:`{d1}{d2} <[ {t1} {t2} ]>`")
        return full

    text = re.sub(
        rf"(?<![A-Za-z0-9_\\])(?:{_v_html_unit}){{2,3}}(?![A-Za-z0-9_'′″<])",
        _repl_sub_seq,
        text,
    )

    # Single uppercase geometric elements with <sub> (excluding S and R which are Conway / radius scalars)
    def _repl_geom_sub(m: re.Match) -> str:
        base = m.group(1)
        pr1 = (m.group(2) or "").replace("′", "'").replace("''", "″")
        sub = _remove_html_tags(m.group(3)).strip()
        pr2 = (m.group(4) or "").replace("′", "'").replace("''", "″")
        if not sub or "\x00PH" in sub:
            return m.group(0)
        disp = f"{base}{pr1}_{{{sub}}}{pr2}"
        targ = f"{base}{pr1}_{sub}{pr2}"
        return _stash(f":g:`{disp} <{targ}>`")

    text = re.sub(
        r"(?<![A-Za-z0-9_\\])([A-QT-Zℓ])(['′″]*)<sub>([^<]+)</sub>(['′″]*)",
        _repl_geom_sub,
        text,
    )

    # 3. Stash inline mathematical equations, ratios, and scalar formulas as :math:
    # 3a. Classical inradius/circumradius/exradius equations and area/sqrt formulas
    inline_eq_patterns = [
        r"\b1/r\s*=\s*1/r<sub>a</sub>\s*\+\s*1/r<sub>b</sub>\s*\+\s*1/r<sub>c</sub>",
        r"\br<sub>a</sub>\s*\+\s*r<sub>b</sub>\s*\+\s*r<sub>c</sub>\s*=\s*r\s*\+\s*4R\b",
        r"\bR\s*=\s*a/\(2\s*sin\s*A\)\s*=\s*abc/\(4\s*\*?\s*[Aa]rea\(ABC\)\)",
        r"\br\s*=\s*2\s*\*?\s*[Aa]rea\(ABC\)/\(a\s*\+\s*b\s*\+\s*c\)",
        r"\b[Aa]rea\(ABC\)\s*=\s*sqrt\([^()]+\)",
        r"\bcot\s+D/2\s*=\s*[^\s,.;]+(?:\s*[+\-*/]\s*[^\s,.;]+)*",
        r"\b2\s*\*\s*[Aa]rea\(ABC\)/\([+\-a-c\s]+\)",
        r"\bsqrt\((?:[^()]|\([^()]*\))+\)",
        r"\bSqrt\[[^\[\]]+\]",
        r"\([x-z\s:]+\)\s*\*\s*\([u-w\s:]+\)\s*=\s*xu\s*:\s*yv\s*:\s*zw",
        r"\b\|f\([a-c,\s]+\)\|\s*≠\s*\|f\([a-c,\s]+\)\|",
        r"\bf\(ta,\s*tb,\s*tc\)\s*=\s*t<sup>h</sup>f\(a,\s*b,\s*c\)",
        r"\b[abc]\s*[≤≥]\s*[abc]\s*\+\s*[abc]\b",
        r"\bx\s*\+\s*y\s*\+\s*z\s*=\s*0\b",
        r"\[area\s+of\s+T\([ABC],\s*X\)\]\[X\([ABC]\)\]<sup>2</sup>(?:\s*=\s*\[area\s+of\s+T\([ABC],\s*X\)\]\[X\([ABC]\)\]<sup>2</sup>)+",
        r"\(distance\s+from\s+[^()]+\)<sup>2</sup>(?:\s*:\s*:)?",
        r"\(SB\s*-\s*SC\)\(SC\s*-\s*SA\)\(SA\s*-\s*SB\)/[^.]+",
        r"\bF\s*=\s*x\[a<sub>4</sub>[^\n.]+",
    ]
    for pat_str in inline_eq_patterns:
        text = re.sub(
            pat_str,
            lambda m: _stash_math_html(m.group(0)) if "\x00PH" not in m.group(0) else m.group(0),
            text,
        )

    # 3b. Homogeneous coordinate triples in prose (e.g., p : q : r, -1 : 1 : 1, 1/a : 1/b : 1/c, csc^4(A/4) : ... : ...)
    _coord_comp = r"-?\s*(?:[0-9a-zA-Z_'′″]+(?:\([^()]+\)|(?:<sup>[^<]+</sup>|<sub>[^<]+</sub>)+)?(?:/[0-9a-zA-Z_'′″()]+)?)"
    _coord_triple_re = re.compile(
        rf"(?<![A-Za-z0-9_:])({_coord_comp}\s*:\s*{_coord_comp}\s*:\s*{_coord_comp})(?![A-Za-z0-9_:])"
    )
    text = _coord_triple_re.sub(
        lambda m: _stash_math_html(m.group(1)) if "\x00PH" not in m.group(1) else m.group(1),
        text,
    )

    # 3c. Explicit function definitions in prose like `where f(p,q,r,A) = (q^2 + r^2 + 2qr cos A)^1/2`
    def _repl_func_def(m: re.Match) -> str:
        full = m.group(0)
        if "\x00PH" in full or "X(" in full or "X[" in full:
            return full
        trail = ""
        while full and full[-1] in ".,;":
            trail = full[-1] + trail
            full = full[:-1]
        return _stash_math_html(full) + trail

    text = re.sub(
        r"\b[fghFGkH]\([a-zA-Z0-9,\s:]+\)\s*=\s*(?:(?!(?:\s+and\b|\s+where\b|\s+for\b))[0-9a-zA-Z_+\-*/^()\[\]\s<>′″'ωΩπ])+",
        _repl_func_def,
        text,
    )

    # 3d. Cyclic sum `$...$` notation in prose
    text = re.sub(
        r"\$[^\$]+\$",
        lambda m: _stash_math_html(m.group(0)) if "\x00PH" not in m.group(0) else m.group(0),
        text,
    )

    # 3e. Remaining scalar tokens with <sub> or non-ordinal <sup> (e.g., r_a, R_a, S_A, S^2, a^2, g(X^-1))
    def _repl_scalar_supsub(m: re.Match) -> str:
        tok = m.group(0)
        if "\x00PH" in tok:
            return tok
        # Skip English ordinals like 1st, 2nd, 3rd, 4th
        if re.match(r"^\d+<sup>(?:st|nd|rd|th)</sup>$", tok, flags=re.IGNORECASE):
            return tok
        return _stash_math_html(tok)

    text = re.sub(
        r"(?:[a-zA-Z]+\()?[a-zA-Z0-9]+(?:\s*(?:<sup>[^<]+</sup>|<sub>[^<]+</sub>))+(?:\)|['′″]|\([^()]+\))?",
        _repl_scalar_supsub,
        text,
    )

    # Convert any remaining <sup>...</sup> and <sub>...</sub> into RST :sup: and :sub:
    def _replace_sup(match: re.Match) -> str:
        raw_inner = match.group(1)
        trail = " " if raw_inner[-1:].isspace() else ""
        val = " ".join(re.sub(r"<[^>]+>", "", raw_inner).split()).strip()
        if not val:
            return trail
        val = val.replace("*", r"\*").replace("|", r"\|")
        return _stash(f":sup:`{val}`") + trail

    def _replace_sub(match: re.Match) -> str:
        raw_inner = match.group(1)
        trail = " " if raw_inner[-1:].isspace() else ""
        val = " ".join(re.sub(r"<[^>]+>", "", raw_inner).split()).strip()
        if not val:
            return trail
        val = val.replace("*", r"\*").replace("|", r"\|")
        return _stash(f":sub:`{val}`") + trail

    text = re.sub(
        r"<sup>(.*?)</sup>", _replace_sup, text, flags=re.DOTALL | re.IGNORECASE
    )
    text = re.sub(
        r"<sub>(.*?)</sub>", _replace_sub, text, flags=re.DOTALL | re.IGNORECASE
    )

    # Convert <b>...</b> and <i>...</i> / <var>...</var>
    def _replace_bold(match: re.Match) -> str:
        raw_inner = match.group(1)
        lead = " " if raw_inner[:1].isspace() else ""
        trail = " " if raw_inner[-1:].isspace() else ""
        val = " ".join(re.sub(r"<[^>]+>", "", raw_inner).split()).strip()
        if not val or "**" in val or "\x00PH" in val:
            return lead + val + trail
        val = val.replace("*", r"\*").replace("|", r"\|")
        return lead + _stash(f"**{val}**") + trail

    def _replace_italic(match: re.Match) -> str:
        raw_inner = match.group(1)
        lead = " " if raw_inner[:1].isspace() else ""
        trail = " " if raw_inner[-1:].isspace() else ""
        val = " ".join(re.sub(r"<[^>]+>", "", raw_inner).split()).strip()
        if not val or "*" in val or "\x00PH" in val:
            return lead + val + trail
        val = val.replace("*", r"\*").replace("|", r"\|")
        return lead + _stash(f"*{val}*") + trail

    text = re.sub(
        r"<b\b[^>]*>(.*?)</b>", _replace_bold, text, flags=re.DOTALL | re.IGNORECASE
    )
    text = re.sub(
        r"<(?:i|var)\b[^>]*>(.*?)</(?:i|var)>",
        _replace_italic,
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )

    # Strip any remaining HTML tags
    text = re.sub(r"</?[a-zA-Z][a-zA-Z0-9]*(?:\s+[^>]*)?>", " ", text)
    # Collapse all whitespace (including raw newlines/tabs from soft-wrapped HTML) into single spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Escape literal asterisks and vertical bars in plain text so docutils never treats them as emphasis or substitutions
    text = text.replace("*", r"\*").replace("|", r"\|")

    # Restore stashed RST spans, adding `\ ` only where needed by Docutils inline markup rules
    def _restore_all(s: str) -> str:
        pattern = re.compile(r"\x00PH(\d+)PH\x00")
        while True:
            m = pattern.search(s)
            if not m:
                break
            idx = int(m.group(1))
            rst_val = placeholders[idx]
            start, end = m.start(), m.end()
            prev_ch = s[start - 1] if start > 0 else " "
            next_ch = s[end] if end < len(s) else " "

            need_pre = prev_ch not in " \t\n-:/'\"<([{"
            need_post = next_ch not in " \t\n-.,:;!?/'\")>]}"

            prefix = r"\ " if need_pre else ""
            suffix = r"\ " if need_post else ""
            s = s[:start] + prefix + rst_val + suffix + s[end:]
        return s

    text = _restore_all(text)
    return text.strip()


def _wrap_x_refs_simple(
    text: str, valid_centers: set[int] | None = None
) -> str:
    """Wrap X(n) and X[n] references in :ref:`X(n) <X(n)>` when n is in valid_centers."""
    if not text:
        return ""

    pattern = re.compile(r"(?<![a-z`:])X[\(\[](\d+)[\)\]](?!`)")

    def _repl_seg(seg: str) -> str:
        out: list[str] = []
        last_idx = 0
        for m in pattern.finditer(seg):
            num_str = m.group(1)
            num = int(num_str)
            start, end = m.start(), m.end()
            out.append(seg[last_idx:start])
            if valid_centers is not None and num not in valid_centers:
                out.append(f"X({num_str})")
            else:
                prev_ch = seg[start - 1] if start > 0 else " "
                next_ch = seg[end] if end < len(seg) else " "
                need_pre = (prev_ch not in " \t\n-:/'\"<([{") and not (
                    last_idx == start and out and out[-1].endswith(r"\ ")
                )
                need_post = next_ch not in " \t\n-.,:;!?/'\")>]}"
                prefix = r"\ " if need_pre else ""
                suffix = r"\ " if need_post else ""
                out.append(f"{prefix}:ref:`X({num_str}) <X({num_str})>`{suffix}")
            last_idx = end
        out.append(seg[last_idx:])
        return "".join(out)

    return _apply_outside_rst_spans(text, _repl_seg)


def filter_center_refs(
    rst_text: str, valid_centers: set[int] | None
) -> str:
    """Downgrade any `:ref:`label <X(n)>`` to plain `label` when `n` is not in `valid_centers`."""
    if not rst_text or valid_centers is None:
        return rst_text

    def _check_ref(m: re.Match) -> str:
        label = m.group(1)
        xnum = int(m.group(2))
        if xnum in valid_centers:
            return m.group(0)
        return label

    return re.sub(r":ref:`([^`<]+?)\s*<X\((\d+)\)>`", _check_ref, rst_text)


def _format_eqn_line_html(ln_html: str) -> str:
    """Format a `<p class="eqn">` line from the Glossary into `:math:` or mixed RST."""
    raw = ln_html.strip()
    if not raw:
        return ""
    plain = " ".join(clean_html_entities(_remove_html_tags(raw)).split()).strip()
    if not plain:
        return ""

    if (
        plain.lower().startswith("where ")
        and "=" in plain
        and "intersect" not in plain.lower()
        and "conjugate" not in plain.lower()
    ):
        m_w = re.match(r"^\s*(where\s+)(.+)$", raw, flags=re.DOTALL | re.IGNORECASE)
        if m_w:
            return f"where {_format_eqn_line_html(m_w.group(2))}"

    # Prose or geometric incidence lines inside <p class="eqn">
    if (
        plain.lower().startswith(("where ", "if ", "for "))
        or "intersect" in plain.lower()
        or "conjugate" in plain.lower()
        or plain.startswith("{")
    ):
        return wrap_geom_refs(_wrap_x_refs_simple(convert_inline_html_to_rst(raw)))

    # Trailing parenthetical note like "(barycentrics)" or "for all (a,b,c) in the domain of f;"
    suffix_rst = ""
    m_for = re.match(r"^(.+?)\s+(for\s+all\b.*)$", raw, flags=re.DOTALL | re.IGNORECASE)
    if m_for:
        raw = m_for.group(1).strip()
        suffix_rst = f" {wrap_geom_refs(convert_inline_html_to_rst(m_for.group(2).strip()))}"
    else:
        m_par = re.match(r"^(.+?)\s*(\([a-zA-Z\s]+\))\s*$", raw, flags=re.DOTALL)
        if m_par:
            raw = m_par.group(1).strip()
            suffix_rst = f" {m_par.group(2).strip()}"

    trail_punct = ""
    while raw and raw[-1] in ".,;":
        trail_punct = raw[-1] + trail_punct
        raw = raw[:-1].rstrip()

    # Check if split by " and "
    if re.search(r"\s+and\s+", raw):
        parts = re.split(r"\s+and\s+", raw)
        ltx_parts = [f":math:`{formula_html_to_latex(p)}`" for p in parts if p.strip()]
        return " and ".join(ltx_parts) + trail_punct + suffix_rst

    ltx = formula_html_to_latex(raw)
    if not ltx:
        return wrap_geom_refs(_wrap_x_refs_simple(convert_inline_html_to_rst(ln_html)))
    return f":math:`{ltx}`{trail_punct}{suffix_rst}"


def _convert_glossary_section_to_rst(section_html: str) -> tuple[str, str]:
    """Convert the HTML body of a glossary entry into (plain_summary, rst_body)."""
    # Strip trailing "Return to ETC" footer if present
    section_html = re.sub(
        r"<hr[^>]*>\s*<a[^>]*>\s*Return to ETC\s*</a>.*$",
        "",
        section_html,
        flags=re.DOTALL | re.IGNORECASE,
    )
    soup = BeautifulSoup(section_html, "html.parser")

    blocks: list[str] = []
    plain_sentences: list[str] = []
    inline_buf: list[str] = []

    def _flush_inline_buf() -> None:
        if not inline_buf:
            return
        combined_html = "".join(inline_buf).strip()
        inline_buf.clear()
        if not combined_html:
            return
        plain_s = " ".join(clean_html_entities(_remove_html_tags(combined_html)).split()).strip()
        if not plain_s:
            return
        conv = wrap_geom_refs(_wrap_x_refs_simple(convert_inline_html_to_rst(combined_html)))
        if conv:
            blocks.append(conv)
            plain_sentences.append(plain_s)

    for child in soup.children:
        if isinstance(child, NavigableString):
            inline_buf.append(str(child))
            continue

        if not isinstance(child, Tag):
            continue

        tag_name = child.name.lower()
        if tag_name in ("a", "b", "i", "var", "sup", "sub", "span"):
            inline_buf.append(str(child))
            continue

        _flush_inline_buf()

        if tag_name == "h2":
            continue

        if tag_name == "p":
            cls = child.get("class") or []
            from .parser import _strip_software_and_nav_refs

            inner_html = child.decode_contents()
            if "eqn" in cls:
                raw_eq_lines = [
                    ln.strip()
                    for ln in re.split(r"<br\s*/?>", inner_html, flags=re.IGNORECASE)
                    if ln.strip()
                ]
                # Join continuation line starting with '+' or '-' onto previous line
                merged_eq_lines: list[str] = []
                for rln in raw_eq_lines:
                    plain_rln = _remove_html_tags(rln).strip()
                    if merged_eq_lines and plain_rln.startswith(("+", "-")):
                        merged_eq_lines[-1] = f"{merged_eq_lines[-1]} {rln}"
                    else:
                        merged_eq_lines.append(rln)
                fmt_eqs = [_format_eqn_line_html(rln) for rln in merged_eq_lines]
                fmt_eqs = [fe for fe in fmt_eqs if fe]
                if fmt_eqs:
                    blocks.append("\n".join(f"   {fe}" for fe in fmt_eqs))
                continue

            # Split on <br> if multi-line inside <p>
            br_lines = [
                wrap_geom_refs(
                    _strip_software_and_nav_refs(
                        _wrap_x_refs_simple(convert_inline_html_to_rst(ln))
                    )
                )
                for ln in re.split(r"<br\s*/?>", inner_html, flags=re.IGNORECASE)
            ]
            br_lines = [ln for ln in br_lines if ln]
            if not br_lines:
                continue

            if len(br_lines) == 1:
                blocks.append(br_lines[0])
            else:
                blocks.append("\n".join(f"| {ln}" for ln in br_lines))
            plain_txt = _strip_software_and_nav_refs(
                " ".join(
                    clean_html_entities(child.get_text(" ", strip=True)).split()
                )
            )
            if plain_txt:
                plain_sentences.append(plain_txt)

        elif tag_name in ("ul", "ol"):
            items: list[str] = []
            for li in child.find_all("li", recursive=False):
                li_rst = wrap_geom_refs(
                    _wrap_x_refs_simple(
                        convert_inline_html_to_rst(li.decode_contents())
                    )
                )
                if li_rst:
                    items.append(f"* {li_rst}")
            if items:
                blocks.append("\n".join(items))

        elif tag_name == "blockquote":
            inner_html = child.decode_contents()
            br_lines = [
                wrap_geom_refs(_wrap_x_refs_simple(convert_inline_html_to_rst(ln)))
                for ln in re.split(r"<br\s*/?>", inner_html, flags=re.IGNORECASE)
            ]
            br_lines = [ln for ln in br_lines if ln]
            if br_lines:
                blocks.append("\n".join(f"   | {ln}" for ln in br_lines))

        elif tag_name == "table":
            rows: list[str] = []
            for tr in child.find_all("tr"):
                cells = [
                    wrap_geom_refs(
                        _wrap_x_refs_simple(
                            convert_inline_html_to_rst(td.decode_contents())
                        )
                    )
                    for td in tr.find_all(["td", "th"])
                ]
                cells = [c for c in cells if c and not re.match(r"^[\.\s]+$", c)]
                if cells:
                    rows.append("   | " + "   —   ".join(cells))
            if rows:
                blocks.append("\n".join(rows))

    _flush_inline_buf()

    summary = " ".join(plain_sentences).strip()
    if len(summary) > 360:
        summary = summary[:357].rsplit(" ", 1)[0] + "..."
    rst_body = "\n\n".join(blocks)
    return summary, rst_body


def extract_glossary_terms(html_content: str) -> dict[str, Any]:
    """Extract all glossary terms, their rich RST bodies, and plain-text summaries from GLOSSARY HTML."""
    parts = re.split(r"(?=<h2\b)", html_content, flags=re.IGNORECASE)
    terms: dict[str, Any] = {}

    for part in parts[1:]:
        h2_match = re.match(
            r"<h2([^>]*)>(.*?)</h2>(.*)", part, flags=re.DOTALL | re.IGNORECASE
        )
        if not h2_match:
            continue
        h2_attrs, h2_inner, body_html = (
            h2_match.group(1),
            h2_match.group(2),
            h2_match.group(3),
        )
        headword = " ".join(
            clean_html_entities(re.sub(r"<[^>]+>", "", h2_inner)).split()
        ).strip()
        if not headword:
            continue

        id_match = re.search(r'id=["\']?([^"\'\s>]+)["\']?', h2_attrs, re.IGNORECASE)
        explicit_id = id_match.group(1) if id_match else None
        slug = apparatus_slug(explicit_id or headword)

        summary, rst_body = _convert_glossary_section_to_rst(body_html)
        terms[headword] = {
            "headword": headword,
            "slug": slug,
            "explicit_id": explicit_id,
            "definition": summary or headword,
            "rst": rst_body,
        }

    # Add the classical named triangles defined inside cevian, anticevian, and central triangle
    for tri_name, info in CLASSICAL_TRIANGLE_ALIASES.items():
        if tri_name not in terms:
            def_rst = wrap_geom_refs(
                _wrap_x_refs_simple(convert_inline_html_to_rst(info["definition"]))
            )
            terms[tri_name] = {
                "headword": tri_name,
                "slug": apparatus_slug(tri_name),
                "target_slug": info["target_slug"],
                "definition": info["definition"],
                "rst": f"{def_rst} (See :term:`{info['target_slug'].replace('-', ' ')} <{info['target_slug']}>`.)",
                "is_alias": True,
            }

    return terms


def extract_glossary_intro_rst(html_content: str) -> str:
    """Extract the introductory methodology section from GLOSSARY HTML as RST."""
    parts = re.split(r"(?=<h2\b)", html_content, flags=re.IGNORECASE)
    if not parts:
        return ""
    header_html = parts[0]
    # Remove everything up to the first <script>...</script> and "Last update: ..."
    header_html = re.sub(
        r"^.*?</script>\s*(?:<br\s*/?>)?\s*(?:Last update:[^\n<]*)?",
        "",
        header_html,
        flags=re.DOTALL | re.IGNORECASE,
    )
    _, rst_body = _convert_glossary_section_to_rst(header_html)
    return rst_body


def generate_glossary_rst(
    terms: dict[str, Any],
    intro_rst: str = "",
    valid_centers: set[int] | None = None,
) -> str:
    """Generate rich `docsrc/glossary.rst` with deterministic `#term-<slug>` anchors."""
    lines: list[str] = [
        ":navigation: header",
        ":order: 2",
        ":layout: book",
        ":book_title: Encyclopedia of Triangle Centers",
        "",
        ".. _glossary:",
        "",
        "Glossary",
        "========",
        "",
    ]

    if intro_rst:
        lines.extend(
            [
                filter_center_refs(intro_rst, valid_centers),
                "",
                "----",
                "",
            ]
        )

    for term_key in sorted(terms.keys(), key=lambda k: k.lower()):
        entry = terms[term_key]
        if isinstance(entry, str):
            # Backwards-compatibility if called with dict[str, str]
            slug = apparatus_slug(term_key)
            headword = term_key
            rst_body = entry
            explicit_id = None
        else:
            slug = entry["slug"]
            headword = entry["headword"]
            rst_body = entry["rst"]
            explicit_id = entry.get("explicit_id")

        anchors = {f"term-{slug}", slug}
        if explicit_id:
            anchors.add(f"term-{apparatus_slug(explicit_id)}")
            anchors.add(apparatus_slug(explicit_id))

        for anchor in sorted(anchors):
            lines.append(f".. _{anchor}:")
        lines.append("")
        lines.append(headword)
        lines.append("-" * max(4, len(headword)))
        lines.append("")
        if rst_body:
            lines.append(filter_center_refs(rst_body, valid_centers))
            lines.append("")

    return "\n".join(lines)


def build_glossary_json(terms: dict[str, Any]) -> dict[str, dict[str, str]]:
    """Build the `resources/glossary.json` dictionary keyed by both slug and headword."""
    reg: dict[str, dict[str, str]] = {}
    for term_key, entry in terms.items():
        if isinstance(entry, str):
            slug = apparatus_slug(term_key)
            item = {"headword": term_key, "definition": entry[:300]}
        else:
            slug = entry["slug"]
            item = {
                "headword": entry["headword"],
                "definition": entry["definition"],
            }
        reg[slug] = item
        reg[term_key] = item
        reg[term_key.lower()] = item
    return reg


def build_persons_json() -> dict[str, dict[str, Any]]:
    """Build the `resources/persons.json` dictionary keyed by slug and alias."""
    reg: dict[str, dict[str, Any]] = {}
    for slug, info in PERSONS_REGISTRY.items():
        entry = {
            "name": info["name"],
            "dates": info["dates"],
            "role": info["role"],
        }
        reg[slug] = entry
        for alias in info.get("aliases", []):
            reg[alias] = entry
            reg[apparatus_slug(alias)] = entry
    return reg


def build_citations_json() -> dict[str, dict[str, str]]:
    """Build the `resources/citations.json` dictionary."""
    return dict(CITATIONS_REGISTRY)


def generate_persons_rst(valid_centers: set[int] | None = None) -> str:
    """Generate `docsrc/persons.rst` with `#person-<slug>` anchors for all `:person:` links."""
    lines = [
        ":navigation: header",
        ":order: 3",
        ":layout: book",
        ":book_title: Encyclopedia of Triangle Centers",
        "",
        ".. _persons:",
        "",
        "Index Nominum (Geometers & Contributors)",
        "========================================",
        "",
        "Biographical register of classical geometers and modern contributors referenced across the *Encyclopedia of Triangle Centers*.",
        "",
    ]
    for slug, info in sorted(
        PERSONS_REGISTRY.items(), key=lambda kv: kv[1]["name"].split()[-1].lower()
    ):
        heading = (
            f"{info['name']} ({info['dates']})" if info.get("dates") else info["name"]
        )
        lines.append(f".. _person-{slug}:")
        lines.append(f".. _{slug}:")
        lines.append("")
        lines.append(heading)
        lines.append("-" * max(4, len(heading)))
        lines.append("")
        role_rst = convert_inline_html_to_rst(info["role"])
        role_rst = _wrap_x_refs_simple(role_rst, valid_centers=valid_centers)
        role_rst = wrap_geom_refs(role_rst)
        lines.append(role_rst)
        lines.append("")
    return "\n".join(lines)


def generate_bibliography_rst() -> str:
    """Generate `docsrc/bibliography.rst` with `#cite-<slug>` anchors for all `:cite:` links."""
    lines = [
        ":navigation: header",
        ":order: 4",
        ":layout: book",
        ":book_title: Encyclopedia of Triangle Centers",
        "",
        ".. _bibliography:",
        "",
        "Bibliography & Cited Sources",
        "============================",
        "",
        "Primary monographs, journals, catalogs, and research forums cited across the *Encyclopedia of Triangle Centers*.",
        "",
    ]
    for slug, info in sorted(CITATIONS_REGISTRY.items()):
        heading = f"{info['author']} — {info['work']}"
        lines.append(f".. _cite-{slug}:")
        lines.append(f".. _{slug}:")
        lines.append("")
        lines.append(heading)
        lines.append("-" * max(4, len(heading)))
        lines.append("")
        lines.append(f"* **Locus**: {info['locus']}")
        if info.get("notes"):
            lines.append(f"* **Notes**: {info['notes']}")
        lines.append("")
    return "\n".join(lines)


# Tokenization pattern to protect existing RST roles and links from nested replacement
_PROTECTED_RST_SPAN_RE = re.compile(
    r"(:[a-zA-Z0-9_]+:`[^`]+`|``[^`]+``|`[^`]+`__?|(?<!\\)\*\*(?:\\.|[^*\n])+\*\*)"
)


def _apply_outside_rst_spans(text: str, transform_fn: Any) -> str:
    """Apply `transform_fn` only to plain text segments outside existing RST roles/links."""
    parts = _PROTECTED_RST_SPAN_RE.split(text)
    out: list[str] = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            out.append(part)
        else:
            out.append(transform_fn(part))
    return "".join(out)


_V_PLAIN_TOK = r"[A-Z](?:''|″|\"|'|′|\\\*|\*)?"
_V_PLAIN_TRI_RE = re.compile(
    rf"(?<![A-Za-z0-9_\x00])({_V_PLAIN_TOK})({_V_PLAIN_TOK})({_V_PLAIN_TOK})(?![A-Za-z0-9_'′″\"*(\x00])"
)
_V_PLAIN_SEG_RE = re.compile(
    rf"(?<![A-Za-z0-9_\x00])({_V_PLAIN_TOK})({_V_PLAIN_TOK})(?![A-Za-z0-9_'′″\"*(\x00])"
)
_SUB_3V_UNSUB_RE = re.compile(
    r"(?<![A-Za-z0-9_\x00])([A-QT-Z])(['′″]?)([a-c1-9]?)(['′″]?)([A-QT-Z])(['′″]?)([a-c1-9]?)(['′″]?)([A-QT-Z])(['′″]?)([a-c1-9]?)(['′″]?)(?![A-Za-z0-9_'′″\x00])"
)
_SUB_2V_UNSUB_RE = re.compile(
    r"(?<![A-Za-z0-9_\x00])([A-Z])(['′″]?)([a-c1-9]?)(['′″]?)([A-Z])(['′″]?)([a-c1-9]?)(['′″]?)(?![A-Za-z0-9_'′″\x00])"
)
_SUB_1V_UNSUB_RE = re.compile(
    r"(?<![A-Za-z0-9_\x00])(?:([A-QT-WYZ])(['′″]?)([a-c1-9])(['′″]?)|(S)(['′″]?)([abc])(['′″]?))(?![A-Za-z0-9_'′″\x00])"
)
_RADII_UNSUB_RE = re.compile(
    r"(?<![A-Za-z0-9_\x00])R([abcs])(['′]?)(?![A-Za-z0-9_'′\x00])"
)
_PRIMED_1V_RE = re.compile(
    r"(?<![A-Za-z0-9_\x00])([A-QT-Z])(''|″|\"|'|′|\\\*|\*)(?![A-Za-z0-9_'′″\"*\x00])"
)
_TRI_AUX_POINTS = {
    "P", "Q", "X", "O", "H", "I", "G", "K", "N", "F", "U", "V", "S"
}
_NAMED_3V_TUPLES = {
    ("D", "E", "F"),
    ("U", "V", "W"),
    ("P", "Q", "X"),
    ("A", "D", "E"),
    ("A", "E", "F"),
}
_SEG_AUX_POINTS = {
    "P", "Q", "X", "O", "H", "I", "K", "D", "E", "F", "U", "V"
}
_NAMED_2V_PAIRS = {
    "PQ", "PX", "PO", "PU", "OI", "OG", "OP", "QO", "IO",
    "DE", "EF", "FD", "DU", "EV", "FW", "DV", "DW", "EU", "EW", "FU", "FV",
    "UV", "VW", "WU", "XY",
}


def _norm_plain_vertex(v: str) -> tuple[str, str]:
    v_clean = v.replace(r"\*", "*").replace("′", "'").replace("''", "″").replace('"', "″")
    return v_clean, v_clean


def wrap_geom_refs(text: str) -> str:
    """Wrap geometric elements (triangles, segments, lines, circles, points) in `:g:` roles."""
    if not text:
        return text

    def _replace_geom(seg: str) -> str:
        stashed: list[str] = []

        def _stash_g(role_str: str) -> str:
            idx = len(stashed)
            stashed.append(role_str)
            return f"\x00GM{idx}GM\x00"

        # 1. Bracketed vertex notation [A], [B], [C]
        seg = re.sub(
            r"(?<![A-Za-z0-9_\x00])\[([ABC])\](?![A-Za-z0-9_\x00])",
            lambda m: _stash_g(f":g:`{m.group(1)} <{m.group(1)}>`"),
            seg,
        )

        # 2. Unsubscripted 3-vertex subscripted triangles (IaIbIc, AaBaCa, A1B1C1, AbBCb, etc.)
        def _repl_3v_unsub(m: re.Match) -> str:
            l1, p1a, s1, p1b, l2, p2a, s2, p2b, l3, p3a, s3, p3b = (
                m.group(1), m.group(2) or "", m.group(3) or "", m.group(4) or "",
                m.group(5), m.group(6) or "", m.group(7) or "", m.group(8) or "",
                m.group(9), m.group(10) or "", m.group(11) or "", m.group(12) or "",
            )
            if not (s1 or s2 or s3):
                return m.group(0)
            # Either all 3 have subscripts, or {l1, l2, l3} == {"A", "B", "C"}
            if not ((s1 and s2 and s3) or {l1, l2, l3} == {"A", "B", "C"}):
                return m.group(0)

            def _fmt(L: str, pa: str, s: str, pb: str) -> tuple[str, str]:
                pa = pa.replace("′", "'").replace("''", "″")
                pb = pb.replace("′", "'").replace("''", "″")
                if s:
                    return f"{L}{pa}_{{{s}}}{pb}", f"{L}{pa}_{s}{pb}"
                return f"{L}{pa}{pb}", f"{L}{pa}{pb}"

            (d1, t1), (d2, t2), (d3, t3) = (
                _fmt(l1, p1a, s1, p1b),
                _fmt(l2, p2a, s2, p2b),
                _fmt(l3, p3a, s3, p3b),
            )
            return _stash_g(f":g:`{d1}{d2}{d3} << {t1} {t2} {t3} >>`")

        seg = _SUB_3V_UNSUB_RE.sub(_repl_3v_unsub, seg)

        # 3. 3-vertex plain/primed triangles (ABC, A'B'C', A″B″C″, BXC, BCP, BCF, DEF, UVW, etc.)
        def _repl_3v_plain(m: re.Match) -> str:
            v1, v2, v3 = m.group(1), m.group(2), m.group(3)
            b1, b2, b3 = v1[0], v2[0], v3[0]
            has_prime = (len(v1) > 1) or (len(v2) > 1) or (len(v3) > 1)
            abc_set = {"A", "B", "C"}

            is_valid = False
            if {b1, b2, b3} == abc_set:
                is_valid = True
            elif b1 in abc_set and b2 in abc_set and b3 in abc_set and has_prime:
                is_valid = True
            elif (b1, b2, b3) in _NAMED_3V_TUPLES:
                is_valid = True
            else:
                abc_in = [b for b in (b1, b2, b3) if b in abc_set]
                other_in = [b for b in (b1, b2, b3) if b not in abc_set]
                if (
                    len(abc_in) == 2
                    and abc_in[0] != abc_in[1]
                    and len(other_in) == 1
                    and other_in[0] in _TRI_AUX_POINTS
                ):
                    is_valid = True

            if not is_valid:
                return m.group(0)

            (d1, t1), (d2, t2), (d3, t3) = (
                _norm_plain_vertex(v1),
                _norm_plain_vertex(v2),
                _norm_plain_vertex(v3),
            )
            return _stash_g(f":g:`{d1}{d2}{d3} << {t1} {t2} {t3} >>`")

        seg = _V_PLAIN_TRI_RE.sub(_repl_3v_plain, seg)

        # 4. 2-vertex segments/lines with unsubscripted [a-c1-9] on one or both vertices (AIa, ASa, TbTc, etc.)
        def _repl_2v_unsub(m: re.Match) -> str:
            l1, p1a, s1, p1b, l2, p2a, s2, p2b = (
                m.group(1), m.group(2) or "", m.group(3) or "", m.group(4) or "",
                m.group(5), m.group(6) or "", m.group(7) or "", m.group(8) or "",
            )
            if not (s1 or s2):
                return m.group(0)
            if (l1, s1, l2, s2) == ("S", "", "A", "a"):
                return m.group(0)

            def _fmt(L: str, pa: str, s: str, pb: str) -> tuple[str, str]:
                pa = pa.replace("′", "'").replace("''", "″")
                pb = pb.replace("′", "'").replace("''", "″")
                if s:
                    return f"{L}{pa}_{{{s}}}{pb}", f"{L}{pa}_{s}{pb}"
                return f"{L}{pa}{pb}", f"{L}{pa}{pb}"

            (d1, t1), (d2, t2) = _fmt(l1, p1a, s1, p1b), _fmt(l2, p2a, s2, p2b)
            return _stash_g(f":g:`{d1}{d2} <[ {t1} {t2} ]>`")

        seg = _SUB_2V_UNSUB_RE.sub(_repl_2v_unsub, seg)

        # 5. 2-vertex plain/primed segments and sidelines (BC, CA, AB, B'C', AA', AP, BP, CP, etc.)
        def _repl_2v_plain(m: re.Match) -> str:
            v1, v2 = m.group(1), m.group(2)
            b1, b2 = v1[0], v2[0]
            has_prime = (len(v1) > 1) or (len(v2) > 1)
            abc_set = {"A", "B", "C"}

            is_valid = False
            if has_prime:
                is_valid = True
            elif b1 != b2:
                if b1 in abc_set and b2 in abc_set:
                    is_valid = True
                elif (b1 in abc_set and b2 in _SEG_AUX_POINTS) or (
                    b2 in abc_set and b1 in _SEG_AUX_POINTS
                ):
                    is_valid = True
                elif (b1 + b2) in _NAMED_2V_PAIRS:
                    is_valid = True

            if not is_valid:
                return m.group(0)

            (d1, t1), (d2, t2) = _norm_plain_vertex(v1), _norm_plain_vertex(v2)
            return _stash_g(f":g:`{d1}{d2} <[ {t1} {t2} ]>`")

        seg = _V_PLAIN_SEG_RE.sub(_repl_2v_plain, seg)

        # 6. Unsubscripted 2-char single elements (Oa, La, Na, Ia, Ma, Ha, Ta, Ja, Pa, Sa, A1, etc.) and radii (Ra, Rb, Rc, Rs)
        seg = _RADII_UNSUB_RE.sub(
            lambda m: _stash_g(f":math:`R_{{{m.group(1)}}}{m.group(2) or ''}`"),
            seg,
        )

        def _repl_1v_unsub(m: re.Match) -> str:
            if m.group(1):
                L, pa, s, pb = m.group(1), m.group(2) or "", m.group(3), m.group(4) or ""
            else:
                L, pa, s, pb = m.group(5), m.group(6) or "", m.group(7), m.group(8) or ""
            pa = pa.replace("′", "'").replace("''", "″")
            pb = pb.replace("′", "'").replace("''", "″")
            return _stash_g(f":g:`{L}{pa}_{{{s}}}{pb} <{L}{pa}_{s}{pb}>`")

        seg = _SUB_1V_UNSUB_RE.sub(_repl_1v_unsub, seg)

        # 7. Primed single-letter elements (A', B', C', A″, B″, C″, P', Q', O', F', X', L', etc.)
        def _repl_1v_primed(m: re.Match) -> str:
            d, t = _norm_plain_vertex(m.group(0))
            return _stash_g(f":g:`{d} <{t}>`")

        seg = _PRIMED_1V_RE.sub(_repl_1v_primed, seg)

        # 8. Unprimed single-letter vertices/points in geometric contexts
        # 8a. Triples like "A, B, C" / "B,C,A" / "A, B, and C" / "D, E, F" / "U, V, W"
        def _repl_abc_triple(m: re.Match) -> str:
            v1, v2, conj, v3 = m.group(1), m.group(2), m.group(3), m.group(4)
            if {v1, v2, v3} not in ({"A", "B", "C"}, {"D", "E", "F"}, {"U", "V", "W"}):
                return m.group(0)
            return (
                f"{_stash_g(f':g:`{v1} <{v1}>`')}, "
                f"{_stash_g(f':g:`{v2} <{v2}>`')}, "
                + (f"{conj} " if conj else "")
                + f"{_stash_g(f':g:`{v3} <{v3}>`')}"
            )

        seg = re.sub(
            r"(?<![A-Za-z0-9_\x00])\b([ABCDEFUVW])\s*,\s*([ABCDEFUVW])\s*,\s*(?:(and|or)\s+)?([ABCDEFUVW])\b(?![A-Za-z0-9_'′″\x00])",
            _repl_abc_triple,
            seg,
        )

        # 8b. Pairs like "B and C", "C and A", "A and B", "E and F", "V and W", "P and Q"
        seg = re.sub(
            r"(?<![A-Za-z0-9_\x00])\b([ABCEFPVW])\s+(and|or)\s+([ABCEFQVW])\b(?![A-Za-z0-9_'′″.\x00])",
            lambda m: (
                f"{_stash_g(f':g:`{m.group(1)} <{m.group(1)}>`')} {m.group(2)} "
                f"{_stash_g(f':g:`{m.group(3)} <{m.group(3)}>`')}"
            ),
            seg,
        )

        # 8c. Hyphenated vertex/point prefixes like A-vertex, A-excircle, P-cevian, P-Brocard, P-aleph
        seg = re.sub(
            r"(?<![A-Za-z0-9_\x00-])([ABCPQXU])(?=-vertex|-excircle|-excenter|-altitude|-bisector|-median|-cevian|-anticevian|-symmedian|-mixtilinear|-pedal|-antipedal|-perspector|-circumconic|-inconic|-Brocard|-isogonal|-isotomic|-Hirst|-aleph|-beth|-gimel|-he|-waw|-zayin|-ceva|-polar|-conic|-cubic|-line|-circle|-point|-triangle\b)",
            lambda m: _stash_g(f":g:`{m.group(1)} <{m.group(1)}>`"),
            seg,
        )

        # 8d. Single letter before `=` (e.g. `Let P = ...`, `Suppose that T = ...`, `D = E = A`)
        seg = re.sub(
            r"(?<![A-Za-z0-9_\x00])\b([ABCPQULOEFXTD])(?=\s*=[^=])",
            lambda m: _stash_g(f":g:`{m.group(1)} <{m.group(1)}>`"),
            seg,
        )

        # 8e. Single letter after geometric prepositions/nouns (excluding person initials like `A. P.`)
        seg = re.sub(
            r"\b(vertex|vertices|point|points|angle|angles|line|lines|circle|circles|triangle|triangles|centered\s+at|through|opposite|about|around|Let|let|at|from|of|in|on|to|with|for)\s+([ABCPQULOEFXTDHIKN])(?=(?:[,;:)—]|\.(?!\s+[A-Z])|\s+(?:and|or|is|are|be|denote|in|on|of|to|with|from|at|parallel|perpendicular|tangent|opposite|where|which|that|for|wrt)\b|$))",
            lambda m: f"{m.group(1)} {_stash_g(f':g:`{m.group(2)} <{m.group(2)}>`')}",
            seg,
        )

        # Restore stashed :g: / :math: roles with Docutils-safe boundary escaping
        gm_pat = re.compile(r"\x00GM(\d+)GM\x00")
        while True:
            m = gm_pat.search(seg)
            if not m:
                break
            idx = int(m.group(1))
            rst_val = stashed[idx]
            start, end = m.start(), m.end()
            prev_ch = seg[start - 1] if start > 0 else " "
            next_ch = seg[end] if end < len(seg) else " "

            need_pre = prev_ch not in " \t\n-:/'\"<([{"
            need_post = (
                next_ch not in " \t\n-.,:;!?/'\")>]}"
            ) and not seg[end:].startswith(r"\ ")

            prefix = r"\ " if need_pre else ""
            suffix = r"\ " if need_post else ""
            seg = seg[:start] + prefix + rst_val + suffix + seg[end:]

        return seg

    return _apply_outside_rst_spans(text, _replace_geom)


_GLOSSARY_PATTERN_CACHE: dict[int, tuple[dict[str, str], re.Pattern[str]]] = {}


def _get_glossary_lookup_and_pattern(
    terms: dict[str, Any] | list[str],
) -> tuple[dict[str, str], re.Pattern[str]] | None:
    cache_key = id(terms)
    if cache_key in _GLOSSARY_PATTERN_CACHE:
        return _GLOSSARY_PATTERN_CACHE[cache_key]

    if isinstance(terms, dict):
        term_names = [
            k for k in terms.keys() if k.lower() not in SKIP_AUTO_WRAP_TERMS
        ]
    else:
        term_names = [
            t for t in terms if t.lower() not in SKIP_AUTO_WRAP_TERMS
        ]

    if not term_names:
        return None

    lookup: dict[str, str] = {}
    phrases: list[str] = []
    for t in term_names:
        slug = (
            terms[t]["slug"]
            if isinstance(terms, dict) and isinstance(terms.get(t), dict)
            else apparatus_slug(t)
        )
        low = t.lower()
        lookup[low] = slug
        phrases.append(t)
        if not low.endswith("s"):
            plural = f"{t}s"
            lookup[plural.lower()] = slug
            phrases.append(plural)

    sorted_phrases = sorted(set(phrases), key=len, reverse=True)
    escaped = [re.escape(p) for p in sorted_phrases]
    pattern = re.compile(r"\b(" + "|".join(escaped) + r")\b", re.IGNORECASE)
    _GLOSSARY_PATTERN_CACHE[cache_key] = (lookup, pattern)
    return lookup, pattern


def wrap_glossary_terms(
    text: str,
    terms: dict[str, Any] | list[str],
    seen_slugs: set[str] | None = None,
) -> str:
    """Wrap technical glossary terms in `:term:`matched <slug>``, avoiding existing RST markup."""
    if not text or not terms:
        return text

    compiled = _get_glossary_lookup_and_pattern(terms)
    if compiled is None:
        return text
    lookup, pattern = compiled

    local_seen = seen_slugs if seen_slugs is not None else set()

    def _replace_segment(seg: str) -> str:
        def _repl(match: re.Match) -> str:
            matched = match.group(0)
            slug = lookup.get(matched.lower())
            if not slug or slug in local_seen:
                return matched
            local_seen.add(slug)
            return f":term:`{matched} <{slug}>`"

        return pattern.sub(_repl, seg)

    return _apply_outside_rst_spans(text, _replace_segment)


_PERSON_ALIAS_MAP: dict[str, str] = {
    alias: slug
    for slug, info in PERSONS_REGISTRY.items()
    for alias in info.get("aliases", [])
}
_SORTED_PERSON_ALIASES = sorted(_PERSON_ALIAS_MAP.keys(), key=len, reverse=True)
_PERSON_PATTERN = re.compile(
    r"\b(" + "|".join(re.escape(a) for a in _SORTED_PERSON_ALIASES) + r")\b"
)
_CITE_PATTERNS = [
    (re.compile(r"\bTCCT\b"), "tcct"),
    (re.compile(r"\bHyacinthos(?:\s*#\d+)?\b"), "hyacinthos"),
    (re.compile(r"\b(?:ADGEOM|Anopolis)(?:\s*#\d+)?\b"), "adgeom"),
    (re.compile(r"\bForum Geometricorum\b"), "forum-geometricorum"),
]


def wrap_persons_and_citations(
    text: str,
    seen_persons: set[str] | None = None,
    seen_cites: set[str] | None = None,
) -> str:
    """Wrap contributor names in `:person:` and standard citations (TCCT, Hyacinthos, ADGEOM) in `:cite:`."""
    if not text:
        return text

    p_seen = seen_persons if seen_persons is not None else set()
    c_seen = seen_cites if seen_cites is not None else set()

    def _replace_persons(seg: str) -> str:
        def _repl(m: re.Match) -> str:
            name = m.group(0)
            slug = _PERSON_ALIAS_MAP.get(name)
            if not slug or slug in p_seen:
                return name
            p_seen.add(slug)
            return f":person:`{name} <{slug}>`"

        return _PERSON_PATTERN.sub(_repl, seg)

    text = _apply_outside_rst_spans(text, _replace_persons)

    def _replace_cites(seg: str) -> str:
        for pat, cslug in _CITE_PATTERNS:
            def _crepl(m: re.Match, s: str = cslug) -> str:
                disp = m.group(0)
                c_seen.add(s)
                return f":cite:`{disp} <{s}>`"

            seg = pat.sub(_crepl, seg)
        return seg

    return _apply_outside_rst_spans(text, _replace_cites)

