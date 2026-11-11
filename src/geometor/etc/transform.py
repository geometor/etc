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
    "< M_a M_b M_c >": ("Medial Triangle", "medial triangle"),
    "< H_a H_b H_c >": ("Orthic Triangle", "orthic triangle"),
    "< T_a T_b T_c >": ("Intouch (Contact) Triangle", "intouch triangle"),
    "< N_a N_b N_c >": ("Extouch Triangle", "extouch triangle"),
    "< I_a I_b I_c >": ("Incentral Triangle", "incentral triangle"),
    "< J_a J_b J_c >": ("Excentral Triangle", "excentral triangle"),
    "< K_a K_b K_c >": ("Anticomplementary Triangle", "anticomplementary triangle"),
    "< Tan_a Tan_b Tan_c >": ("Tangential Triangle", "tangential triangle"),
    "< Sym_a Sym_b Sym_c >": ("Symmedial Triangle", "symmedial triangle"),
    "< Eu_a Eu_b Eu_c >": ("Euler (Feuerbach) Triangle", "euler triangle"),
    "< Ref_a Ref_b Ref_c >": ("Reflection Triangle", "reflection triangle"),
    "< Cm_a Cm_b Cm_c >": ("Circummedial Triangle", "circummedial triangle"),
    "< H'_a H'_b H'_c >": ("Orthic-of-Orthic Triangle", "orthic triangle"),
    "< O_A O_B O_C >": ("Kosnita Triangle", "kosnita triangle"),
    "< Nap_a Nap_b Nap_c >": ("Outer Napoleon Triangle", "outer napoleon triangle"),
    "< Nap'_a Nap'_b Nap'_c >": ("Inner Napoleon Triangle", "inner napoleon triangle"),
    "< P_a P_b P_c >": ("Cevian Triangle", "cevian triangle"),
}

_CIRCLE_TERM_SLUGS: dict[str, tuple[str, str]] = {
    "circumcircle": ("Circumcircle", "circumcircle"),
    "incircle": ("Incircle", "incircle"),
    "nine_point_circle": ("Nine-Point Circle", "nine-point circle"),
    "spieker_circle": ("Spieker Circle", "spieker circle"),
    "bevan_circle": ("Bevan Circle", "bevan circle"),
}

_CONCURRENCE_KIND_LABELS: dict[str, str] = {
    "Cevian": " (Cevians)",
    "Median": " (Medians)",
    "Altitude": " (Altitudes)",
    "Angle": " (Angle Bisectors)",
    "Symmedian": " (Symmedians)",
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
    covered_guide_pts: set[str] = {"R_a", "R_b"}
    equil_polys = [
        el for el in elements
        if el["type"] == "polygon" and el["ID"] in {"< B C A' >", "< C A B' >", "< A B C' >"}
    ]
    if len(equil_polys) == 3:
        covered_guide_pts.update({"A'", "B'", "C'"})
        bullets.append(
            "* **Equilateral Side Triangles:** "
            ":g:`△BCA' << B C A' >>`, :g:`△CAB' << C A B' >>`, :g:`△ABC' << A B C' >>` "
            "erected on sidelines with apexes :g:`A' <A'>`, :g:`B' <B'>`, :g:`C' <C'>`"
        )

    for el in elements:
        if el["type"] != "polygon" or "incident" in el["classes"]:
            continue
        pid = el["ID"]
        if pid in {"< A B C >", "< B C A' >", "< C A B' >", "< A B C' >"}:
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

    # 2. Auxiliary Guide Points not already part of a drawn polygon (e.g. M_a..c in X(3)/X(5), H_a..c in X(5), I_a..c in X(1))
    rem_guides = [
        el["ID"] for el in elements
        if el["type"] == "point" and el["guide"] and "incident" not in el["classes"] and el["ID"] not in covered_guide_pts
    ]
    if rem_guides:
        groups: list[tuple[str, list[str], str]] = [
            ("M_", ["M_a", "M_b", "M_c"], "Side midpoints of :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`"),
            ("H_", ["H_a", "H_b", "H_c"], "Altitude feet on :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, :g:`AB <[ A B ]>`"),
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
    for el in elements:
        if el["type"] != "circle" or el["guide"] or "incident" in el["classes"]:
            continue
        cid = el["ID"]
        c_info = _KNOWN_CIRCLE_INFO.get(cid)
        c_desc = c_info[1] if c_info else f"Centered at {el.get('center', '')}"
        if cid in _CIRCLE_TERM_SLUGS:
            c_lbl, c_slug = _CIRCLE_TERM_SLUGS[cid]
            c_head = f":term:`{c_lbl} <{c_slug}>` (:g:`{cid} <{cid}>`)"
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
            e_tag = " (:term:`Euler line <euler line>`)" if is_euler else ""
            central_lines.append(f":g:`{{{i_n}, {j_n}}} <{lid}>`{e_tag}")
        else:
            inner_l = lid[2:-2].strip() if lid.startswith("[") and lid.endswith("]") else lid
            pts_l = inner_l.split()
            disp_l = f"{pts_l[0]}–{pts_l[1]}" if len(pts_l) == 2 else lid
            concur_lines.append(f":g:`{disp_l} <{lid}>`")

    if concur_lines:
        l_first = next(
            (el["ID"] for el in elements if el["type"] == "line" and el["ID"] not in {"[ A B ]", "[ B C ]", "[ C A ]"} and not el["ID"].startswith("{")),
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
    1: (
        ":doc:`T_1: Isogonal Conjugate <../../../topics/isogonal-conjugate/index>` • "
        ":doc:`T_2: Isotomic Conjugate <../../../topics/isotomic-conjugate/index>` • "
        ":doc:`T_3: Complement & Anticomplement <../../../topics/complement-and-anticomplement/index>` • "
        ":doc:`T_4: Harmonic Conjugate & Cross-Ratio <../../../topics/harmonic-conjugate/index>` • "
        ":doc:`T_5: Circle Inversion <../../../topics/circle-inversion/index>` • "
        ":doc:`T_7: The Nagel Line <../../../topics/nagel-line/index>` • "
        ":doc:`T_9: The Feuerbach Line <../../../topics/feuerbach-line/index>` • "
        ":doc:`T_10: The OI Line (Incenter–Circumcenter Axis) <../../../topics/oi-line/index>` • "
        ":doc:`T_11: The Soddy Line <../../../topics/soddy-line/index>` • "
        ":doc:`T_12: The Fuhrmann & Spieker Central Lines <../../../topics/fuhrmann-and-spieker-lines/index>` • "
        ":doc:`T_14: The Incircle & Excircles <../../../topics/incircle-and-excircles/index>` • "
        ":doc:`T_16: The Nine-Point (Feuerbach) Circle <../../../topics/nine-point-circle/index>` • "
        ":doc:`T_17: The Spieker Circle <../../../topics/spieker-circle/index>` • "
        ":doc:`T_20: Medial & Anticomplementary Triangles <../../../topics/medial-and-anticomplementary-triangles/index>` • "
        ":doc:`T_22: Intouch (Contact) & Extouch Triangles <../../../topics/intouch-and-extouch-triangles/index>` • "
        ":doc:`T_23: Incentral & Excentral Triangles <../../../topics/incentral-and-excentral-triangles/index>`"
    ),
}


def _format_four_triangle_table_rst(num: int) -> list[str]:
    """Build the 4-Triangle Exact Symbolic Coordinate & Invariant RST table for ``X_num``."""
    from .symbolic_cache import CenterSymbolicRegistry, format_symbolic_latex
    from .triangles import CANONICAL_TRIANGLES

    tri_specs = [
        ("heronian", r"**Heronian** :math:`(15, 13, 14)`", r":math:`\mathbb{Q}`"),
        ("right", r"**Right** :math:`(3, 4, 5)`", r":math:`\mathbb{Q}`"),
        ("kepler", r"**Kepler** :math:`(1, \sqrt{\phi}, \phi)`", r":math:`\mathbb{Q}(\sqrt{\phi})`"),
        ("kimberling", r"**Kimberling** :math:`(6, 9, 13)`", r":math:`\mathbb{Q}(\sqrt{35})`"),
    ]
    dist_col = (
        r"Inradius & Quadrance :math:`(r,\, Q_r)`"
        if num == 1
        else r"Shortest Trilinear :math:`(d_{\min},\, Q)`"
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
    for t_key, t_label, f_latex in tri_specs:
        tri = CANONICAL_TRIANGLES[t_key]
        rec = CenterSymbolicRegistry(tri).get(num)
        if rec is None:
            continue
        kp = rec.is_kepler
        sa_parts = [format_symbolic_latex(sa, kepler_phi=kp) for sa in rec.sub_areas]
        sa_ltx = rf"\left({sa_parts[0]},\; {sa_parts[1]},\; {sa_parts[2]}\right)"
        d_val = tri.r if num == 1 else rec.search_value
        q_val = tri.simplify(d_val * d_val)
        d_ltx = format_symbolic_latex(d_val, kepler_phi=kp)
        q_ltx = format_symbolic_latex(q_val, kepler_phi=kp)
        if num == 1:
            dq_cell = rf":math:`r = {d_ltx},\; Q_r = {q_ltx}`"
        else:
            dq_cell = rf":math:`{d_ltx}\; (Q = {q_ltx})`"
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
    """Format the Unified 5-Act Visual & Symbolic Dossier (`index.rst`) for centers with a 5-act plate suite."""
    from .ops import get_center_concordance
    from .symbolic_cache import CenterSymbolicRegistry
    from .triangles import CANONICAL_TRIANGLES

    key = data["key"]
    title = data.get("title", "")
    num = int(data.get("num") or re.sub(r"[^0-9]", "", key) or 0)
    if num > 0:
        key = f"X_{num}"

    concordance = get_center_concordance(num)
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
        lines.append(f".. figure:: {figure_uri}")
        lines.append(f"   :alt: {alt_title}")
        lines.append("   :align: center")
        lines.append("")
        lines.append(
            f"   {cap_title} constructed in exact rational coordinates on the Heronian reference triangle "
            r":math:`(a, b, c) = (15, 13, 14)` over :math:`\mathbb{Q}` with vertices :g:`A <A>` = :math:`(0, 0)`, "
            r":g:`B <B>` = :math:`(14, 0)`, :g:`C <C>` = :math:`(5, 12)`, area :math:`\Delta = 84`, and inradius :math:`r = 4`. "
            r"Switch tabs above to inspect exact constructions on Right :math:`(3, 4, 5)`, Kepler :math:`(1, \sqrt{\phi}, \phi)`, "
            r"and Kimberling :math:`(6, 9, 13)`."
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
                r":math:`(\alpha, \beta, \gamma)` and shaded barycentric sub-triangles :math:`(\Delta_a, \Delta_b, \Delta_c)`."
            ),
            "",
        ]
    )
    if num == 1:
        lines.extend(
            [
                (
                    r"* **Trilinear Coordinates** (:math:`\alpha : \beta : \gamma = 1 : 1 : 1`): Dropping orthogonal perpendiculars "
                    r":g:`X_1T_a </ X_1 T_a />`, :g:`X_1T_b </ X_1 T_b />`, and :g:`X_1T_c </ X_1 T_c />` from :g:`X_1 <X_1>` "
                    r"to sidelines :g:`BC <[ B C ]>`, :g:`CA <[ C A ]>`, and :g:`AB <[ A B ]>` meets the sides at right-spread "
                    r"touchpoints :g:`T_a <T_a>` = :math:`\left(\frac{46}{5}, \frac{32}{5}\right)`, :g:`T_b <T_b>` = :math:`\left(\frac{30}{13}, \frac{72}{13}\right)`, "
                    r"and :g:`T_c <T_c>` = :math:`(6, 0)`. Every strut equals the exact inradius :math:`r = 4` (quadrance :math:`Q_r = 16`), "
                    r"realizing :math:`4 : 4 : 4 = 1 : 1 : 1`."
                ),
                (
                    r"* **Barycentric Coordinates** (:math:`u : v : w = a : b : c`): Joining :g:`X_1 <X_1>` to the vertices along "
                    r":g:`X_1A </ X_1 A />`, :g:`X_1B </ X_1 B />`, and :g:`X_1C </ X_1 C />` partitions :math:`\triangle ABC` into "
                    r"three sub-triangles :g:`△X_1BC << X_1 B C >>`, :g:`△X_1CA << X_1 C A >>`, and :g:`△X_1AB << X_1 A B >>`. "
                    r"Sharing common altitude :math:`r = 4`, their exact signed areas on :math:`(15, 13, 14)` are "
                    r":math:`\Delta_a = \frac{1}{2}(15)(4) = 30`, :math:`\Delta_b = \frac{1}{2}(13)(4) = 26`, and "
                    r":math:`\Delta_c = \frac{1}{2}(14)(4) = 28` (:math:`30 + 26 + 28 = 84 = \Delta`), in exact ratio "
                    r":math:`30 : 26 : 28 = 15 : 13 : 14 = a : b : c`."
                ),
                "",
            ]
        )

    lines.extend(_format_four_triangle_table_rst(num))

    has_coords = any(data.get(k) for k in ("trilinears", "barycentrics", "tripolars"))
    alt_coord_bullets: list[str] = []
    if has_coords or approx_search > 1e-12:
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
        elif approx_search > 1e-12:
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
    if (entry_dir / "03_central_lines.svg").is_file():
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
        if num == 1:
            lines.extend(
                [
                    r"* **Nagel Line** :g:`{1, 2, 8, 10} <{ 2, 8 }>` — collinear axis of :g:`X_1 <X_1>`, :ref:`X_2 <X_2>` (*Centroid*, :math:`(\frac{19}{3}, 4)`), :ref:`X_10 <X_10>` (*Spieker Center*, :math:`(\frac{13}{2}, 4)`), and :ref:`X_8 <X_8>` (*Nagel Point*, :math:`(7, 4)`). On :math:`(15, 13, 14)`, its exact equation is :math:`y - 4 = 0` (spread :math:`0`, **parallel to baseline** :g:`AB <[ A B ]>`).",
                    r"* **Feuerbach Line** :g:`{1, 5, 11} <{ 5, 11 }>` — collinear axis of :g:`X_1 <X_1>`, :ref:`X_5 <X_5>` (*Nine-Point Center*, :math:`(6, \frac{63}{16})`), and :ref:`X_11 <X_11>` (*Feuerbach Point*, :math:`(6, 8)`). On :math:`(15, 13, 14)`, its exact equation is :math:`x - 6 = 0` (spread :math:`1`, **perpendicular to baseline** :g:`AB <[ A B ]>` and orthogonal to the Nagel line).",
                    r"* **OI Line (Incenter–Circumcenter Axis)** :g:`{1, 3, 40} <{ 3, 40 }>` — joins :g:`X_1 <X_1>`, :ref:`X_3 <X_3>` (*Circumcenter*, :math:`(7, \frac{33}{8})`), and :ref:`X_40 <X_40>` (*Bevan Point*, :math:`(8, \frac{17}{4})`), with exact equation :math:`x - 8y + 26 = 0` (spread :math:`\frac{1}{65}`).",
                    r"* **Incenter–Symmedian Line** :g:`{1, 6, 9} <{ 6, 9 }>` — joins :g:`X_1 <X_1>`, :ref:`X_6 <X_6>` (*Symmedian Point*, :math:`(\frac{1673}{295}, \frac{1176}{295})`), and :ref:`X_9 <X_9>` (*Mittenpunkt*, :math:`(\frac{973}{146}, \frac{294}{73})`), with exact equation :math:`4x - 97y + 364 = 0` (spread :math:`\frac{16}{9425}`).",
                    r"* **Soddy Line** :g:`{1, 7, 20} <{ 7, 20 }>` — joins :g:`X_1 <X_1>`, :ref:`X_7 <X_7>` (*Gergonne Point*, :math:`(\frac{414}{73}, \frac{288}{73})`), and :ref:`X_20 <X_20>` (*de Longchamps Point*, :math:`(9, \frac{9}{2})`), with exact equation :math:`x - 6y + 18 = 0` (spread :math:`\frac{1}{37}`).",
                    "",
                ]
            )

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
    if (entry_dir / "04_relations.svg").is_file():
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
        if num == 1:
            lines.extend(
                [
                    r"* **Self-Isogonal Fixed Point:** :g:`X_1 <X_1>` is its own :term:`isogonal conjugate <isogonal-conjugate>` (:math:`1^{-1} : 1^{-1} : 1^{-1} = 1 : 1 : 1`), acting as the identity element of trilinear multiplication.",
                    r"* **Isotomic Conjugate:** :g:`X_75 <X_75>` (:ref:`X_75 <X_75>`, homogeneous barycentrics :math:`bc : ca : ab = 182 : 210 : 195`) at exact rational coordinates :math:`\left(\frac{3915}{587}, \frac{2340}{587}\right)`, joined along :g:`{1, 75} <{ 1, 75 }>`.",
                    r"* **Anticomplement of Spieker Center:** :g:`X_1 <X_1>` is the :term:`anticomplement <anticomplement>` of :g:`X_10 <X_10>` (:ref:`Spieker Center <X_10>`, :math:`\left(\frac{13}{2}, 4\right)`), dilated from homothetic center :g:`X_2 <X_2>` (:ref:`Centroid <X_2>`, :math:`\left(\frac{19}{3}, 4\right)`) by factor :math:`-2` along :g:`{1, 10} <{ 1, 10 }>`.",
                    r"* **Complement of Nagel Point:** :g:`X_1 <X_1>` is the :term:`complement <complement>` of :g:`X_8 <X_8>` (:ref:`Nagel Point <X_8>`, :math:`(7, 4)`), dilated from :g:`X_2 <X_2>` by factor :math:`-\frac{1}{2}` along :g:`{1, 8} <{ 1, 8 }>`; equivalently, :g:`X_10 <X_10>` is the exact midpoint of :g:`X_1 <X_1>` and :g:`X_8 <X_8>`.",
                    r"* **Circumcircle Inverse:** Inversion in :g:`circumcircle <circumcircle>` centered at :g:`X_3 <X_3>` = :math:`\left(7, \frac{33}{8}\right)` (:math:`R^2 = \frac{4225}{64}`) maps :g:`X_1 <X_1>` along the :g:`OI axis <{ 1, 3 }>` (:math:`Q(X_1, X_3) = \frac{65}{64}`, scale :math:`R^2 / Q = 65`) to :ref:`X_36 <X_36>` at exact integer coordinates :math:`(-58, -4)`.",
                    "",
                ]
            )

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
        if num == 1:
            lines.extend(
                [
                    (
                        r"Across all four number fields — rational :math:`\mathbb{Q}` on :g:`Heronian (15, 13, 14) <heronian-X_1>` "
                        r"(:math:`X_1 = (6, 4)`, :g:`r = 4 <heronian-incircle>`) and Pythagorean :g:`Right (3, 4, 5) <right-X_1>` "
                        r"(:math:`X_1 = (3, 1)`, :g:`r = 1 <right-incircle>`), golden quadratic tower :math:`\mathbb{Q}(\sqrt{\phi})` on "
                        r":g:`Kepler (1, √φ, φ) <kepler-X_1>`, and quadratic :math:`\mathbb{Q}(\sqrt{35})` on "
                        r":g:`Kimberling (6, 9, 13) <kimberling-X_1>` (:g:`r = 2\sqrt{35}/7 <kimberling-incircle>`) — "
                        r"**X_1** remains strictly interior, equidistant from all three sidelines (:math:`1 : 1 : 1`), and partitions "
                        r"the triangle area in exact proportion :math:`a : b : c`."
                    ),
                    "",
                ]
            )

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

    return "\n".join(lines).rstrip() + "\n"


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
    num = data.get("num")
    if num and num > 0:
        key = f"X_{num}"
    title = data.get("title", "")
    alt_title = f"{key} — {title}" if title and title != key else key
    cap_title = f"**{key}** (*{title}*)" if title and title != key else f"**{key}**"

    is_heronian = False
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
        num=data.get("num"),
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
        if is_heronian:
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

    return "\n".join(lines).rstrip() + "\n"


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





