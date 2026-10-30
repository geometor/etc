"""Semantic HTML parser for Encyclopedia of Triangle Centers (ETC) entries and preambles."""

from __future__ import annotations

import re
from typing import Any

from .glossary import (
    clean_html_entities,
    convert_inline_html_to_rst,
    formula_html_to_latex,
    wrap_geom_refs,
)


def remove_tags(text: str) -> str:
    """Remove HTML tags from text."""
    return re.sub(r"<[^>]+>", "", text)


def clean_text(text: str) -> str:
    """Clean up inline HTML text into single-line RST-safe text."""
    if not text:
        return ""
    return convert_inline_html_to_rst(text)


def _format_where_clause(clause_html: str) -> str:
    """Format a trailing `where ...` clause, wrapping algebraic definitions in `:math:`."""
    s = clause_html.strip().lstrip(",").strip()
    if not s:
        return ""

    # Match equations `LHS = RHS` inside the where-clause and convert algebraic ones to :math:
    def _repl_eq(m: re.Match) -> str:
        lhs = m.group(1).strip()
        rhs = m.group(2).strip()
        trail = ""
        while rhs and rhs[-1] in ".,;":
            trail = rhs[-1] + trail
            rhs = rhs[:-1].rstrip()
        plain_rhs = clean_html_entities(remove_tags(rhs)).strip()
        eng_words = [
            w
            for w in re.findall(r"[A-Za-z]{4,}", plain_rhs)
            if w.lower()
            not in {
                "sqrt",
                "area",
                "sin",
                "cos",
                "tan",
                "cot",
                "sec",
                "csc",
            }
        ]
        if eng_words or re.search(r"\bX[\(\[]\d+[\)\]]", plain_rhs):
            return m.group(0)
        ltx = formula_html_to_latex(f"{lhs} = {rhs}")
        if not ltx:
            return m.group(0)
        return f":math:`{ltx}`{trail}"

    s_math = re.sub(
        r"(?<![A-Za-z0-9_])([A-Za-z0-9_'′″<sub></sup>]+(?:\([^()]*\))?)\s*=\s*((?:[^,;()]|\([^()]*\))+?)(?=(?:\s*[,;]\s*|\s+and\s+|\s+for\s+|$))",
        _repl_eq,
        s,
    )
    # Stash any `:math:` spans we just created before calling convert_inline_html_to_rst
    stashed: list[str] = []

    def _stash_m(m: re.Match) -> str:
        idx = len(stashed)
        stashed.append(m.group(0))
        return f"@@WMATH{idx}@@"

    s_stashed = re.sub(r":math:`[^`]+`", _stash_m, s_math)
    rst = convert_inline_html_to_rst(s_stashed)
    for idx, val in enumerate(stashed):
        rst = rst.replace(f"@@WMATH{idx}@@", val)
    return rst


def format_coordinate_line(coord_html: str) -> str:
    """Format a single coordinate line (possibly with a trailing ', where ...' clause) into RST."""
    raw = re.sub(r"^\s*[:=]\s*", "", clean_html_entities(coord_html).strip()).strip()
    if not raw:
        return ""

    # Separate trailing parenthetical author/date or cf. attribution
    attr_rst = ""
    attr_match = re.match(
        r"^(.+?)\s*,?\s*(\((?:[A-Z][A-Za-z0-9.\s,'/-]+(?:\d{4}|\d{1,2}/\d{1,2}/\d{2,4})|cf\.?\b)[^()]*\))\s*$",
        raw,
        flags=re.DOTALL,
    )
    if attr_match:
        raw = attr_match.group(1).strip()
        attr_rst = f" {convert_inline_html_to_rst(attr_match.group(2).strip())}"

    # Check if there is a prose clause after the coordinate ratio (e.g., ", where ...")
    clause_match = re.match(
        r"^(.+?)\s*(?:,\s*|\s+)((?:where\b|[A-Za-z0-9_'′″]+\s+as\s+(?:in|at)\b).*)$",
        raw,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if clause_match:
        formula_part = clause_match.group(1).strip().rstrip(",;")
        clause_part = clause_match.group(2).strip()
        clause_rst = f", {_format_where_clause(clause_part)}"
    else:
        formula_part = raw.rstrip(",;")
        clause_rst = ""

    plain_formula = clean_html_entities(remove_tags(formula_part)).strip()

    # Check if formula_part is actually an English prose description (e.g., "square of semi-minor axis of A-Soddy ellipse : :")
    # or contains X(n) references
    english_words = [
        w
        for w in re.findall(r"[A-Za-z]{4,}", plain_formula)
        if w.lower()
        not in {"sqrt", "area", "cos", "sin", "tan", "cot", "sec", "csc", "where"}
    ]
    has_x_ref = bool(re.search(r"\bX[\(\[]\d+[\)\]]", plain_formula))

    if len(english_words) >= 2 or has_x_ref:
        return f"{convert_inline_html_to_rst(raw)}{attr_rst}"

    latex_str = formula_html_to_latex(formula_part)
    if not latex_str:
        return f"{convert_inline_html_to_rst(raw)}{attr_rst}"
    return f":math:`{latex_str}`{clause_rst}{attr_rst}"


_COMB_TARGET_RE = re.compile(
    r"(X[\(\[]\d+[\)\]]|\[[ABC]\]|(?<![A-Za-z0-9_])[IJONMHTP][abc](?![A-Za-z0-9_]))"
)


def _format_comb_coeff_html(coeff_html: str) -> str:
    """Format an algebraic coefficient or divisor in a linear combination into `:math:`."""
    c = coeff_html.strip()
    if not c:
        return ""
    # Strip leading/trailing multiplication `*`
    c = re.sub(r"^\*\s*|\s*\*$", "", c).strip()
    if not c:
        return ""
    plain_c = clean_html_entities(remove_tags(c)).strip()
    if not plain_c:
        return ""
    # If it contains English words (like "is the midpoint of"), fall back to inline RST
    eng = [
        w
        for w in re.findall(r"[A-Za-z]{4,}", plain_c)
        if w.lower()
        not in {"sqrt", "area", "sin", "cos", "tan", "cot", "sec", "csc"}
    ]
    if eng:
        return convert_inline_html_to_rst(c)
    ltx = formula_html_to_latex(c)
    if not ltx:
        return convert_inline_html_to_rst(c)
    return f":math:`{ltx}`"


def format_combination_line(comb_html: str) -> str:
    """Format a linear combination line (e.g., `X(6) = (r^2 + s^2 + 2rR)*X(2) - 2r^2*X(3)`) into RST."""
    raw = clean_html_entities(comb_html).strip()
    if not raw:
        return ""

    # Separate trailing parenthetical author/date attribution
    attr_rst = ""
    attr_match = re.match(
        r"^(.+?)\s*,?\s*(\((?:[A-Z][A-Za-z0-9.\s,'/-]+(?:\d{4}|\d{1,2}/\d{1,2}/\d{2,4})|cf\.?\b)[^()]*\))\s*$",
        raw,
        flags=re.DOTALL,
    )
    if attr_match:
        raw = attr_match.group(1).strip()
        attr_rst = f" {convert_inline_html_to_rst(attr_match.group(2).strip())}"

    # Separate trailing `, where ...` or `; ...` clause
    clause_rst = ""
    clause_match = re.match(
        r"^(.+?)\s*(?:,\s*where\b|;\s*)(.*)$",
        raw,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if clause_match:
        sep_is_where = "where" in raw[clause_match.start(1) + len(clause_match.group(1)) : clause_match.start(2)].lower()
        raw = clause_match.group(1).strip()
        rest = clause_match.group(2).strip()
        if sep_is_where:
            clause_rst = f", {_format_where_clause('where ' + rest)}"
        else:
            clause_rst = f"; {convert_inline_html_to_rst(rest)}"

    # Check if there is a trailing ratio like `, 2:1` or `, 1 : 2`
    ratio_rst = ""
    ratio_match = re.match(
        r"^(.+?)\s*,\s*([0-9a-zA-Z_+\-*/^()<sub></sup>\s]+:[0-9a-zA-Z_+\-*/^()<sub></sup>\s]+)\s*$",
        raw,
        flags=re.DOTALL,
    )
    if ratio_match and "=" in ratio_match.group(1):
        raw = ratio_match.group(1).strip()
        r_ltx = formula_html_to_latex(ratio_match.group(2).strip())
        if r_ltx:
            ratio_rst = f", :math:`{r_ltx}`"

    parts = _COMB_TARGET_RE.split(raw)
    if len(parts) < 3 or "=" not in raw:
        return f"{convert_inline_html_to_rst(raw)}{ratio_rst}{clause_rst}{attr_rst}"

    out: list[str] = []
    idx = 0
    while idx < len(parts):
        if idx % 2 == 1:
            # Target point token: X(n), [A], Ja, etc.
            tok = parts[idx]
            if tok.startswith("[") and tok.endswith("]"):
                v = tok[1:-1]
                out.append(f":g:`{v} <{v}>`")
            elif re.match(r"^[IJONMHTP][abc]$", tok):
                out.append(f":g:`{tok[0]}_{{{tok[1]}}} <{tok[0]}_{tok[1]}>`")
            else:
                out.append(tok)
            idx += 1
            continue

        sep = parts[idx]
        if not sep.strip():
            idx += 1
            continue

        # Check if sep starts with `/ divisor` for the preceding target point
        div_m = re.match(
            r"^\s*/\s*(\([^()]+\)|[A-Za-z0-9_'′″]+(?:\s*(?:<sup>[^<]+</sup>|<sub>[^<]+</sub>))*)(.*)$",
            sep,
            flags=re.DOTALL,
        )
        if div_m and idx > 0:
            div_rst = _format_comb_coeff_html(div_m.group(1))
            out.append(f" / {div_rst}")
            sep = div_m.group(2)

        if not sep.strip():
            idx += 1
            continue

        # Now sep should be an operator (`=`, `+`, `-`, `,`) optionally followed by a coefficient for the next target point
        op_m = re.match(r"^\s*([=+\-,])\s*(.*)$", sep, flags=re.DOTALL)
        if op_m:
            op, rem = op_m.group(1), op_m.group(2).strip()
            out.append(f" {op} " if op != "," else ", ")
            if rem:
                coeff_rst = _format_comb_coeff_html(rem)
                if coeff_rst:
                    out.append(f"{coeff_rst} ")
        else:
            coeff_rst = _format_comb_coeff_html(sep)
            if coeff_rst:
                out.append(f"{coeff_rst} ")
        idx += 1

    res = " ".join("".join(out).split()).strip()
    return f"{res}{ratio_rst}{clause_rst}{attr_rst}"


def parse_h3(html_content: str) -> dict[str, Any] | None:
    """Parse the <h3> tag to extract key, num, title, aliases, and named HTML anchor."""
    match = re.search(r"<h3([^>]*)>(.*?)</h3>", html_content, re.DOTALL | re.IGNORECASE)
    if not match:
        return None

    h3_attrs, h3_inner = match.group(1), match.group(2)

    # Look for named anchor <a id="Incenter"> or <a name="Incenter"> inside <h3> or immediately after </h3>
    anchor_id = None
    after_h3 = html_content[match.end() : match.end() + 200]
    for search_zone in (h3_inner, after_h3):
        a_m = re.search(
            r'<a\s+(?:id|name)=["\']?([^"\'\s>]+)["\']?\s*>\s*</a>',
            search_zone,
            re.IGNORECASE,
        )
        if a_m:
            anchor_id = a_m.group(1).strip()
            break

    clean_h3 = " ".join(clean_html_entities(remove_tags(h3_inner)).split()).strip()
    key_match = re.search(r"X\((\d+)\)", clean_h3)
    if not key_match:
        return None

    num = int(key_match.group(1))
    key = f"X({num})"

    title = re.sub(
        r"^(?:X[\(\[]\d+[\)\]]\s*=\s*)+", "", clean_h3, flags=re.IGNORECASE
    ).strip()
    if not title or title == clean_h3:
        title = re.sub(
            r"^X[\(\[]\d+[\)\]]\s*", "", clean_h3, flags=re.IGNORECASE
        ).strip()
    if not title:
        title = clean_h3

    # Extract parenthetical aliases at the end of the title if present, e.g.
    # "SYMMEDIAN POINT (LEMOINE POINT, GREBE POINT)" -> primary="SYMMEDIAN POINT", aliases=["LEMOINE POINT", "GREBE POINT"]
    aliases: list[str] = []
    alias_m = re.match(r"^([A-Za-z0-9\s\-\']{4,}?)\s+\(([^()]+(?:POINT|CENTER)[^()]*)\)\s*$", title)
    if alias_m and not alias_m.group(1).strip().upper().endswith(("SIMILICENTER", "CONJUGATE", "PERSPECTOR")):
        primary_title = alias_m.group(1).strip()
        aliases = [a.strip() for a in alias_m.group(2).split(",") if a.strip()]
    else:
        primary_title = title

    return {
        "key": key,
        "num": num,
        "title": title,
        "primary_title": primary_title,
        "aliases": aliases,
        "anchor_id": anchor_id,
        "h3_end": match.end(),
    }


def _parse_header_block(header_html: str) -> dict[str, list[str]]:
    """Parse coordinates (Trilinears, Barycentrics, Tripolars), combinations, and header notes."""
    trilinears: list[str] = []
    barycentrics: list[str] = []
    tripolars: list[str] = []
    combinations: list[str] = []
    extra_notes: list[str] = []

    # 1. Extract <b>...</b> blocks in the header (linear combinations / combos)
    def _extract_b(match: re.Match) -> str:
        b_inner = match.group(1)
        for line in re.split(r"<br\s*/?>", b_inner, flags=re.IGNORECASE):
            raw_ln = line.strip()
            if not raw_ln:
                continue
            plain_ln = clean_html_entities(remove_tags(raw_ln)).strip()
            if not plain_ln:
                continue
            # Merge standalone parenthetical attribution onto previous combination
            if combinations and re.match(r"^\([A-Z][^()]+\)\.?$", plain_ln):
                combinations[-1] = f"{combinations[-1]} {convert_inline_html_to_rst(raw_ln)}"
            else:
                formatted_c = format_combination_line(raw_ln)
                if formatted_c:
                    combinations.append(formatted_c)
        return ""

    coord_zone = re.sub(
        r"<b\b[^>]*>(.*?)</b>", _extract_b, header_html, flags=re.DOTALL | re.IGNORECASE
    )

    # Strip empty <a id="..."></a> anchors
    coord_zone = re.sub(
        r"<a\b[^>]*>\s*</a>", "", coord_zone, flags=re.DOTALL | re.IGNORECASE
    )

    # 2. Split remaining coordinate zone on <br> and group continuation lines
    raw_lines = re.split(r"<br\s*/?>", coord_zone, flags=re.IGNORECASE)
    current_list: list[str] | None = None

    coord_prefix_re = re.compile(
        r"^\s*(Trilinears?|Barycentrics?|Tripolars?)\b\s*:?\s*(.+)$",
        re.DOTALL | re.IGNORECASE,
    )

    for raw_ln in raw_lines:
        ln_strip = raw_ln.strip()
        if not ln_strip:
            continue
        plain_check = " ".join(clean_html_entities(remove_tags(ln_strip)).split()).strip()
        if not plain_check:
            continue

        m = coord_prefix_re.match(ln_strip)
        if m:
            ctype = m.group(1).lower()
            expr = m.group(2).strip()
            if ctype.startswith("trilinear"):
                current_list = trilinears
            elif ctype.startswith("barycentric"):
                current_list = barycentrics
            else:
                current_list = tripolars
            current_list.append(expr)
        elif re.match(r"^=\s*", plain_check) and current_list is not None:
            # Alternate coordinate line starting with `=`
            alt_expr = re.sub(r"^\s*=\s*", "", ln_strip).strip()
            if alt_expr:
                current_list.append(alt_expr)
        elif (
            re.match(r"^X[\(\[]\d+[\)\]]\s*=", plain_check)
            and len(re.findall(r"X[\(\[]\d+[\)\]]", plain_check)) >= 2
        ):
            # Unbolded linear combination in the header
            formatted_c = format_combination_line(ln_strip)
            if formatted_c:
                combinations.append(formatted_c)
            current_list = None
        elif re.match(
            r"^(?:Let\s+|As\s+a\s+point\b|For\s+a\b|X[\(\[]\d+[\)\]]\s+is\b)",
            plain_check,
        ):
            # Narrative note placed inside the header before the first <p>
            cleaned_n = _strip_software_and_nav_refs(convert_inline_html_to_rst(ln_strip))
            if cleaned_n:
                extra_notes.append(cleaned_n)
            current_list = None
        else:
            # Continuation line (e.g., "where f(a,b,c) = ...")
            if current_list:
                prev_c = current_list[-1].rstrip()
                if prev_c.endswith((",", ";")) or re.search(
                    r"\bwhere\s*$", prev_c, flags=re.IGNORECASE
                ):
                    current_list[-1] = f"{prev_c} {ln_strip}"
                else:
                    current_list[-1] = f"{prev_c}, {ln_strip}"

    return {
        "trilinears": [format_coordinate_line(c) for c in trilinears if c.strip()],
        "barycentrics": [format_coordinate_line(c) for c in barycentrics if c.strip()],
        "tripolars": [format_coordinate_line(c) for c in tripolars if c.strip()],
        "combinations": combinations,
        "extra_notes": extra_notes,
    }


def _parse_incidence_block(raw_block: str, center_num: int) -> dict[str, Any]:
    """Parse an 'X(n) lies on ...' paragraph into structured curves, line pairs, and RST."""
    cleaned = convert_inline_html_to_rst(raw_block)

    # Extract line pairs after "these lines:", "this line:", "the following lines:", etc.
    lines_pairs: list[tuple[int, int]] = []
    curves_text = cleaned
    lines_split = re.split(
        r"\b(?:(?:and|as\s+well\s+as)\s+)?(?:on\s+)?(?:these|this|the\s+following)\s+(?:\(?parallel\)?\s+)?lines?\s*:\s*",
        cleaned,
        maxsplit=1,
        flags=re.IGNORECASE,
    )
    if len(lines_split) == 2:
        curves_prefix = lines_split[0].strip().rstrip(",")
        curves_prefix = re.sub(
            r"^\s*X[\(\[]\d+[\)\]]\s+lies(?:\s+on)?\s*$",
            "",
            curves_prefix,
            flags=re.IGNORECASE,
        ).strip()
        pairs_zone = lines_split[1].strip()
        for pm in re.finditer(r"\{?\s*(\d+)\s*,\s*(\d+)\s*\}?", pairs_zone):
            lines_pairs.append((int(pm.group(1)), int(pm.group(2))))
        curves_text = curves_prefix

    return {
        "raw_rst": cleaned,
        "curves_prefix": curves_text,
        "lines": lines_pairs,
    }


def _parse_relations_block(raw_block: str) -> list[str]:
    """Split an 'X(n) = ...' paragraph on <br> (or newline before 'X(n) =') and join tuple continuation lines."""
    lines = re.split(
        r"<br\s*/?>|\n(?=\s*X[\(\[]\d+[\)\]]\s*=)",
        raw_block,
        flags=re.IGNORECASE,
    )
    relations: list[str] = []

    for ln in lines:
        cleaned = convert_inline_html_to_rst(ln)
        if not cleaned:
            continue
        # If line starts with a tuple like "(1,7)" or "{1,7}" and previous line ended with ":", join it
        if relations and (
            relations[-1].endswith(":")
            or re.match(r"^[\(\{]\s*\d+\s*,", cleaned)
        ):
            relations[-1] = f"{relations[-1]} {cleaned}"
        else:
            relations.append(cleaned)

    return relations


def _strip_software_and_nav_refs(text: str) -> str:
    """Remove GeoGebra, Geometer's Sketchpad, and dead top-of-page navigation references."""
    if not text:
        return ""
    s = text
    # 1. Remove inline "; if you have GeoGebra, see Figure..." clauses
    s = re.sub(
        r";?\s*if\s+you\s+have\s+(?:GeoGebra|(?:The\s+)?Geometer'?s\s+Sketchpad)\s*,\s*see\s+[^.;\n]+",
        "",
        s,
        flags=re.IGNORECASE,
    )
    # 2. Remove sentences starting with "If you have (The) Geometer's Sketchpad..." or "If you have GeoGebra..."
    # Note: filenames contain ".gsp" / ".ggb", so only stop at a period followed by whitespace or end-of-line.
    s = re.sub(
        r"\bIf\s+you\s+have\s+(?:(?:The\s+)?Geometer'?s\s+Sketchpad|GeoGebra)\b(?:(?!\.(?:\s+[A-Z]|\s*$))[^\n])*(?:\.(?=\s+[A-Z]|\s*$)|\s*$)",
        "",
        s,
        flags=re.IGNORECASE,
    )
    # 2b. Remove "For access to a sketch of ..., see X(n)."
    s = re.sub(
        r"\bFor\s+access\s+to\s+a\s+sketch\s+of\b[^.\n]*\.?",
        "",
        s,
        flags=re.IGNORECASE,
    )
    # 3. Clean up follow-on sentence "These sketches include the ..." -> "The ..."
    s = re.sub(
        r"\bThese\s+sketches\s+include\s+the\b",
        "The",
        s,
        flags=re.IGNORECASE,
    )
    s = re.sub(
        r"\bThese\s+sketches\s+include\b",
        "See also",
        s,
        flags=re.IGNORECASE,
    )
    # 4. Remove dead "For a list of other harmonic conjugates of X(n), click Tables at the top of this page."
    s = re.sub(
        r"\s*For\s+a\s+list\s+of\s+other\s+harmonic\s+conjugates\s+of\s+X\(\d+\),\s*click\s+(?:\*\*Tables\*\*|Tables)\s+at\s+the\s+top\s+of\s+this\s+page\.?",
        "",
        s,
        flags=re.IGNORECASE,
    )
    # 5. Drop standalone .gsp / .ggb link lines
    if re.match(
        r"^\s*(?:\*\*[^*\n]+\*\*|`[^`\n]+`__)\s*(?:\(``[^`\n]*\.(?:gsp|ggb)``\))?[.,;]?\s*$",
        s,
        flags=re.IGNORECASE,
    ):
        return ""
    return " ".join(s.split()).strip()


def _format_single_note_lines(note_lines: list[str]) -> str:
    """Format <br>-separated lines within a single note paragraph into cohesive RST."""
    # Filter out multi-line Sketchpad/GeoGebra sketch lists
    filtered: list[str] = []
    skipping_sketches = False
    for ln in note_lines:
        if re.match(
            r"^\s*If\s+you\s+have\s+(?:(?:The\s+)?Geometer'?s\s+Sketchpad|GeoGebra)\b.*:\s*$",
            ln,
            flags=re.IGNORECASE,
        ):
            skipping_sketches = True
            continue
        if skipping_sketches:
            if (
                re.search(r"\.(?:gsp|ggb)\b|Sketchpad|GeoGebra", ln, flags=re.IGNORECASE)
                or ln.strip().startswith("**")
            ):
                continue
            skipping_sketches = False
        cleaned_ln = _strip_software_and_nav_refs(ln)
        if cleaned_ln:
            filtered.append(cleaned_ln)

    if not filtered:
        return ""

    # If the final line is a standalone parenthetical attribution "(Author, Date)", merge onto previous line
    if (
        len(filtered) >= 2
        and re.match(r"^\([A-Z][^()]+\)\.?$", filtered[-1].strip())
    ):
        attr = filtered.pop().strip()
        filtered[-1] = f"{filtered[-1].rstrip()} {attr}"

    if len(filtered) == 1:
        return filtered[0]

    # If line 0 introduces definitions ("... let", "...:", etc.) and middle lines are definitions
    first = filtered[0]
    if re.search(r"(?:\blet|\bwhere|\bas|\bfollows|[:;,])\s*$", first, flags=re.IGNORECASE):
        if len(filtered) >= 3 and re.match(
            r"^(?:The|Then|These|This|Each|Every|Hence|Thus|Moreover|Furthermore|Claim|Between|In\s+particular|X\(\d+\))\b",
            filtered[-1],
        ):
            steps = "\n".join(f"   * {ln}" for ln in filtered[1:-1])
            return f"{first}\n\n{steps}\n\n{filtered[-1]}"
        steps = "\n".join(f"   * {ln}" for ln in filtered[1:])
        return f"{first}\n\n{steps}"

    # Check if all lines are labeled properties like "Equation: ...", "Center: ..."
    if all(re.match(r"^[A-Z][A-Za-z\s()-]{1,35}:\s+", ln) for ln in filtered):
        return "\n".join(f"* {ln}" for ln in filtered)

    return "\n\n".join(filtered)


def _group_logical_notes(raw_notes: list[str]) -> list[str]:
    """Group multi-paragraph continuation notes (formulas, circle lists, attributions) into cohesive notes."""
    grouped: list[str] = []

    incomplete_end_re = re.compile(
        r"(?:[:;,=]|\b(?:defined\s+by|given\s+by|namely|as\s+follows|follows|let|where|with|by|is|are|equal\s+to|such\s+that|for\s+which))\s*$",
        re.IGNORECASE,
    )
    circle_item_re = re.compile(r"^\((\d+)\s*;\s*(.+)\)\.?$")
    standalone_attr_re = re.compile(r"^\([A-Z][^()]+\)\.?$")
    lower_cont_re = re.compile(
        r"^(?:and|or|where|then|which|that|with|for|having|satisfying|is|are|cyclic\s+sum)\b"
    )

    for note in raw_notes:
        note_s = note.strip()
        if not note_s:
            continue

        if not grouped:
            grouped.append(note_s)
            continue

        prev = grouped[-1].rstrip()
        prev_last_line = prev.splitlines()[-1].strip()
        prev_incomplete = bool(incomplete_end_re.search(prev_last_line)) and not bool(
            re.search(r"\([A-Z][^()]+\d{4}[^()]*\)\.?$", prev_last_line)
        )

        # 1. Standalone parenthetical attribution "(Author, Date)"
        if standalone_attr_re.match(note_s):
            grouped[-1] = f"{prev} {note_s}"
            continue

        # 2. Circle-list item "(187; Schoute circle, 15, 16)"
        cm = circle_item_re.match(note_s)
        if cm:
            c_idx = cm.group(1)
            rest = cm.group(2).rstrip(")")
            # Format center index as X(c_idx) so wrap_refs links it
            bullet_line = f"   * (X({c_idx}); {rest})"
            if prev.splitlines()[-1].startswith("   * ("):
                grouped[-1] = f"{prev}\n{bullet_line}"
            else:
                grouped[-1] = f"{prev}\n\n{bullet_line}"
            continue

        # 3. Concluding sentence after a circle list
        if re.match(
            r"^(?:This\s+list\s+of\s+circles|Related\s+circles\s+are\s+discussed)\b",
            note_s,
            flags=re.IGNORECASE,
        ):
            grouped[-1] = f"{prev}\n\n{note_s}"
            continue

        # 4. Formula or lowercase continuation
        is_formula_cont = bool(
            re.match(r"^(?:[\(\[-]|[a-zA-Z0-9_]+(?:\\?\s*:sup:|[\^\*\+\-\/]))", note_s)
            or (": :" in note_s and not re.match(r"^[A-Z][a-z]{2,}\b", note_s))
            or ("= 0" in note_s and not re.match(r"^[A-Z][a-z]{2,}\b", note_s))
        )
        is_lower_cont = bool(lower_cont_re.match(note_s)) and note_s[0].islower()

        if prev_incomplete or is_formula_cont or is_lower_cont:
            if is_formula_cont and not is_lower_cont and "\n" not in note_s:
                grouped[-1] = f"{prev}\n\n   {note_s}"
            else:
                grouped[-1] = f"{prev}\n\n{note_s}"
            continue

        grouped.append(note_s)

    return grouped


def parse_center(html_content: str) -> dict[str, Any] | None:
    """Parse a center's HTML content into a rich structured dictionary."""
    h3_info = parse_h3(html_content)
    if not h3_info:
        return None

    key = h3_info["key"]
    num = h3_info["num"]
    after_h3 = html_content[h3_info["h3_end"] :]

    # Split at the first <p\b, <ul\b, <ol\b, <table\b, <blockquote\b, or <hr\b
    body_start_m = re.search(
        r"<(?:p|ul|ol|table|blockquote|hr)\b", after_h3, flags=re.IGNORECASE
    )
    if body_start_m:
        header_html = after_h3[: body_start_m.start()]
        body_html = after_h3[body_start_m.start() :]
    else:
        header_html = after_h3
        body_html = ""

    header_data = _parse_header_block(header_html)
    combinations = list(header_data["combinations"])

    # Strip HTML comments and trailing <hr> from body_html
    body_html = re.sub(r"<!--.*?-->", "", body_html, flags=re.DOTALL)
    body_html = re.sub(r"<hr\b[^>]*>", "", body_html, flags=re.IGNORECASE)

    # Extract any <p class="bold">, <p style="font-weight: bold">, or <p><b>X(n) = ...</b> blocks as combinations
    def _extract_bold_p(match: re.Match) -> str:
        inner = match.group(1)
        for ln in re.split(r"<br\s*/?>", inner, flags=re.IGNORECASE):
            raw_ln = ln.strip()
            if not raw_ln:
                continue
            plain_ln = clean_html_entities(remove_tags(raw_ln)).strip()
            if not plain_ln:
                continue
            if combinations and re.match(r"^\([A-Z][^()]+\)\.?$", plain_ln):
                combinations[-1] = f"{combinations[-1]} {convert_inline_html_to_rst(raw_ln)}"
            else:
                c_ln = format_combination_line(raw_ln)
                if c_ln:
                    combinations.append(c_ln)
        return ""

    body_html = re.sub(
        r'<p\s+(?:class=["\']?bold["\']?|style=["\'][^"\']*font-weight:\s*bold[^"\']*["\'])[^>]*>(.*?)</p>',
        _extract_bold_p,
        body_html,
        flags=re.DOTALL | re.IGNORECASE,
    )
    body_html = re.sub(
        r"<b>\s*(X[\(\[]\d+[\)\]]\s*=[^<]*?[+-]\s*\d*\s*X[\(\[]\d+[\)\]][^<]*?)</b>",
        _extract_bold_p,
        body_html,
        flags=re.DOTALL | re.IGNORECASE,
    )

    # Split remaining body by any <p...> or </p> tag, AND split where <br> precedes "X(n) =" or "X(n) lies on"
    body_html = re.sub(
        r"<br\s*/?>\s*(?=(?:<b>\s*)?X[\(\[]\d+[\)\]]\s*(?:=|lies\s+on\b))",
        "</p><p>",
        body_html,
        flags=re.IGNORECASE,
    )
    raw_segments = re.split(r"</?p(?:\s+[^>]*)?>", body_html, flags=re.IGNORECASE)

    raw_notes: list[str] = list(header_data.get("extra_notes", []))
    incidences: list[dict[str, Any]] = []
    relations: list[str] = []

    lies_on_re = re.compile(
        r"^\s*X[\(\[]\d+[\)\]]\s+lies\s+on\b", re.DOTALL | re.IGNORECASE
    )
    relation_re = re.compile(
        r"^\s*X[\(\[]\d+[\)\]]\s*=", re.DOTALL | re.IGNORECASE
    )
    coord_seg_re = re.compile(
        r"^\s*(?:Trilinears?|Barycentrics?|Tripolars?)\b",
        re.DOTALL | re.IGNORECASE,
    )

    for seg in raw_segments:
        seg_s = seg.strip()
        if not seg_s:
            continue
        plain_seg = clean_html_entities(remove_tags(seg_s)).strip()
        if not plain_seg:
            continue

        if coord_seg_re.match(plain_seg):
            extra_hdr = _parse_header_block(seg_s)
            header_data["trilinears"].extend(extra_hdr["trilinears"])
            header_data["barycentrics"].extend(extra_hdr["barycentrics"])
            header_data["tripolars"].extend(extra_hdr["tripolars"])
            combinations.extend(extra_hdr["combinations"])
            raw_notes.extend(extra_hdr.get("extra_notes", []))
        elif lies_on_re.match(plain_seg):
            incidences.append(_parse_incidence_block(seg_s, num))
        elif relation_re.match(plain_seg):
            relations.extend(_parse_relations_block(seg_s))
        else:
            # Narrative / construction note paragraph
            br_parts = [
                convert_inline_html_to_rst(bp)
                for bp in re.split(r"<br\s*/?>", seg_s, flags=re.IGNORECASE)
            ]
            br_parts = [bp for bp in br_parts if bp]
            if not br_parts:
                continue
            note_lines: list[str] = []
            for bp in br_parts:
                if re.match(r"^X[\(\[]\d+[\)\]]\s*=", bp):
                    relations.append(bp)
                else:
                    note_lines.append(bp)
            formatted_note = _format_single_note_lines(note_lines)
            if formatted_note:
                raw_notes.append(formatted_note)

    notes = _group_logical_notes(raw_notes)

    # Collect all referenced center numbers (dependencies) across all fields
    dep_nums: set[int] = set()
    all_text_blobs = (
        [h3_info["title"]]
        + header_data["trilinears"]
        + header_data["barycentrics"]
        + header_data["tripolars"]
        + combinations
        + notes
        + relations
        + [inc["raw_rst"] for inc in incidences]
    )
    for blob in all_text_blobs:
        for xm in re.finditer(r"\bX[\(\[](\d+)[\)\]]", blob):
            dep_nums.add(int(xm.group(1)))
    for inc in incidences:
        for i_num, j_num in inc["lines"]:
            dep_nums.add(i_num)
            dep_nums.add(j_num)
    for rel in relations:
        if "for these" in rel.lower():
            for tm in re.finditer(r"[\(\{]\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*(\d+))?\s*[\)\}]", rel):
                dep_nums.add(int(tm.group(1)))
                dep_nums.add(int(tm.group(2)))
                if tm.group(3):
                    dep_nums.add(int(tm.group(3)))

    dep_nums.discard(num)
    dependencies = [f"X({d})" for d in sorted(dep_nums)]

    return {
        "key": key,
        "num": num,
        "title": h3_info["title"],
        "primary_title": h3_info["primary_title"],
        "aliases": h3_info["aliases"],
        "anchor_id": h3_info["anchor_id"],
        "trilinears": header_data["trilinears"],
        "barycentrics": header_data["barycentrics"],
        "tripolars": header_data["tripolars"],
        "combinations": combinations,
        "notes": notes,
        "incidences": incidences,
        "relations": relations,
        "dependencies": dependencies,
    }


def parse_preamble(preamble_html: str) -> dict[str, Any]:
    """Parse an inter-center preamble HTML block into a title and list of RST paragraphs."""
    title_m = re.search(
        r'<p[^>]*class=["\']?preamble-title["\']?[^>]*>(.*?)</p>',
        preamble_html,
        re.DOTALL | re.IGNORECASE,
    )
    title = (
        " ".join(clean_html_entities(remove_tags(title_m.group(1))).split()).strip(" ,")
        if title_m
        else "Preamble"
    )

    # Extract inside <div class="preamble-sect">...</div> if present
    sect_m = re.search(
        r'<div[^>]*class=["\']?preamble-sect["\']?[^>]*>(.*)',
        preamble_html,
        re.DOTALL | re.IGNORECASE,
    )
    body = sect_m.group(1) if sect_m else preamble_html
    body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
    body = re.sub(r"<hr\b[^>]*>.*", "", body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r"</div>\s*$", "", body, flags=re.IGNORECASE)

    segments = re.split(r"</?p(?:\s+[^>]*)?>", body, flags=re.IGNORECASE)
    paragraphs: list[str] = []
    for seg in segments:
        seg_s = seg.strip()
        if not seg_s:
            continue
        br_lines = [
            convert_inline_html_to_rst(ln)
            for ln in re.split(r"<br\s*/?>", seg_s, flags=re.IGNORECASE)
        ]
        br_lines = [ln for ln in br_lines if ln]
        if len(br_lines) == 1:
            paragraphs.append(br_lines[0])
        elif len(br_lines) > 1:
            paragraphs.append("\n".join(f"| {ln}" for ln in br_lines))

    return {
        "title": title,
        "paragraphs": paragraphs,
    }
