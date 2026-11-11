"""Central color assignment strategy and registry for GEOMETOR ETC diagrams and videos."""

from __future__ import annotations

import re

# 10-token high-contrast dark-mode palette:
# token -> (stroke_hex, badge_bg_rgba, badge_border_rgba)
PALETTE_TOKENS: dict[str, tuple[str, str, str]] = {
    "gold": ("#e8b85a", "rgba(232, 184, 90, 0.14)", "rgba(232, 184, 90, 0.55)"),
    "orange": ("#fb923c", "rgba(251, 146, 60, 0.14)", "rgba(251, 146, 60, 0.58)"),
    "teal": ("#2dd4bf", "rgba(45, 212, 191, 0.14)", "rgba(45, 212, 191, 0.58)"),
    "blue": ("#38bdf8", "rgba(56, 189, 248, 0.14)", "rgba(56, 189, 248, 0.58)"),
    "purple": ("#a78bfa", "rgba(167, 139, 250, 0.14)", "rgba(167, 139, 250, 0.58)"),
    "orchid": ("#e879f9", "rgba(232, 121, 249, 0.14)", "rgba(232, 121, 249, 0.58)"),
    "pink": ("#f472b6", "rgba(244, 114, 182, 0.14)", "rgba(244, 114, 182, 0.58)"),
    "green": ("#4ade80", "rgba(74, 222, 128, 0.14)", "rgba(74, 222, 128, 0.58)"),
    "lime": ("#a3e635", "rgba(163, 230, 53, 0.14)", "rgba(163, 230, 53, 0.58)"),
    "muted": ("#94a3b8", "rgba(148, 163, 184, 0.10)", "rgba(148, 163, 184, 0.32)"),
}

LINE_COLOR_RING: tuple[str, ...] = (
    "orange",
    "teal",
    "blue",
    "purple",
    "orchid",
    "pink",
    "green",
    "lime",
)

PARTNER_COLOR_RING: tuple[str, ...] = (
    "blue",
    "green",
    "orange",
    "purple",
    "teal",
    "pink",
    "lime",
)

REFERENCE_TRIANGLE_COLORS: dict[str, str] = {
    "heronian": "gold",
    "acute": "gold",
    "right": "blue",
    "kepler": "green",
    "kimberling": "purple",
}

NAMED_CIRCLE_COLORS: dict[str, str] = {
    "incircle": "pink",
    "circumcircle": "blue",
    "nine_point_circle": "teal",
    "nine-point circle": "teal",
    "spieker_circle": "orange",
    "spieker circle": "orange",
    "excircle": "purple",
    "excircle_a": "purple",
    "excircle_b": "purple",
    "excircle_c": "purple",
    "fuhrmann_circle": "lime",
    "fuhrmann circle": "lime",
    "brocard_circle": "purple",
    "brocard circle": "purple",
    "apollonian_circle": "green",
    "secondary_circle": "orange",
}

# Canonical named lines: (display_name, known_centers_frozenset, token)
CANONICAL_CENTRAL_LINES: tuple[tuple[str, frozenset[int], str], ...] = (
    ("Euler Line", frozenset({2, 3, 4, 5, 20, 30}), "gold"),
    ("Nagel Line", frozenset({1, 2, 8, 10}), "orange"),
    ("Feuerbach Line", frozenset({1, 5, 11, 12}), "teal"),
    ("OI Line", frozenset({1, 3, 40, 55, 56}), "blue"),
    ("Brocard Axis", frozenset({3, 6, 15, 16, 32}), "purple"),
    ("Soddy Line", frozenset({1, 7, 20, 175, 176}), "orchid"),
    ("Incenter–Symmedian Line", frozenset({1, 6, 9, 37}), "pink"),
    ("Centroid–Gergonne Line", frozenset({2, 7, 9}), "green"),
    ("Gergonne–Nagel Line", frozenset({7, 8, 65}), "lime"),
    ("Orthocenter–Spieker Line", frozenset({4, 9, 10, 19}), "blue"),
    ("Fuhrmann Line", frozenset({4, 8, 72}), "pink"),
    ("Symmedian–Isogonic Line", frozenset({6, 13, 14}), "green"),
    ("Symmedian–Napoleon Line", frozenset({6, 17, 18}), "blue"),
    ("Nine-Point–Fermat Line", frozenset({5, 13, 18}), "orange"),
    ("Nine-Point–2nd Isogonic Line", frozenset({5, 14, 17}), "purple"),
    ("Circumcenter–1st Napoleon Line", frozenset({3, 13, 17}), "green"),
    ("Circumcenter–2nd Napoleon Line", frozenset({3, 14, 18}), "orange"),
    ("Centroid–2nd Isodynamic Line", frozenset({2, 13, 16}), "pink"),
    ("Centroid–1st Isodynamic Line", frozenset({2, 14, 15}), "teal"),
    ("Orthocenter–1st Napoleon Line", frozenset({4, 15, 17}), "teal"),
    ("Orthocenter–2nd Napoleon Line", frozenset({4, 16, 18}), "orchid"),
    ("Symmedian–Clawson Line", frozenset({6, 19, 25}), "orange"),
    ("Incenter–Clawson Line", frozenset({1, 19, 28}), "pink"),
    ("Centroid–Feuerbach Line", frozenset({2, 11, 55}), "blue"),
    ("Orthocenter–Feuerbach Line", frozenset({4, 11, 56}), "green"),
    ("Centroid–X_12 Line", frozenset({2, 12, 56}), "purple"),
    ("Orthocenter–X_12 Line", frozenset({4, 12, 55}), "orange"),
)


def token_hex(token: str) -> str:
    """Return the primary hex color for a semantic palette token."""
    return PALETTE_TOKENS.get(token, PALETTE_TOKENS["gold"])[0]


def get_circle_color_token(circle_id_or_name: str, classes: list[str] | None = None) -> str:
    """Return the canonical color token for a named circle."""
    low = (circle_id_or_name or "").strip().lower().replace("-", "_")
    if low in NAMED_CIRCLE_COLORS:
        return NAMED_CIRCLE_COLORS[low]
    for cls in classes or []:
        c_low = cls.strip().lower().replace("-", "_")
        if c_low in NAMED_CIRCLE_COLORS:
            return NAMED_CIRCLE_COLORS[c_low]
    for key, tok in NAMED_CIRCLE_COLORS.items():
        if key in low:
            return tok
    return "pink"


def get_central_line_color_token(
    centers_or_id: str | list[int] | set[int],
    line_name: str = "",
    used_tokens: set[str] | None = None,
) -> str:
    """Return the canonical color token for a central line given its center indices or `{a, b, ...}` ID."""
    if isinstance(centers_or_id, str):
        nums = sorted({int(x) for x in re.findall(r"\d+", centers_or_id)})
    else:
        nums = sorted({int(x) for x in centers_or_id})

    num_set = frozenset(nums)
    if len(num_set) >= 2:
        for _, known_set, tok in CANONICAL_CENTRAL_LINES:
            if num_set <= known_set:
                if used_tokens is not None:
                    used_tokens.add(tok)
                return tok

    if line_name:
        ln_low = line_name.strip().lower()
        for canon_name, _, tok in CANONICAL_CENTRAL_LINES:
            if canon_name.lower() in ln_low or ln_low in canon_name.lower():
                if used_tokens is not None:
                    used_tokens.add(tok)
                return tok

    # Deterministic Golden-Ratio step fallback for general central lines {i, j, ...}
    if len(nums) >= 2:
        idx = (nums[0] * 3 + nums[1] * 5) % len(LINE_COLOR_RING)
    elif len(nums) == 1:
        idx = (nums[0] * 5) % len(LINE_COLOR_RING)
    else:
        idx = 0

    for offset in range(len(LINE_COLOR_RING)):
        cand = LINE_COLOR_RING[(idx + offset) % len(LINE_COLOR_RING)]
        if used_tokens is None or cand not in used_tokens:
            if used_tokens is not None:
                used_tokens.add(cand)
            return cand

    tok = LINE_COLOR_RING[idx]
    if used_tokens is not None:
        used_tokens.add(tok)
    return tok
