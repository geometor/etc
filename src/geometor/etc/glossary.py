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
    )
    return html.unescape(text)


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

    # Convert <sup>...</sup> and <sub>...</sub> into RST :sup: and :sub:
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

    for child in soup.children:
        if isinstance(child, NavigableString):
            raw_s = str(child).strip()
            if raw_s:
                conv = _wrap_x_refs_simple(convert_inline_html_to_rst(raw_s))
                if conv:
                    blocks.append(conv)
                    plain_sentences.append(" ".join(raw_s.split()))
            continue

        if not isinstance(child, Tag):
            continue

        tag_name = child.name.lower()
        if tag_name == "h2":
            continue

        if tag_name == "p":
            cls = child.get("class") or []
            from .parser import _strip_software_and_nav_refs

            inner_html = child.decode_contents()
            # Split on <br> if multi-line inside <p>
            br_lines = [
                _strip_software_and_nav_refs(
                    _wrap_x_refs_simple(convert_inline_html_to_rst(ln))
                )
                for ln in re.split(r"<br\s*/?>", inner_html, flags=re.IGNORECASE)
            ]
            br_lines = [ln for ln in br_lines if ln]
            if not br_lines:
                continue

            if "eqn" in cls:
                eqn_block = "\n".join(f"   {ln}" for ln in br_lines)
                blocks.append(eqn_block)
            else:
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
                li_rst = _wrap_x_refs_simple(
                    convert_inline_html_to_rst(li.decode_contents())
                )
                if li_rst:
                    items.append(f"* {li_rst}")
            if items:
                blocks.append("\n".join(items))

        elif tag_name == "blockquote":
            inner_html = child.decode_contents()
            br_lines = [
                _wrap_x_refs_simple(convert_inline_html_to_rst(ln))
                for ln in re.split(r"<br\s*/?>", inner_html, flags=re.IGNORECASE)
            ]
            br_lines = [ln for ln in br_lines if ln]
            if br_lines:
                blocks.append("\n".join(f"   | {ln}" for ln in br_lines))

        elif tag_name == "table":
            rows: list[str] = []
            for tr in child.find_all("tr"):
                cells = [
                    _wrap_x_refs_simple(
                        convert_inline_html_to_rst(td.decode_contents())
                    )
                    for td in tr.find_all(["td", "th"])
                ]
                cells = [c for c in cells if c and not re.match(r"^[\.\s]+$", c)]
                if cells:
                    rows.append("   | " + "   —   ".join(cells))
            if rows:
                blocks.append("\n".join(rows))

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
            terms[tri_name] = {
                "headword": tri_name,
                "slug": apparatus_slug(tri_name),
                "target_slug": info["target_slug"],
                "definition": info["definition"],
                "rst": f"{_wrap_x_refs_simple(info['definition'])} (See :term:`{info['target_slug'].replace('-', ' ')} <{info['target_slug']}>`.)",
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
        role_rst = info["role"].replace("|", r"\|")
        role_rst = _wrap_x_refs_simple(role_rst, valid_centers=valid_centers)
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

