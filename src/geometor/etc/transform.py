"""Transform parsed ETC center and preamble structures into semantic ReStructuredText."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .glossary import (
    _apply_outside_rst_spans,
    filter_center_refs,
    wrap_geom_refs,
    wrap_glossary_terms,
    wrap_persons_and_citations,
)
from .parser import parse_preamble


def format_rst_header(title: str, char: str = "=") -> str:
    """Create an RST section header with matching underline length."""
    line = char * max(4, len(title))
    return f"{title}\n{line}\n\n"


def wrap_refs(
    text: str, valid_centers: set[int] | None = None
) -> str:
    """Wrap X(n), X[n], and X_n references in `:ref:`X_n <X_n>`` outside existing RST roles."""
    if not text:
        return ""

    pattern = re.compile(r"(?<![a-z])X(?:[\(\[](\d+)[\)\]]|_(\d+))")

    def _repl_seg(seg: str) -> str:
        out: list[str] = []
        last_idx = 0
        for m in pattern.finditer(seg):
            num_str = m.group(1) or m.group(2)
            num = int(num_str)
            start, end = m.start(), m.end()
            out.append(seg[last_idx:start])
            if valid_centers is not None and num not in valid_centers:
                out.append(f"X_{num_str}")
            else:
                prev_ch = seg[start - 1] if start > 0 else " "
                next_ch = seg[end] if end < len(seg) else " "
                need_pre = (prev_ch not in " \t\n-:/'\"<([{") and not (
                    last_idx == start and out and out[-1].endswith(r"\ ")
                )
                need_post = (
                    next_ch not in " \t\n-.,:;!?/'\")>]}"
                ) and not seg[end:].startswith(r"\ ")
                prefix = r"\ " if need_pre else ""
                suffix = r"\ " if need_post else ""
                out.append(f"{prefix}:ref:`X_{num_str} <X_{num_str}>`{suffix}")
            last_idx = end
        out.append(seg[last_idx:])
        joined = "".join(out)
        return re.sub(r"(?<![a-z])X[\(\[]([ijkn])[\)\]]", r"X_\1", joined)

    return _apply_outside_rst_spans(text, _repl_seg)


def _wrap_relation_tuples(
    rel_text: str, valid_centers: set[int] | None = None
) -> str:
    """Wrap bare integer tuples after 'for these (i,j):' into clickable `:ref:` links."""
    colon_match = re.search(
        r"(for\s+these\s+[^:]+:\s*)(.+)$",
        rel_text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if not colon_match:
        return rel_text

    prefix = rel_text[: colon_match.end(1)]
    tail = colon_match.group(2)

    def _fmt_num(n_str: str) -> str:
        n_int = int(n_str)
        if valid_centers is None or n_int in valid_centers:
            return f":ref:`{n_str} <X_{n_str}>`"
        return n_str

    def _tuple_repl(m: re.Match) -> str:
        open_br, inner, close_br = m.group(1), m.group(2), m.group(3)
        nums = [n.strip() for n in inner.split(",") if n.strip().isdigit()]
        if not nums:
            return m.group(0)
        linked = ", ".join(_fmt_num(n) for n in nums)
        return f"{open_br}{linked}{close_br}"

    linked_tail = re.sub(
        r"([\(\{])\s*(\d+(?:\s*,\s*\d+)+)\s*([\)\}])",
        _tuple_repl,
        tail,
    )
    return f"{prefix}{linked_tail}"


def _enrich_text(
    text: str,
    glossary_terms: dict[str, Any] | list[str] | None,
    seen_terms: set[str],
    seen_persons: set[str],
    seen_cites: set[str],
    valid_centers: set[int] | None = None,
) -> str:
    """Apply X(n) reference linking, glossary `:term:` linking, `:person:`/`:cite:` linking, and `:g:` role wrapping."""
    text = wrap_refs(text, valid_centers=valid_centers)
    if glossary_terms:
        text = wrap_glossary_terms(text, glossary_terms, seen_slugs=seen_terms)
    text = wrap_persons_and_citations(
        text, seen_persons=seen_persons, seen_cites=seen_cites
    )
    text = wrap_geom_refs(text)
    res = filter_center_refs(text, valid_centers)
    res = re.sub(
        r"(:(?:ref|term|person|cite|g|math):`[^`]+`)(?=[(\[{<A-Za-z0-9_])",
        r"\1\ ",
        res,
    )
    res = re.sub(r"::(\s*)$", r":\1", res, flags=re.MULTILINE)
    return res



_NON_DEFINING_NOTE_RE = re.compile(
    r"^\s*(?:"
    r"as\s+a\s+point\s+on\s+the\s+euler\s+line|"
    r"barycentrics\s+|trilinears\s+|tripolars\s+|"
    r"\*|"
    r"see\s+|"
    r"the\s+name\s+of\s+this\s+point|"
    r"this\s+point\s+is\s+mentioned|"
    r"for\s+an\s+artistic|"
    r"a\s+construction\s+of\s+x\(\d+\)|"
    r"x\(\d+\)\s+lies\s+(?:on\s+)?the\b|"
    r"if,?\s+however\b|"
    r"however\s*,|"
    r"the\s+above\s+construction|"
    r"similarly\s*,|"
    r"more\s+generally\s*,|"
    r"although\s+|"
    r"constructions\s+received\s+from"
    r")",
    re.IGNORECASE,
)


def _is_non_defining_note(s: str) -> bool:
    s_str = s.strip()
    if not s_str or len(s_str) <= 10:
        return True
    if _NON_DEFINING_NOTE_RE.match(s_str):
        return True
    if "../bstud/" in s_str.lower():
        return True
    # Pure bibliographic / citation-only short note ending in a year
    return bool(
        len(s_str) < 95
        and re.search(r"\b(?:19|20)\d{2}\.?\s*$", s_str)
        and not re.search(
            r"\b(?:let|is\s+the|concur|perspector|intersection|center|triangle|circle|conjugate|midpoint|reflection)\b",
            s_str,
            re.IGNORECASE,
        )
    )


_PROPER_TITLE_NAMES: dict[str, str] = {
    "feuerbach": "Feuerbach",
    "gergonne": "Gergonne",
    "nagel": "Nagel",
    "spieker": "Spieker",
    "euler": "Euler",
    "fermat": "Fermat",
    "apollonius": "Apollonius",
    "napoleon": "Napoleon",
    "mittenpunkt": "Mittenpunkt",
    "lemoine": "Lemoine",
    "brocard": "Brocard",
    "steiner": "Steiner",
    "tarry": "Tarry",
    "clawson": "Clawson",
    "longchamps": "Longchamps",
    "schiffler": "Schiffler",
    "exeter": "Exeter",
    "bevan": "Bevan",
    "kosnita": "Kosnita",
    "monge": "Monge",
}


def _format_title_as_prose(title: str) -> str:
    """Convert an ALL-CAPS ETC title into readable prose while preserving X_n, ABC, and proper names."""
    s = title.strip().lower()
    s = re.sub(r"\bx(?:_|\()(\d+)\)?", lambda m: f"X_{m.group(1)}", s)
    s = re.sub(r"\babc\b", "ABC", s)
    for low_k, cap_v in _PROPER_TITLE_NAMES.items():
        s = re.sub(rf"\b{low_k}\b", cap_v, s)
    return s


def _extract_primary_enunciation(
    notes: list[str],
    relations: list[str],
    num: int | None = None,
    title: str = "",
) -> tuple[str, list[str]]:
    """Extract a consistent primary defining statement for ``.. enunciation::`` and return remaining notes."""
    remaining = list(notes)
    title_clean = (title or "").strip()
    title_low = title_clean.lower()

    # Check if the title itself is an explicit operator/triangle definition (e.g. "CENTROID OF ORTHIC TRIANGLE",
    # "INSIMILICENTER(CIRCUMCIRCLE, INCIRCLE)", "X(6)-BETH CONJUGATE OF X(4)")
    title_is_operator = bool(
        re.search(
            r"\b(?:centroid|orthocenter|incenter|circumcenter|symmedian\s+point|nine-point\s+center|"
            r"reflection|midpoint|complement|anticomplement|cevapoint|crosspoint|isogonal\s+conjugate|"
            r"isotomic\s+conjugate|insimilicenter|exsimilicenter|homothetic\s+center|perspector|"
            r"inverse|antipode|harmonic\s+conjugate)\s+(?:of|in)\b|"
            r"\b(?:insimilicenter|exsimilicenter|homothetic\s+center)\s*\(|"
            r"\bx\(\d+\)-[a-z]+\s+conjugate\s+of\b",
            title_low,
        )
    )

    # Extract distinctive proper-name words from title (e.g. "spieker", "longchamps", "schiffler", "kosnita")
    generic_words = {
        "point", "center", "first", "second", "third", "1st", "2nd", "3rd", "4th",
        "triangle", "circle", "line", "the", "and", "of", "in", "on", "to", "for",
        "with", "isogonal", "isotomic", "conjugate", "complement", "anticomplement",
        "midpoint", "reflection", "perspector", "centroid", "orthocenter", "incenter",
        "circumcenter", "symmedian", "euler", "homothetic", "insimilicenter", "exsimilicenter",
        "inverse", "antipode", "crosspoint", "cevapoint", "circumcircle", "incircle",
        "excircle", "nine", "harmonic",
    }
    eponym_words = [
        w for w in re.findall(r"[a-z]{4,}", title_low)
        if w not in generic_words
    ]

    # Score candidate notes among the first 7 notes
    best_idx: int | None = None
    best_score = -999
    for idx, note in enumerate(remaining[:7]):
        s = note.strip()
        if _is_non_defining_note(s):
            continue
        low = s.lower()
        score = 0
        # Prefer notes without multi-paragraph breaks, or whose paragraphs are self-contained
        if "\n" not in s:
            score += 20
        else:
            paras = [p.strip() for p in s.split("\n\n") if p.strip()]
            first_p = paras[0] if paras else ""
            if first_p.rstrip().lower().endswith(("let", "where", "as", "follows", ":", ";", ",", "=")):
                score -= 15
            elif len(paras) > 1 and paras[1].lstrip().startswith("*"):
                score -= 10
        # Penalize dated contributor notes "(Author, Month DD, YYYY)" or "MM/DD/YY"
        has_date = bool(re.search(r"\b(?:199\d|20[0-2]\d)\b|\b\d{1,2}/\d{1,2}/\d{2,4}\b", s))
        if has_date:
            score -= 60
        else:
            score += 25
        # Penalize secondary multi-step contributor constructions (A″ / A'' / hexyl / half-altitude)
        if re.search(r"[A-Z][″\"]|[A-Z]''|\b(?:hexyl|half-altitude|ara|johnson)\s+triangle\b", s, re.IGNORECASE):
            score -= 55
        # Penalize secondary one-line "{X(i),X(j)}-harmonic conjugate of X(k)" notes when title is not a harmonic conjugate
        if "harmonic conjugate" not in title_low and re.match(
            r"^x\(\d+\)\s+is\s+the\s+\{x\(\d+\)\s*,\s*x\(\d+\)\}-harmonic\s+conjugate\s+of\s+x\(\d+\)\.?$",
            low,
        ):
            score -= 50
        # Strong bonus if note mentions the center's proper eponym (e.g. "Spieker", "De Longchamps", "Schiffler", "Kosnita")
        if eponym_words and any(ew in low for ew in eponym_words):
            score += 45
        # If title is an explicit operator (e.g. "CENTROID OF ORTHIC TRIANGLE"), penalize a note that starts with
        # "Let A'B'C' be the <different triangle>" unrelated to the title
        if title_is_operator and low.startswith("let "):
            title_tris = re.findall(r"\b([a-z\-]+)\s+triangle\b", title_low)
            note_tris = re.findall(r"\b([a-z\-]+)\s+triangle\b", low[:120])
            if title_tris and note_tris and title_tris[0] != note_tris[0]:
                score -= 60
            elif not title_tris and note_tris:
                score -= 50
        # Slight preference for earlier position
        score -= idx * 4
        if score > best_score:
            best_score = score
            best_idx = idx

    # If no canonical un-dated note scored >= 0, prefer the explicit operator title or canonical low-numbered relation
    if best_score < 0:
        if title_is_operator and num is not None:
            return f"X_{num} is the {_format_title_as_prose(title_clean)}.", remaining
        max_k_allowed = max((num or 1) + 15, 50)
        for rel in relations:
            r_s = rel.strip()
            r_low = r_s.lower()
            if not r_s or "for these" in r_low or "\n" in r_s:
                continue
            if re.search(r"\b(?:199\d|20[0-2]\d)\b|\b\d{1,2}/\d{1,2}/\d{2,4}\b", r_s):
                continue
            if "harmonic conjugate" in r_low and "harmonic conjugate" not in title_low:
                continue
            ref_nums = [
                int(m_n)
                for m_n in re.findall(r"X(?:_|\()(\d+)\)?|\{\s*(\d+)\s*,\s*(\d+)\s*\}", r_s)
                for m_n in (m_n if isinstance(m_n, tuple) else (m_n,))
                if m_n
            ]
            if any(k_n > max_k_allowed for k_n in ref_nums):
                continue
            if (
                len(relations) > 1
                and re.search(r"=\s*(?:isogonal|isotomic)\s+conjugate\s+of\b", r_low)
                and "conjugate" not in title_low
            ):
                continue
            return r_s, remaining

    if best_idx is not None:
        chosen = remaining[best_idx].strip()
        if "\n" not in chosen:
            del remaining[best_idx]
            chosen = re.sub(
                r"\s*For\s+details\s+and\s+generalization,\s+see\s*$",
                "",
                chosen,
                flags=re.IGNORECASE,
            ).strip()
            return chosen, remaining
        paras = [p.strip() for p in chosen.split("\n\n") if p.strip()]
        first_p = paras[0]
        # Only split off `first_p` if it is a complete sentence and doesn't introduce bullet items
        can_split = (
            len(paras) > 1
            and "\n" not in first_p
            and not first_p.rstrip().lower().endswith(("let", "where", "as", "follows", ":", ";", ",", "="))
            and not paras[1].lstrip().startswith("*")
        )
        if can_split:
            remaining[best_idx] = "\n\n".join(paras[1:])
            first_p = re.sub(
                r"\s*For\s+details\s+and\s+generalization,\s+see\s*$",
                "",
                first_p,
                flags=re.IGNORECASE,
            ).strip()
            return first_p, remaining
        del remaining[best_idx]
        return chosen, remaining

    for rel in relations:
        r_s = rel.strip()
        if r_s and "for these" not in r_s.lower() and "\n" not in r_s:
            return r_s, remaining

    if title_is_operator and num is not None:
        return f"X_{num} is the {_format_title_as_prose(title_clean)}.", remaining

    return "", remaining


_POLYGON_TERM_SLUGS: dict[str, tuple[str, str]] = {
    "< M_a M_b M_c >": ("Medial Triangle", "medial-triangle"),
    "< H_a H_b H_c >": ("Orthic Triangle", "orthic-triangle"),
    "< T_a T_b T_c >": ("Intouch (Contact) Triangle", "intouch-triangle"),
    "< N_a N_b N_c >": ("Extouch Triangle", "extouch-triangle"),
    "< I_a I_b I_c >": ("Incentral Triangle", "incentral-triangle"),
    "< J_a J_b J_c >": ("Excentral Triangle", "excentral-triangle"),
    "< K_a K_b K_c >": ("Anticomplementary Triangle", "anticomplementary-triangle"),
    "< Tan_a Tan_b Tan_c >": ("Tangential Triangle", "tangential-triangle"),
    "< Sym_a Sym_b Sym_c >": ("Symmedial Triangle", "symmedial-triangle"),
    "< F_a F_b F_c >": ("Feuerbach Triangle", "feuerbach-triangle"),
    "< Pd_a Pd_b Pd_c >": ("Equilateral Pedal Triangle", "pedal-triangle"),
    "< Eu_a Eu_b Eu_c >": ("Euler (Feuerbach) Triangle", "euler-triangle"),
    "< Cm_a Cm_b Cm_c >": ("Circummedial Triangle", "circummedial-triangle"),
    "< H'_a H'_b H'_c >": ("Orthic-of-Orthic Triangle", "orthic-triangle"),
    "< Nap_a Nap_b Nap_c >": ("Outer Napoleon Triangle", "outer-napoleon-triangle"),
    "< Nap'_a Nap'_b Nap'_c >": ("Inner Napoleon Triangle", "inner-napoleon-triangle"),
    "< P_a P_b P_c >": ("Cevian Triangle", "cevian-triangle"),
}

_CIRCLE_DISPLAY_NAMES: dict[str, str] = {
    "circumcircle": "Circumcircle",
    "incircle": "Incircle",
    "nine_point_circle": "Nine-Point Circle",
    "spieker_circle": "Spieker Circle",
    "bevan_circle": "Bevan Circle",
    "orthocentroidal_circle": "Orthocentroidal Circle",
    "A-Apollonian circle": "A-Apollonian Circle",
    "B-Apollonian circle": "B-Apollonian Circle",
    "C-Apollonian circle": "C-Apollonian Circle",
}

_CONCURRENCE_KIND_LABELS: dict[str, str] = {
    "Cevian": " (Cevians)",
    "Median": " (Medians)",
    "Altitude": " (Altitudes)",
    "Angle": " (Angle Bisectors)",
    "Internal": " (Angle Bisectors)",
    "Medial": " (Medial Angle Bisectors)",
    "Symmedian": " (Symmedians)",
    "A-Symmedian": " (Symmedians)",
    "Mittenpunkt": " (Excenter–Midpoint Symmedians)",
    "Feuerbach": " (Feuerbach Cevians)",
    "Gergonne": " (Gergonne Cevians)",
    "Nagel": " (Nagel Splitters)",
    "Outer": " (Outer Cevians)",
    "Inner": " (Inner Cevians)",
    "A-Cevian": " (Cevians)",
    "Perpendicular": " (Perpendicular Bisectors)",
    "Perspectivity": " (Perspectivity Lines)",
}


def _format_constructed_elements_rst(
    model: Any,
    data: dict[str, Any],
    enun_raw: str,
    valid_centers: set[int] | None = None,
) -> list[str]:
    """Build a 'Constructed Elements' summary block documenting all primary elements shown in the SVG figure."""
    if model is None:
        return []
    from .render import (
        _CONSTRUCTION_LINE_INFO,
        _KNOWN_CIRCLE_INFO,
        _KNOWN_POLYGON_INFO,
        _load_center_names,
        model_to_elements_list,
    )

    elements = model_to_elements_list(model)
    if not elements:
        return []

    target_key = data.get("key", "")
    center_names = _load_center_names()
    bullets: list[str] = []

    # 1. Derived Triangles (Polygons other than < A B C >)
    covered_guide_pts: set[str] = {
        "R_a",
        "R_b",
        "P_mc",
        "Ap_a",
        "Ap_b",
        "Ap_c",
        "T_sp",
        "S_c",
    }
    outer_equil_polys = [
        el
        for el in elements
        if el["type"] == "polygon"
        and el["ID"] in {"< B C A' >", "< C A B' >", "< A B C' >"}
    ]
    if len(outer_equil_polys) == 3:
        covered_guide_pts.update({"A'", "B'", "C'"})
        bullets.append(
            "* **Outward Equilateral Side Triangles:** "
            ":g:`△BCA' << B C A' >>`, :g:`△CAB' << C A B' >>`, :g:`△ABC' << A B C' >>` "
            "erected outward on sidelines with apexes :g:`A' <A'>`, :g:`B' <B'>`, :g:`C' <C'>`"
        )

    inner_equil_polys = [
        el
        for el in elements
        if el["type"] == "polygon"
        and el["ID"] in {"< B C A'' >", "< C A B'' >", "< A B C'' >"}
    ]
    if len(inner_equil_polys) == 3:
        covered_guide_pts.update({"A''", "B''", "C''"})
        bullets.append(
            "* **Inward Equilateral Side Triangles:** "
            ":g:`△BCA'' << B C A'' >>`, :g:`△CAB'' << C A B'' >>`, :g:`△ABC'' << A B C'' >>` "
            "erected inward on sidelines with apexes :g:`A'' <A''>`, :g:`B'' <B''>`, :g:`C'' <C''>`"
        )

    skip_polys = {
        "< A B C >",
        "< B C A' >",
        "< C A B' >",
        "< A B C' >",
        "< B C A'' >",
        "< C A B'' >",
        "< A B C'' >",
    }
    for el in elements:
        if el["type"] != "polygon" or "incident" in el["classes"]:
            continue
        pid = el["ID"]
        if pid in skip_polys:
            continue
        v_ids = el.get("points") or []
        covered_guide_pts.update(v_ids)
        inner_id = pid[2:-2].strip()
        p_info = _KNOWN_POLYGON_INFO.get(pid)
        desc = p_info[1] if p_info else "Constructed derived triangle"

        if pid in _POLYGON_TERM_SLUGS:
            t_lbl, t_slug = _POLYGON_TERM_SLUGS[pid]
            title_part = f":term:`{t_lbl} <{t_slug}>` :g:`△{''.join(v_ids)} << {inner_id} >>`"
        else:
            p_title = p_info[0] if p_info else f"Triangle {pid}"
            title_part = f"**{p_title}** :g:`{pid} << {inner_id} >>`"

        v_chips = [f":g:`{vid} <{vid}>`" for vid in v_ids]
        verts_part = f" — vertices {', '.join(v_chips)}" if v_chips else ""
        bullets.append(f"* **Derived Triangle:** {title_part}{verts_part} ({desc})")

    # 2. Auxiliary Guide Points not already part of a drawn polygon
    rem_guides = [
        el["ID"]
        for el in elements
        if el["type"] == "point"
        and el["guide"]
        and "incident" not in el["classes"]
        and el["ID"] not in covered_guide_pts
    ]
    if rem_guides:
        groups: list[tuple[str, list[str], str]] = [
            ("M_", ["M_a", "M_b", "M_c"], "Side midpoints of :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`"),
            ("H_", ["H_a", "H_b", "H_c"], "Altitude feet on :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`"),
            ("Eu_", ["Eu_a", "Eu_b", "Eu_c"], "Euler midpoints halfway between :g:`A <A>`, :g:`B <B>`, :g:`C <C>` and the orthocenter"),
            ("I_", ["I_a", "I_b", "I_c"], "Internal angle bisector feet on :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`"),
            ("T_", ["T_a", "T_b", "T_c"], "Incircle touchpoints (right-spread pedal feet) on :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`"),
            ("Sym_", ["Sym_a", "Sym_b", "Sym_c"], "Symmedian feet on :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`"),
            ("P_", ["P_a", "P_b", "P_c"], "Sideline cevian traces on :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`"),
        ]
        used_g: set[str] = set()
        for _, g_ids, g_desc in groups:
            present = [gid for gid in g_ids if gid in rem_guides]
            if len(present) == 3:
                used_g.update(present)
                chips = [f":g:`{gid} <{gid}>`" for gid in present]
                bullets.append(f"* **Auxiliary Points:** {', '.join(chips)} — {g_desc}")
        other_g = [gid for gid in rem_guides if gid not in used_g]
        if other_g:
            chips = [f":g:`{gid} <{gid}>`" for gid in other_g]
            bullets.append(f"* **Auxiliary Points:** {', '.join(chips)}")

    # 3. Circles
    apollonian_cids = [
        el["ID"]
        for el in elements
        if el["type"] == "circle"
        and el["ID"] in {"A-Apollonian circle", "B-Apollonian circle", "C-Apollonian circle"}
    ]
    if len(apollonian_cids) == 3:
        bullets.append(
            "* **Apollonian Circles:** "
            ":g:`A-Apollonian <A-Apollonian circle>`, "
            ":g:`B-Apollonian <B-Apollonian circle>`, "
            ":g:`C-Apollonian <C-Apollonian circle>` "
            "— coaxial circles through :g:`A <A>`, :g:`B <B>`, :g:`C <C>` orthogonal to :g:`circumcircle <circumcircle>`"
        )

    for el in elements:
        if el["type"] != "circle" or el["guide"] or "incident" in el["classes"]:
            continue
        cid = el["ID"]
        if cid in {"A-Apollonian circle", "B-Apollonian circle", "C-Apollonian circle"} and len(apollonian_cids) == 3:
            continue
        c_info = _KNOWN_CIRCLE_INFO.get(cid)
        c_desc = c_info[1] if c_info else f"Centered at {el.get('center', '')}"
        if cid in _CIRCLE_DISPLAY_NAMES:
            c_lbl = _CIRCLE_DISPLAY_NAMES[cid]
            c_head = f"**{c_lbl}** (:g:`{cid} <{cid}>`)"
        else:
            c_title = c_info[0] if c_info else cid
            c_head = f":g:`{c_title} <{cid}>`"
        bullets.append(f"* **Circle:** {c_head} — {c_desc}")

    # 4. Concurrence Lines & Central Lines
    concur_lines: list[str] = []
    central_lines: list[str] = []
    for el in elements:
        if el["type"] != "line" or el["guide"] or "incident" in el["classes"]:
            continue
        lid = el["ID"]
        if lid in {"[ A B ]", "[ B C ]", "[ C A ]"}:
            continue
        m_cl = re.match(r"^\{\s*(\d+)\s*,\s*(\d+)\s*\}$", lid)
        if m_cl:
            i_n, j_n = int(m_cl.group(1)), int(m_cl.group(2))
            is_euler = {i_n, j_n} <= {2, 3, 4, 5, 20, 30}
            e_tag = " (Euler line)" if is_euler else ""
            central_lines.append(f":g:`{{{i_n}, {j_n}}} <{lid}>`{e_tag}")
        else:
            inner_l = lid[2:-2].strip() if lid.startswith("[") and lid.endswith("]") else lid
            pts_l = inner_l.split()
            disp_l = f"{pts_l[0]}–{pts_l[1]}" if len(pts_l) == 2 else lid
            concur_lines.append(f":g:`{disp_l} <{lid}>`")

    if concur_lines:
        l_first = next(
            (
                el["ID"]
                for el in elements
                if el["type"] == "line"
                and el["ID"] not in {"[ A B ]", "[ B C ]", "[ C A ]"}
                and not el["ID"].startswith("{")
            ),
            "",
        )
        l_desc = _CONSTRUCTION_LINE_INFO.get(l_first, ("", ""))[0]
        first_w = l_desc.split()[0] if l_desc else ""
        kind_prefix = _CONCURRENCE_KIND_LABELS.get(first_w, "")
        bullets.append(
            f"* **Concurrence Lines{kind_prefix}:** {', '.join(concur_lines)} concurring at :g:`{target_key} <{target_key}>`"
        )
    if central_lines:
        bullets.append(f"* **Central Lines:** {', '.join(central_lines)}")

    # 5. Related Centers Shown in Construction
    rel_centers: list[str] = []
    for el in elements:
        if el["type"] != "point" or el["guide"] or "incident" in el["classes"]:
            continue
        pid = el["ID"]
        if pid in {"A", "B", "C", target_key}:
            continue
        m_x = re.match(r"^X(?:_|\()(\d+)\)?$", pid)
        if m_x:
            c_num = int(m_x.group(1))
            c_title = center_names.get(str(c_num), "")
            if len(c_title) > 36 and "(" in c_title:
                c_title = c_title.split("(")[0].strip()
            can_ref = valid_centers is None or c_num in valid_centers
            if c_title and can_ref:
                title_suffix = f" (:ref:`{c_title} <{pid}>`)"
            elif c_title:
                title_suffix = f" ({c_title})"
            elif can_ref:
                title_suffix = f" (:ref:`page <{pid}>`)"
            else:
                title_suffix = ""
            rel_centers.append(f":g:`{pid} <{pid}>`{title_suffix}")

    if rel_centers:
        bullets.append(f"* **Related Centers:** {', '.join(rel_centers)}")

    if not bullets:
        return []

    out = [
        ".. admonition:: Constructed Elements",
        "   :class: note",
        "",
    ]
    for b in bullets:
        out.append(f"   {b}")
    out.append("")
    return out


_COLLECTION_1_TOPIC_GUIDES: dict[int, str] = {
    1: ":doc:`T_1: Isogonal Conjugate <../../../topics/isogonal-conjugate/index>` • :doc:`T_2: Isotomic Conjugate <../../../topics/isotomic-conjugate/index>` • :doc:`T_3: Complement & Anticomplement <../../../topics/complement-and-anticomplement/index>` • :doc:`T_4: Harmonic Conjugate & Cross-Ratio <../../../topics/harmonic-conjugate/index>` • :doc:`T_5: Circle Inversion <../../../topics/circle-inversion/index>` • :doc:`T_7: The Nagel Line <../../../topics/nagel-line/index>` • :doc:`T_9: The Feuerbach Line <../../../topics/feuerbach-line/index>` • :doc:`T_10: The OI Line (Incenter–Circumcenter Axis) <../../../topics/oi-line/index>` • :doc:`T_11: The Soddy Line <../../../topics/soddy-line/index>` • :doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_14: The Incircle & Excircles <../../../topics/incircle-and-excircles/index>` • :doc:`T_16: The Nine-Point (Feuerbach) Circle <../../../topics/nine-point-circle/index>` • :doc:`T_17: The Spieker Circle <../../../topics/spieker-circle/index>` • :doc:`T_20: Medial & Anticomplementary Triangles <../../../topics/medial-and-anticomplementary-triangles/index>` • :doc:`T_22: Intouch (Contact) & Extouch Triangles <../../../topics/intouch-and-extouch-triangles/index>` • :doc:`T_23: Incentral & Excentral Triangles <../../../topics/incentral-and-excentral-triangles/index>`",
    2: ":doc:`T_1: Isogonal Conjugate <../../../topics/isogonal-conjugate/index>` • :doc:`T_2: Isotomic Conjugate <../../../topics/isotomic-conjugate/index>` • :doc:`T_3: Complement & Anticomplement <../../../topics/complement-and-anticomplement/index>` • :doc:`T_4: Harmonic Conjugate & Cross-Ratio <../../../topics/harmonic-conjugate/index>` • :doc:`T_6: The Euler Line <../../../topics/euler-line/index>` • :doc:`T_7: The Nagel Line <../../../topics/nagel-line/index>` • :doc:`T_11: The Soddy Line <../../../topics/soddy-line/index>` • :doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_15: The Circumcircle <../../../topics/circumcircle/index>` • :doc:`T_16: The Nine-Point (Feuerbach) Circle <../../../topics/nine-point-circle/index>` • :doc:`T_17: The Spieker Circle <../../../topics/spieker-circle/index>` • :doc:`T_19: The Brocard & Orthocentroidal Circles <../../../topics/brocard-and-orthocentroidal-circles/index>` • :doc:`T_20: Medial & Anticomplementary Triangles <../../../topics/medial-and-anticomplementary-triangles/index>` • :doc:`T_22: Intouch (Contact) & Extouch Triangles <../../../topics/intouch-and-extouch-triangles/index>` • :doc:`T_24: Equilateral, Isogonic & Napoleon Triangles <../../../topics/isogonic-and-napoleon-triangles/index>`",
    3: ":doc:`T_1: Isogonal Conjugate <../../../topics/isogonal-conjugate/index>` • :doc:`T_3: Complement & Anticomplement <../../../topics/complement-and-anticomplement/index>` • :doc:`T_4: Harmonic Conjugate & Cross-Ratio <../../../topics/harmonic-conjugate/index>` • :doc:`T_5: Circle Inversion <../../../topics/circle-inversion/index>` • :doc:`T_6: The Euler Line <../../../topics/euler-line/index>` • :doc:`T_8: The Brocard Axis <../../../topics/brocard-axis/index>` • :doc:`T_10: The OI Line (Incenter–Circumcenter Axis) <../../../topics/oi-line/index>` • :doc:`T_11: The Soddy Line <../../../topics/soddy-line/index>` • :doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_15: The Circumcircle <../../../topics/circumcircle/index>` • :doc:`T_16: The Nine-Point (Feuerbach) Circle <../../../topics/nine-point-circle/index>` • :doc:`T_18: The Apollonian Circles <../../../topics/apollonian-circles/index>` • :doc:`T_19: The Brocard & Orthocentroidal Circles <../../../topics/brocard-and-orthocentroidal-circles/index>` • :doc:`T_20: Medial & Anticomplementary Triangles <../../../topics/medial-and-anticomplementary-triangles/index>` • :doc:`T_21: Orthic & Tangential Triangles <../../../topics/orthic-and-tangential-triangles/index>` • :doc:`T_23: Incentral & Excentral Triangles <../../../topics/incentral-and-excentral-triangles/index>` • :doc:`T_24: Equilateral, Isogonic & Napoleon Triangles <../../../topics/isogonic-and-napoleon-triangles/index>`",
    4: ":doc:`T_1: Isogonal Conjugate <../../../topics/isogonal-conjugate/index>` • :doc:`T_2: Isotomic Conjugate <../../../topics/isotomic-conjugate/index>` • :doc:`T_3: Complement & Anticomplement <../../../topics/complement-and-anticomplement/index>` • :doc:`T_4: Harmonic Conjugate & Cross-Ratio <../../../topics/harmonic-conjugate/index>` • :doc:`T_5: Circle Inversion <../../../topics/circle-inversion/index>` • :doc:`T_6: The Euler Line <../../../topics/euler-line/index>` • :doc:`T_11: The Soddy Line <../../../topics/soddy-line/index>` • :doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_15: The Circumcircle <../../../topics/circumcircle/index>` • :doc:`T_16: The Nine-Point (Feuerbach) Circle <../../../topics/nine-point-circle/index>` • :doc:`T_17: The Spieker Circle <../../../topics/spieker-circle/index>` • :doc:`T_19: The Brocard & Orthocentroidal Circles <../../../topics/brocard-and-orthocentroidal-circles/index>` • :doc:`T_20: Medial & Anticomplementary Triangles <../../../topics/medial-and-anticomplementary-triangles/index>` • :doc:`T_21: Orthic & Tangential Triangles <../../../topics/orthic-and-tangential-triangles/index>` • :doc:`T_23: Incentral & Excentral Triangles <../../../topics/incentral-and-excentral-triangles/index>` • :doc:`T_24: Equilateral, Isogonic & Napoleon Triangles <../../../topics/isogonic-and-napoleon-triangles/index>`",
    5: ":doc:`T_3: Complement & Anticomplement <../../../topics/complement-and-anticomplement/index>` • :doc:`T_4: Harmonic Conjugate & Cross-Ratio <../../../topics/harmonic-conjugate/index>` • :doc:`T_6: The Euler Line <../../../topics/euler-line/index>` • :doc:`T_9: The Feuerbach Line <../../../topics/feuerbach-line/index>` • :doc:`T_15: The Circumcircle <../../../topics/circumcircle/index>` • :doc:`T_16: The Nine-Point (Feuerbach) Circle <../../../topics/nine-point-circle/index>` • :doc:`T_19: The Brocard & Orthocentroidal Circles <../../../topics/brocard-and-orthocentroidal-circles/index>` • :doc:`T_20: Medial & Anticomplementary Triangles <../../../topics/medial-and-anticomplementary-triangles/index>` • :doc:`T_21: Orthic & Tangential Triangles <../../../topics/orthic-and-tangential-triangles/index>`",
    6: ":doc:`T_1: Isogonal Conjugate <../../../topics/isogonal-conjugate/index>` • :doc:`T_5: Circle Inversion <../../../topics/circle-inversion/index>` • :doc:`T_8: The Brocard Axis <../../../topics/brocard-axis/index>` • :doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_15: The Circumcircle <../../../topics/circumcircle/index>` • :doc:`T_18: The Apollonian Circles <../../../topics/apollonian-circles/index>` • :doc:`T_19: The Brocard & Orthocentroidal Circles <../../../topics/brocard-and-orthocentroidal-circles/index>` • :doc:`T_21: Orthic & Tangential Triangles <../../../topics/orthic-and-tangential-triangles/index>` • :doc:`T_23: Incentral & Excentral Triangles <../../../topics/incentral-and-excentral-triangles/index>`",
    7: ":doc:`T_2: Isotomic Conjugate <../../../topics/isotomic-conjugate/index>` • :doc:`T_11: The Soddy Line <../../../topics/soddy-line/index>` • :doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_14: The Incircle & Excircles <../../../topics/incircle-and-excircles/index>` • :doc:`T_22: Intouch (Contact) & Extouch Triangles <../../../topics/intouch-and-extouch-triangles/index>`",
    8: ":doc:`T_2: Isotomic Conjugate <../../../topics/isotomic-conjugate/index>` • :doc:`T_3: Complement & Anticomplement <../../../topics/complement-and-anticomplement/index>` • :doc:`T_7: The Nagel Line <../../../topics/nagel-line/index>` • :doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_14: The Incircle & Excircles <../../../topics/incircle-and-excircles/index>` • :doc:`T_17: The Spieker Circle <../../../topics/spieker-circle/index>` • :doc:`T_20: Medial & Anticomplementary Triangles <../../../topics/medial-and-anticomplementary-triangles/index>` • :doc:`T_22: Intouch (Contact) & Extouch Triangles <../../../topics/intouch-and-extouch-triangles/index>`",
    9: ":doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_14: The Incircle & Excircles <../../../topics/incircle-and-excircles/index>` • :doc:`T_17: The Spieker Circle <../../../topics/spieker-circle/index>` • :doc:`T_22: Intouch (Contact) & Extouch Triangles <../../../topics/intouch-and-extouch-triangles/index>` • :doc:`T_23: Incentral & Excentral Triangles <../../../topics/incentral-and-excentral-triangles/index>`",
    10: ":doc:`T_3: Complement & Anticomplement <../../../topics/complement-and-anticomplement/index>` • :doc:`T_7: The Nagel Line <../../../topics/nagel-line/index>` • :doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_17: The Spieker Circle <../../../topics/spieker-circle/index>` • :doc:`T_20: Medial & Anticomplementary Triangles <../../../topics/medial-and-anticomplementary-triangles/index>`",
    11: ":doc:`T_4: Harmonic Conjugate & Cross-Ratio <../../../topics/harmonic-conjugate/index>` • :doc:`T_9: The Feuerbach Line <../../../topics/feuerbach-line/index>` • :doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_14: The Incircle & Excircles <../../../topics/incircle-and-excircles/index>` • :doc:`T_16: The Nine-Point (Feuerbach) Circle <../../../topics/nine-point-circle/index>` • :doc:`T_22: Intouch (Contact) & Extouch Triangles <../../../topics/intouch-and-extouch-triangles/index>`",
    12: ":doc:`T_4: Harmonic Conjugate & Cross-Ratio <../../../topics/harmonic-conjugate/index>` • :doc:`T_9: The Feuerbach Line <../../../topics/feuerbach-line/index>` • :doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_14: The Incircle & Excircles <../../../topics/incircle-and-excircles/index>` • :doc:`T_16: The Nine-Point (Feuerbach) Circle <../../../topics/nine-point-circle/index>`",
    13: ":doc:`T_1: Isogonal Conjugate <../../../topics/isogonal-conjugate/index>` • :doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_18: The Apollonian Circles <../../../topics/apollonian-circles/index>` • :doc:`T_24: Equilateral, Isogonic & Napoleon Triangles <../../../topics/isogonic-and-napoleon-triangles/index>`",
    14: ":doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_18: The Apollonian Circles <../../../topics/apollonian-circles/index>` • :doc:`T_24: Equilateral, Isogonic & Napoleon Triangles <../../../topics/isogonic-and-napoleon-triangles/index>`",
    15: ":doc:`T_1: Isogonal Conjugate <../../../topics/isogonal-conjugate/index>` • :doc:`T_5: Circle Inversion <../../../topics/circle-inversion/index>` • :doc:`T_8: The Brocard Axis <../../../topics/brocard-axis/index>` • :doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_15: The Circumcircle <../../../topics/circumcircle/index>` • :doc:`T_18: The Apollonian Circles <../../../topics/apollonian-circles/index>` • :doc:`T_24: Equilateral, Isogonic & Napoleon Triangles <../../../topics/isogonic-and-napoleon-triangles/index>`",
    16: ":doc:`T_5: Circle Inversion <../../../topics/circle-inversion/index>` • :doc:`T_8: The Brocard Axis <../../../topics/brocard-axis/index>` • :doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_15: The Circumcircle <../../../topics/circumcircle/index>` • :doc:`T_18: The Apollonian Circles <../../../topics/apollonian-circles/index>` • :doc:`T_24: Equilateral, Isogonic & Napoleon Triangles <../../../topics/isogonic-and-napoleon-triangles/index>`",
    17: ":doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_24: Equilateral, Isogonic & Napoleon Triangles <../../../topics/isogonic-and-napoleon-triangles/index>`",
    18: ":doc:`T_13: The Isogonic & Napoleon Central Lines <../../../topics/isogonic-and-napoleon-lines/index>` • :doc:`T_24: Equilateral, Isogonic & Napoleon Triangles <../../../topics/isogonic-and-napoleon-triangles/index>`",
    19: ":doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • :doc:`T_19: The Brocard & Orthocentroidal Circles <../../../topics/brocard-and-orthocentroidal-circles/index>` • :doc:`T_21: Orthic & Tangential Triangles <../../../topics/orthic-and-tangential-triangles/index>`",
}


def extract_svg_element_refs(svg_path: Path) -> set[str]:
    """Return all ``data-ref`` and ``.etc-elements-meta`` catalog keys present in ``svg_path``."""
    import json
    import xml.etree.ElementTree as ET

    if not svg_path.is_file():
        return set()
    root = ET.fromstring(svg_path.read_text(encoding="utf-8"))
    refs = {el.attrib["data-ref"] for el in root.iter() if "data-ref" in el.attrib}
    for el in root.iter():
        if el.attrib.get("class") == "etc-elements-meta" and el.text:
            meta = json.loads(el.text)
            if isinstance(meta, dict):
                refs.update(meta.keys())
    return refs


_G_ROLE_PARSE_RE = re.compile(r":g:`(?:([^`<]+?)\s*<(.+?)>|([^`<]+))`")


def _reconcile_g_roles_with_svgs(rst_text: str, svg_refs: set[str]) -> str:
    """Normalize or unwrap ``:g:`` roles so every ``:g:`` link resolves to an element in ``svg_refs``."""
    if not svg_refs or ":g:`" not in rst_text:
        return rst_text

    # Build lookup tables for reversed 2-point lines [ Q P ] -> [ P Q ] and permuted 3-point polygons
    line_rev_map: dict[str, str] = {}
    poly_set_map: dict[frozenset[str], str] = {}
    for ref_id in sorted(svg_refs):
        if ref_id.startswith("[") and ref_id.endswith("]"):
            pts = ref_id[1:-1].strip().split()
            if len(pts) == 2:
                line_rev_map[f"[ {pts[1]} {pts[0]} ]"] = ref_id
        elif ref_id.startswith("<") and ref_id.endswith(">"):
            pts = ref_id[1:-1].strip().split()
            if len(pts) == 3:
                poly_set_map.setdefault(frozenset(pts), ref_id)

    out_chunks: list[str] = []
    last_idx = 0
    for m in _G_ROLE_PARSE_RE.finditer(rst_text):
        start, end = m.start(), m.end()
        out_chunks.append(rst_text[last_idx:start])
        if m.group(2) is not None:
            disp = m.group(1).strip()
            targ = m.group(2).strip()
        else:
            disp = m.group(3).strip()
            targ = disp

        resolved: str | None = None
        if targ in svg_refs:
            resolved = targ
        elif targ in line_rev_map:
            resolved = line_rev_map[targ]
        elif targ.startswith("<") and targ.endswith(">"):
            pts = targ[1:-1].strip().split()
            if len(pts) == 3 and frozenset(pts) in poly_set_map:
                resolved = poly_set_map[frozenset(pts)]

        if resolved is not None:
            out_chunks.append(f":g:`{disp} <{resolved}>`")
        else:
            clean_disp = disp.replace("{", "").replace("}", "")
            out_chunks.append(f"``{clean_disp}``")
        last_idx = end

    out_chunks.append(rst_text[last_idx:])
    return "".join(out_chunks)


def _short_center_title(raw_title: str) -> str:
    """Format a concise readable center title from ``_load_center_names()``."""
    clean = raw_title.lstrip("=").strip()
    if len(clean) > 38 and "(" in clean:
        clean = clean.split("(")[0].strip()
    if clean.isupper():
        return _format_title_as_prose(clean).title()
    return clean


def _format_four_triangle_table_rst(num: int) -> list[str]:
    """Build the 4-Triangle Exact Symbolic Coordinate & Invariant RST table for ``X_num``."""
    from .plates import CIRCLE_CENTER_SPECS
    from .symbolic_cache import CenterSymbolicRegistry, format_symbolic_latex
    from .triangles import CANONICAL_TRIANGLES

    tri_specs = [
        ("heronian", r"**Heronian** :math:`(15, 13, 14)`"),
        ("right", r"**Right** :math:`(3, 4, 5)`"),
        ("kepler", r"**Kepler** :math:`(1, \sqrt{\phi}, \phi)`"),
        ("kimberling", r"**Kimberling** :math:`(6, 9, 13)`"),
    ]
    c_spec = CIRCLE_CENTER_SPECS.get(num)
    dist_col = (
        c_spec.table_header
        if c_spec is not None
        else r"Directed Trilinear :math:`(d_a,\, Q_a)`"
    )
    out = [
        ".. list-table:: Exact Symbolic Coordinates & Invariants Across the Four Reference Triangles",
        "   :header-rows: 1",
        "   :widths: 18 10 18 14 16 14 14",
        "",
        "   * - Reference Triangle",
        "     - Field",
        r"     - Cartesian :math:`(x, y)`",
        r"     - Trilinears :math:`\alpha : \beta : \gamma`",
        r"     - Barycentrics :math:`u : v : w`",
        r"     - Sub-Areas :math:`(\Delta_a, \Delta_b, \Delta_c)`",
        f"     - {dist_col}",
    ]
    for t_key, t_label in tri_specs:
        tri = CANONICAL_TRIANGLES[t_key]
        rec = CenterSymbolicRegistry(tri).get(num)
        if rec is None:
            continue
        kp = rec.is_kepler
        f_latex = f":math:`{tri.coordinate_field_latex([*rec.xy, *rec.bary])}`"
        sa_parts = [format_symbolic_latex(sa, kepler_phi=kp) for sa in rec.sub_areas]
        sa_ltx = rf"\left({sa_parts[0]},\; {sa_parts[1]},\; {sa_parts[2]}\right)"
        if c_spec is not None:
            d_val = c_spec.radius_fn(tri)
            q_val = tri.simplify(d_val * d_val)
            d_ltx = format_symbolic_latex(d_val, kepler_phi=kp)
            q_ltx = format_symbolic_latex(q_val, kepler_phi=kp)
            dq_cell = rf":math:`{c_spec.r_sym} = {d_ltx},\; {c_spec.q_sym} = {q_ltx}`"
        else:
            d_val = rec.search_value
            q_val = tri.simplify(d_val * d_val)
            d_ltx = format_symbolic_latex(d_val, kepler_phi=kp)
            q_ltx = format_symbolic_latex(q_val, kepler_phi=kp)
            dq_cell = rf":math:`{d_ltx}\; (Q_a = {q_ltx})`"
        out.extend(
            [
                f"   * - {t_label}",
                f"     - {f_latex}",
                f"     - :math:`{rec.xy_latex()}`",
                f"     - :math:`{rec.trilinear_latex()}`",
                f"     - :math:`{rec.bary_latex()}`",
                f"     - :math:`{sa_ltx}`",
                f"     - {dq_cell}",
            ]
        )
    out.append("")
    return out


def _format_act2_prose_rst(num: int) -> list[str]:
    """Generate Act 2 homogeneous trilinear and barycentric narrative from exact Heronian invariants."""
    import sympy as sp
    from geometor.model import exact_sign, zero_test

    from .plates import CIRCLE_CENTER_SPECS, exact_pedal_foot_and_param
    from .symbolic_cache import CenterSymbolicRegistry, format_symbolic_latex
    from .triangles import CANONICAL_TRIANGLES

    tri = CANONICAL_TRIANGLES["heronian"]
    rec = CenterSymbolicRegistry(tri).get(num)
    key = f"X_{num}"

    pa_ex, _ = exact_pedal_foot_and_param(rec.xy, tri.B_xy, tri.C_xy, tri)
    pb_ex, _ = exact_pedal_foot_and_param(rec.xy, tri.C_xy, tri.A_xy, tri)
    pc_ex, _ = exact_pedal_foot_and_param(rec.xy, tri.A_xy, tri.B_xy, tri)

    def _pt_ltx(pt: tuple[sp.Expr, sp.Expr]) -> str:
        return rf"\left({format_symbolic_latex(pt[0])},\; {format_symbolic_latex(pt[1])}\right)"

    sa, sb, sc = rec.sub_areas
    abs_a = tri.simplify(-sa) if exact_sign(sa) < 0 else sa
    abs_b = tri.simplify(-sb) if exact_sign(sb) < 0 else sb
    abs_c = tri.simplify(-sc) if exact_sign(sc) < 0 else sc
    da = tri.simplify(sp.Integer(2) * abs_a / tri.a)
    db = tri.simplify(sp.Integer(2) * abs_b / tri.b)
    dc = tri.simplify(sp.Integer(2) * abs_c / tri.c)
    da_ltx = format_symbolic_latex(da)
    db_ltx = format_symbolic_latex(db)
    dc_ltx = format_symbolic_latex(dc)

    c_spec = CIRCLE_CENTER_SPECS.get(num)
    if c_spec is not None:
        r_val = c_spec.radius_fn(tri)
        q_val = tri.simplify(r_val * r_val)
        r_ltx = format_symbolic_latex(r_val)
        q_ltx = format_symbolic_latex(q_val)
        if zero_test(da - db) and zero_test(db - dc):
            dist_tail = (
                f"Every orthogonal strut equals the radius of :g:`{c_spec.circle_label.lower()} <{c_spec.circle_id}>` "
                rf"(:math:`{c_spec.r_sym} = {r_ltx}`, quadrance :math:`{c_spec.q_sym} = {q_ltx}`), "
                rf"realizing :math:`\alpha : \beta : \gamma = {rec.trilinear_latex()}`."
            )
        else:
            dist_tail = (
                rf"The orthogonal strut lengths are :math:`\left({da_ltx},\; {db_ltx},\; {dc_ltx}\right)`, "
                rf"realizing :math:`\alpha : \beta : \gamma = {rec.trilinear_latex()}`, while "
                f":g:`{c_spec.circle_label.lower()} <{c_spec.circle_id}>` has exact radius "
                rf":math:`{c_spec.r_sym} = {r_ltx}` (quadrance :math:`{c_spec.q_sym} = {q_ltx}`)."
            )
    else:
        neg_sides = [
            lbl
            for lbl, area_v in (("BC", sa), ("CA", sb), ("AB", sc))
            if exact_sign(area_v) < 0
        ]
        sign_note = (
            f" (directed negatively across {', '.join(neg_sides)} since :g:`{key} <{key}>` lies exterior)"
            if neg_sides
            else ""
        )
        dist_tail = (
            rf"The orthogonal strut lengths on :math:`(15, 13, 14)` are :math:`d_a = {da_ltx}`, "
            rf":math:`d_b = {db_ltx}`, and :math:`d_c = {dc_ltx}`{sign_note}, reducing to homogeneous trilinears "
            rf":math:`\alpha : \beta : \gamma = {rec.trilinear_latex()}`."
        )

    trilin_bullet = (
        rf"* **Trilinear Coordinates** (:math:`\alpha : \beta : \gamma = {rec.trilinear_latex()}`): "
        rf"Dropping orthogonal perpendiculars :g:`{key}T_a </ {key} T_a />`, :g:`{key}T_b </ {key} T_b />`, "
        rf"and :g:`{key}T_c </ {key} T_c />` from :g:`{key} <{key}>` to sidelines :g:`BC <[ B C ]>`, "
        rf":g:`CA <[ C A ]>`, and :g:`AB <[ A B ]>` meets the sides at right-spread pedal feet "
        rf":g:`T_a <T_a>` = :math:`{_pt_ltx(pa_ex)}`, :g:`T_b <T_b>` = :math:`{_pt_ltx(pb_ex)}`, "
        rf"and :g:`T_c <T_c>` = :math:`{_pt_ltx(pc_ex)}`. {dist_tail}"
    )

    sa_ltx = format_symbolic_latex(sa)
    sb_ltx = format_symbolic_latex(sb)
    sc_ltx = format_symbolic_latex(sc)
    has_neg_area = any(exact_sign(v) < 0 for v in (sa, sb, sc))
    orient_note = (
        "with negative signed orientation across the crossed sideline(s), summing algebraically to "
        if has_neg_area
        else "summing to "
    )
    bary_bullet = (
        rf"* **Barycentric Coordinates** (:math:`u : v : w = {rec.bary_latex()}`): "
        rf"Joining :g:`{key} <{key}>` to the vertices along :g:`{key}A </ {key} A />`, "
        rf":g:`{key}B </ {key} B />`, and :g:`{key}C </ {key} C />` forms signed sub-triangles "
        rf":g:`△{key}BC << {key} B C >>`, :g:`△{key}CA << {key} C A >>`, and :g:`△{key}AB << {key} A B >>` "
        rf"of exact signed areas :math:`\Delta_a = {sa_ltx}`, :math:`\Delta_b = {sb_ltx}`, and "
        rf":math:`\Delta_c = {sc_ltx}` ({orient_note}:math:`\Delta_a + \Delta_b + \Delta_c = 84 = \Delta`), "
        rf"in homogeneous ratio :math:`u : v : w = {rec.bary_latex()}`."
    )
    return [trilin_bullet, bary_bullet, ""]


def _classify_central_line_name(
    col_set: set[int], i_n: int, j_n: int, center_names: dict[str, str]
) -> str:
    """Return the classical name of a central line from its collinear center indices."""
    if col_set & {2, 3, 4, 5, 20, 30} and len(col_set & {2, 3, 4, 5, 20, 30}) >= 2:
        return "Euler Line"
    if len(col_set & {1, 2, 8, 10}) >= 2:
        return "Nagel Line"
    if len(col_set & {1, 5, 11, 12}) >= 2:
        return "Feuerbach Line"
    if len(col_set & {3, 6, 15, 16}) >= 2:
        return "Brocard Axis"
    if len(col_set & {1, 3, 35, 36, 40}) >= 2 and 1 in col_set and 3 in col_set:
        return "OI Line (Incenter–Circumcenter Axis)"
    if len(col_set & {1, 7, 20}) >= 2 and 1 in col_set and 7 in col_set:
        return "Soddy Line"
    if len(col_set & {6, 13, 14}) >= 2 and ({13, 14} <= col_set or {6, 13} <= col_set or {6, 14} <= col_set):
        return "Fermat Axis"
    if len(col_set & {6, 17, 18}) >= 2 and ({17, 18} <= col_set or {6, 17} <= col_set or {6, 18} <= col_set):
        return "Napoleon Line"
    if len(col_set & {1, 6, 9}) >= 2 and 1 in col_set and (6 in col_set or 9 in col_set):
        return "Incenter–Symmedian Line"
    if len(col_set & {2, 7, 9}) >= 2 and 7 in col_set and (2 in col_set or 9 in col_set):
        return "Gergonne–Centroid–Mittenpunkt Line"
    if len(col_set & {4, 9, 10, 19}) >= 2 and 9 in col_set and (4 in col_set or 10 in col_set):
        return "Orthocenter–Mittenpunkt–Spieker Axis"
    t_i = _short_center_title(center_names.get(str(i_n), f"X_{i_n}"))
    t_j = _short_center_title(center_names.get(str(j_n), f"X_{j_n}"))
    return f"{t_i}–{t_j} Central Line"


def _format_act3_prose_rst(
    num: int,
    model: Any,
    svg_03_refs: set[str],
    valid_centers: set[int] | None = None,
) -> list[str]:
    """Generate Act 3 incident central line bullets directly from the symbolic ``model`` and ``03_central_lines.svg``."""
    import sympy.geometry as spg
    from geometor.model import line_spread, zero_test

    from .plates import _exact_line_eq_pair
    from .render import _load_center_names, model_to_elements_list
    from .symbolic_cache import (
        EXACT_CYCLIC_BARYCENTRICS,
        CenterSymbolicRegistry,
        format_symbolic_latex,
    )
    from .triangles import CANONICAL_TRIANGLES

    if model is None:
        return []
    tri = CANONICAL_TRIANGLES["heronian"]
    reg = CenterSymbolicRegistry(tri)
    center_names = _load_center_names()
    elements = model_to_elements_list(model)

    plotted_centers: set[int] = set()
    for el in elements:
        if el["type"] == "point":
            m_x = re.match(r"^X_(\d+)$", el["ID"])
            if m_x:
                plotted_centers.add(int(m_x.group(1)))

    ab_el = model.get_element_by_ID("[ A B ]")
    out: list[str] = []

    for el in elements:
        if el["type"] != "line":
            continue
        lid = el["ID"]
        m_cl = re.match(r"^\{\s*(\d+)\s*,\s*(\d+)\s*\}$", lid)
        if not m_cl or lid not in svg_03_refs:
            continue
        i_n, j_n = int(m_cl.group(1)), int(m_cl.group(2))
        if i_n not in EXACT_CYCLIC_BARYCENTRICS or j_n not in EXACT_CYCLIC_BARYCENTRICS:
            continue
        rec_i = reg.get(i_n)
        rec_j = reg.get(j_n)

        col_nums: list[int] = []
        for cand in sorted(plotted_centers | {num, i_n, j_n}):
            if cand not in EXACT_CYCLIC_BARYCENTRICS:
                continue
            rc = reg.get(cand)
            det = (
                (rec_j.xy[0] - rec_i.xy[0]) * (rc.xy[1] - rec_i.xy[1])
                - (rec_j.xy[1] - rec_i.xy[1]) * (rc.xy[0] - rec_i.xy[0])
            )
            if zero_test(det):
                col_nums.append(cand)

        line_name = _classify_central_line_name(set(col_nums), i_n, j_n, center_names)
        set_disp = "{" + ", ".join(str(k) for k in col_nums) + "}"

        pt_parts: list[str] = []
        for k in col_nums:
            xk = f"X_{k}"
            if k == num:
                pt_parts.append(f":g:`{xk} <{xk}>`")
                continue
            rk = reg.get(k)
            t_short = _short_center_title(center_names.get(str(k), xk))
            can_ref = valid_centers is None or k in valid_centers
            if xk in svg_03_refs:
                head = f":g:`{xk} <{xk}>`"
                if can_ref:
                    pt_parts.append(f"{head} (:ref:`{t_short} <{xk}>`, :math:`{rk.xy_latex()}`)")
                else:
                    pt_parts.append(f"{head} (*{t_short}*, :math:`{rk.xy_latex()}`)")
            elif can_ref:
                pt_parts.append(f":ref:`{xk} <{xk}>` (*{t_short}*, :math:`{rk.xy_latex()}`)")
            else:
                pt_parts.append(f"**{xk}** (*{t_short}*, :math:`{rk.xy_latex()}`)")

        eq_ltx, _ = _exact_line_eq_pair(rec_i.xy, rec_j.xy, tri)
        line_geom = spg.Line(spg.Point(*rec_i.xy), spg.Point(*rec_j.xy))
        if isinstance(ab_el, spg.Line):
            spr = tri.simplify(line_spread(ab_el, line_geom))
            spr_ltx = format_symbolic_latex(spr)
            if zero_test(spr):
                spr_clause = "spread :math:`0`, **parallel to baseline** :g:`AB <[ A B ]>`"
            elif zero_test(spr - 1):
                spr_clause = "spread :math:`1`, **perpendicular to baseline** :g:`AB <[ A B ]>`"
            else:
                spr_clause = rf"spread :math:`{spr_ltx}` relative to :g:`AB <[ A B ]>`"
        else:
            spr_clause = ""

        eq_tail = (
            rf"with exact Cartesian equation :math:`{eq_ltx}` ({spr_clause})."
            if spr_clause
            else rf"with exact Cartesian equation :math:`{eq_ltx}`."
        )
        out.append(
            f"* **{line_name}** :g:`{set_disp} <{lid}>` — collinear axis through "
            f"{', '.join(pt_parts)}, {eq_tail}"
        )

    if out:
        out.append("")
    return out


def _format_act4_prose_rst(
    num: int,
    svg_04_refs: set[str],
    valid_centers: set[int] | None = None,
) -> list[str]:
    """Generate Act 4 functional relations & conjugate bullets from ``CenterRelationsBundle`` and ``04_relations.svg``."""
    import sympy as sp

    from .plates import AlgebraicPartnerInfo, build_center_relations_bundle
    from .render import _load_center_names
    from .symbolic_cache import CenterSymbolicRegistry, format_symbolic_latex
    from .triangles import CANONICAL_TRIANGLES

    tri = CANONICAL_TRIANGLES["heronian"]
    reg = CenterSymbolicRegistry(tri)
    rec = reg.get(num)
    bundle = build_center_relations_bundle(num, preset="heronian")
    center_names = _load_center_names()
    key = f"X_{num}"

    def _xy_ltx(xy: tuple[sp.Expr, sp.Expr]) -> str:
        return rf"\left({format_symbolic_latex(xy[0])},\; {format_symbolic_latex(xy[1])}\right)"

    def _bary_ltx(bary: tuple[sp.Expr, sp.Expr, sp.Expr]) -> str:
        return " : ".join(format_symbolic_latex(c) for c in bary)

    def _fmt_partner(info: AlgebraicPartnerInfo, include_bary: bool = False) -> str:
        pnum = info.partner_num
        bary_part = (
            rf", homogeneous barycentrics :math:`{_bary_ltx(info.bary)}`"
            if (include_bary and info.bary is not None)
            else ""
        )
        xy_part = rf" at :math:`{_xy_ltx(info.xy)}`" if info.xy is not None else ""
        if pnum is not None:
            px = f"X_{pnum}"
            t_short = _short_center_title(info.partner_title or center_names.get(str(pnum), px))
            can_ref = valid_centers is None or pnum in valid_centers
            pair_lid = f"{{ {min(num, pnum)}, {max(num, pnum)} }}"
            line_tail = (
                f", joined along :g:`{{{min(num, pnum)}, {max(num, pnum)}}} <{pair_lid}>`"
                if pair_lid in svg_04_refs
                else ""
            )
            if px in svg_04_refs:
                ref_chip = f":ref:`{t_short} <{px}>`" if can_ref else f"*{t_short}*"
                return f":g:`{px} <{px}>` ({ref_chip}{bary_part}){xy_part}{line_tail}"
            if can_ref:
                return f":ref:`{px} <{px}>` (*{t_short}*{bary_part}){xy_part}"
            return f"**{px}** (*{t_short}*{bary_part}){xy_part}"
        return f"exact algebraic point{xy_part} (homogeneous barycentrics :math:`{_bary_ltx(info.bary)}`) " if info.bary else f"exact algebraic point{xy_part}"

    bullets: list[str] = []

    # 1. Isogonal Conjugate
    ig = bundle.isogonal
    if ig.is_self:
        bullets.append(
            rf"* **Self-Isogonal Fixed Point:** :g:`{key} <{key}>` is its own "
            rf":term:`isogonal conjugate <isogonal-conjugate>` (:math:`{rec.trilinear_latex()}`), "
            "acting as a fixed point of trilinear inversion."
        )
    elif ig.is_ideal:
        bullets.append(
            r"* **Isogonal Conjugate:** Lies on the ideal line at infinity :math:`u + v + w = 0`."
        )
    else:
        bullets.append(
            f"* **Isogonal Conjugate:** {_fmt_partner(ig, include_bary=True)} "
            f"(:term:`isogonal conjugate <isogonal-conjugate>` via :math:`a^2 vw : b^2 wu : c^2 uv`)."
        )

    # 2. Isotomic Conjugate
    it = bundle.isotomic
    if it.is_self:
        bullets.append(
            rf"* **Self-Isotomic Fixed Point:** :g:`{key} <{key}>` is its own "
            rf":term:`isotomic conjugate <isotomic-conjugate>` (:math:`{rec.bary_latex()}`), "
            "acting as the identity element of barycentric multiplication."
        )
    elif it.is_ideal:
        bullets.append(
            r"* **Isotomic Conjugate:** Lies on the ideal line at infinity :math:`u + v + w = 0`."
        )
    else:
        bullets.append(
            f"* **Isotomic Conjugate:** {_fmt_partner(it, include_bary=True)} "
            f"(:term:`isotomic conjugate <isotomic-conjugate>` via :math:`vw : wu : uv`)."
        )

    # 3. Complement & Anticomplement (Homothetic Dilations from X_2)
    x2_chip = ":g:`X_2 <X_2>`" if "X_2" in svg_04_refs else ":ref:`X_2 <X_2>`"
    comp = bundle.complement
    anti = bundle.anticomplement
    if comp.is_self and anti.is_self:
        bullets.append(
            rf"* **Homothetic Center of Complement & Anticomplement:** :g:`{key} <{key}>` is the fixed "
            r"homothetic center for both :term:`complement <complement>` (factor :math:`-\frac{1}{2}`) "
            r"and :term:`anticomplement <anticomplement>` (factor :math:`-2`) dilations."
        )
    else:
        bullets.append(
            f"* **Complement:** {_fmt_partner(comp)} — :term:`complement <complement>` of "
            rf":g:`{key} <{key}>` dilated from {x2_chip} by factor :math:`-\frac{{1}}{{2}}`."
        )
        bullets.append(
            f"* **Anticomplement:** {_fmt_partner(anti)} — :term:`anticomplement <anticomplement>` of "
            rf":g:`{key} <{key}>` dilated from {x2_chip} by factor :math:`-2`."
        )

    # 4. Circumcircle Inversion
    ci = bundle.circumcircle_inverse
    x3_chip = ":g:`X_3 <X_3>`" if "X_3" in svg_04_refs else ":ref:`X_3 <X_3>`"
    circ_chip = ":g:`circumcircle <circumcircle>`" if "circumcircle" in svg_04_refs else "the circumcircle"
    if ci.is_center_of_inversion:
        bullets.append(
            rf"* **Center of Circumcircle Inversion:** :g:`{key} <{key}>` is the center of {circ_chip} "
            r"(:math:`R = \frac{65}{8}`, :math:`Q_R = \frac{4225}{64}`), mapping under circumcircle inversion "
            r"to the ideal line at infinity :math:`u + v + w = 0`."
        )
    else:
        q_op_ltx = format_symbolic_latex(ci.inversion_quadrance) if ci.inversion_quadrance is not None else ""
        sc_ltx = format_symbolic_latex(ci.inversion_scale) if ci.inversion_scale is not None else ""
        ray_id = f"{{ {min(num, 3)}, {max(num, 3)} }}"
        ray_part = (
            f" along :g:`{{{min(num, 3)}, {max(num, 3)}}} <{ray_id}>`"
            if ray_id in svg_04_refs
            else ""
        )
        bullets.append(
            rf"* **Circumcircle Inverse:** Inversion in {circ_chip} centered at {x3_chip} = "
            rf":math:`\left(7, \frac{{33}}{{8}}\right)` (:math:`Q_R = \frac{{4225}}{{64}}`) maps "
            rf":g:`{key} <{key}>`{ray_part} (:math:`Q({key}, X_3) = {q_op_ltx}`, scale :math:`Q_R / Q = {sc_ltx}`) "
            f"to {_fmt_partner(ci)}."
        )

    # 5. Quadratic Galois Conjugate over Q(sqrt(3)) (for X_13..X_18)
    if bundle.galois_conjugate is not None:
        bullets.append(
            r"* **Quadratic :math:`\sqrt{3}` Conjugate:** Conjugation :math:`\sqrt{3} \mapsto -\sqrt{3}` "
            rf"over :math:`\mathbb{{Q}}(\sqrt{{3}})` maps :g:`{key} <{key}>` (outward/inward equilateral "
            f"orientation reversal) directly to {_fmt_partner(bundle.galois_conjugate)}."
        )

    # 6. Harmonic Conjugate on the Feuerbach Line (for X_11 <-> X_12)
    if bundle.harmonic_feuerbach_partner is not None:
        h_k = bundle.harmonic_feuerbach_partner
        hk_rec = reg.get(h_k)
        hk_id = f"X_{h_k}"
        hk_title = _short_center_title(center_names.get(str(h_k), hk_id))
        hk_chip = (
            f":g:`{hk_id} <{hk_id}>` (:ref:`{hk_title} <{hk_id}>`, :math:`{hk_rec.xy_latex()}`)"
            if hk_id in svg_04_refs
            else f":ref:`{hk_id} <{hk_id}>` (*{hk_title}*, :math:`{hk_rec.xy_latex()}`)"
        )
        x1_c = ":g:`X_1 <X_1>`" if "X_1" in svg_04_refs else ":ref:`X_1 <X_1>`"
        x5_c = ":g:`X_5 <X_5>`" if "X_5" in svg_04_refs else ":ref:`X_5 <X_5>`"
        bullets.append(
            f"* **Feuerbach Harmonic Conjugate:** {hk_chip} divides {x1_c} and {x5_c} harmonically "
            rf"with :g:`{key} <{key}>` in exact projective cross-ratio :math:`(X_1, X_5; X_{{11}}, X_{{12}}) = -1`."
        )

    bullets.append("")
    return bullets


def _format_act5_prose_rst(num: int) -> list[str]:
    """Generate Act 5 four-triangle symbolic invariance synthesis for ``X_num``."""
    from geometor.model import exact_sign, zero_test

    from .plates import CIRCLE_CENTER_SPECS
    from .symbolic_cache import CenterSymbolicRegistry, format_symbolic_latex
    from .triangles import CANONICAL_TRIANGLES

    key = f"X_{num}"
    c_spec = CIRCLE_CENTER_SPECS.get(num)

    recs = {
        k: CenterSymbolicRegistry(CANONICAL_TRIANGLES[k]).get(num)
        for k in ("heronian", "right", "kepler", "kimberling")
    }
    tris = {k: CANONICAL_TRIANGLES[k] for k in ("heronian", "right", "kepler", "kimberling")}

    def _panel_phrase(t_key: str, disp_lbl: str) -> str:
        tri = tris[t_key]
        rec = recs[t_key]
        kp = rec.is_kepler
        fld = tri.coordinate_field_latex([*rec.xy, *rec.bary])
        extra = ""
        if c_spec is not None:
            r_val = c_spec.radius_fn(tri)
            r_ltx = format_symbolic_latex(r_val, kepler_phi=kp)
            extra = (
                f", :g:`{c_spec.r_sym} <{t_key}-{c_spec.circle_id}>` = :math:`{r_ltx}`"
            )
        if t_key == "kepler" and len(rec.xy_latex()) > 65:
            return rf":g:`{disp_lbl} <{t_key}-{key}>` over :math:`{fld}`{extra}"
        return rf":g:`{disp_lbl} <{t_key}-{key}>` over :math:`{fld}` (:math:`{key} = {rec.xy_latex()}`{extra})"

    p_hero = _panel_phrase("heronian", "Heronian (15, 13, 14)")
    p_right = _panel_phrase("right", "Right (3, 4, 5)")
    p_kep = _panel_phrase("kepler", "Kepler (1, √φ, φ)")
    p_kim = _panel_phrase("kimberling", "Kimberling (6, 9, 13)")

    rec_r = recs["right"]
    if zero_test(rec_r.sub_areas[0]) and zero_test(rec_r.sub_areas[1]):
        regime = (
            f"on right-angled triangles (:math:`\\angle C = 90^\\circ`), **{key}** coincides exactly with the "
            f"right-angle vertex :g:`C <right-C>` / :g:`C <kepler-C>` (:math:`0 : 0 : 1`), whereas on acute "
            f":g:`Heronian <panel-heronian>` it lies strictly interior and on obtuse :g:`Kimberling <panel-kimberling>` "
            f"it crosses into the exterior."
        )
    elif zero_test(rec_r.sub_areas[2]):
        regime = (
            f"by Thales's theorem (:math:`\\angle C = 90^\\circ`), **{key}** falls directly on the midpoint of "
            f"hypotenuse :math:`AB` (:math:`\\Delta_c = 0`) on both :g:`Right (3, 4, 5) <panel-right>` and "
            f":g:`Kepler (1, √φ, φ) <panel-kepler>`, lies strictly interior on acute :g:`Heronian <panel-heronian>`, "
            f"and moves strictly exterior (:math:`\\Delta_c < 0`) on obtuse :g:`Kimberling <panel-kimberling>`."
        )
    else:
        int_keys = [
            lbl
            for t_k, lbl in (
                ("heronian", "Heronian"),
                ("right", "Right"),
                ("kepler", "Kepler"),
                ("kimberling", "Kimberling"),
            )
            if all(exact_sign(sa) > 0 for sa in recs[t_k].sub_areas)
        ]
        if len(int_keys) == 4:
            regime = (
                f"**{key}** remains strictly interior (:math:`\\Delta_a, \\Delta_b, \\Delta_c > 0`) across all four "
                f"acute, Pythagorean right, golden right, and obtuse scalene triangles, preserving its exact "
                f"homogeneous law :math:`u : v : w` without floating-point approximation."
            )
        elif not int_keys:
            regime = (
                f"**{key}** lies strictly exterior across all four reference triangles (carrying at least one "
                f"negative signed sub-area :math:`\\Delta_k < 0` while preserving :math:`\\Delta_a + \\Delta_b + \\Delta_c = \\Delta`)."
            )
        else:
            ext_keys = [
                lbl
                for lbl in ("Heronian", "Right", "Kepler", "Kimberling")
                if lbl not in int_keys
            ]
            regime = (
                f"**{key}** lies strictly interior on {', '.join(int_keys)} while crossing outside "
                f":math:`\\triangle ABC` on {', '.join(ext_keys)} (where signed sub-areas change sign across "
                f"the sidelines while still summing algebraically to :math:`\\Delta`)."
            )

    return [
        f"Across the four canonical algebraic number fields — {p_hero}, {p_right}, {p_kep}, and {p_kim} — {regime}",
        "",
    ]


def _format_five_act_center_rst(
    data: dict[str, Any],
    entry_dir: Path,
    glossary_terms: dict[str, Any] | list[str] | None = None,
    preambles: list[dict[str, Any]] | None = None,
    valid_centers: set[int] | None = None,
    figure_uri: str | None = None,
    search_value: float | None = None,
    include_model_py: bool = False,
    model: Any = None,
) -> str:
    """Format the Unified 5-Act Visual & Symbolic Dossier (`index.rst`) for any center with a 5-act plate suite."""
    from .ops import get_center_concordance
    from .plates import CIRCLE_CENTER_SPECS
    from .symbolic_cache import CenterSymbolicRegistry, format_symbolic_latex
    from .triangles import CANONICAL_TRIANGLES

    key = data["key"]
    title = data.get("title", "")
    num = int(data.get("num") or re.sub(r"[^0-9]", "", key) or 0)
    if num > 0:
        key = f"X_{num}"

    concordance = get_center_concordance(num)
    hero_tri = CANONICAL_TRIANGLES["heronian"]
    hero_rec = CenterSymbolicRegistry(hero_tri).get(num)
    kimb_tri = CANONICAL_TRIANGLES["kimberling"]
    kimb_rec = CenterSymbolicRegistry(kimb_tri).get(num)
    exact_search_ltx = kimb_rec.search_latex() if kimb_rec is not None else ""
    approx_search = (
        kimb_rec.approx_search_value()
        if kimb_rec is not None
        else (search_value or 0.0)
    )

    lines: list[str] = [
        f":order: {num}",
        f":canonical_id: {key}",
    ]
    if title and title != key:
        lines.append(f":subtitle: {title}")
    aliases = data.get("aliases") or []
    if aliases:
        lines.append(f":aliases: {', '.join(aliases)}")
    if data.get("dependencies"):
        lines.append(f":dependencies: {', '.join(data['dependencies'])}")
    lines.append("")

    # Anchors (including canonical snake_case constructor anchor!)
    lines.append(f".. _X_{num}:")
    anchor_id = data.get("anchor_id")
    seen_anchors = {f"x_{num}"}
    if anchor_id and anchor_id.lower() not in seen_anchors and anchor_id not in {f"X_{num}", f"X({num})"}:
        lines.append(f".. _{anchor_id}:")
        seen_anchors.add(anchor_id.lower())
    if concordance and concordance.function_name.lower() not in seen_anchors:
        lines.append(f".. _{concordance.function_name}:")
    lines.append("")

    lines.append(key)
    lines.append("=" * max(4, len(key)))
    lines.append("")
    if title and title != key:
        lines.append(f".. rubric:: {title}")
        lines.append("")

    if concordance:
        search_part = (
            rf" • **Search Value** :math:`(6, 9, 13)`: :math:`{exact_search_ltx} \approx {approx_search:.12f}`"
            if exact_search_ltx
            else ""
        )
        lines.append(
            f"``{concordance.signature}`` • **{concordance.classical_ref}** • "
            f"**Kimberling** ``X({num})``{search_part}"
        )
        lines.append("")

    seen_terms: set[str] = set()
    seen_persons: set[str] = set()
    seen_cites: set[str] = set()

    raw_notes = data.get("notes") or []
    raw_relations = data.get("relations") or []
    enun_raw, remaining_notes = _extract_primary_enunciation(
        raw_notes, raw_relations, num=num, title=title
    )

    # ------------------------------------------------------------------
    # Act 1: Primary Construction & Concurrence
    # ------------------------------------------------------------------
    if enun_raw:
        enriched_enun = _enrich_text(
            enun_raw,
            glossary_terms,
            seen_terms,
            seen_persons,
            seen_cites,
            valid_centers=valid_centers,
        )
        lines.append(".. enunciation::")
        lines.append("")
        for e_ln in enriched_enun.splitlines():
            lines.append(f"   {e_ln}" if e_ln.strip() else "")
        lines.append("")

    if preambles:
        for p_item in preambles:
            parsed_p = parse_preamble(p_item.get("html", ""))
            p_title = parsed_p["title"] or p_item.get("title", "Preamble")
            p_paras = parsed_p["paragraphs"]
            p_id = p_item.get("id")
            if p_id:
                lines.append(f".. _{p_id}:")
                lines.append("")
            lines.append(f".. admonition:: Group Preamble — {p_title}")
            lines.append("   :class: note")
            lines.append("")
            for para in p_paras or [p_title]:
                enriched_para = _enrich_text(
                    para, glossary_terms, seen_terms, seen_persons, seen_cites, valid_centers=valid_centers
                )
                for p_ln in enriched_para.splitlines():
                    lines.append(f"   {p_ln}" if p_ln.strip() else "")
                lines.append("")

    alt_title = f"{key} — {title}" if title and title != key else key
    cap_title = f"**{key}** (*{title}*)" if title and title != key else f"**{key}**"
    if figure_uri:
        h_field = hero_tri.coordinate_field_latex([*hero_rec.xy, *hero_rec.bary])
        field_adj = "exact rational" if h_field == r"\mathbb{Q}" else "exact algebraic"
        c_spec = CIRCLE_CENTER_SPECS.get(num)
        circle_clause = ""
        if c_spec is not None:
            r_ltx = format_symbolic_latex(c_spec.radius_fn(hero_tri))
            circle_clause = rf", and {c_spec.circle_label.lower()} radius :math:`{c_spec.r_sym} = {r_ltx}`"
        lines.append(f".. figure:: {figure_uri}")
        lines.append(f"   :alt: {alt_title}")
        lines.append("   :align: center")
        lines.append("")
        lines.append(
            f"   {cap_title} constructed at :g:`{key} <{key}>` = :math:`{hero_rec.xy_latex()}` in {field_adj} "
            f"coordinates on the Heronian reference triangle :math:`(a, b, c) = (15, 13, 14)` over "
            rf":math:`{h_field}` with vertices :g:`A <A>` = :math:`(0, 0)`, :g:`B <B>` = :math:`(14, 0)`, "
            rf":g:`C <C>` = :math:`(5, 12)`, and area :math:`\Delta = 84`{circle_clause}. "
            r"Switch tabs above to inspect exact constructions on Right :math:`(3, 4, 5)`, "
            r"Kepler :math:`(1, \sqrt{\phi}, \phi)`, and Kimberling :math:`(6, 9, 13)`."
        )
        lines.append("")

    if model is not None:
        lines.extend(
            _format_constructed_elements_rst(
                model, data, enun_raw, valid_centers=valid_centers
            )
        )

    # ------------------------------------------------------------------
    # Act 2: Homogeneous Coordinates & Exact Symbolic Invariants
    # ------------------------------------------------------------------
    lines.extend(
        [
            "Homogeneous Coordinates & Exact Invariants",
            "------------------------------------------",
            "",
            ".. figure:: 02_coordinates.svg",
            f"   :alt: {key} — Homogeneous Trilinear Distances and Barycentric Sub-Areas",
            "   :align: center",
            "",
            (
                f"   **Homogeneous Coordinates of {key}** on Heronian :math:`(15, 13, 14)`: orthogonal trilinear struts "
                r":math:`(\alpha, \beta, \gamma)` and signed barycentric sub-triangles :math:`(\Delta_a, \Delta_b, \Delta_c)`."
            ),
            "",
        ]
    )
    lines.extend(_format_act2_prose_rst(num))
    lines.extend(_format_four_triangle_table_rst(num))

    has_coords = any(data.get(k) for k in ("trilinears", "barycentrics", "tripolars"))
    alt_coord_bullets: list[str] = []
    if has_coords or abs(approx_search) > 1e-12:
        lines.append(".. signature:: center")
        lines.append("")
        for coord_key, coord_label in (
            ("trilinears", "Trilinears"),
            ("barycentrics", "Barycentrics"),
            ("tripolars", "Tripolars"),
        ):
            items = data.get(coord_key) or []
            if not items:
                continue
            enriched_items = []
            for item in items:
                enr = _enrich_text(
                    " ".join(item.splitlines()).strip(),
                    glossary_terms,
                    seen_terms,
                    seen_persons,
                    seen_cites,
                    valid_centers=valid_centers,
                )
                if enr:
                    enriched_items.append(enr)
            if not enriched_items:
                continue
            lines.append(f"   | **{coord_label}:** {enriched_items[0]}")
            rest_start = 1
            if len(enriched_items) > 1 and enriched_items[1].lower().startswith("where"):
                lines.append(f"   |   {enriched_items[1]}")
                rest_start = 2
            for extra_it in enriched_items[rest_start:]:
                alt_coord_bullets.append(f"**{coord_label}:** {extra_it}")

        if exact_search_ltx:
            lines.append(
                rf"   | **Search Value (6, 9, 13):** :math:`{exact_search_ltx} \approx {approx_search:.12f}`"
            )
        elif abs(approx_search) > 1e-12:
            lines.append(f"   | **Search Value (6, 9, 13):** :math:`{approx_search:.12f}`")
        lines.append("")

    if alt_coord_bullets:
        n_alt = len(alt_coord_bullets)
        lines.extend(
            [
                ".. collapse:: Alternate Coordinates",
                f"   :badge: {'1 form' if n_alt == 1 else f'{n_alt} forms'}",
                "",
            ]
        )
        for b_line in alt_coord_bullets:
            lines.append(f"   * {b_line}")
        lines.append("")

    combos = data.get("combinations") or []
    if combos:
        n_combos = len(combos)
        lines.extend(
            [
                ".. collapse:: Linear Combinations",
                f"   :badge: {'1 combination' if n_combos == 1 else f'{n_combos} combinations'}",
                "",
            ]
        )
        for combo in combos:
            enriched_combo = _enrich_text(
                combo, glossary_terms, seen_terms, seen_persons, seen_cites, valid_centers=valid_centers
            )
            combo_lines = [ln.strip() for ln in enriched_combo.splitlines() if ln.strip()]
            if combo_lines:
                lines.append(f"   * {' '.join(combo_lines)}")
        lines.append("")

    # ------------------------------------------------------------------
    # Act 3: Incident Central Lines
    # ------------------------------------------------------------------
    svg_03_path = entry_dir / "03_central_lines.svg"
    if svg_03_path.is_file():
        svg_03_refs = extract_svg_element_refs(svg_03_path)
        lines.extend(
            [
                "Incident Central Lines",
                "----------------------",
                "",
                ".. figure:: 03_central_lines.svg",
                f"   :alt: {key} — Incident Central Lines",
                "   :align: center",
                "",
                f"   **Principal Central Lines Through {key}** on Heronian :math:`(15, 13, 14)`.",
                "",
            ]
        )
        lines.extend(_format_act3_prose_rst(num, model, svg_03_refs, valid_centers=valid_centers))

    incidences = data.get("incidences") or []
    for inc in incidences:
        if isinstance(inc, dict):
            line_pairs = inc.get("lines") or []
            curves_prefix = inc.get("curves_prefix", "")
            if line_pairs:
                enriched_prefix = _enrich_text(
                    curves_prefix, glossary_terms, seen_terms, seen_persons, seen_cites, valid_centers=valid_centers
                ).strip()
                is_bare_key = bool(
                    re.match(
                        r"^(?::ref:`X(?:_|\()\d+\)? <X(?:_|\()\d+\)?>`|X(?:_|\()\d+\)?)\s*$",
                        enriched_prefix,
                    )
                )
                if enriched_prefix and not is_bare_key:
                    lines.append(".. container:: note-item")
                    lines.append("")
                    for c_ln in f"{enriched_prefix}.".splitlines():
                        lines.append(f"   {c_ln}" if c_ln.strip() else "")
                    lines.append("")

                def _fmt_inc_pt(pt: int) -> str:
                    if valid_centers is None or pt in valid_centers:
                        return f":ref:`{pt} <X_{pt}>`"
                    return str(pt)

                formatted_pairs = [f"{{{_fmt_inc_pt(i)}, {_fmt_inc_pt(j)}}}" for i, j in line_pairs]
                n_lines = len(line_pairs)
                lines.extend(
                    [
                        ".. collapse:: Full Incident Central Line Catalog",
                        f"   :badge: {'1 line' if n_lines == 1 else f'{n_lines} lines'}",
                        "   :class: line-catalog",
                        "",
                        f"   {', '.join(formatted_pairs)}",
                        "",
                    ]
                )

    # ------------------------------------------------------------------
    # Act 4: Functional Relations & Conjugates
    # ------------------------------------------------------------------
    svg_04_path = entry_dir / "04_relations.svg"
    if svg_04_path.is_file():
        svg_04_refs = extract_svg_element_refs(svg_04_path)
        lines.extend(
            [
                "Functional Relations & Conjugates",
                "---------------------------------",
                "",
                ".. figure:: 04_relations.svg",
                f"   :alt: {key} — Functional Relations and Conjugates",
                "   :align: center",
                "",
                f"   **Conjugate & Homothetic Partners of {key}** on Heronian :math:`(15, 13, 14)`.",
                "",
            ]
        )
        lines.extend(_format_act4_prose_rst(num, svg_04_refs, valid_centers=valid_centers))

    if raw_relations:
        n_rels = len(raw_relations)
        lines.extend(
            [
                ".. collapse:: Full Functional Relations Catalog",
                f"   :badge: {'1 relation' if n_rels == 1 else f'{n_rels} relations'}",
                "",
            ]
        )
        for rel in raw_relations:
            rel_with_tuples = _wrap_relation_tuples(rel, valid_centers=valid_centers)
            enriched_rel = _enrich_text(
                rel_with_tuples, glossary_terms, seen_terms, seen_persons, seen_cites, valid_centers=valid_centers
            )
            rel_lines = [ln.strip() for ln in enriched_rel.splitlines() if ln.strip()]
            if rel_lines:
                lines.append(f"   * {' '.join(rel_lines)}")
        lines.append("")

    # ------------------------------------------------------------------
    # Act 5: Four-Triangle Symbolic Invariance
    # ------------------------------------------------------------------
    if (entry_dir / "05_four_triangles.svg").is_file():
        lines.extend(
            [
                "Four-Triangle Symbolic Invariance",
                "---------------------------------",
                "",
                ".. figure:: 05_four_triangles.svg",
                f"   :alt: {key} — Invariance Across Four Canonical Symbolic Reference Triangles",
                "   :align: center",
                "",
                (
                    f"   **Four-Triangle Invariance of {key}** across :g:`Heronian (15, 13, 14) <panel-heronian>`, "
                    r":g:`Right (3, 4, 5) <panel-right>`, :g:`Kepler (1, √φ, φ) <panel-kepler>`, and "
                    r":g:`Kimberling (6, 9, 13) <panel-kimberling>`."
                ),
                "",
            ]
        )
        lines.extend(_format_act5_prose_rst(num))

    if num in _COLLECTION_1_TOPIC_GUIDES:
        lines.extend(
            [
                ".. admonition:: Related Collection 1 Topic Guides",
                "   :class: tip",
                "",
                f"   {_COLLECTION_1_TOPIC_GUIDES[num]}",
                "",
            ]
        )

    if remaining_notes:
        lines.extend(["Notes", "-----", ""])

        def _fmt_circle_idx(m: re.Match) -> str:
            idx_str = m.group(1)
            idx_int = int(idx_str)
            if valid_centers is None or idx_int in valid_centers:
                return f":ref:`{idx_str} <X_{idx_str}>`"
            return idx_str

        for note in remaining_notes:
            enriched_note = _enrich_text(
                note, glossary_terms, seen_terms, seen_persons, seen_cites, valid_centers=valid_centers
            )
            lines.append(".. container:: note-item")
            lines.append("")
            for n_ln in enriched_note.splitlines():
                if n_ln.strip().startswith("* (") and ";" in n_ln:
                    n_ln = re.sub(r"(?<=[;,]\s)(\d+)\b", _fmt_circle_idx, n_ln)
                lines.append(f"   {n_ln}" if n_ln.strip() else "")
            lines.append("")

    if include_model_py:
        lines.extend([".. toctree::", "   :hidden:", "", "   code", ""])

    page_svg_refs: set[str] = set()
    for svg_name in (
        figure_uri or f"x-{num:05d}.svg",
        "02_coordinates.svg",
        "03_central_lines.svg",
        "04_relations.svg",
        "05_four_triangles.svg",
    ):
        page_svg_refs.update(extract_svg_element_refs(entry_dir / svg_name))

    raw_rst = "\n".join(lines).rstrip() + "\n"
    return _reconcile_g_roles_with_svgs(raw_rst, page_svg_refs)


def transform_center_to_rst(
    data: dict[str, Any],
    glossary_terms: dict[str, Any] | list[str] | None = None,
    preambles: list[dict[str, Any]] | None = None,
    valid_centers: set[int] | None = None,
    figure_uri: str | None = None,
    kimberling_figure_uri: str | None = None,
    search_value: float | None = None,
    include_model_py: bool = False,
    model: Any = None,
    entry_dir: str | Path | None = None,
) -> str:
    """Transform a parsed center dictionary into the Book Codex Overview track (`index.rst`)."""
    if not data or not data.get("key"):
        return ""

    if entry_dir is not None:
        e_path = Path(entry_dir)
        if (e_path / "02_coordinates.svg").is_file() and (e_path / "05_four_triangles.svg").is_file():
            return _format_five_act_center_rst(
                data=data,
                entry_dir=e_path,
                glossary_terms=glossary_terms,
                preambles=preambles,
                valid_centers=valid_centers,
                figure_uri=figure_uri,
                search_value=search_value,
                include_model_py=include_model_py,
                model=model,
            )

    key = data["key"]
    title = data.get("title", "")
    num = data.get("num")
    if num is None:
        try:
            num = int(re.sub(r"[^0-9]", "", key))
        except ValueError:
            num = 0
    if num > 0:
        key = f"X_{num}"

    lines: list[str] = [
        f":order: {num}",
        f":canonical_id: {key}",
    ]
    if title and title != key:
        lines.append(f":subtitle: {title}")

    aliases = data.get("aliases") or []
    if aliases:
        lines.append(f":aliases: {', '.join(aliases)}")

    if data.get("dependencies"):
        lines.append(f":dependencies: {', '.join(data['dependencies'])}")

    lines.append("")

    # Anchors
    lines.append(f".. _X_{num}:")
    anchor_id = data.get("anchor_id")
    if anchor_id and anchor_id not in {f"X_{num}", f"X({num})"}:
        lines.append(f".. _{anchor_id}:")
    lines.append("")

    # Document Title (=) — Line 1: X_n (centered)
    lines.append(key)
    lines.append("=" * max(4, len(key)))
    lines.append("")

    # Subtitle — Line 2: centered .. rubric:: subtitle
    if title and title != key:
        lines.append(f".. rubric:: {title}")
        lines.append("")

    seen_terms: set[str] = set()
    seen_persons: set[str] = set()
    seen_cites: set[str] = set()

    raw_notes = data.get("notes") or []
    raw_relations = data.get("relations") or []
    enun_raw, remaining_notes = _extract_primary_enunciation(
        raw_notes, raw_relations, num=num, title=title
    )

    if enun_raw:
        enriched_enun = _enrich_text(
            enun_raw,
            glossary_terms,
            seen_terms,
            seen_persons,
            seen_cites,
            valid_centers=valid_centers,
        )
        lines.append(".. enunciation::")
        lines.append("")
        for e_ln in enriched_enun.splitlines():
            lines.append(f"   {e_ln}" if e_ln.strip() else "")
        lines.append("")

    # Optional preceding inter-center group preamble(s)
    if preambles:
        for p_item in preambles:
            parsed_p = parse_preamble(p_item.get("html", ""))
            p_title = parsed_p["title"] or p_item.get("title", "Preamble")
            p_paras = parsed_p["paragraphs"]
            p_id = p_item.get("id")
            if p_id:
                lines.append(f".. _{p_id}:")
                lines.append("")
            if p_paras:
                lines.append(f".. admonition:: Group Preamble — {p_title}")
                lines.append("   :class: note")
                lines.append("")
                for para in p_paras:
                    enriched_para = _enrich_text(
                        para,
                        glossary_terms,
                        seen_terms,
                        seen_persons,
                        seen_cites,
                        valid_centers=valid_centers,
                    )
                    for p_ln in enriched_para.splitlines():
                        lines.append(f"   {p_ln}" if p_ln.strip() else "")
                    lines.append("")
            else:
                lines.append(".. admonition:: Group Preamble")
                lines.append("   :class: note")
                lines.append("")
                enriched_title = _enrich_text(
                    p_title,
                    glossary_terms,
                    seen_terms,
                    seen_persons,
                    seen_cites,
                    valid_centers=valid_centers,
                )
                for p_ln in enriched_title.splitlines():
                    lines.append(f"   {p_ln}" if p_ln.strip() else "")
                lines.append("")

    # 1. Primary Geometric Construction Figure (4-Tab Interactive Panel)
    alt_title = f"{key} — {title}" if title and title != key else key
    cap_title = f"**{key}** (*{title}*)" if title and title != key else f"**{key}**"
    if figure_uri:
        lines.append(f".. figure:: {figure_uri}")
        lines.append(f"   :alt: {alt_title}")
        lines.append("   :align: center")
        lines.append("")
        lines.append(
            f"   {cap_title} constructed on acute reference triangle "
            r":math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`."
        )
        lines.append("")

    # 1b. Constructed Elements Card (links prose symbols & derived triangles/circles/lines to SVG elements)
    if model is not None:
        lines.extend(
            _format_constructed_elements_rst(
                model, data, enun_raw, valid_centers=valid_centers
            )
        )

    # 2. Compact Coordinate Signature Card (.. signature:: center) + Alternate Coordinates
    has_coords = any(
        data.get(k) for k in ("trilinears", "barycentrics", "tripolars")
    )
    alt_coord_bullets: list[str] = []
    if has_coords or (search_value is not None and abs(search_value) > 1e-12):
        lines.append(".. signature:: center")
        lines.append("")
        for coord_key, coord_label in (
            ("trilinears", "Trilinears"),
            ("barycentrics", "Barycentrics"),
            ("tripolars", "Tripolars"),
        ):
            items = data.get(coord_key) or []
            if not items:
                continue
            enriched_items = []
            for item in items:
                enr = _enrich_text(
                    " ".join(item.splitlines()).strip(),
                    glossary_terms,
                    seen_terms,
                    seen_persons,
                    seen_cites,
                    valid_centers=valid_centers,
                )
                if enr:
                    enriched_items.append(enr)
            if not enriched_items:
                continue
            lines.append(f"   | **{coord_label}:** {enriched_items[0]}")
            rest_start = 1
            if len(enriched_items) > 1 and enriched_items[1].lower().startswith(
                "where"
            ):
                lines.append(f"   |   {enriched_items[1]}")
                rest_start = 2
            for extra_it in enriched_items[rest_start:]:
                alt_coord_bullets.append(f"**{coord_label}:** {extra_it}")

        if search_value is not None and abs(search_value) > 1e-12:
            lines.append(
                f"   | **Search Value (6, 9, 13):** :math:`{search_value:.12f}`"
            )
        lines.append("")

    if alt_coord_bullets:
        n_alt = len(alt_coord_bullets)
        alt_badge = "1 form" if n_alt == 1 else f"{n_alt} forms"
        lines.append(".. collapse:: Alternate Coordinates")
        lines.append(f"   :badge: {alt_badge}")
        lines.append("")
        for b_line in alt_coord_bullets:
            lines.append(f"   * {b_line}")
        lines.append("")

    # 3. Collapsible Linear Combinations
    combos = data.get("combinations") or []
    if combos:
        n_combos = len(combos)
        combo_badge = (
            "1 combination" if n_combos == 1 else f"{n_combos} combinations"
        )
        lines.append(".. collapse:: Linear Combinations")
        lines.append(f"   :badge: {combo_badge}")
        lines.append("")
        for combo in combos:
            enriched_combo = _enrich_text(
                combo,
                glossary_terms,
                seen_terms,
                seen_persons,
                seen_cites,
                valid_centers=valid_centers,
            )
            combo_lines = [
                ln.strip() for ln in enriched_combo.splitlines() if ln.strip()
            ]
            if combo_lines:
                lines.append(f"   * {' '.join(combo_lines)}")
        lines.append("")

    # 4. Incidence (Curves visible + Collapsible Incident Central Lines)
    incidences = data.get("incidences") or []
    if incidences:
        for inc in incidences:
            if isinstance(inc, dict):
                line_pairs = inc.get("lines") or []
                curves_prefix = inc.get("curves_prefix", "")
                if line_pairs:
                    enriched_prefix = _enrich_text(
                        curves_prefix,
                        glossary_terms,
                        seen_terms,
                        seen_persons,
                        seen_cites,
                        valid_centers=valid_centers,
                    ).strip()
                    is_bare_key = bool(
                        re.match(
                            r"^(?::ref:`X(?:_|\()\d+\)? <X(?:_|\()\d+\)?>`|X(?:_|\()\d+\)?)\s*$",
                            enriched_prefix,
                        )
                    )
                    if enriched_prefix and not is_bare_key:
                        lines.append(".. container:: note-item")
                        lines.append("")
                        for c_ln in f"{enriched_prefix}.".splitlines():
                            lines.append(f"   {c_ln}" if c_ln.strip() else "")
                        lines.append("")

                    def _fmt_inc_pt(pt: int) -> str:
                        if valid_centers is None or pt in valid_centers:
                            return f":ref:`{pt} <X_{pt}>`"
                        return str(pt)

                    formatted_pairs = [
                        f"{{{_fmt_inc_pt(i)}, {_fmt_inc_pt(j)}}}"
                        for i, j in line_pairs
                    ]
                    n_lines = len(line_pairs)
                    badge_lbl = "1 line" if n_lines == 1 else f"{n_lines} lines"
                    lines.append(".. collapse:: Incident Central Lines")
                    lines.append(f"   :badge: {badge_lbl}")
                    lines.append("   :class: line-catalog")
                    lines.append("")
                    lines.append(f"   {', '.join(formatted_pairs)}")
                    lines.append("")
                else:
                    raw_inc = _enrich_text(
                        inc.get("raw_rst", ""),
                        glossary_terms,
                        seen_terms,
                        seen_persons,
                        seen_cites,
                        valid_centers=valid_centers,
                    ).strip()
                    if raw_inc:
                        lines.append(".. container:: note-item")
                        lines.append("")
                        for r_ln in raw_inc.splitlines():
                            lines.append(f"   {r_ln}" if r_ln.strip() else "")
                        lines.append("")
            else:
                str_inc = _enrich_text(
                    str(inc),
                    glossary_terms,
                    seen_terms,
                    seen_persons,
                    seen_cites,
                    valid_centers=valid_centers,
                ).strip()
                if str_inc:
                    lines.append(".. container:: note-item")
                    lines.append("")
                    for s_ln in str_inc.splitlines():
                        lines.append(f"   {s_ln}" if s_ln.strip() else "")
                    lines.append("")

    # 5. Collapsible Functional Relations
    if raw_relations:
        n_rels = len(raw_relations)
        rel_badge = "1 relation" if n_rels == 1 else f"{n_rels} relations"
        lines.append(".. collapse:: Functional Relations")
        lines.append(f"   :badge: {rel_badge}")
        lines.append("")
        for rel in raw_relations:
            rel_with_tuples = _wrap_relation_tuples(
                rel, valid_centers=valid_centers
            )
            enriched_rel = _enrich_text(
                rel_with_tuples,
                glossary_terms,
                seen_terms,
                seen_persons,
                seen_cites,
                valid_centers=valid_centers,
            )
            rel_lines = [ln.strip() for ln in enriched_rel.splitlines() if ln.strip()]
            if rel_lines:
                lines.append(f"   * {' '.join(rel_lines)}")
        lines.append("")

    # 6. Remaining Notes
    if remaining_notes:
        lines.append("Notes")
        lines.append("-----")
        lines.append("")

        def _fmt_circle_idx(m: re.Match) -> str:
            idx_str = m.group(1)
            idx_int = int(idx_str)
            if valid_centers is None or idx_int in valid_centers:
                return f":ref:`{idx_str} <X_{idx_str}>`"
            return idx_str

        for note in remaining_notes:
            enriched_note = _enrich_text(
                note,
                glossary_terms,
                seen_terms,
                seen_persons,
                seen_cites,
                valid_centers=valid_centers,
            )
            lines.append(".. container:: note-item")
            lines.append("")
            for n_ln in enriched_note.splitlines():
                if n_ln.strip().startswith("* (") and ";" in n_ln:
                    n_ln = re.sub(
                        r"(?<=[;,]\s)(\d+)\b",
                        _fmt_circle_idx,
                        n_ln,
                    )
                lines.append(f"   {n_ln}" if n_ln.strip() else "")
            lines.append("")

    # 7. Companion Code Track Toctree
    if include_model_py:
        lines.append(".. toctree::")
        lines.append("   :hidden:")
        lines.append("")
        lines.append("   code")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def transform_center_to_code_rst(
    data: dict[str, Any],
    glossary_terms: dict[str, Any] | list[str] | None = None,
    valid_centers: set[int] | None = None,
    figure_uri: str | None = None,
    entry_dir: str | Path | None = None,
) -> str:
    """Transform a parsed center dictionary into the companion Code track (`code.rst`)."""
    if not data or not data.get("key"):
        return ""

    key = data["key"]
    num = int(data.get("num") or re.sub(r"[^0-9]", "", key) or 0)
    if num > 0:
        key = f"X_{num}"
    title = data.get("title", "")
    alt_title = f"{key} — {title}" if title and title != key else key
    cap_title = f"**{key}** (*{title}*)" if title and title != key else f"**{key}**"

    is_heronian = False
    svg_file: Path | None = None
    if entry_dir is not None and figure_uri:
        svg_file = Path(entry_dir) / figure_uri
        if svg_file.is_file():
            head_txt = svg_file.read_text(encoding="utf-8")[:512]
            if 'data-triangle="heronian"' in head_txt:
                is_heronian = True

    lines: list[str] = [
        f":canonical_id: {key}",
    ]
    if title and title != key:
        lines.append(f":subtitle: {title}")
    lines.extend(
        [
            "",
            key,
            "=" * max(4, len(key)),
            "",
        ]
    )

    if title and title != key:
        lines.append(f".. rubric:: {title}")
        lines.append("")

    enun_raw, _ = _extract_primary_enunciation(
        data.get("notes") or [],
        data.get("relations") or [],
        num=num,
        title=title,
    )
    if enun_raw:
        enriched_enun = _enrich_text(
            enun_raw,
            glossary_terms,
            set(),
            set(),
            set(),
            valid_centers=valid_centers,
        )
        lines.append(".. enunciation::")
        lines.append("")
        for e_ln in enriched_enun.splitlines():
            lines.append(f"   {e_ln}" if e_ln.strip() else "")
        lines.append("")

    if figure_uri:
        lines.append(f".. figure:: {figure_uri}")
        lines.append(f"   :alt: {alt_title}")
        lines.append("   :align: center")
        lines.append("")
        if is_heronian and num > 0:
            from .symbolic_cache import CenterSymbolicRegistry
            from .triangles import CANONICAL_TRIANGLES

            hero_tri = CANONICAL_TRIANGLES["heronian"]
            hero_rec = CenterSymbolicRegistry(hero_tri).get(num)
            if hero_rec is not None:
                h_field = hero_tri.coordinate_field_latex([*hero_rec.xy, *hero_rec.bary])
                field_adj = "exact rational" if h_field == r"\mathbb{Q}" else "exact algebraic"
                lines.append(
                    f"   {cap_title} constructed at :g:`{key} <{key}>` = :math:`{hero_rec.xy_latex()}` in {field_adj} "
                    f"coordinates on the Heronian reference triangle :math:`(a, b, c) = (15, 13, 14)` over "
                    rf":math:`{h_field}` with vertices :g:`A <A>` = :math:`(0, 0)`, :g:`B <B>` = :math:`(14, 0)`, "
                    r":g:`C <C>` = :math:`(5, 12)`."
                )
            else:
                lines.append(
                    f"   {cap_title} constructed in exact rational coordinates on the Heronian reference triangle "
                    r":math:`(a, b, c) = (15, 13, 14)` over :math:`\mathbb{Q}` with vertices :g:`A <A>` = :math:`(0, 0)`, "
                    r":g:`B <B>` = :math:`(14, 0)`, :g:`C <C>` = :math:`(5, 12)`."
                )
        else:
            lines.append(
                f"   {cap_title} constructed on acute reference triangle "
                r":math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`."
            )
        lines.append("")

    lines.append(".. literalinclude:: model.py")
    lines.append("   :language: python")
    lines.append("")

    raw_rst = "\n".join(lines).rstrip() + "\n"
    if is_heronian and svg_file is not None and svg_file.is_file():
        return _reconcile_g_roles_with_svgs(raw_rst, extract_svg_element_refs(svg_file))
    return raw_rst


# ---------------------------------------------------------------------------
# Thematic Collection Definitions (Option #2 — Preamble & Family Groupings)
# ---------------------------------------------------------------------------

THEMATIC_COLLECTIONS: list[tuple[int, int, str, str]] = [
    (
        1,
        19,
        "Classical & Ancient Centers",
        "The foundational centers of classical triangle geometry: the incenter, centroid, circumcenter, orthocenter, nine-point center, symmedian point, Gergonne, Nagel, Mittenpunkt, Spieker, Feuerbach, Fermat, isodynamic, Napoleon, and Clawson points.",
    ),
    (
        20,
        30,
        "Euler Line Centers",
        "Classical centers lying on the Euler line X_2 X_3, including the De Longchamps point, Schiffler point, Exeter point, far-out point, homothetic center of the orthic and tangential triangles, and the Euler infinity point.",
    ),
    (
        31,
        58,
        "Power Points, Circle Similicenters & Named Centers",
        "2nd and 3rd power points, the Bevan point, Brocard midpoint, Kosnita point, and internal and external centers of similitude of the circumcircle, incircle, and nine-point circle.",
    ),
    (
        59,
        97,
        "Isogonal & Isotomic Conjugates of Classical Centers",
        "Isogonal conjugates (X_59–X_74) and isotomic and cross conjugates (X_75–X_97) of the classical centers X_1–X_58.",
    ),
    (
        98,
        112,
        "Centers on the Circumcircle",
        "Notable points on the circumcircle of ABC, including the Tarry point, Steiner point, anticomplementary, Feuerbach, Kiepert, and Jerabek antipodes, and centers derived from circumcircle mappings.",
    ),
    (
        113,
        139,
        "Centers on the Nine-Point Circle & Orthic Centers",
        "Points on the nine-point circle (X_113–X_139), centers of the Kiepert, Feuerbach, and Jerabek rectangular hyperbolas, and centers transferred to the orthic triangle.",
    ),
    (
        140,
        190,
        "Derived Triangle Centers, Isoscelizers & Ajima-Malfatti Points",
        "Complements, anticomplements, and classical centers evaluated on the medial, orthic, tangential, and excentral triangles, together with congruent isoscelizer, equal detour, and Ajima-Malfatti points.",
    ),
    (
        191,
        236,
        "Ceva Conjugates",
        "Perspectors of the cevian triangle of P and the anticevian triangle of Q (P-Ceva conjugates of Q) for classical triangle centers.",
    ),
    (
        237,
        248,
        "Line Conjugates",
        "Intersections of line PQ with the trilinear polar of the isogonal conjugate of P (P-line conjugates of Q).",
    ),
    (
        249,
        297,
        "Isogonal Conjugates II & Hirst Inverses",
        "Isogonal conjugates of centers X_115–X_248, together with cross conjugates and X_2-Hirst inverses.",
    ),
    (
        298,
        350,
        "Isotomic Conjugates II",
        "Isotomic conjugates of previously cataloged triangle centers, together with X_2-Hirst inverses and radical centers.",
    ),
    (
        351,
        400,
        "Parry Circle, Morley/Yff Centers & Pedal Centroids",
        "The Parry circle center, Morley trisector centers, Yff equal-parallelians, trisected-perimeter, and equilateral-cevian points, Kenmotu point, and centroids of pedal and cevian triangles.",
    ),
    (
        401,
        484,
        "Euler Line Substitutions & Hirst Inverses",
        "Centers lying on the Euler line generated by X_k-substitutions and Hirst inversions, followed by the Tixier point, Ajima-Malfatti radical center, and Evans perspectors.",
    ),
    (
        485,
        510,
        "Vecten Square Centers & Isoscelizer Centers",
        "Inner and outer Vecten points and square-associated centers (Vierkanten in een driehoek, X_485–X_495), harmonic conjugates, and isoscelizer-associated centers (X_503–X_510).",
    ),
    (
        511,
        565,
        "Centers on the Line at Infinity & Vector Directions",
        "Points on the line at infinity x + y + z = 0 (X_511–X_526, isogonal conjugates of circumcircle points), unit vector direction centers, and classical midpoints.",
    ),
    (
        566,
        642,
        "Brocard Axis Circles & Gibert Centers",
        "Centers on the Brocard axis X_3 X_6 whose circles cut equal chords on the sidelines of ABC (X_566–X_584), congruent shrunk insquares points, and centers contributed by Bernard Gibert (X_616–X_642).",
    ),
    (
        643,
        693,
        "Crossdifferences & Trilinear Poles",
        "Trilinear multipliers for the Kiepert and Yff parabolas, crossdifferences of classical centers, and trilinear poles of central lines.",
    ),
    (
        694,
        768,
        "Even (p, q) Circumcircle Points",
        "Even trigonometric (p, q) points on the circumcircle and line at infinity, paired with their isogonal conjugates.",
    ),
    (
        769,
        843,
        "Odd o-(p, q) Circumcircle Points",
        "Odd trigonometric o-(p, q) points on the circumcircle and line at infinity, paired with their isogonal conjugates.",
    ),
    (
        844,
        900,
        "Hatzipolakis-Yiu Centers, Hirst Inverses & Crossdifferences",
        "Hatzipolakis-Yiu points, the Yiu angle point (X_848), Kiepert hyperbola multipliers, Hirst inverses, and Euler line intercepts.",
    ),
    (
        901,
        1000,
        "Star-Named Centers, Ehrmann Points & Anticomplements",
        "Star-named centers (Agena, Achernar, Algenib, Alcor), Ehrmann points, anticomplements, and midpoints of classical triangle centers.",
    ),
    (
        1001,
        1069,
        "Classical Midpoints, Euler Intercepts & Cevapoints",
        "Midpoints of classical centers, Euler line intercepts, collinearity intersections, cevapoints, and pure-angle trilinear centers.",
    ),
    (
        1070,
        1114,
        "Cross Conjugates, Trilinear Squares & Euler-Circumcircle Intersections",
        "Cross conjugates, trilinear squares and cubes of classical centers, and the intersections of the Euler line with the circumcircle (X_1113, X_1114).",
    ),
    (
        1115,
        1165,
        "Morley-Taylor-Marr, Hofstadter, Ehrmann & Star Centers",
        "Morley-Taylor-Marr centers, Hofstadter points, the Ehrmann congruent squares point (X_1144), Grebe triangle centers, and star-named points (Aldebaran, Algjebbah, Altair, Altais).",
    ),
    (
        1166,
        1208,
        "Saragossa Points",
        "1st, 2nd, and 3rd Saragossa points (Q, Q', Q'') constructed from the cevian and circumcevian triangles of classical centers.",
    ),
    (
        1209,
        1285,
        "Saragossa Conjugates, Sharygin Points & Lemoine Homothetic Center",
        "Isogonal and isotomic conjugates of the Saragossa points, Sharygin points, and the Lemoine homothetic center (X_1285).",
    ),
    (
        1286,
        1311,
        "Collings Transforms",
        "Concurrence points on the circumcircle of the circumcircles of AB'C', A'BC', and A'B'C, where A'B'C' is the reflection of ABC in P.",
    ),
    (
        1312,
        1353,
        "Moses Intersections, Circumcircle Inverses, Wernau Points & Similicenters",
        "Moses orthocentroidal-Euler intersections, circumcircle inverses, 1st and 2nd Wernau points (X_1337, X_1338), and similicenters of the circumcircle, nine-point circle, orthocentroidal circle, and Brocard circle.",
    ),
    (
        1354,
        1392,
        "Brisse Transforms, Rigby/Griffiths Points & Complementary Conjugates",
        "Polynomial centers on the incircle generated by the Brisse transform (X_1354–X_1367), Rigby and Griffiths points, and complementary and anticomplementary conjugates.",
    ),
    (
        1393,
        1477,
        "Beth Conjugates & Harmonic Conjugates",
        "Fixed-point P-beth conjugates of P and harmonic conjugates along central lines.",
    ),
    (
        1478,
        1511,
        "Johnson-Yff Circle, Perspectors & Star-Named Centers",
        "The Johnson-Yff circle center, tangential-of-tangential perspectors, star-named centers (Bellatrix, Betelgeuse, Biham), and Napoleon and Fermat crosssums.",
    ),
    (
        1512,
        1600,
        "Orthojoins, Moses Circle Centers & Star-Named Centers",
        "Orthojoins H(X) — orthopoles of the trilinear polars of isogonal conjugates (X_1512–X_1568) — together with Moses circle similicenters and star-named centers (Capella, Caph, Cebalrai, Celaeno, Chertan, Chort).",
    ),
    (
        1601,
        1661,
        "TCC-Perspectors & Tripolar Centroids",
        "Perspectors of the tangential triangle and the circumcevian triangle of P (X_1601–X_1634), tripolar centroids (X_1635–X_1651), and Evans and Grinberg perspectors.",
    ),
    (
        1662,
        1706,
        "Circle-Related Points",
        "Internal and external centers of similitude among the circumcircle, incircle, nine-point circle, Brocard circle, 1st and 2nd Lemoine circles, Apollonius circle, and Bevan circle.",
    ),
    (
        1707,
        1788,
        "Mimosa Transforms",
        "Centers generated by the Mimosa transform M(X) of classical triangle centers.",
    ),
    (
        1789,
        1823,
        "Inverse Mimosa Transforms & Aleph Conjugates",
        "Inverse Mimosa transforms of classical triangle centers and aleph conjugates.",
    ),
    (
        1824,
        1907,
        "Zosma Transforms",
        "Isogonal conjugates of the inverse Mimosa transforms (Z(X)) of classical triangle centers.",
    ),
    (
        1908,
        2000,
        "Bicentric Pairs PU(k) & Orthocorrespondents",
        "Midpoints, crosssums, crossdifferences, trilinear poles, and trilinear products of bicentric pairs PU(k) (X_1908–X_1982), Vega transforms, and orthocorrespondents (X_1992–X_2000).",
    ),
    (
        2001,
        2054,
        "Orthocorrespondents, Gallatly Circle & Euler-Vecten-Gibert Points",
        "Orthocorrespondents of classical centers (X_2001–X_2006), similicenters and intersections of the Gallatly circle (X_2007–X_2040), and the six Euler-Vecten-Gibert points and harmonic conjugates (X_2041–X_2054).",
    ),
    (
        2055,
        2119,
        "Orion Transforms, Circumcircle Inverses, PK/NK Transforms, Reflections & Kepler Points",
        "Orion transforms OT(X) (X_2055–X_2065), Caroli and Cursa points, circumcircle inverses (X_2070–X_2080), PK and NK transforms (X_2081–X_2092), classical reflections (X_2093–X_2105), and Kepler points and their isotomic conjugates (X_2106–X_2119).",
    ),
    (
        2120,
        2147,
        "Eigencenters & Eigentransforms",
        "Eigentransforms ET(X) — eigencenters of the cevian triangles of classical centers — paired with their isogonal conjugates on the self-isogonal cubic Z(X) (X_2120–X_2143), followed by X_2-eigentransforms (X_2144–X_2147).",
    ),
    (
        2148,
        2254,
        "Isotomic Conjugates (X_2-Isoconjugates) I",
        "Isotomic conjugates (X_2-isoconjugates) of triangle centers X_5 through X_892.",
    ),
    (
        2255,
        2364,
        "Isotomic Conjugates (X_2-Isoconjugates) II",
        "Isotomic conjugates (X_2-isoconjugates) of triangle centers X_901 through X_2099.",
    ),
    (
        2365,
        2445,
        "Circumcircle CIR(X) Points & Gibert-Simson Transforms",
        "Circumcevian-eigentransform points CIR(X) on the circumcircle and their isogonal conjugates (X_2365–X_2393), followed by Gibert-Simson transforms GS(X) on the Simson cubic K010 (X_2394–X_2419) and their isogonal conjugates on K162 (X_2420–X_2445).",
    ),
    (
        2446,
        2520,
        "Circle & Conic Intersections, Lemoine Inverses & Radical Centers I",
        "Intersections of central lines with the incircle, Bevan circle, Steiner inellipse, and Steiner circumellipse, inverses in the 1st and 2nd Lemoine circles, and circle radical centers (X_2446–X_2520).",
    ),
    (
        2521,
        2593,
        "Circle Similicenters, Radical Centers & Isoconjugates II",
        "Similicenters and intersections involving the orthocentroidal, 2nd Brocard, Parry, and Gallatly circles (X_2521–X_2573), followed by isogonal and X_k-isoconjugates (X_2574–X_2593).",
    ),
    (
        2594,
        2676,
        "Bicentric Pairs PU(68)–PU(85) & Golden Arbelos Points",
        "Sums, differences, crosssums, crossdifferences, trilinear poles, and midpoints of bicentric pairs PU(68) through PU(85) (X_2594–X_2670), together with the 1st and 2nd Golden Arbelos points (X_2671–X_2676).",
    ),
    (
        2677,
        2770,
        "Rigby-Simson RS(P, U) & Simson-Rigby SR(P, U) Points",
        "Rigby-Simson orthopoles RS(P, U) where the Simson lines of circumcircle points P and U meet (X_2677–X_2686), and Simson-Rigby circumcircle points SR(P, U) whose Simson lines pass through RS(P, U) perpendicular to PU (X_2687–X_2770).",
    ),
    (
        2771,
        2854,
        "Isogonal Conjugates of Simson-Rigby SR(P, U) Points",
        "Points on the line at infinity formed as the isogonal conjugates of the Simson-Rigby circumcircle points X_2687–X_2770.",
    ),
    (
        2855,
        2882,
        "Simson-Moses SM(P, U) Points & Conjugates",
        "Simson-Moses circumcircle points SM(P, U) generated by isotomic conjugation of circumcircle pairs (X_2855–X_2868) and their isogonal conjugates on the line at infinity (X_2869–X_2882).",
    ),
    (
        2883,
        2966,
        "Isogonal Conjugates with Respect to Special Triangles",
        "Complementary (medial-isogonal), anticomplementary-isogonal, tangential-isogonal, and excentral-isogonal conjugates of classical triangle centers, together with trilinear and barycentric products.",
    ),
    (
        2967,
        3000,
        "MacBeath Points, Dual Centers DC(X) / CD(X) & Central Line Intersections",
        "The eight MacBeath points (X_2967–X_2974), circle radical centers (X_2975–X_2978), dual triangle mappings DC(X) and CD(X) (X_2979–X_2998), the Danneels-Bevan homothetic center (X_2999), and the Soddy-antiorthic intersection (X_3000).",
    ),
    (
        3001,
        3118,
        "Central Line Intersections, Stevanović Points & T/G Mappings",
        "Pairwise intersections of the Brocard, de Longchamps, Gergonne, Lemoine, Nagel, orthic, Soddy, and Fermat axes (X_3001–X_3019), the 4th–10th Stevanović points (X_3020–X_3026), antipodal circle mappings and complements (X_3027–X_3111), and Quang Tuan Bui's TgX and GtX mappings (X_3112–X_3118).",
    ),
    (
        3119,
        3217,
        "Danneels Perspectors & X_i-Ceva Conjugates",
        "Eric Danneels' parallel-cevian perspectors (X_3119–X_3126) and a systematic catalog of X_i-Ceva conjugates of classical and central points (X_3127–X_3217).",
    ),
    (
        3218,
        3309,
        "Side-Swapping SS(a → bc) Points, Parabola Vertices & Morley Equilateral Triangles",
        "Side-swapping transformations SS(a → bc), vertices of the inscribed Kiepert and Yff parabolas (X_3233–X_3234), reflections in X_1 (X_3241–X_3245), and centers and perspectors of the six equilateral triangles related to the 1st, 2nd, and 3rd Morley triangles (X_3272–X_3283).",
    ),
    (
        3310,
        3414,
        "Incircle Transforms T(U), Trigonometric Offset Points & Kiepert Cusps",
        "Barycentric products of perpendicular directions (X_3310), incircle transforms T(U) lying on the incircle (X_3318–X_3328), Darboux-cubic reflections and conjugates (X_3341–X_3358), trigonometric phase-shifted centers cos/sin/sec/csc/tan/cot(A ± θ) (X_3364–X_3409), and the Brocard-Kiepert-Fermat cusps (X_3411–X_3414).",
    ),
    (
        3415,
        3514,
        "Vertex Conjugates, Saragossa Points & Neuberg Cubic Intersections",
        "U-vertex conjugates of X formed from circumcevian vertex triangles (X_3415–X_3458), 1st Saragossa points (X_3449–X_3454), X_5- and X_30-Ceva conjugates on the Neuberg cubic (X_3460–X_3488), and the 1st dilation center and its circumcircle inverse (X_3513–X_3514).",
    ),
    (
        3515,
        3601,
        "Euler Line Intercepts & Named Geometric Centers",
        "Euler line intercepts of central lines (X_3515–X_3552), together with the Dosa, Pappus, Moses circumcircle/infinity, Don Quixote, Beltrami-Euler, Beltrami-Parry, Myakishev conic, Dixit, Odehnal, and Liu points (X_3555–X_3601).",
    ),
    (
        3602,
        3662,
        "Morley Cubics, Medial Homothetic Centers H(X; M, t) & Kirikami-Schiffler Points",
        "Centers associated with the three Morley cubics K029–K031 (X_3602–X_3615), medial-triangle t-dilation homothetic centers H(X; M, t) and their isogonal conjugates H⁻¹(X; M, t) (X_3616–X_3637), Soddy-Gergonne, Kirikami, Alkaid, and Almach points (X_3638–X_3646), and Kirikami-Schiffler points KS(T) (X_3647–X_3662).",
    ),
    (
        3663,
        3757,
        "Central Triangle Combos Xcom(T) I: Intouch, Extouch, Incentral & Hexyl Triangles",
        "Combo centers X_k-com(T) evaluated on the intouch (X_3663–X_3677), extouch (X_3678–X_3719), incentral (X_3720–X_3728), excentral, tangential, 1st Brocard, and hexyl triangles (X_3729–X_3738), plus matrix-product combos n(incentral)*n(medial) and inverse-triangle combos (X_3739–X_3757).",
    ),
    (
        3758,
        3861,
        "Central Triangle Combos Xcom(T) II: Parameterized T(f, g) & Euler Triangles",
        "Combo centers X_k-com[T(f, g)] and X_k-com[Inverse(nT(f, g))] for parameterized central triangles (X_3758–X_3810), followed by combo centers on the 1st through 5th Euler triangles (X_3811–X_3861).",
    ),
    (
        3862,
        4000,
        "Inverse Central Triangle Combos Xcom[Inverse(n(T))]",
        "Perspectors of ABC and parameterized central triangles T(f, g) (X_3862–X_3867), inverse 3rd/4th/5th Euler triangle combos (X_3868–X_3910), and combos and inverse-triangle combos across the intouch, extouch, orthic, tangential, hexyl, Brocard, incentral, excentral, intangents, and extangents triangles (X_3911–X_4000).",
    ),
]


def get_collection_spec(num: int) -> tuple[int, int, str, str]:
    """Return `(start_num, end_num, title, summary)` for center `num`."""
    for start_num, end_num, c_title, c_summary in THEMATIC_COLLECTIONS:
        if start_num <= num <= end_num:
            return (start_num, end_num, c_title, c_summary)
    start_num = ((max(1, num) - 1) // 100) * 100 + 1
    end_num = start_num + 99
    return (
        start_num,
        end_num,
        f"Centers X_{start_num}–X_{end_num}",
        f"Triangle centers X_{start_num} through X_{end_num}.",
    )


def get_collection_folder_name(start_num: int, end_num: int) -> str:
    """Return the subdirectory name for a collection range `(start_num, end_num)`."""
    return f"c-{start_num:05d}-{end_num:05d}"


_SHARED_GEN_STATE: dict[str, Any] = {}


def _process_center_index(idx: int) -> None:
    """Worker function for fork-based parallel center folder generation."""
    state = _SHARED_GEN_STATE
    center = state["centers"][idx]
    if not center:
        return

    out_path: Path = state["out_path"]
    acute_reg = state["acute_reg"]
    right_reg = state["right_reg"]
    kepler_reg = state["kepler_reg"]
    kimb_reg = state["kimb_reg"]
    kimb_ctx = state["kimb_ctx"]
    render_graphics: bool = state["render_graphics"]
    glossary_terms = state["glossary_terms"]
    valid_centers = state["valid_centers"]
    build_center_model = state["build_center_model"]
    generate_center_model_py = state["generate_center_model_py"]
    write_center_svg = state["write_center_svg"]

    key = center["key"]
    num = center.get("num")
    if num is None:
        try:
            num = int(re.sub(r"[^0-9]", "", key))
        except ValueError:
            num = 0
    if num > 0:
        key = f"X_{num}"

    start_num, end_num, _, _ = get_collection_spec(num)
    coll_dir = out_path / get_collection_folder_name(start_num, end_num)
    folder_name = f"x-{num:05d}" if num > 0 else key
    entry_dir = coll_dir / folder_name
    entry_dir.mkdir(parents=True, exist_ok=True)
    filepath = entry_dir / "index.rst"
    code_rst_path = entry_dir / "code.rst"
    model_py_path = entry_dir / "model.py"

    figure_uri: str | None = None
    search_val: float | None = None
    has_model_py = False
    model_acute = None

    if num in kimb_reg.bary_cache:
        kb = kimb_reg.bary_cache[num]
        if abs(sum(kb)) > 1e-6:
            search_val = kimb_ctx.kimberling_search_value(*kb)

    svg_name = f"x-{num:05d}.svg"
    right_svg_name = f"x-{num:05d}-right.svg"
    kepler_svg_name = f"x-{num:05d}-kepler.svg"
    kimb_svg_name = f"x-{num:05d}-kimberling.svg"

    model_py_changed = False
    is_symbolic_model_py = (
        model_py_path.is_file()
        and "construct_reference_triangle" in model_py_path.read_text(encoding="utf-8")
    )
    if is_symbolic_model_py:
        import runpy

        has_model_py = True
        mod_ns = runpy.run_path(str(model_py_path))
        if "build_model" in mod_ns:
            model_acute = mod_ns["build_model"]("heronian")
    elif num in acute_reg.xy_cache:
        model_py_code = generate_center_model_py(center, acute_reg)
        if not model_py_path.is_file() or model_py_path.read_text(encoding="utf-8") != model_py_code:
            model_py_path.write_text(model_py_code, encoding="utf-8")
            model_py_changed = True
        has_model_py = True
        model_acute = build_center_model(center, acute_reg)

    all_svgs_exist = (
        not model_py_changed
        and (entry_dir / svg_name).is_file()
        and (entry_dir / right_svg_name).is_file()
        and (entry_dir / kepler_svg_name).is_file()
        and (entry_dir / kimb_svg_name).is_file()
        and (entry_dir / f"x-{num:05d}.json").is_file()
    )

    if render_graphics and model_acute is not None and not all_svgs_exist and not is_symbolic_model_py:
        write_center_svg(
            model_acute,
            entry_dir / svg_name,
            subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
        )
        model_acute.save(str(entry_dir / f"x-{num:05d}.json"))
        figure_uri = svg_name

        if num in right_reg.xy_cache:
            model_right = build_center_model(center, right_reg)
            write_center_svg(
                model_right,
                entry_dir / right_svg_name,
                subtitle="(a, b, c) = (3, 4, 5) | AB = 1",
            )

        if num in kepler_reg.xy_cache:
            model_kepler = build_center_model(center, kepler_reg)
            write_center_svg(
                model_kepler,
                entry_dir / kepler_svg_name,
                subtitle="Kepler (1, √φ, φ) | AB = 1",
            )

        if num in kimb_reg.xy_cache:
            model_kimb = build_center_model(center, kimb_reg)
            write_center_svg(
                model_kimb,
                entry_dir / kimb_svg_name,
                subtitle="Kimberling (6, 9, 13) | AB = 1",
            )
    else:
        if (entry_dir / svg_name).exists():
            figure_uri = svg_name
        if model_py_path.exists():
            has_model_py = True

    rst_content = transform_center_to_rst(
        center,
        glossary_terms=glossary_terms,
        preambles=None,
        valid_centers=valid_centers,
        figure_uri=figure_uri,
        search_value=search_val,
        include_model_py=has_model_py,
        model=model_acute,
        entry_dir=entry_dir,
    )
    if not filepath.is_file() or filepath.read_text(encoding="utf-8") != rst_content:
        filepath.write_text(rst_content, encoding="utf-8")

    if has_model_py:
        code_rst_content = transform_center_to_code_rst(
            center,
            glossary_terms=glossary_terms,
            valid_centers=valid_centers,
            figure_uri=figure_uri,
            entry_dir=entry_dir,
        )
        if not code_rst_path.is_file() or code_rst_path.read_text(encoding="utf-8") != code_rst_content:
            code_rst_path.write_text(code_rst_content, encoding="utf-8")
    elif code_rst_path.exists():
        code_rst_path.unlink()


def generate_rst_files(
    centers: list[dict[str, Any]],
    output_dir: str | Path,
    glossary_terms: dict[str, Any] | list[str] | None = None,
    preambles_by_center: dict[str, list[dict[str, Any]]] | None = None,
    valid_centers: set[int] | None = None,
    render_graphics: bool = True,
    constructions_dir: str | Path | None = None,
) -> None:
    """Generate thematic collection folders (`c-XXXXX-YYYYY/`) and per-center folders (`x-NNNNN/`)."""
    import concurrent.futures
    import multiprocessing
    import shutil

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    if valid_centers is None:
        valid_centers = set()
        for c in centers:
            if not c:
                continue
            cnum = c.get("num")
            if cnum is None and c.get("key"):
                try:
                    cnum = int(re.sub(r"[^0-9]", "", c["key"]))
                except ValueError:
                    cnum = None
            if cnum:
                valid_centers.add(int(cnum))

    # Migrate any flat `out_path / x-NNNNN` folders into their thematic collection folders
    active_collections: dict[tuple[int, int], tuple[str, str, list[int]]] = {}
    for c in centers:
        if not c or not c.get("num"):
            continue
        num = int(c["num"])
        start_num, end_num, c_title, c_summary = get_collection_spec(num)
        coll_key = (start_num, end_num)
        if coll_key not in active_collections:
            active_collections[coll_key] = (c_title, c_summary, [])
        active_collections[coll_key][2].append(num)

        coll_dir = out_path / get_collection_folder_name(start_num, end_num)
        coll_dir.mkdir(parents=True, exist_ok=True)
        flat_dir = out_path / f"x-{num:05d}"
        target_dir = coll_dir / f"x-{num:05d}"
        if flat_dir.is_dir():
            if not target_dir.exists():
                shutil.move(str(flat_dir), str(target_dir))
            else:
                for f_item in flat_dir.iterdir():
                    dest_item = target_dir / f_item.name
                    if not dest_item.exists():
                        shutil.move(str(f_item), str(dest_item))
                shutil.rmtree(flat_dir, ignore_errors=True)

    from .construct import (
        TRIANGLE_PRESETS,
        CenterRegistry,
        TriangleContext,
        build_center_model,
        build_collection_model,
        generate_center_model_py,
        select_collection_centers,
    )
    from .glossary import _get_glossary_lookup_and_pattern
    from .render import write_center_svg

    if glossary_terms:
        _get_glossary_lookup_and_pattern(glossary_terms)

    # Build coordinate and construction registries on (5, 6, 7), (3, 4, 5), Kepler, and Kimberling (6, 9, 13)
    print(f"Resolving coordinates and incidences for {len(centers)} centers...", flush=True)
    acute_ctx = TriangleContext(*TRIANGLE_PRESETS["acute"])
    acute_reg = CenterRegistry(centers, acute_ctx)
    right_ctx = TriangleContext(*TRIANGLE_PRESETS["right"])
    right_reg = CenterRegistry(centers, right_ctx)
    kepler_ctx = TriangleContext(*TRIANGLE_PRESETS["kepler"])
    kepler_reg = CenterRegistry(centers, kepler_ctx)
    kimb_ctx = TriangleContext(*TRIANGLE_PRESETS["kimberling"])
    kimb_reg = CenterRegistry(centers, kimb_ctx)
    print(f"Resolved {len(acute_reg.xy_cache)} / {len(centers)} centers.", flush=True)

    max_num = max(valid_centers) if valid_centers else 2000
    index_lines = [
        ":navigation: header",
        ":order: 1",
        ":layout: book",
        ":book_title: Encyclopedia of Triangle Centers",
        "",
        "Encyclopedia of Triangle Centers",
        "================================",
        "",
        f".. rubric:: Thematic Collections (X_1–X_{max_num})",
        "",
        ".. collection::",
        "   :type: collection",
        "   :sort: order",
        "",
    ]

    _SHARED_GEN_STATE.clear()
    _SHARED_GEN_STATE.update(
        {
            "centers": centers,
            "out_path": out_path,
            "acute_reg": acute_reg,
            "right_reg": right_reg,
            "kepler_reg": kepler_reg,
            "kimb_reg": kimb_reg,
            "kimb_ctx": kimb_ctx,
            "render_graphics": render_graphics,
            "glossary_terms": glossary_terms,
            "preambles_by_center": preambles_by_center,
            "valid_centers": valid_centers,
            "build_center_model": build_center_model,
            "generate_center_model_py": generate_center_model_py,
            "write_center_svg": write_center_svg,
        }
    )

    total = len(centers)
    if total > 200:
        mp_ctx = multiprocessing.get_context("fork")
        with concurrent.futures.ProcessPoolExecutor(mp_context=mp_ctx) as pool:
            for done_idx, _ in enumerate(
                pool.map(_process_center_index, range(total), chunksize=64), 1
            ):
                if done_idx % 2000 == 0 or done_idx == total:
                    print(
                        f"Generated {done_idx} / {total} center folders...",
                        flush=True,
                    )
    else:
        for idx in range(total):
            _process_center_index(idx)

    _SHARED_GEN_STATE.clear()

    # Generate thematic collection `index.rst` files and multi-center collection SVGs
    for (start_num, end_num), (c_title, c_summary, c_nums) in sorted(active_collections.items()):
        c_nums_sorted = sorted(c_nums)
        first_num = c_nums_sorted[0]
        last_num = c_nums_sorted[-1]
        coll_folder = get_collection_folder_name(start_num, end_num)
        coll_dir = out_path / coll_folder
        range_label = f"X_{first_num}–X_{last_num}"
        coll_svg_name = f"{coll_folder}.svg"
        coll_svg_path = coll_dir / coll_svg_name

        selected_nums = select_collection_centers(c_nums_sorted, acute_reg, max_points=16)

        coll_svgs_exist = (
            coll_svg_path.is_file()
            and (coll_dir / f"{coll_folder}-right.svg").is_file()
            and (coll_dir / f"{coll_folder}-kepler.svg").is_file()
            and (coll_dir / f"{coll_folder}-kimberling.svg").is_file()
        )
        if (start_num, end_num) == (1, 19):
            if render_graphics and not coll_svgs_exist:
                from .ops import build_symbolic_collection_1_model

                c1_specs = [
                    ("heronian", coll_svg_path, "Heronian (15, 13, 14) | ℚ(√3) | Δ = 84, r = 4, R = 65/8"),
                    ("right", coll_dir / f"{coll_folder}-right.svg", "Right (3, 4, 5) | ℚ(√3) | Δ = 6, r = 1, R = 5/2"),
                    ("kepler", coll_dir / f"{coll_folder}-kepler.svg", "Kepler (1, √φ, φ) | ℚ(φ, √φ, √3) | Δ = √φ / 2"),
                    ("kimberling", coll_dir / f"{coll_folder}-kimberling.svg", "Kimberling (6, 9, 13) | ℚ(√35, √3) | Δ = 3√35"),
                ]
                for p_key, p_svg, p_sub in c1_specs:
                    write_center_svg(
                        build_symbolic_collection_1_model(p_key),
                        p_svg,
                        subtitle=p_sub,
                    )
            if coll_svg_path.is_file() and 'data-triangle="heronian"' in coll_svg_path.read_text(encoding="utf-8")[:512]:
                (coll_dir / "index.rst").write_text(
                    format_symbolic_collection_1_rst(
                        coll_dir,
                        c_title=c_title,
                        c_summary=c_summary,
                        glossary_terms=glossary_terms,
                        valid_centers=valid_centers,
                    ),
                    encoding="utf-8",
                )
                continue

        if render_graphics and not coll_svgs_exist:
            m_acute = build_collection_model(selected_nums, acute_reg, collection_title=c_title, range_label=range_label)
            write_center_svg(m_acute, coll_svg_path, subtitle="(a, b, c) = (5, 6, 7) | AB = 1")
            m_right = build_collection_model(selected_nums, right_reg, collection_title=c_title, range_label=range_label)
            write_center_svg(m_right, coll_dir / f"{coll_folder}-right.svg", subtitle="(a, b, c) = (3, 4, 5) | AB = 1")
            m_kepler = build_collection_model(selected_nums, kepler_reg, collection_title=c_title, range_label=range_label)
            write_center_svg(m_kepler, coll_dir / f"{coll_folder}-kepler.svg", subtitle="(a, b, c) = (1, √φ, φ) | AB = 1")
            m_kimb = build_collection_model(selected_nums, kimb_reg, collection_title=c_title, range_label=range_label)
            write_center_svg(m_kimb, coll_dir / f"{coll_folder}-kimberling.svg", subtitle="(a, b, c) = (6, 9, 13) | AB = 1")

        c_lines: list[str] = [
            f":order: {start_num}",
            ":type: collection",
            f":canonical_id: {range_label}",
            f":subtitle: {c_title}",
            "",
            f".. _{coll_folder}:",
            "",
            range_label,
            "=" * max(4, len(range_label)),
            "",
            f".. rubric:: {c_title}",
            "",
        ]

        seen_terms: set[str] = set()
        seen_persons: set[str] = set()
        seen_cites: set[str] = set()
        enriched_summary = _enrich_text(
            c_summary,
            glossary_terms,
            seen_terms,
            seen_persons,
            seen_cites,
            valid_centers=valid_centers,
        )
        c_lines.append(".. enunciation::")
        c_lines.append("")
        for s_ln in enriched_summary.splitlines():
            c_lines.append(f"   {s_ln}" if s_ln.strip() else "")
        c_lines.append("")

        if coll_svg_path.is_file():
            alt_c = f"{range_label} — {c_title}"
            n_sel = len(selected_nums)
            n_tot = len(c_nums_sorted)
            count_phrase = (
                f"{n_sel} centers"
                if n_sel == n_tot
                else f"{n_sel} representative centers (from {n_tot} in collection)"
            )
            c_lines.append(f".. figure:: {coll_svg_name}")
            c_lines.append(f"   :alt: {alt_c}")
            c_lines.append("   :align: center")
            c_lines.append("")
            c_lines.append(
                f"   **{range_label}** (*{c_title}*) — {count_phrase} constructed on acute reference triangle "
                r":math:`(a, b, c) = (5, 6, 7)` with unit baseline :g:`AB <[ A B ]>` = :math:`1`."
            )
            c_lines.append("")

        # Include any Group Preambles whose anchor center lies in this collection
        if preambles_by_center:
            for n_k in c_nums_sorted:
                p_list = (
                    preambles_by_center.get(f"X_{n_k}")
                    or preambles_by_center.get(f"X({n_k})")
                )
                if not p_list:
                    continue
                for p_item in p_list:
                    parsed_p = parse_preamble(p_item.get("html", ""))
                    p_title = parsed_p["title"] or p_item.get("title", "Preamble")
                    p_title = re.sub(r"\bX\((\d+)\)", r"X_\1", p_title)
                    g_title = p_item.get("guide_title", "")
                    if g_title:
                        g_title_norm = re.sub(r"\bX\((\d+)\)", r"X_\1", g_title)
                        if g_title_norm.lower() not in p_title.lower():
                            p_title = f"{p_title} ({g_title_norm})"
                    p_paras = parsed_p["paragraphs"]
                    p_id = p_item.get("id")
                    if p_id:
                        c_lines.append(f".. _{p_id}:")
                        c_lines.append("")
                    if p_paras:
                        c_lines.append(f".. admonition:: Group Preamble — {p_title}")
                        c_lines.append("   :class: note")
                        c_lines.append("")
                        for para in p_paras:
                            enriched_para = _enrich_text(
                                para,
                                glossary_terms,
                                seen_terms,
                                seen_persons,
                                seen_cites,
                                valid_centers=valid_centers,
                            )
                            for p_ln in enriched_para.splitlines():
                                c_lines.append(f"   {p_ln}" if p_ln.strip() else "")
                            c_lines.append("")

        c_lines.extend(
            [
                ".. collection::",
                "   :sort: order",
                "",
            ]
        )
        (coll_dir / "index.rst").write_text("\n".join(c_lines), encoding="utf-8")

    (out_path / "index.rst").write_text("\n".join(index_lines), encoding="utf-8")


def format_symbolic_collection_1_rst(
    coll_dir: str | Path,
    c_title: str = "Classical & Ancient Centers",
    c_summary: str = (
        "The foundational centers of classical triangle geometry: the incenter, centroid, "
        "circumcenter, orthocenter, nine-point center, symmedian point, Gergonne, Nagel, "
        "Mittenpunkt, Spieker, Feuerbach, Fermat, isodynamic, Napoleon, and Clawson points."
    ),
    glossary_terms: dict[str, Any] | list[str] | None = None,
    valid_centers: set[int] | None = None,
) -> str:
    """Format the exact symbolic Collection 1 (`c-00001-00019/index.rst`) overview page."""
    from .ops import get_center_concordance

    c_path = Path(coll_dir)
    svg_path = c_path / "c-00001-00019.svg"
    range_label = "X_1–X_19"

    lines: list[str] = [
        ":order: 1",
        ":type: collection",
        f":canonical_id: {range_label}",
        f":subtitle: {c_title}",
        "",
        ".. _c-00001-00019:",
        "",
        range_label,
        "=" * len(range_label),
        "",
        f".. rubric:: {c_title}",
        "",
    ]

    enriched_summary = _enrich_text(
        c_summary,
        glossary_terms,
        set(),
        set(),
        set(),
        valid_centers=valid_centers,
    )
    lines.append(".. enunciation::")
    lines.append("")
    for s_ln in enriched_summary.splitlines():
        lines.append(f"   {s_ln}" if s_ln.strip() else "")
    lines.append("")

    lines.extend(
        [
            ".. figure:: c-00001-00019.svg",
            f"   :alt: {range_label} — {c_title}",
            "   :align: center",
            "",
            (
                f"   **{range_label}** (*{c_title}*) — Complete 19-center constellation constructed in exact "
                r"symbolic coordinates on the Heronian reference triangle :math:`(a, b, c) = (15, 13, 14)` over "
                r":math:`\mathbb{Q}(\sqrt{3})` with vertices :g:`A <A>` = :math:`(0, 0)`, :g:`B <B>` = :math:`(14, 0)`, "
                r":g:`C <C>` = :math:`(5, 12)`, area :math:`\Delta = 84`, :g:`incircle <incircle>` (:math:`r = 4`), "
                r":g:`nine-point circle <nine_point_circle>` (:math:`R_9 = \frac{65}{16}`), and "
                r":g:`circumcircle <circumcircle>` (:math:`R = \frac{65}{8}`). Switch tabs above to inspect the full "
                r"constellation on Right :math:`(3, 4, 5)`, Kepler :math:`(1, \sqrt{\phi}, \phi)`, and Kimberling :math:`(6, 9, 13)`."
            ),
            "",
        ]
    )

    def _c_chip(n: int) -> str:
        conc = get_center_concordance(n)
        raw_t = re.sub(r"\s*\(.*?\)", "", conc.title).strip() if conc else f"X_{n}"
        short = raw_t.title()
        if "Harmonic Conjugate" in short:
            short = "Harmonic Feuerbach Point"
        short = short.replace("1St ", "1st ").replace("2Nd ", "2nd ")
        return f":g:`X_{n} <X_{n}>` (:ref:`{short} <X_{n}>`)"

    rat_chips = ", ".join(_c_chip(n) for n in (*range(1, 13), 19))
    eq_chips = ", ".join(_c_chip(n) for n in range(13, 19))

    lines.extend(
        [
            ".. admonition:: Exact Symbolic Constellation",
            "   :class: constructed-elements",
            "",
            (
                "   * **Reference Triangle & Classical Circles:** :g:`ABC << A B C >>` with vertices "
                ":g:`A <A>`, :g:`B <B>`, :g:`C <C>`; sidelines :g:`a <[ B C ]>`, :g:`b <[ C A ]>`, :g:`c <[ A B ]>`; "
                ":g:`circumcircle <circumcircle>` (center :g:`X_3 <X_3>`), :g:`incircle <incircle>` (center :g:`X_1 <X_1>`), "
                "and :g:`nine-point circle <nine_point_circle>` (center :g:`X_5 <X_5>`, internally tangent to the incircle at :g:`X_11 <X_11>`)."
            ),
            (
                "   * **Fundamental Central Axes:** :g:`Euler Line <{ 2, 3 }>` (:g:`X_2 <X_2>`, :g:`X_3 <X_3>`, :g:`X_4 <X_4>`, :g:`X_5 <X_5>`), "
                ":g:`Nagel Line <{ 1, 2 }>` (:g:`X_1 <X_1>`, :g:`X_2 <X_2>`, :g:`X_8 <X_8>`, :g:`X_10 <X_10>`), "
                ":g:`Brocard Axis <{ 3, 6 }>` (:g:`X_3 <X_3>`, :g:`X_6 <X_6>`, :g:`X_15 <X_15>`, :g:`X_16 <X_16>`), and "
                ":g:`Feuerbach Line <{ 1, 5 }>` (:g:`X_1 <X_1>`, :g:`X_5 <X_5>`, :g:`X_11 <X_11>`, :g:`X_12 <X_12>`)."
            ),
            rf"   * **Rational Sub-Constellation over** :math:`\mathbb{{Q}}` **(13 centers):** {rat_chips}.",
            rf"   * **Equilateral Quadratic Extension over** :math:`\mathbb{{Q}}(\sqrt{{3}})` **(6 centers):** {eq_chips}.",
            "",
            ".. seealso::",
            "",
            "   **Companion Topic Guides**: :doc:`Collection 1 Topics: Conjugacies, Central Lines, Circles & Triangles <../../topics/index>` (:math:`T_1`–:math:`T_{24}`)",
            "",
            ".. collection::",
            "   :sort: order",
            "",
        ]
    )

    raw_rst = "\n".join(lines).rstrip() + "\n"
    if svg_path.is_file():
        return _reconcile_g_roles_with_svgs(raw_rst, extract_svg_element_refs(svg_path))
    return raw_rst


def generate_preambles_guide_rst(
    guide_data: dict[str, Any],
    glossary_terms: dict[str, Any] | list[str] | None = None,
    valid_centers: set[int] | None = None,
) -> str:
    """Generate `docsrc/preambles.rst` from Kimberling's `Guide_to_preambles_in_ETC.html`."""
    lines: list[str] = [
        ":navigation: header",
        ":order: 2",
        "",
        ".. _preambles-guide:",
        "",
        "Guide to Preambles in ETC",
        "=========================",
        "",
        ".. rubric:: Prepared by Clark Kimberling (August 2026)",
        "",
        "This Guide catalogs the inter-center group preambles across all 37 Parts of the *Encyclopedia of Triangle Centers* (ETC), providing a searchable index of thematic center families, geometric transformations, contributors, and definitions.",
        "",
    ]

    entries = guide_data.get("entries", [])
    by_part: dict[int, list[dict[str, Any]]] = {}
    for entry in entries:
        by_part.setdefault(int(entry.get("part", 1)), []).append(entry)

    for part_num in sorted(by_part.keys()):
        part_entries = by_part[part_num]
        sec_title = f"Part {part_num}"
        lines.append(f".. _preambles-part-{part_num}:")
        lines.append("")
        lines.append(sec_title)
        lines.append("-" * max(4, len(sec_title)))
        lines.append("")

        for entry in part_entries:
            e_id = entry.get("id", "")
            s_num = int(entry.get("start_num", 0))
            e_num = int(entry.get("end_num", s_num))
            title = entry.get("title", "")
            title_norm = re.sub(r"\bX\((\d+)\)", r"X_\1", title)

            if valid_centers and s_num in valid_centers:
                s_ref = f":ref:`X_{s_num} <X_{s_num}>`"
            else:
                s_ref = f"**X_{s_num}**"

            if e_num != s_num:
                if valid_centers and e_num in valid_centers:
                    e_ref = f":ref:`X_{e_num} <X_{e_num}>`"
                else:
                    e_ref = f"**X_{e_num}**"
                range_str = f"{s_ref}–{e_ref}"
            else:
                range_str = s_ref

            if e_id:
                lines.append(f".. _{e_id}:")
                lines.append("")

            if title_norm and not re.match(r"^(?:Centers|Points)\s+X_", title_norm, re.IGNORECASE):
                lines.append(f"* {range_str} — **{title_norm}**")
            else:
                lines.append(f"* {range_str}")

            body_html = entry.get("html", "")
            if body_html:
                parsed_b = parse_preamble(body_html)
                seen_terms: set[str] = set()
                seen_persons: set[str] = set()
                seen_cites: set[str] = set()
                for para in parsed_b.get("paragraphs", []):
                    enriched_p = _enrich_text(
                        para,
                        glossary_terms,
                        seen_terms,
                        seen_persons,
                        seen_cites,
                        valid_centers=valid_centers,
                    )
                    lines.append("")
                    for p_ln in enriched_p.splitlines():
                        lines.append(f"  {p_ln}" if p_ln.strip() else "")
            lines.append("")

    return "\n".join(lines)





