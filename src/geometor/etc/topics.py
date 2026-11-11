"""Topic Video and Documentation Generator for GEOMETOR ETC Collection 1 (X_1–X_19).

Covers every major geometric transformation, named central line, named circle, and
classical derived triangle encountered across Collection 1 (X_1 through X_19),
coordinating text token colors (`g-tok` gold, `coincide-tok` sky-blue, `eq-tok` green)
with solid/dotted geometric elements in the SVG stage.
"""

from __future__ import annotations

import html
import math
import re
from pathlib import Path
from typing import Any

from geometor.model import Model

from .construct import (
    CenterRegistry,
    TriangleContext,
    _add_circle,
    _add_line,
    _add_point,
    _add_polygon,
)
from .render import render_model_svg
from .video import _mute_other_spans, generate_four_triangles_svg

# ---------------------------------------------------------------------------
# Topic Catalog for Collection 1 (X_1–X_19)
# ---------------------------------------------------------------------------

COLLECTION_1_TOPICS: list[dict[str, Any]] = [
    # =========================================================================
    # I. TRANSFORMATIONS & CONJUGACIES (T_1 – T_5)
    # =========================================================================
    {
        "num": 1,
        "code": "T_1",
        "slug": "isogonal-conjugate",
        "category": "Transformations & Conjugacies",
        "title": "Isogonal Conjugate",
        "short_title": "ISOGONAL CONJUGATE",
        "enunciation": "The reflection of concurrent cevians across the interior angle bisectors of triangle ABC, inverting trilinear coordinates α : β : γ ↦ 1/α : 1/β : 1/γ.",
        "primary_center": 6,
        "centers": [1, 2, 6, 3, 4, 13, 15],
        "pairs": [(2, 6), (3, 4), (13, 15)],
        "lines": [(2, 6), (3, 4), (13, 15)],
        "circles": ["incircle", "circumcircle"],
        "triangles": ["medial"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Isogonal Conjugate is the fundamental angular reflection of triangle geometry. <pause> Reflecting the three cevians of a point P across the interior angle bisectors A X one, B X one, and C X one <pause> yields three new concurrent lines meeting at its isogonal conjugate P star.

[bell:construction]
In homogeneous trilinear coordinates, <pause> isogonal conjugation simply takes the reciprocal of each distance: <pause> alpha, beta, gamma maps to one over alpha, <pause> one over beta, <pause> one over gamma. <pause> Across Collection One, <pause> the Incenter X one is self-isogonal. <pause> The Centroid X two and Symmedian Point X six are isogonal conjugates, <pause> transforming medians into symmedians. <pause> And the Circumcenter X three and Orthocenter X four are isogonal conjugates, <pause> reflecting perpendicular bisectors into altitudes.

[bell:insight]
Even the equilateral centers obey isogonal duality: <pause> the First and Second Fermat points X thirteen and X fourteen <pause> map directly to the First and Second Isodynamic points X fifteen and X sixteen.
""",
        "s1": (
            "P = α : β : γ  ⟷  P* = 1/α : 1/β : 1/γ",
            '<span class="clause-line"><b>Isogonal Conjugacy:</b> Reflecting the cevians of <span class="g-tok">X_2</span> across the angle bisectors through <span class="g-tok">X_1</span> produces the symmedians concurring at <span class="coincide-tok">X_6</span>, while <span class="eq-tok">incircle</span> and <span class="eq-tok">circumcircle</span> anchor the metric duality.</span>',
            "CEVIAN REFLECTION • ∠ACP = ∠BCP*",
            "Isogonal lines make equal angles with the interior angle bisectors at vertices A, B, and C.",
        ),
        "s2": (
            "(X_2, X_6) • (X_3, X_4) • (X_13, X_15)",
            '<span class="clause-line"><b>Reciprocal Trilinears:</b> <span class="g-tok">α : β : γ</span> maps to <span class="coincide-tok">1/α : 1/β : 1/γ</span> and barycentrics <span class="g-tok">u : v : w</span> map to <span class="eq-tok">a²/u : b²/v : c²/w</span>.</span>',
            "ALGEBRAIC INVOLUTION",
            "Points on the circumcircle map to the line at infinity; the sidelines of △ABC are singular.",
        ),
        "s3": (
            "Classic Isogonal Pairs in Collection 1",
            '<span class="clause-line"><b>Collection 1 Action:</b> Medians and symmedians pair <span class="g-tok">{2, 6}</span>, circumcenter and orthocenter pair <span class="coincide-tok">{3, 4}</span>, and Fermat and Isodynamic centers pair <span class="eq-tok">{13, 15}</span>.</span>',
            "ISOGONAL PAIRS",
            "Self-isogonal fixed points are the incenter X_1 and the three excenters I_a, I_b, I_c.",
        ),
        "s4": (
            "X_1 Fixed • X_2 ↔ X_6 • X_3 ↔ X_4 • X_13 ↔ X_15",
            '<span class="clause-line"><b>Conjugate Network:</b> <span class="g-tok">X_1</span> is fixed; <span class="coincide-tok">X_2</span> conjugates with <span class="coincide-tok">X_6</span>; <span class="eq-tok">X_3</span> conjugates with <span class="eq-tok">X_4</span>; and <span class="g-tok">X_13</span> conjugates with <span class="g-tok">X_15</span>.</span>',
            "GLOBAL DUALITY",
            "Also pairs Gergonne X_7 ↔ X_55, Nagel X_8 ↔ X_57, and Napoleon X_17 ↔ X_18.",
        ),
    },
    {
        "num": 2,
        "code": "T_2",
        "slug": "isotomic-conjugate",
        "category": "Transformations & Conjugacies",
        "title": "Isotomic Conjugate",
        "short_title": "ISOTOMIC CONJUGATE",
        "enunciation": "The reflection of concurrent cevians across the side midpoints of triangle ABC, inverting barycentric coordinates u : v : w ↦ 1/u : 1/v : 1/w.",
        "primary_center": 7,
        "centers": [2, 7, 8, 1, 4],
        "pairs": [(7, 8)],
        "lines": [(1, 7, 8), (2, 7), (2, 8)],
        "circles": ["incircle"],
        "triangles": ["medial", "intouch"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Isotomic Conjugate is the affine counterpart of isogonal conjugation. <pause> Reflecting each cevian foot of a point P across the midpoint of its side <pause> produces three new concurrent cevians meeting at the isotomic conjugate Paggers.

[bell:construction]
Because isotomic reflection acts purely on segment ratios along the sidelines, <pause> it inverts homogeneous barycentric coordinates: <pause> u, v, w maps to one over u, <pause> one over v, <pause> one over w. <pause> The Centroid X two is the unique interior fixed point of isotomic conjugation.

[bell:insight]
In Collection One, <pause> the Gergonne Point X seven and the Nagel Point X eight form the flagship isotomic pair: <pause> because the incircle and excircle touch points are symmetric about the side midpoints, <pause> X seven and X eight are exact isotomic conjugates.
""",
        "s1": (
            "P = u : v : w  ⟷  P† = 1/u : 1/v : 1/w",
            '<span class="clause-line"><b>Isotomic Conjugacy:</b> Reflecting cevian feet across the side midpoints of the <span class="coincide-tok">medial triangle M_a M_b M_c</span> fixes the centroid <span class="g-tok">X_2</span> and swaps touch-point cevians of the <span class="eq-tok">incircle</span>.</span>',
            "MIDPOINT SYMMETRY • BD = CE",
            "By Ceva's theorem, reflecting cevian feet across M_a, M_b, M_c preserves concurrence.",
        ),
        "s2": (
            "Barycentrics u : v : w ↦ 1/u : 1/v : 1/w",
            '<span class="clause-line"><b>Reciprocal Barycentrics:</b> Sub-area weights <span class="g-tok">u : v : w</span> invert to <span class="coincide-tok">1/u : 1/v : 1/w</span> while trilinears map to <span class="eq-tok">(bc α)⁻¹ : (ca β)⁻¹ : (ab γ)⁻¹</span>.</span>',
            "AFFINE INVOLUTION",
            "Isotomic conjugation commutes with every affine transformation of triangle ABC.",
        ),
        "s3": (
            "Gergonne–Nagel Isotomic Axis {7, 8}",
            '<span class="clause-line"><b>Collection 1 Action:</b> The Soddy line <span class="g-tok">{1, 7, 8}</span> and centroid axes <span class="coincide-tok">{2, 7}</span> and <span class="eq-tok">{2, 8}</span> frame the Gergonne–Nagel isotomic pair.</span>',
            "TOUCH-POINT SYMMETRY",
            "Incircle and excircle tangency points lie at distance s − b and s − c from opposite vertices.",
        ),
        "s4": (
            "X_2 Self-Isotomic • X_7 ↔ X_8",
            '<span class="clause-line"><b>Conjugate Network:</b> <span class="g-tok">X_2</span> is self-isotomic, while Gergonne point <span class="coincide-tok">X_7</span> and Nagel point <span class="eq-tok">X_8</span> are mutual isotomic conjugates.</span>',
            "ISOTOMIC PAIRS",
            "Also pairs Incenter X_1 ↔ X_75 (isotomic conjugate of incenter) and Orthocenter X_4 ↔ X_69.",
        ),
    },
    {
        "num": 3,
        "code": "T_3",
        "slug": "complement-and-anticomplement",
        "category": "Transformations & Conjugacies",
        "title": "Complement & Anticomplement",
        "short_title": "COMPLEMENT & ANTICOMPLEMENT",
        "enunciation": "Homothety centered at the Centroid X_2 with ratio −1/2 (complement) and ratio −2 (anticomplement), mapping every triangle element to its medial or anticomplementary counterpart.",
        "primary_center": 2,
        "centers": [2, 1, 8, 10, 3, 4, 5],
        "pairs": [(1, 10), (1, 8), (3, 5), (3, 4)],
        "lines": [(1, 2, 8, 10), (2, 3, 4, 5)],
        "circles": ["nine_point_circle"],
        "triangles": ["medial"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Complement and Anticomplement are the two universal homothety operators centered at the Centroid X two. <pause> Because the centroid divides every median in a two-to-one ratio, <pause> dilation through X two by negative one-half maps triangle A B C onto its medial triangle.

[bell:construction]
For any center P, <pause> its complement lies on line P X two on the opposite side of X two at half the distance, <pause> with barycentric coordinates v plus w, <pause> w plus u, <pause> u plus v. <pause> Its anticomplement lies at twice the distance in the opposite direction, <pause> with barycentrics negative u plus v plus w, <pause> u minus v plus w, <pause> u plus v minus w.

[bell:insight]
This single homothety organizes two of the most famous lines in Collection One: <pause> on the Euler line, <pause> X five is the complement of X three and X four is the anticomplement of X three; <pause> on the Nagel line, <pause> Spieker center X ten is the complement of Incenter X one and Nagel point X eight is its anticomplement.
""",
        "s1": (
            "Complement h(X_2, −1/2) • Anticomplement h(X_2, −2)",
            '<span class="clause-line"><b>Centroid Homothety:</b> Dilation at <span class="g-tok">X_2</span> by ratio −1/2 maps <span class="g-tok">△ABC</span> to the <span class="coincide-tok">medial triangle M_a M_b M_c</span> and the circumcircle to the <span class="eq-tok">nine-point circle</span>.</span>',
            "HOMOTHETIC SCALING",
            "Every center of the medial triangle is the exact complement of the corresponding center of △ABC.",
        ),
        "s2": (
            "u : v : w  ↦  v+w : w+u : u+v  ⟷  −u+v+w : u−v+w : u+v−w",
            '<span class="clause-line"><b>Barycentric Shift:</b> Complement maps <span class="g-tok">u : v : w</span> to <span class="coincide-tok">v+w : w+u : u+v</span>; anticomplement maps to <span class="eq-tok">−u+v+w : u−v+w : u+v−w</span>.</span>',
            "COLLINEAR TRIPLETS",
            "For any point P, its anticomplement P', P, X_2, and complement P'' form a 6 : 2 : 1 segment ratio.",
        ),
        "s3": (
            "Euler Line {2, 3, 4, 5} & Nagel Line {1, 2, 8, 10}",
            '<span class="clause-line"><b>Collection 1 Action:</b> Centroid <span class="g-tok">X_2</span> is the intersection of the Nagel homothety axis <span class="g-tok">{1, 2, 8, 10}</span> and the Euler homothety axis <span class="coincide-tok">{2, 3, 4, 5}</span>.</span>',
            "PARALLEL GEOMETRIES",
            "The Euler line of △ABC and the Nagel line of △ABC are linked by a 1 : −2 dilation about X_2.",
        ),
        "s4": (
            "(X_8 → X_1 → X_10) • (X_4 → X_3 → X_5)",
            '<span class="clause-line"><b>Homothetic Chains:</b> On the Nagel axis <span class="coincide-tok">X_8</span> → <span class="coincide-tok">X_1</span> → <span class="coincide-tok">X_10</span>; on the Euler axis <span class="eq-tok">X_4</span> → <span class="eq-tok">X_3</span> → <span class="eq-tok">X_5</span>.</span>',
            "MIDPOINT THEOREM",
            "X_10 is the midpoint of X_1 X_8, and X_5 is the midpoint of X_3 X_4.",
        ),
    },
    {
        "num": 4,
        "code": "T_4",
        "slug": "harmonic-conjugate",
        "category": "Transformations & Conjugacies",
        "title": "Harmonic Conjugate & Cross-Ratio",
        "short_title": "HARMONIC CONJUGATE",
        "enunciation": "Four collinear centers (A, B; C, D) form a harmonic range when C and D divide segment AB internally and externally in the same ratio, yielding cross-ratio −1.",
        "primary_center": 5,
        "centers": [2, 3, 4, 5, 1, 11, 12],
        "pairs": [(3, 5), (2, 4), (11, 12)],
        "lines": [(2, 3, 4, 5), (1, 5, 11, 12)],
        "circles": ["incircle", "nine_point_circle"],
        "triangles": ["medial"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Harmonic Conjugate governs projective division along central lines. <pause> Four collinear points A, B, C, and D form a harmonic range when C and D divide segment A B internally and externally in the exact same ratio.

[bell:construction]
Because the Centroid X two divides the segment from Circumcenter X three to Orthocenter X four in a one-to-two ratio, <pause> and the Nine-Point Center X five bisects X three X four, <pause> the four classical Euler centers X two, X four, X three, and X five form a canonical harmonic range with cross-ratio negative one.

[bell:insight]
Harmonic division recurs across Collection One: <pause> on the Feuerbach line, <pause> the Feuerbach point X eleven and its harmonic conjugate X twelve divide the ইনcenter X one and Nine-Point Center X five internally and externally in the ratio of their radii.
""",
        "s1": (
            "(A, B; C, D) = (AC / CB) : (AD / DB) = −1",
            '<span class="clause-line"><b>Harmonic Range:</b> On the Euler line through <span class="g-tok">X_5</span>, internal and external division of <span class="g-tok">X_3</span> and <span class="g-tok">X_4</span> with <span class="g-tok">X_2</span> links the <span class="coincide-tok">medial triangle M_a M_b M_c</span> and <span class="eq-tok">nine-point circle</span>.</span>',
            "PROJECTIVE INVARIANCE",
            "Cross-ratio (A, B; C, D) = −1 is preserved under every projective collineation.",
        ),
        "s2": (
            "Euler Range (X_3, X_4; X_2, X_5) = −1",
            '<span class="clause-line"><b>Homogeneous Linear Combination:</b> If <span class="g-tok">C = p·A + q·B</span>, then its harmonic conjugate with respect to A and B is <span class="coincide-tok">D = p·A − q·B</span>, satisfying <span class="eq-tok">2/AB = 1/AC + 1/AD</span>.</span>',
            "HARMONIC MEAN",
            "On the Euler line: X_2 : X_5 divide X_3 X_4 in ratios 1 : 2 and 1 : −1.",
        ),
        "s3": (
            "Euler Line {2, 3, 4, 5} & Feuerbach Line {1, 5, 11, 12}",
            '<span class="clause-line"><b>Collection 1 Harmonic Axes:</b> The Euler line <span class="g-tok">{2, 3, 4, 5}</span> and Feuerbach line <span class="coincide-tok">{1, 5, 11, 12}</span> meet at the Nine-Point Center <span class="g-tok">X_5</span>.</span>',
            "SIMILICENTER DUALITY",
            "Internal and external centers of similitude of any two circles are harmonic conjugates with respect to their centers.",
        ),
        "s4": (
            "(X_2, X_4; X_3, X_5) = −1 • (X_1, X_5; X_11, X_12) = −1",
            '<span class="clause-line"><b>Harmonic Quartets:</b> Euler centers <span class="coincide-tok">X_2</span>, <span class="coincide-tok">X_3</span>, <span class="coincide-tok">X_4</span>, <span class="g-tok">X_5</span> and Feuerbach centers <span class="eq-tok">X_1</span>, <span class="g-tok">X_5</span>, <span class="eq-tok">X_11</span>, <span class="eq-tok">X_12</span>.</span>',
            "APOLLONIAN HARMONICS",
            "On the Brocard axis, (X_3, X_6; X_15, X_16) also forms a classical harmonic structure.",
        ),
    },
    {
        "num": 5,
        "code": "T_5",
        "slug": "circle-inversion",
        "category": "Transformations & Conjugacies",
        "title": "Circle Inversion",
        "short_title": "CIRCLE INVERSION",
        "enunciation": "Radial mapping across a reference circle of center O and radius R sending point P to P' on ray OP such that OP · OP' = R².",
        "primary_center": 15,
        "centers": [3, 6, 15, 16, 1, 4],
        "pairs": [(15, 16), (3, 6)],
        "lines": [(3, 6, 15, 16), (3, 4)],
        "circles": ["circumcircle", "incircle"],
        "triangles": [],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> Circle Inversion is the conformal radial reflection across a circle of radius R. <pause> A point P at distance d from the center O maps to a point P prime along the same ray O P <pause> at distance R squared over d, <pause> so that the product of their radial distances equals R squared.

[bell:construction]
In Collection One, <pause> inversion in the Circumcircle centered at X three <pause> maps the First Isodynamic Point X fifteen inside the triangle <pause> directly onto the Second Isodynamic Point X sixteen outside the triangle along the Brocard axis.

[bell:insight]
Because the three Apollonian circles pass through both X fifteen and X sixteen, <pause> each Apollonian circle is orthogonal to the circumcircle and invariant under circumcircle inversion.
""",
        "s1": (
            "OP · OP' = R²  •  X_15 ↔ X_16 in Circumcircle",
            '<span class="clause-line"><b>Circumcircle Inversion:</b> Radial inversion across the <span class="coincide-tok">circumcircle</span> centered at <span class="g-tok">X_3</span> exchanges the 1st Isodynamic point <span class="g-tok">X_15</span> and 2nd Isodynamic point <span class="g-tok">X_16</span>.</span>',
            "ORTHOGONAL CIRCLES",
            "Any circle passing through a pair of inverse points is strictly orthogonal to the circle of inversion.",
        ),
        "s2": (
            "Radial Product |X_3 X_15| · |X_3 X_16| = R²",
            '<span class="clause-line"><b>Algebraic Formula:</b> Inversion of <span class="g-tok">P</span> in the circumcircle reflects along ray from <span class="coincide-tok">X_3</span> with radial product <span class="eq-tok">OP · OP\' = R²</span>.</span>',
            "CONFORMAL INVOLUTION",
            "Circle inversion preserves angles between curves and maps generalized circles to generalized circles.",
        ),
        "s3": (
            "Brocard Axis {3, 6, 15, 16} & Euler Line {3, 4}",
            '<span class="clause-line"><b>Collection 1 Inversion Axes:</b> The Brocard axis <span class="g-tok">{3, 6, 15, 16}</span> carries the inverse pair <span class="g-tok">X_15</span>, <span class="g-tok">X_16</span> while <span class="coincide-tok">{3, 4}</span> carries the orthocenter inverse X_186.</span>',
            "RADIAL AXES THROUGH X_3",
            "Every line through the circumcenter X_3 is invariant as a set under circumcircle inversion.",
        ),
        "s4": (
            "X_15 ↔ X_16 on Brocard Axis {3, 6, 15, 16}",
            '<span class="clause-line"><b>Inverse Partners:</b> On the Brocard axis through <span class="coincide-tok">X_3</span> and <span class="coincide-tok">X_6</span>, <span class="g-tok">X_15</span> and <span class="coincide-tok">X_16</span> are exact circumcircle inverses.</span>',
            "INVERSION CATALOG",
            "Incenter X_1 inverts in the circumcircle to X_36; Orthocenter X_4 inverts to X_186.",
        ),
    },
    # =========================================================================
    # II. NAMED CENTRAL LINES OF COLLECTION 1 (T_6 – T_13)
    # =========================================================================
    {
        "num": 6,
        "code": "T_6",
        "slug": "euler-line",
        "category": "Named Central Lines",
        "title": "The Euler Line",
        "short_title": "THE EULER LINE",
        "enunciation": "Leonhard Euler's 1765 central line passing through the Centroid X_2, Circumcenter X_3, Orthocenter X_4, and Nine-Point Center X_5 of every non-equilateral triangle.",
        "primary_center": 2,
        "centers": [2, 3, 4, 5, 20, 30],
        "pairs": [(2, 3), (3, 4), (4, 5)],
        "lines": [(2, 3, 4, 5, 20)],
        "circles": ["circumcircle", "nine_point_circle"],
        "triangles": ["medial", "orthic"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Euler Line is the foundational central line discovered by Leonhard Euler in seventeen sixty-five. <pause> In every non-equilateral triangle, <pause> the Centroid X two, <pause> the Circumcenter X three, <pause> the Orthocenter X four, <pause> and the Nine-Point Center X five are strictly collinear.

[bell:construction]
Because the medial triangle and reference triangle A B C are homothetic at the Centroid X two with scale factor negative one-half, <pause> the orthocenter of the medial triangle is the circumcenter X three of A B C. <pause> Consequently, <pause> X two lies between X three and X four at exactly one-third the distance from X three to X four.

[bell:insight]
The Nine-Point Center X five bisects segment X three X four, <pause> creating the canonical Euler segment ratios: <pause> X three to X two, <pause> X two to X five, <pause> and X five to X four <pause> stand in the exact proportion two to one to three.
""",
        "s1": (
            "Euler Line L(2, 3, 4, 5, 20, 30) • |X_3 X_2| : |X_2 X_5| : |X_5 X_4| = 2 : 1 : 3",
            '<span class="clause-line"><b>The Euler Line:</b> Connects <span class="g-tok">X_2</span>, <span class="g-tok">X_3</span>, <span class="g-tok">X_4</span>, and <span class="g-tok">X_5</span> across the <span class="coincide-tok">medial triangle M_a M_b M_c</span> and <span class="eq-tok">nine-point circle</span>.</span>',
            "EULER (1765) • NOVI COMMENTARII",
            "On an equilateral triangle, X_2, X_3, X_4, and X_5 coincide and the Euler line is indeterminate.",
        ),
        "s2": (
            "Trilinear Equation: sin(2A) sin(B−C) α + sin(2B) sin(C−A) β + sin(2C) sin(A−B) γ = 0",
            '<span class="clause-line"><b>Shinagawa Coefficients:</b> Every Euler center is a linear combination <span class="g-tok">p·X_4 + q·X_3</span> with <span class="coincide-tok">X_2 = (1, 2)</span> and <span class="eq-tok">X_5 = (1, 1)</span>.</span>',
            "EULER INFINITY POINT X_30",
            "X_30 is the point at infinity of the Euler line; X_20 (de Longchamps) is the reflection of X_4 in X_3.",
        ),
        "s3": (
            "Collinearity {2, 3, 4, 5, 20}",
            '<span class="clause-line"><b>Central Line Spine:</b> The Euler line <span class="g-tok">{2, 3, 4, 5, 20}</span> links the circumcenter, centroid, nine-point center, orthocenter, and de Longchamps point.</span>',
            "2 : 1 : 3 SEGMENT RATIOS",
            "X_2 trisects X_3 X_4, while X_5 bisects X_3 X_4.",
        ),
        "s4": (
            "X_3 • X_2 • X_5 • X_4 • X_20",
            '<span class="clause-line"><b>Ordered Euler Sequence:</b> <span class="g-tok">X_2</span>, <span class="coincide-tok">X_3</span>, <span class="coincide-tok">X_4</span>, <span class="coincide-tok">X_5</span>, and <span class="coincide-tok">X_20</span> lie in exact rational ratio along the Euler axis.</span>',
            "COLLECTION 1 ANCHOR",
            "Four of the first five centers in Kimberling's Encyclopedia lie on the Euler line.",
        ),
    },
    {
        "num": 7,
        "code": "T_7",
        "slug": "nagel-line",
        "category": "Named Central Lines",
        "title": "The Nagel Line",
        "short_title": "THE NAGEL LINE",
        "enunciation": "The central line passing through the Incenter X_1, Centroid X_2, Nagel Point X_8, and Spieker Center X_10, forming the tritangent counterpart to the Euler line.",
        "primary_center": 10,
        "centers": [1, 2, 8, 10],
        "pairs": [(1, 10), (1, 8)],
        "lines": [(1, 2, 8, 10)],
        "circles": ["incircle", "spieker_circle"],
        "triangles": ["medial"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Nagel Line is the tritangent counterpart of the Euler line, <pause> passing through the Incenter X one, <pause> the Centroid X two, <pause> the Nagel Point X eight, <pause> and the Spieker Center X ten.

[bell:construction]
Because the Spieker Center X ten is the incenter of the medial triangle, <pause> and the medial triangle is the image of triangle A B C under homothety at X two with factor negative one-half, <pause> X ten is the complement of X one, <pause> and the Nagel Point X eight is the anticomplement of X one.

[bell:insight]
Just as Xthree, X two, X five, and X four divide the Euler line in the ratio two to one to three, <pause> X one, X two, X ten, and X eight divide the Nagel line in the exact same proportion: <pause> two to one to three.
""",
        "s1": (
            "Nagel Line L(1, 2, 8, 10) • |X_1 X_2| : |X_2 X_10| : |X_10 X_8| = 2 : 1 : 3",
            '<span class="clause-line"><b>The Nagel Line:</b> Connects <span class="g-tok">X_1</span>, <span class="g-tok">X_2</span>, <span class="g-tok">X_8</span>, and <span class="g-tok">X_10</span> across the <span class="coincide-tok">medial triangle M_a M_b M_c</span> and <span class="eq-tok">incircle</span>.</span>',
            "CHRISTIAN HEINRICH VON NAGEL (1836)",
            "The Spieker circle of the medial triangle is the −1/2 homothetic image of the incircle at X_2.",
        ),
        "s2": (
            "Homothety at X_2: X_8 ↦ X_1 ↦ X_10",
            '<span class="clause-line"><b>Barycentric Progression:</b> <span class="g-tok">X_1 = a:b:c</span>, <span class="coincide-tok">X_2 = 1:1:1</span>, <span class="eq-tok">X_8 = s−a:s−b:s−c</span>, and <span class="g-tok">X_10 = b+c:c+a:a+b</span>.</span>',
            "PERIMETER CENTER X_10",
            "X_10 is the center of mass of the uniform wire perimeter of triangle ABC.",
        ),
        "s3": (
            "Collinearity {1, 2, 8, 10}",
            '<span class="clause-line"><b>Nagel Axis:</b> The central line <span class="g-tok">{1, 2, 8, 10}</span> intersects the Euler line at the Centroid <span class="g-tok">X_2</span>.</span>',
            "2 : 1 : 3 SEGMENT RATIOS",
            "X_10 is the exact midpoint of segment X_1 X_8, and X_2 trisects segment X_1 X_8.",
        ),
        "s4": (
            "X_1 • X_2 • X_10 • X_8",
            '<span class="clause-line"><b>Ordered Nagel Sequence:</b> <span class="coincide-tok">X_1</span>, <span class="coincide-tok">X_2</span>, <span class="g-tok">X_10</span>, and <span class="coincide-tok">X_8</span> mirror the Euler quartet under inscribed geometry.</span>',
            "COLLECTION 1 QUARTET",
            "Links four fundamental centers of Collection 1 along a single homothetic axis.",
        ),
    },
    {
        "num": 8,
        "code": "T_8",
        "slug": "brocard-axis",
        "category": "Named Central Lines",
        "title": "The Brocard Axis",
        "short_title": "THE BROCARD AXIS",
        "enunciation": "The central line passing through the Circumcenter X_3, Symmedian Point X_6, and the 1st and 2nd Isodynamic Points X_15 and X_16, perpendicular to the Lemoine axis.",
        "primary_center": 6,
        "centers": [3, 6, 15, 16],
        "pairs": [(3, 6), (15, 16)],
        "lines": [(3, 6, 15, 16)],
        "circles": ["circumcircle", "brocard_circle"],
        "triangles": [],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Brocard Axis is the central line connecting the Circumcenter X three and the Symmedian Point X six. <pause> It serves as the line of symmetry of the Brocard configuration and is perpendicular to the Lemoine axis.

[bell:construction]
Because the three Apollonian circles have their centers on the Lemoine axis, <pause> their common radical chord is the Brocard axis. <pause> The two intersection points of all three Apollonian circles—the First and Second Isodynamic Points X fifteen and X sixteen—lie directly on the Brocard axis.

[bell:insight]
Segment X three X six is the diameter of the Brocard circle, <pause> while X fifteen and X sixteen are mutual inverses in the circumcircle and harmonic conjugates with respect to the Apollonian structure along the Brocard axis.
""",
        "s1": (
            "Brocard Axis L(3, 6, 15, 16) ⊥ Lemoine Axis",
            '<span class="clause-line"><b>The Brocard Axis:</b> Connects Circumcenter <span class="g-tok">X_3</span> and Symmedian Point <span class="g-tok">X_6</span> with Isodynamic Points <span class="g-tok">X_15</span>, <span class="g-tok">X_16</span> across the <span class="coincide-tok">circumcircle</span>.</span>',
            "HENRI BROCARD & ÉMILE LEMOINE",
            "Isogonal conjugate of the Brocard axis is the Kiepert hyperbola.",
        ),
        "s2": (
            "Trilinear Equation: bc(b²−c²)α + ca(c²−a²)β + ab(a²−b²)γ = 0",
            '<span class="clause-line"><b>Radical Chord of Apollonian Circles:</b> <span class="g-tok">X_3 = cos A : cos B : cos C</span> and <span class="coincide-tok">X_6 = a : b : c</span> span the axis containing <span class="eq-tok">X_15, X_16</span>.</span>',
            "ISOGONAL TRANSFORM TO KIEPERT HYPERBOLA",
            "Every point on the Kiepert hyperbola has its isogonal conjugate on the Brocard axis.",
        ),
        "s3": (
            "Collinearity {3, 6, 15, 16}",
            '<span class="clause-line"><b>Brocard Collinearity:</b> The Brocard axis <span class="g-tok">{3, 6, 15, 16}</span> is the common radical line of the three Apollonian circles.</span>',
            "DIAMETER OF BROCARD CIRCLE",
            "Segment X_3 X_6 is the diameter of the Brocard circle passing through the two Brocard points.",
        ),
        "s4": (
            "X_3 • X_6 • X_15 • X_16",
            '<span class="clause-line"><b>Brocard Quartet:</b> <span class="coincide-tok">X_3</span>, <span class="g-tok">X_6</span>, <span class="coincide-tok">X_15</span>, and <span class="coincide-tok">X_16</span> align on the Brocard axis.</span>',
            "KIEPERT DUALITY",
            "Isogonal conjugation maps the Kiepert centers {X_2, X_4, X_13, X_14} onto the Brocard axis {X_6, X_3, X_15, X_16}.",
        ),
    },
    {
        "num": 9,
        "code": "T_9",
        "slug": "feuerbach-line",
        "category": "Named Central Lines",
        "title": "The Feuerbach Line",
        "short_title": "THE FEUERBACH LINE",
        "enunciation": "The line of centers passing through the Incenter X_1, Nine-Point Center X_5, Feuerbach Point X_11, and its harmonic conjugate X_12 at the tangency of the incircle and nine-point circle.",
        "primary_center": 11,
        "centers": [1, 5, 11, 12],
        "pairs": [(1, 5), (11, 12)],
        "lines": [(1, 5, 11, 12)],
        "circles": ["incircle", "nine_point_circle"],
        "triangles": ["medial"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Feuerbach Line is the line of centers of the incircle and the nine-point circle. <pause> By Karl Wilhelm Feuerbach's eighteen twenty-two theorem, <pause> the incircle and nine-point circle are internally tangent at the Feuerbach Point X eleven.

[bell:construction]
Because the point of tangency of any two tangent circles lies on the line joining their centers, <pause> Incenter X one, <pause> Nine-Point Center X five, <pause> and Feuerbach Point X eleven are strictly collinear, <pause> with distance X one X five equal to R over two minus r.

[bell:insight]
The external center of similitude of the incircle and nine-point circle is X twelve, <pause> which lies on the same Feuerbach line as the harmonic conjugate of X eleven with respect to X one and X five.
""",
        "s1": (
            "Feuerbach Line L(1, 5, 11, 12) • |X_1 X_5| = |R/2 − r|",
            '<span class="clause-line"><b>The Feuerbach Line:</b> Joins Incenter <span class="g-tok">X_1</span> and Nine-Point Center <span class="g-tok">X_5</span> through tangency point <span class="g-tok">X_11</span> and <span class="g-tok">X_12</span> of the <span class="coincide-tok">incircle</span> and <span class="eq-tok">nine-point circle</span>.</span>',
            "FEUERBACH'S THEOREM (1822)",
            "Internal tangency requires the distance between centers |X_1 X_5| to equal the difference of radii |R/2 − r|.",
        ),
        "s2": (
            "Harmonic Similicenters: X_11 (Internal) & X_12 (External)",
            '<span class="clause-line"><b>Tangency & Similitude:</b> <span class="g-tok">X_11</span> is the internal tangency point and <span class="coincide-tok">X_12</span> is the harmonic conjugate dividing <span class="eq-tok">X_1 X_5</span> in ratio <span class="eq-tok">r : R/2</span>.</span>',
            "HARMONIC RANGE (X_1, X_5; X_11, X_12) = −1",
            "X_11 and X_12 are the internal and external centers of similitude of the incircle and nine-point circle.",
        ),
        "s3": (
            "Collinearity {1, 5, 11, 12}",
            '<span class="clause-line"><b>Feuerbach Axis:</b> The central line <span class="g-tok">{1, 5, 11, 12}</span> connects two tangent circles and four Collection 1 centers.</span>',
            "LINE OF CENTERS",
            "Perpendicular to the common tangent of the incircle and nine-point circle at X_11.",
        ),
        "s4": (
            "X_1 • X_5 • X_11 • X_12",
            '<span class="clause-line"><b>Feuerbach Quartet:</b> <span class="coincide-tok">X_1</span>, <span class="coincide-tok">X_5</span>, <span class="g-tok">X_11</span>, and <span class="coincide-tok">X_12</span> form a harmonic quartet on the Feuerbach line.</span>',
            "COLLECTION 1 HARMONIC PAIR",
            "X_11 and X_12 are also perspectors of the orthic and intouch configurations.",
        ),
    },
    {
        "num": 10,
        "code": "T_10",
        "slug": "oi-line",
        "category": "Named Central Lines",
        "title": "The OI Line (Incenter–Circumcenter Axis)",
        "short_title": "THE OI LINE",
        "enunciation": "The central line joining the Incenter X_1 and Circumcenter X_3, carrying the Bevan Point X_40 and the insimilicenter X_55 and exsimilicenter X_56 of the incircle and circumcircle.",
        "primary_center": 1,
        "centers": [1, 3, 40, 55, 56, 57],
        "pairs": [(1, 3), (1, 40)],
        "lines": [(1, 3, 40, 55, 56)],
        "circles": ["incircle", "circumcircle"],
        "triangles": [],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the O I Line is the central axis joining the Incenter X one and the Circumcenter X three. <pause> By Euler's formula, <pause> the squared distance between X one and X three equals R times R minus two r.

[bell:construction]
Because the incircle and circumcircle are centered at X one and X three, <pause> both of their centers of similitude—the insimilicenter X fifty-five and exsimilicenter X fifty-six—lie on the O I line. <pause> Furthermore, <pause> the reflection of X one across X three is the Bevan Point X forty, <pause> the circumcenter of the excentral triangle.

[bell:insight]
Through isogonal conjugation, <pause> the Gergonne Point X seven pairs with X fifty-five and the Nagel Point X eight pairs with X fifty-seven on the O I line, <pause> uniting the tritangent and circumcircle geometries.
""",
        "s1": (
            "OI Line L(1, 3, 40, 55, 56, 57) • |X_1 X_3|² = R(R − 2r)",
            '<span class="clause-line"><b>The OI Line:</b> Connects Incenter <span class="g-tok">X_1</span> and Circumcenter <span class="g-tok">X_3</span> as the line of centers of the <span class="coincide-tok">incircle</span> and <span class="eq-tok">circumcircle</span>.</span>',
            "EULER'S INEQUALITY R ≥ 2r",
            "Since |X_1 X_3|² = R(R − 2r) ≥ 0, the circumradius R is at least twice the inradius r.",
        ),
        "s2": (
            "Similicenters X_55 (Internal) & X_56 (External) • Bevan Point X_40",
            '<span class="clause-line"><b>Similitude & Reflection:</b> <span class="g-tok">X_3</span> is the midpoint of <span class="coincide-tok">X_1</span> and Bevan point <span class="coincide-tok">X_40</span>; <span class="eq-tok">X_55, X_56</span> divide <span class="g-tok">X_1 X_3</span> in ratio <span class="eq-tok">r : R</span>.</span>',
            "PONCELET PORISM AXIS",
            "The OI line is the axis of symmetry for Poncelet's bicentric triangle family between the incircle and circumcircle.",
        ),
        "s3": (
            "Collinearity {1, 3, 40, 55, 56}",
            '<span class="clause-line"><b>OI Central Axis:</b> The line <span class="g-tok">{1, 3, 40, 55, 56}</span> governs the metric separation between inscribed and circumscribed circles.</span>',
            "CIRCUMCIRCLE–INCIRCLE AXIS",
            "Contains X_1, X_3, X_36 (circumcircle inverse of X_1), X_40, X_55, X_56, and X_57.",
        ),
        "s4": (
            "X_1 • X_3 • X_40 • X_55 • X_56",
            '<span class="clause-line"><b>OI Line Centers:</b> <span class="g-tok">X_1</span>, <span class="coincide-tok">X_3</span>, <span class="coincide-tok">X_40</span>, <span class="coincide-tok">X_55</span>, and <span class="coincide-tok">X_56</span> align along the OI axis.</span>',
            "ISOGONAL LINKS TO X_7 & X_8",
            "X_55 is the isogonal conjugate of Gergonne X_7; X_56 is the isogonal conjugate of X_55's harmonic partner.",
        ),
    },
    {
        "num": 11,
        "code": "T_11",
        "slug": "soddy-line",
        "category": "Named Central Lines",
        "title": "The Soddy Line",
        "short_title": "THE SODDY LINE",
        "enunciation": "The central line passing through the Incenter X_1, Gergonne Point X_7, and de Longchamps Point X_20, carrying the inner and outer Soddy centers X_175 and X_176.",
        "primary_center": 7,
        "centers": [1, 7, 20, 2, 3, 4],
        "pairs": [(1, 7), (7, 20)],
        "lines": [(1, 7, 20), (2, 3, 4, 20)],
        "circles": ["incircle"],
        "triangles": ["intouch"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Soddy Line is the central axis passing through the Incenter X one and the Gergonne Point X seven. <pause> Extending this line reveals a remarkable incidence: <pause> it intersects the Euler line at the de Longchamps Point X twenty.

[bell:construction]
Three mutually tangent circles centered at vertices A, B, and C with radii s minus a, s minus b, and s minus c touch at the exact vertices of the intouch triangle. <pause> By Frederick Soddy's nineteen thirty-six theorem, <pause> the inner and outer Soddy circles tangent to all three vertex circles have their centers X one-seventy-five and X one-seventy-six on line X one X seven.

[bell:insight]
Because the Soddy line and Euler line are orthogonal in key configurations and intersect at X twenty, <pause> the Soddy line bridges the intouch contact geometry of X seven with the Euler axis of X two, X three, and X four.
""",
        "s1": (
            "Soddy Line L(1, 7, 20, 175, 176)",
            '<span class="clause-line"><b>The Soddy Line:</b> Connects Incenter <span class="g-tok">X_1</span> and Gergonne Point <span class="g-tok">X_7</span> across the <span class="coincide-tok">intouch triangle T_a T_b T_c</span> and <span class="eq-tok">incircle</span>.</span>',
            "FREDERICK SODDY (1936) • DESCARTES CIRCLE THEOREM",
            "The three mutually tangent vertex circles of radii s−a, s−b, s−c meet at T_a, T_b, T_c.",
        ),
        "s2": (
            "Intersection with Euler Line at de Longchamps Point X_20",
            '<span class="clause-line"><b>Euler–Soddy Intersection:</b> The Soddy line through <span class="g-tok">X_1</span> and <span class="g-tok">X_7</span> meets the Euler line <span class="coincide-tok">{2, 3, 4, 20}</span> at <span class="eq-tok">X_20</span>.</span>',
            "RADICAL & PERSPECTION AXIS",
            "Perpendicular to the Gergonne line (trilinear polar of X_7).",
        ),
        "s3": (
            "Soddy Line {1, 7, 20} ∩ Euler Line {2, 3, 4, 20}",
            '<span class="clause-line"><b>Crossing Central Axes:</b> The Soddy line <span class="g-tok">{1, 7, 20}</span> and the Euler line <span class="coincide-tok">{2, 3, 4, 20}</span> intersect at <span class="g-tok">X_20</span>.</span>',
            "DE LONGCHAMPS INTERSECTION",
            "X_20 is the anticomplement of the orthocenter X_4 and reflection of X_4 in X_3.",
        ),
        "s4": (
            "X_1 • X_7 • X_20",
            '<span class="clause-line"><b>Soddy Collinearity:</b> <span class="coincide-tok">X_1</span>, <span class="g-tok">X_7</span>, and <span class="coincide-tok">X_20</span> anchor the Soddy axis on <span class="g-tok">△ABC</span>.</span>',
            "SODDY CENTERS X_175 & X_176",
            "The inner and outer Soddy centers divide X_1 and X_7 harmonically with the Descartes curvatures.",
        ),
    },
    {
        "num": 12,
        "code": "T_12",
        "slug": "fuhrmann-and-spieker-lines",
        "category": "Named Central Lines",
        "title": "The Fuhrmann & Spieker Central Lines",
        "short_title": "FUHRMANN & SPIEKER LINES",
        "enunciation": "The network of central lines linking the Orthocenter X_4, Mittenpunkt X_9, Spieker Center X_10, Feuerbach Partner X_12, and Clawson Point X_19.",
        "primary_center": 9,
        "centers": [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 19],
        "pairs": [(4, 9), (4, 10), (1, 9)],
        "lines": [(4, 9, 10), (1, 6, 9), (2, 7, 9), (3, 12, 19)],
        "circles": ["incircle", "spieker_circle"],
        "triangles": ["medial"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Mittenpunkt X nine and Spieker Center X ten sit at the crossroads of the Fuhrmann and Spieker central lines. <pause> Line X four X nine X ten connects the Orthocenter X four directly through the Mittenpunkt X nine to the Spieker Center X ten.

[bell:construction]
At the same time, <pause> Mittenpunkt X nine lies at the intersection of two additional classical lines: <pause> line X one X six X nine connecting the Incenter and Symmedian Point, <pause> and line X two X seven X nine connecting the Centroid and Gergonne Point.

[bell:insight]
Together with line X three X twelve X nineteen linking the Circumcenter, Feuerbach harmonic conjugate, and Clawson point, <pause> these axes bind the orthic, medial, and excentral triangles into a single projective web.
""",
        "s1": (
            "Fuhrmann–Spieker Axis L(4, 9, 10) • Mittenpunkt Pencils L(1, 6, 9) & L(2, 7, 9)",
            '<span class="clause-line"><b>Mittenpunkt & Spieker Web:</b> <span class="g-tok">X_9</span> and <span class="g-tok">X_10</span> align with Orthocenter <span class="g-tok">X_4</span> across the <span class="coincide-tok">medial triangle M_a M_b M_c</span> and <span class="eq-tok">incircle</span>.</span>',
            "CHRISTIAN VON NAGEL & WILHELM FUHRMANN",
            "X_9 is the symmedian point of the excentral triangle; X_10 is the incenter of the medial triangle.",
        ),
        "s2": (
            "Three Concurrent Central Lines at Mittenpunkt X_9",
            '<span class="clause-line"><b>Concurrence at X_9:</b> <span class="g-tok">{4, 9, 10}</span>, <span class="coincide-tok">{1, 6, 9}</span>, and <span class="eq-tok">{2, 7, 9}</span> all concur at Mittenpunkt <span class="g-tok">X_9</span>.</span>',
            "HOMOTHETIC & ISOGONAL BRIDGES",
            "X_9 is the complement of the Gergonne point X_7 (since X_2 divides X_7 X_9 in 2 : 1 ratio).",
        ),
        "s3": (
            "Collinearities {4, 9, 10} • {1, 6, 9} • {2, 7, 9}",
            '<span class="clause-line"><b>Central Line Pencils:</b> <span class="g-tok">{4, 9, 10}</span> meets <span class="coincide-tok">{1, 6, 9}</span> and <span class="eq-tok">{2, 7, 9}</span> at <span class="g-tok">X_9</span>.</span>',
            "CLAWSON & FEUERBACH CROSSINGS",
            "Line {2, 11, 19} and {3, 12, 19} similarly cross at the Clawson point X_19.",
        ),
        "s4": (
            "X_4 • X_9 • X_10 • X_1 • X_6 • X_2 • X_7",
            '<span class="clause-line"><b>Connected Centers:</b> <span class="g-tok">X_9</span> links <span class="coincide-tok">X_4</span> and <span class="coincide-tok">X_10</span> with <span class="eq-tok">X_1</span>, <span class="eq-tok">X_6</span> and <span class="g-tok">X_2</span>, <span class="g-tok">X_7</span>.</span>',
            "COLLECTION 1 SYNTHESIS",
            "Nine of the nineteen centers in Collection 1 meet along the Mittenpunkt and Spieker pencils.",
        ),
    },
    {
        "num": 13,
        "code": "T_13",
        "slug": "isogonic-and-napoleon-lines",
        "category": "Named Central Lines",
        "title": "The Isogonic & Napoleon Central Lines",
        "short_title": "ISOGONIC & NAPOLEON LINES",
        "enunciation": "The central axes generated by outer and inner equilateral triangles on the sides of △ABC, linking Fermat points X_13, X_14, Isodynamic points X_15, X_16, and Napoleon points X_17, X_18.",
        "primary_center": 13,
        "centers": [2, 3, 4, 6, 13, 14, 15, 16, 17, 18],
        "pairs": [(13, 15), (14, 16), (17, 18)],
        "lines": [(3, 6, 15, 16), (2, 13, 17), (4, 13, 18), (6, 13, 16)],
        "circles": ["circumcircle"],
        "triangles": [],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> centers X thirteen through X eighteen form the Equilateral Triad of Collection One: <pause> the First and Second Fermat points X thirteen and X fourteen, <pause> the First and Second Isodynamic points X fifteen and X sixteen, <pause> and the First and Second Napoleon points X seventeen and X eighteen.

[bell:construction]
Erecting outer and inner equilateral triangles on the sides of triangle A B C <pause> produces two families of concurrent cevians. <pause> Connecting the apexes gives the Fermat points X thirteen and X fourteen; <pause> connecting the centroids of the equilateral triangles gives the Napoleon points X seventeen and X eighteen.

[bell:insight]
These six equilateral centers are woven into the classical centers by remarkable central lines: <pause> X fifteen and X sixteen lie on the Brocard axis with X three and X six; <pause> X two, X thirteen, and X seventeen are collinear; <pause> and X four, X thirteen, and X eighteen are collinear.
""",
        "s1": (
            "Equilateral Triad: Fermat (X_13, X_14) • Isodynamic (X_15, X_16) • Napoleon (X_17, X_18)",
            '<span class="clause-line"><b>Equilateral Central Lines:</b> Fermat points <span class="g-tok">X_13</span>, <span class="g-tok">X_14</span>, Isodynamic points <span class="coincide-tok">X_15</span>, <span class="coincide-tok">X_16</span>, and Napoleon points <span class="eq-tok">X_17</span>, <span class="eq-tok">X_18</span> on the <span class="coincide-tok">circumcircle</span> stage.</span>',
            "TORRICELLI, FERMAT, APOLLONIUS & NAPOLEON",
            "All six centers arise from the π/3 and −π/3 Kiepert equilateral constructions on sides BC, CA, AB.",
        ),
        "s2": (
            "Kiepert Hyperbola {2, 4, 13, 14, 17, 18} ↔ Brocard Axis {3, 6, 15, 16}",
            '<span class="clause-line"><b>Kiepert–Brocard Duality:</b> <span class="g-tok">X_13, X_14, X_17, X_18</span> lie on the Kiepert hyperbola with <span class="coincide-tok">X_2, X_4</span>, while their isogonal partners <span class="eq-tok">X_15, X_16</span> lie on the Brocard axis.</span>',
            "60° & 30° KIEPERT PARAMETERS",
            "Kiepert hyperbola K(θ) gives X_13, X_14 at θ = ±60° and X_17, X_18 at θ = ±30°.",
        ),
        "s3": (
            "Collinearities {3, 6, 15, 16} • {2, 13, 17} • {4, 13, 18}",
            '<span class="clause-line"><b>Equilateral Axes:</b> Brocard axis <span class="g-tok">{3, 6, 15, 16}</span>, centroid–Fermat–Napoleon line <span class="coincide-tok">{2, 13, 17}</span>, and orthocenter–Fermat–Napoleon line <span class="eq-tok">{4, 13, 18}</span>.</span>',
            "CROSS-ALIGNMENT OF TRIADS",
            "Line {6, 13, 16} and {6, 14, 15} also cross at the Symmedian point X_6.",
        ),
        "s4": (
            "X_13 ↔ X_15 • X_14 ↔ X_16 • X_17 ↔ X_18",
            '<span class="clause-line"><b>Isogonal Pairs:</b> <span class="g-tok">X_13</span> and <span class="coincide-tok">X_15</span>, <span class="eq-tok">X_14</span> and <span class="eq-tok">X_16</span>, and <span class="coincide-tok">X_17</span> and <span class="coincide-tok">X_18</span>.</span>',
            "COMPLETE EQUILATERAL SUBSYSTEM",
            "Together X_13–X_18 form a closed subsystem under isogonal conjugation and circumcircle inversion.",
        ),
    },
    # =========================================================================
    # III. NAMED CIRCLES OF COLLECTION 1 (T_14 – T_19)
    # =========================================================================
    {
        "num": 14,
        "code": "T_14",
        "slug": "incircle-and-excircles",
        "category": "Named Circles",
        "title": "The Incircle & Excircles",
        "short_title": "INCIRCLE & EXCIRCLES",
        "enunciation": "The four tritangent circles tangent to all three sidelines of triangle ABC: the interior Incircle centered at X_1 (radius r = Δ/s) and the three exterior Excircles.",
        "primary_center": 1,
        "centers": [1, 7, 8, 9, 11, 12],
        "pairs": [(1, 7), (1, 8), (1, 11)],
        "lines": [(1, 7), (1, 8), (1, 11, 12)],
        "circles": ["incircle"],
        "triangles": ["intouch"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Incircle and three Excircles are the four tritangent circles tangent to all three sidelines of triangle A B C. <pause> The interior angle bisectors concur at the Incenter X one, <pause> while the exterior angle bisectors meet at the three excenters J A, J B, and J C.

[bell:construction]
The incircle has radius r equal to the area Delta divided by the semiperimeter s, <pause> touching the sides at the intouch triangle T a, T b, T c. <pause> Seven of the nineteen centers in Collection One—X one, X seven, X eight, X nine, X ten, X eleven, and X twelve—are generated directly by the tritangent circles.

[bell:insight]
Connecting the vertices to the incircle touch points gives the Gergonne Point X seven; <pause> connecting them to the excircle touch points gives the Nagel Point X eight; <pause> and the incircle's tangency with the nine-point circle defines the Feuerbach Point X eleven.
""",
        "s1": (
            "Incircle (Center X_1, Radius r = Δ/s) • Excircles (Radii r_a, r_b, r_c)",
            '<span class="clause-line"><b>The Incircle & Excircles:</b> Centered at <span class="g-tok">X_1</span>, the <span class="eq-tok">incircle</span> touches the sidelines at the <span class="coincide-tok">intouch triangle T_a T_b T_c</span>.</span>',
            "EUCLID BOOK IV • PROPOSITION 4",
            "1/r = 1/r_a + 1/r_b + 1/r_c and Area(△ABC) = √(r · r_a · r_b · r_c).",
        ),
        "s2": (
            "Touch-Point Distances: AT_b = AT_c = s−a • BT_c = BT_a = s−b • CT_a = CT_b = s−c",
            '<span class="clause-line"><b>Tritangent Metrics:</b> Inradius <span class="g-tok">r = Δ/s</span>, exradii <span class="coincide-tok">r_a = Δ/(s−a)</span>, and touch segments <span class="eq-tok">s−a : s−b : s−c</span>.</span>',
            "SEVEN COLLECTION 1 CENTERS",
            "Generates X_1 (Incenter), X_7 (Gergonne), X_8 (Nagel), X_9 (Mittenpunkt), X_10 (Spieker), X_11, X_12.",
        ),
        "s3": (
            "Tritangent Axes {1, 7} • {1, 8} • {1, 11, 12}",
            '<span class="clause-line"><b>Tritangent Pencils:</b> <span class="g-tok">X_1</span> anchors the Soddy axis <span class="g-tok">{1, 7}</span>, Nagel axis <span class="coincide-tok">{1, 8}</span>, and Feuerbach axis <span class="eq-tok">{1, 11, 12}</span>.</span>',
            "RADICAL & HOMOTHETIC AXES",
            "The Spieker center X_10 is the radical center of the three excircles.",
        ),
        "s4": (
            "X_1 • X_7 • X_8 • X_9 • X_11 • X_12",
            '<span class="clause-line"><b>Tritangent Family:</b> <span class="g-tok">X_1</span>, <span class="coincide-tok">X_7</span>, <span class="eq-tok">X_8</span>, <span class="g-tok">X_9</span>, <span class="coincide-tok">X_11</span>, and <span class="coincide-tok">X_12</span>.</span>',
            "TRITANGENT HARMONY",
            "Replacing (a, b, c) with (−a, b, c) transforms the incenter into the A-excenter.",
        ),
    },
    {
        "num": 15,
        "code": "T_15",
        "slug": "circumcircle",
        "category": "Named Circles",
        "title": "The Circumcircle",
        "short_title": "THE CIRCUMCIRCLE",
        "enunciation": "The unique circle passing through vertices A, B, and C of triangle ABC, centered at the Circumcenter X_3 with radius R = abc / (4Δ).",
        "primary_center": 3,
        "centers": [3, 2, 4, 5, 6, 15, 16],
        "pairs": [(3, 4), (3, 6), (15, 16)],
        "lines": [(2, 3, 4, 5), (3, 6, 15, 16)],
        "circles": ["circumcircle"],
        "triangles": [],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Circumcircle is the unique circle passing through the three vertices A, B, and C of reference triangle A B C. <pause> Its center is the Circumcenter X three, <pause> the concurrence of the three perpendicular bisectors of the sides.

[bell:construction]
By the Law of Sines, <pause> the diameter two R of the circumcircle equals a over sine A, <pause> b over sine B, <pause> and c over sine C, <pause> giving circumradius R equal to a b c divided by four Delta. <pause> Its homogeneous barycentric equation is a squared v w plus b squared w u plus c squared u v equals zero.

[bell:insight]
In Collection One, <pause> the circumcircle is theisogonal dual of the line at infinity, <pause> the circle of inversion exchanging the Isodynamic Points X fifteen and X sixteen, <pause> and the parent of the Nine-Point Circle under one-half dilation.
""",
        "s1": (
            "Circumcircle (Center X_3, Radius R = abc / 4Δ) • 2R = a/sin A = b/sin B = c/sin C",
            '<span class="clause-line"><b>The Circumcircle:</b> Passes through <span class="g-tok">A</span>, <span class="g-tok">B</span>, <span class="g-tok">C</span> with center <span class="g-tok">X_3</span> on the perpendicular bisectors of <span class="g-tok">△ABC</span>.</span>',
            "EUCLID BOOK IV • PROPOSITION 5",
            "Barycentric equation: a²vw + b²wu + c²uv = 0; trilinear equation: aβγ + bγα + cαβ = 0.",
        ),
        "s2": (
            "Isogonal Transform of the Line at Infinity (u + v + w = 0)",
            '<span class="clause-line"><b>Projective & Metric Role:</b> <span class="g-tok">X_3 = cos A : cos B : cos C</span> anchors the <span class="coincide-tok">circumcircle</span> of radius <span class="eq-tok">R = abc / (4Δ)</span>.</span>',
            "SIMSON LINE LOCUS",
            "The pedal feet of a point P are collinear (forming a Simson line) if and only if P lies on the circumcircle.",
        ),
        "s3": (
            "Euler Line {2, 3, 4, 5} & Brocard Axis {3, 6, 15, 16}",
            '<span class="clause-line"><b>Orthogonal Axes at X_3:</b> <span class="g-tok">X_3</span> is the origin of the Euler line <span class="g-tok">{2, 3, 4, 5}</span> and the Brocard axis <span class="coincide-tok">{3, 6, 15, 16}</span>.</span>',
            "RADIAL INVERSION CENTER",
            "X_15 and X_16 are mutual inverses in the circumcircle along the Brocard axis.",
        ),
        "s4": (
            "X_3 • X_2 • X_4 • X_5 • X_6 • X_15 • X_16",
            '<span class="clause-line"><b>Circumcircle Network:</b> <span class="g-tok">X_3</span> links <span class="coincide-tok">X_2</span>, <span class="coincide-tok">X_4</span>, <span class="coincide-tok">X_5</span> on the Euler line and <span class="eq-tok">X_6</span>, <span class="eq-tok">X_15</span>, <span class="eq-tok">X_16</span> on the Brocard axis.</span>',
            "TANGENTIAL POLARITY",
            "The tangents to the circumcircle at A, B, C form the tangential triangle, whose perspector is X_6.",
        ),
    },
    {
        "num": 16,
        "code": "T_16",
        "slug": "nine-point-circle",
        "category": "Named Circles",
        "title": "The Nine-Point (Feuerbach) Circle",
        "short_title": "NINE-POINT CIRCLE",
        "enunciation": "The circle of radius R/2 centered at X_5 passing through the 3 side midpoints, 3 altitude feet, and 3 Euler midpoints of triangle ABC, tangent to the incircle at X_11.",
        "primary_center": 5,
        "centers": [5, 1, 2, 3, 4, 11, 12],
        "pairs": [(5, 11), (3, 5), (4, 5)],
        "lines": [(2, 3, 4, 5), (1, 5, 11, 12)],
        "circles": ["nine_point_circle", "incircle"],
        "triangles": ["medial", "orthic"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Nine-Point Circle—also called the Feuerbach or Euler circle—is the circle centered at X five with radius R over two, <pause> exactly half the circumradius of triangle A B C.

[bell:construction]
It passes simultaneously through nine classical points: <pause> the three side midpoints M a, M b, M c of the medial triangle, <pause> the three altitude feet H a, H b, H c of the orthic triangle, <pause> and the three Euler midpoints halfway from each vertex to the Orthocenter X four.

[bell:insight]
By Feuerbach's theorem, <pause> the nine-point circle is internally tangent to the incircle at the Feuerbach Point X eleven <pause> and externally tangent to all three excircles, <pause> making X five the bridge between the Euler and Feuerbach lines.
""",
        "s1": (
            "Nine-Point Circle (Center X_5, Radius R/2) • 3 Midpoints + 3 Altitude Feet + 3 Euler Points",
            '<span class="clause-line"><b>The Nine-Point Circle:</b> Centered at <span class="g-tok">X_5</span>, the <span class="eq-tok">nine-point circle</span> circumscribes both the <span class="coincide-tok">medial triangle M_a M_b M_c</span> and the orthic triangle.</span>',
            "PONCELET, BRIANCHON & FEUERBACH (1821–1822)",
            "Dilation of the circumcircle by −1/2 at X_2 or +1/2 at X_4 produces the exact same nine-point circle.",
        ),
        "s2": (
            "Midpoint of X_3 and X_4 • Tangency with Incircle at Feuerbach Point X_11",
            '<span class="clause-line"><b>Dual Homothety:</b> <span class="g-tok">X_5</span> is the complement of <span class="coincide-tok">X_3</span> and midpoint of <span class="coincide-tok">X_3 X_4</span>, tangent to the incircle at <span class="eq-tok">X_11</span>.</span>',
            "FEUERBACH TANGENCY",
            "|X_1 X_5| = |R/2 − r|, proving internal tangency of the incircle and nine-point circle at X_11.",
        ),
        "s3": (
            "Euler Line {2, 3, 4, 5} ∩ Feuerbach Line {1, 5, 11, 12}",
            '<span class="clause-line"><b>Intersection at X_5:</b> The Euler line <span class="g-tok">{2, 3, 4, 5}</span> and Feuerbach line <span class="coincide-tok">{1, 5, 11, 12}</span> cross at <span class="g-tok">X_5</span>.</span>',
            "NINE-POINT NEXUS",
            "X_11 always lies strictly on the nine-point circle.",
        ),
        "s4": (
            "X_5 • X_2 • X_3 • X_4 • X_1 • X_11 • X_12",
            '<span class="clause-line"><b>Nine-Point Family:</b> <span class="g-tok">X_5</span> unites <span class="coincide-tok">X_2</span>, <span class="coincide-tok">X_3</span>, <span class="coincide-tok">X_4</span> with <span class="eq-tok">X_1</span>, <span class="eq-tok">X_11</span>, <span class="eq-tok">X_12</span>.</span>',
            "ORTHIC & MEDIAL CIRCUMCIRCLE",
            "Because the medial and orthic triangles share the same circumcircle, their circumcenters coincide at X_5.",
        ),
    },
    {
        "num": 17,
        "code": "T_17",
        "slug": "spieker-circle",
        "category": "Named Circles",
        "title": "The Spieker Circle",
        "short_title": "THE SPIEKER CIRCLE",
        "enunciation": "The incircle of the medial triangle M_a M_b M_c, centered at the Spieker Center X_10 with radius r/2, and the radical circle of the three excircles.",
        "primary_center": 10,
        "centers": [10, 1, 2, 8, 4, 9],
        "pairs": [(1, 10), (8, 10), (4, 10)],
        "lines": [(1, 2, 8, 10), (4, 9, 10)],
        "circles": ["spieker_circle", "incircle"],
        "triangles": ["medial"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Spieker Circle is the inscribed circle of the medial triangle M a M b M c. <pause> Named after nineteenth-century geometer Theodor Spieker, <pause> its center is the Spieker Center X ten, <pause> and its radius is r over two, <pause> half the inradius of triangle A B C.

[bell:construction]
Because the medial triangle is the complement of triangle A B C under homothety at the Centroid X two, <pause> the Spieker circle is the exact complement of the incircle, <pause> and X ten lies on the Nagel line halfway between the Incenter X one and the Nagel Point X eight.

[bell:insight]
Moreover, <pause> the Spieker Center X ten is the radical center of the three excircles of triangle A B C, <pause> and the Spieker circle is orthogonal to all three excircles in key radical projections.
""",
        "s1": (
            "Spieker Circle (Center X_10, Radius r/2) • Incircle of Medial Triangle M_a M_b M_c",
            '<span class="clause-line"><b>The Spieker Circle:</b> Centered at <span class="g-tok">X_10</span>, the <span class="eq-tok">Spieker circle</span> is inscribed in the <span class="coincide-tok">medial triangle M_a M_b M_c</span>.</span>',
            "THEODOR SPIEKER (1888)",
            "Dilation of the incircle at X_2 by factor −1/2 produces the Spieker circle of radius r/2.",
        ),
        "s2": (
            "Midpoint of X_1 and X_8 on the Nagel Line • Barycentrics b+c : c+a : a+b",
            '<span class="clause-line"><b>Perimeter Centroid:</b> <span class="g-tok">X_10 = b+c : c+a : a+b</span> is the complement of <span class="coincide-tok">X_1</span> and midpoint of <span class="eq-tok">X_1 X_8</span>.</span>',
            "RADICAL CENTER OF EXCIRCLES",
            "Equal tangents can be drawn from X_10 to all three excircles of △ABC.",
        ),
        "s3": (
            "Nagel Line {1, 2, 8, 10} ∩ Fuhrmann–Spieker Line {4, 9, 10}",
            '<span class="clause-line"><b>Spieker Axes:</b> The Nagel line <span class="g-tok">{1, 2, 8, 10}</span> and the Fuhrmann–Spieker axis <span class="coincide-tok">{4, 9, 10}</span> meet at <span class="g-tok">X_10</span>.</span>',
            "MEDIAL INCIRCLE GEOMETRY",
            "Every property of X_1 in △ABC translates to X_10 inside the medial triangle M_a M_b M_c.",
        ),
        "s4": (
            "X_10 • X_1 • X_2 • X_8 • X_4 • X_9",
            '<span class="clause-line"><b>Spieker Network:</b> <span class="g-tok">X_10</span> bisects <span class="coincide-tok">X_1</span> and <span class="coincide-tok">X_8</span> through <span class="coincide-tok">X_2</span>, and aligns with <span class="eq-tok">X_4</span> and <span class="eq-tok">X_9</span>.</span>',
            "COLLECTION 1 ANCHOR",
            "Connects the incenter, centroid, orthocenter, Nagel point, and Mittenpunkt.",
        ),
    },
    {
        "num": 18,
        "code": "T_18",
        "slug": "apollonian-circles",
        "category": "Named Circles",
        "title": "The Apollonian Circles",
        "short_title": "APOLLONIAN CIRCLES",
        "enunciation": "The three circles of Apollonius passing through each vertex and its interior and exterior angle-bisector feet, intersecting at the 1st and 2nd Isodynamic Points X_15 and X_16.",
        "primary_center": 15,
        "centers": [15, 16, 3, 6, 13, 14],
        "pairs": [(15, 16), (13, 15), (14, 16)],
        "lines": [(3, 6, 15, 16), (6, 13, 16), (6, 14, 15)],
        "circles": ["apollonian_circles", "circumcircle"],
        "triangles": [],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the three Apollonian Circles are the loci of points whose distances to two vertices of triangle A B C are in the inverse ratio of the adjacent sides: <pause> P B to P C equals c to b, <pause> P C to P A equals a to c, <pause> and P A to P B equals b to a.

[bell:construction]
The A-Apollonian circle has diameter I a J a between the interior and exterior angle-bisector feet on side B C, <pause> and passes directly through vertex A. <pause> All three Apollonian circles belong to a coaxial pencil whose common chord is the Brocard axis.

[bell:insight]
Their two common intersection points are the First and Second Isodynamic Points X fifteen and X sixteen, <pause> where the distances to vertices A, B, and C are strictly inversely proportional to the sidelengths a, b, and c.
""",
        "s1": (
            "Three Apollonian Circles: PB/PC = c/b • PC/PA = a/c • PA/PB = b/a",
            '<span class="clause-line"><b>The Apollonian Circles:</b> Intersect on the Brocard axis at the 1st Isodynamic Point <span class="g-tok">X_15</span> and 2nd Isodynamic Point <span class="g-tok">X_16</span>, orthogonal to the <span class="coincide-tok">circumcircle</span>.</span>',
            "APOLLONIUS OF PERGA • LOCUS OF CONSTANT RATIO",
            "Diameter of the A-Apollonian circle is the harmonic segment between interior and exterior bisector feet on BC.",
        ),
        "s2": (
            "Coaxial Pencil Centered on the Lemoine Axis • Radical Axis = Brocard Axis",
            '<span class="clause-line"><b>Equidistant Pedal Property:</b> At <span class="g-tok">X_15</span> and <span class="coincide-tok">X_16</span>, vertex distances satisfy <span class="eq-tok">a·|PA| = b·|PB| = c·|PC|</span> and the pedal triangle is equilateral.</span>',
            "EQUILATERAL PEDAL TRIANGLES",
            "X_15 and X_16 are the unique points in the plane whose pedal triangles on △ABC are equilateral.",
        ),
        "s3": (
            "Brocard Axis {3, 6, 15, 16} & Symmedian Crossings {6, 13, 16} • {6, 14, 15}",
            '<span class="clause-line"><b>Apollonian Axes:</b> Radical axis <span class="g-tok">{3, 6, 15, 16}</span> meets Fermat–Isodynamic lines <span class="coincide-tok">{6, 13, 16}</span> and <span class="eq-tok">{6, 14, 15}</span> at <span class="g-tok">X_6</span>.</span>',
            "RADICAL CHORD",
            "All three Apollonian circles intersect orthogonally with the circumcircle of △ABC.",
        ),
        "s4": (
            "X_15 • X_16 • X_3 • X_6 • X_13 • X_14",
            '<span class="clause-line"><b>Isodynamic Network:</b> <span class="g-tok">X_15</span> and <span class="coincide-tok">X_16</span> pair isogonally with Fermat points <span class="eq-tok">X_13</span> and <span class="eq-tok">X_14</span> across <span class="coincide-tok">X_3, X_6</span>.</span>',
            "MOBIUS EQUILATERAL INVARIANCE",
            "A Möbius transformation sending X_15 to 0 and X_16 to ∞ maps △ABC to an equilateral triangle.",
        ),
    },
    {
        "num": 19,
        "code": "T_19",
        "slug": "brocard-and-orthocentroidal-circles",
        "category": "Named Circles",
        "title": "The Brocard & Orthocentroidal Circles",
        "short_title": "BROCARD & ORTHOCENTROIDAL CIRCLES",
        "enunciation": "Two fundamental diameter circles of triangle geometry: the Brocard Circle on diameter X_3 X_6 and the Orthocentroidal Circle on diameter X_2 X_4.",
        "primary_center": 6,
        "centers": [2, 3, 4, 5, 6, 19],
        "pairs": [(3, 6), (2, 4)],
        "lines": [(3, 6), (2, 3, 4, 5)],
        "circles": ["brocard_circle", "orthocentroidal_circle"],
        "triangles": ["medial"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> two classical circles are constructed directly on segments between Collection One centers: <pause> the Brocard Circle with diameter X three X six, <pause> and the Orthocentroidal Circle with diameter X two X four.

[bell:construction]
The Brocard circle passes through the Circumcenter X three, <pause> the Symmedian Point X six, <pause> the two Brocard points, <pause> and the vertices of the First and Second Brocard triangles. <pause> The Orthocentroidal circle has diameter from the Centroid X two to the Orthocenter X four along the Euler line.

[bell:insight]
By Andrew Guinand's nineteen eighty-four theorem, <pause> the Incenter X one always lies strictly inside the open orthocentroidal disk—except in an equilateral triangle—revealing the deep metric boundary governed by X two and X four.
""",
        "s1": (
            "Brocard Circle (Diameter X_3 X_6) • Orthocentroidal Circle (Diameter X_2 X_4)",
            '<span class="clause-line"><b>Diameter Circles:</b> The <span class="coincide-tok">Brocard circle</span> on diameter <span class="g-tok">X_3 X_6</span> and the <span class="eq-tok">orthocentroidal circle</span> on diameter <span class="g-tok">X_2 X_4</span>.</span>',
            "BROCARD (1881) & GUINAND (1984)",
            "Every pedal of X_6 onto the perpendicular bisectors lies on the Brocard circle.",
        ),
        "s2": (
            "Brocard Circle Center X_182 (Midpoint of X_3 X_6) • Orthocentroidal Center X_381 (Midpoint of X_2 X_4)",
            '<span class="clause-line"><b>Midpoint Centers:</b> Brocard diameter <span class="g-tok">X_3 X_6</span> and Euler diameter <span class="coincide-tok">X_2 X_4</span> bound the interior locus of <span class="eq-tok">X_1</span> and <span class="eq-tok">X_6</span>.</span>',
            "GUINAND'S THEOREM",
            "In any non-equilateral triangle, X_1 lies inside the orthocentroidal disk and never on the Euler line unless isosceles.",
        ),
        "s3": (
            "Brocard Axis {3, 6} & Euler Line {2, 3, 4, 5}",
            '<span class="clause-line"><b>Diameter Axes:</b> The Brocard axis <span class="g-tok">{3, 6}</span> and Euler line <span class="coincide-tok">{2, 3, 4, 5}</span> form the perpendicular diameters of the two circles at <span class="g-tok">X_3</span>.</span>',
            "RADICAL AXIS",
            "The radical axis of the circumcircle and Brocard circle is the Lemoine line.",
        ),
        "s4": (
            "X_2 • X_3 • X_4 • X_5 • X_6",
            '<span class="clause-line"><b>Five Classical Centers:</b> <span class="coincide-tok">X_2</span>, <span class="coincide-tok">X_3</span>, <span class="coincide-tok">X_4</span>, <span class="coincide-tok">X_5</span> on the Euler line and <span class="g-tok">X_6</span> on the Brocard circle.</span>',
            "CLAWSON & SYMMEDIAN GEOMETRY",
            "The orthocentroidal and Brocard circles are linked by pedal projections and isogonal inversion.",
        ),
    },
    # =========================================================================
    # IV. DERIVED CENTRAL TRIANGLES OF COLLECTION 1 (T_20 – T_24)
    # =========================================================================
    {
        "num": 20,
        "code": "T_20",
        "slug": "medial-and-anticomplementary-triangles",
        "category": "Derived Central Triangles",
        "title": "Medial & Anticomplementary Triangles",
        "short_title": "MEDIAL & ANTICOMPLEMENTARY TRIANGLES",
        "enunciation": "The Medial Triangle M_a M_b M_c formed by the side midpoints (cevian triangle of X_2) and the Anticomplementary Triangle formed by lines through A, B, C parallel to the opposite sides.",
        "primary_center": 2,
        "centers": [2, 1, 3, 4, 5, 8, 10],
        "pairs": [(3, 5), (4, 3), (1, 10), (8, 1)],
        "lines": [(2, 3, 4, 5), (1, 2, 8, 10)],
        "circles": ["nine_point_circle", "spieker_circle"],
        "triangles": ["medial"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Medial Triangle M a M b M c and the Anticomplementary Triangle A prime B prime C prime are the two central triangles generated by the Centroid X two. <pause> The medial triangle is the cevian triangle of X two, <pause> while the anticomplementary triangle is the anticevian triangle of X two.

[bell:construction]
Because the sides of both triangles are strictly parallel to the sides of reference triangle A B C, <pause> all three triangles are homothetic at the Centroid X two with scale factors one-half, <pause> one, <pause> and two.

[bell:insight]
This three-level hierarchy explains the core centers of Collection One at a glance: <pause> the circumcenter of the medial triangle is the Nine-Point Center X five; <pause> its orthocenter is the Circumcenter X three; <pause> its incenter is the Spieker Center X ten; <pause> and the incenter of the anticomplementary triangle is the Nagel Point X eight.
""",
        "s1": (
            "Medial Triangle M_a M_b M_c (Scale −1/2) • Anticomplementary Triangle (Scale −2)",
            '<span class="clause-line"><b>Medial & Anticomplementary Hierarchy:</b> Centered at <span class="g-tok">X_2</span>, the <span class="coincide-tok">medial triangle M_a M_b M_c</span> has circumcircle equal to the <span class="eq-tok">nine-point circle</span> and incircle equal to the <span class="eq-tok">Spieker circle</span>.</span>',
            "CEVIAN & ANTICEVIAN TRIANGLES OF X_2",
            "Area(Medial) = 1/4 Area(△ABC); Area(Anticomplementary) = 4 Area(△ABC).",
        ),
        "s2": (
            "Center Mapping: X_4 (Anticomp) ↦ X_3 (△ABC) ↦ X_5 (Medial)  •  X_8 ↦ X_1 ↦ X_10",
            '<span class="clause-line"><b>Shift of Centers:</b> Passing from anticomplementary to <span class="g-tok">△ABC</span> to medial maps <span class="coincide-tok">X_4 ↦ X_3 ↦ X_5</span> and <span class="eq-tok">X_8 ↦ X_1 ↦ X_10</span>.</span>',
            "THREE-GENERATION LADDER",
            "△ABC is simultaneously the medial triangle of its anticomplementary triangle.",
        ),
        "s3": (
            "Euler Line {2, 3, 4, 5} & Nagel Line {1, 2, 8, 10}",
            '<span class="clause-line"><b>Dual Homothetic Axes:</b> The Euler line <span class="g-tok">{2, 3, 4, 5}</span> and Nagel line <span class="coincide-tok">{1, 2, 8, 10}</span> cross at the common centroid <span class="g-tok">X_2</span>.</span>',
            "SHARED CENTROID X_2",
            "The medial, reference, and anticomplementary triangles all share the exact same centroid X_2.",
        ),
        "s4": (
            "X_2 • (X_4, X_3, X_5) • (X_8, X_1, X_10)",
            '<span class="clause-line"><b>Homothetic Triads:</b> <span class="g-tok">X_2</span> governs the Euler triad <span class="coincide-tok">X_3, X_4, X_5</span> and the Nagel triad <span class="eq-tok">X_1, X_8, X_10</span>.</span>',
            "UNIVERSAL TEMPLATE",
            "Every triangle center X_n has a medial counterpart (complement) and anticomplementary counterpart (anticomplement).",
        ),
    },
    {
        "num": 21,
        "code": "T_21",
        "slug": "orthic-and-tangential-triangles",
        "category": "Derived Central Triangles",
        "title": "Orthic & Tangential Triangles",
        "short_title": "ORTHIC & TANGENTIAL TRIANGLES",
        "enunciation": "The Orthic Triangle H_a H_b H_c formed by the altitude feet of X_4 and the Tangential Triangle formed by the tangents to the circumcircle at A, B, and C (perspector X_6).",
        "primary_center": 4,
        "centers": [4, 3, 5, 6, 19],
        "pairs": [(3, 4), (4, 6), (4, 19)],
        "lines": [(3, 4, 5), (3, 6), (4, 19)],
        "circles": ["nine_point_circle", "circumcircle"],
        "triangles": ["orthic"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Orthic Triangle H a H b H c and the Tangential Triangle T A T B T C form a classic dual pair. <pause> The orthic triangle is both the cevian and pedal triangle of the Orthocenter X four, <pause> while the tangential triangle is bounded by the tangents to the circumcircle at A, B, and C, <pause> with perspector at the Symmedian Point X six.

[bell:construction]
Because the circumcircle radius to each vertex A, B, C is perpendicular to the corresponding side of the orthic triangle, <pause> the sides of the orthic triangle and the sides of the tangential triangle are strictly parallel! <pause> Consequently, <pause> the orthic and tangential triangles are homothetic.

[bell:insight]
In acute triangles, <pause> the Orthocenter X four is the incenter of the orthic triangle, <pause> while the radical axis and cross-intersections of the orthic and reference triangles produce the Clawson Point X nineteen.
""",
        "s1": (
            "Orthic Triangle H_a H_b H_c (Perspector X_4) • Tangential Triangle (Perspector X_6)",
            '<span class="clause-line"><b>Orthic & Tangential Duality:</b> The <span class="coincide-tok">orthic triangle H_a H_b H_c</span> of <span class="g-tok">X_4</span> is inscribed in the <span class="eq-tok">nine-point circle</span> and homothetic to the tangential triangle of <span class="g-tok">X_6</span>.</span>',
            "FAGNANO'S MINIMUM PERIMETER TRIANGLE (1775)",
            "In any acute triangle, the orthic triangle has the minimum perimeter of all inscribed triangles.",
        ),
        "s2": (
            "Parallel Corresponding Sides: H_b H_c ∥ Tangent at A  (since OA ⊥ H_b H_c)",
            '<span class="clause-line"><b>Parallel Side Theorem:</b> Circumradii from <span class="g-tok">X_3</span> are perpendicular to the orthic sides <span class="coincide-tok">H_a H_b H_c</span>, making them parallel to the tangents of <span class="eq-tok">X_6</span>.</span>',
            "ORTHIC INCENTER X_4",
            "Altitudes AD, BE, CF bisect the interior angles of the orthic triangle H_a H_b H_c.",
        ),
        "s3": (
            "Euler Line {3, 4, 5} • Brocard Axis {3, 6} • Clawson Axis {4, 19}",
            '<span class="clause-line"><b>Orthic–Tangential Axes:</b> Euler line <span class="g-tok">{3, 4, 5}</span>, Brocard axis <span class="coincide-tok">{3, 6}</span>, and Clawson line <span class="eq-tok">{4, 19}</span>.</span>',
            "CLAWSON POINT X_19",
            "X_19 is the second center of similitude of the orthic and excentral configurations and perspector of the orthic axis.",
        ),
        "s4": (
            "X_4 • X_3 • X_5 • X_6 • X_19",
            '<span class="clause-line"><b>Orthic Network:</b> <span class="g-tok">X_4</span>, <span class="coincide-tok">X_3</span>, <span class="coincide-tok">X_5</span>, <span class="eq-tok">X_6</span>, and Clawson point <span class="eq-tok">X_19</span>.</span>',
            "POLAR TRIANGLE RESPECT TO CIRCUMCIRCLE",
            "The tangential triangle is the polar triangle of △ABC with respect to the circumcircle, and anticevian of X_6.",
        ),
    },
    {
        "num": 22,
        "code": "T_22",
        "slug": "intouch-and-extouch-triangles",
        "category": "Derived Central Triangles",
        "title": "Intouch (Contact) & Extouch Triangles",
        "short_title": "INTOUCH & EXTOUCH TRIANGLES",
        "enunciation": "The Intouch Triangle T_a T_b T_c formed by the points of tangency of the incircle (perspector X_7 Gergonne point) and the Extouch Triangle formed by the excircle touch points (perspector X_8 Nagel point).",
        "primary_center": 7,
        "centers": [7, 8, 1, 2, 9, 11],
        "pairs": [(7, 8), (2, 7), (2, 8)],
        "lines": [(1, 7), (1, 2, 8), (2, 7, 9)],
        "circles": ["incircle"],
        "triangles": ["intouch"],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Intouch Triangle T a T b T c—also called the Contact Triangle—and the Extouch Triangle E a E b E c record where the incircle and excircles touch the sidelines of triangle A B C.

[bell:construction]
By Ceva's theorem, <pause> the cevians to the three incircle touch points concur at the Gergonne Point X seven, <pause> making the intouch triangle both the pedal triangle of X one and the cevian triangle of X seven. <pause> The cevians to the three excircle touch points concur at the Nagel Point X eight, <pause> making the extouch triangle the cevian triangle of X eight.

[bell:insight]
Because each intouch vertex and extouch vertex are equidistant from the opposite ends of their side, <pause> the intouch and extouch triangles are isotomic duals, <pause> and X seven and X eight are isotomic conjugates.
""",
        "s1": (
            "Intouch Triangle T_a T_b T_c (Perspector X_7) • Extouch Triangle E_a E_b E_c (Perspector X_8)",
            '<span class="clause-line"><b>Contact Triangles:</b> The <span class="coincide-tok">intouch triangle T_a T_b T_c</span> inscribed in the <span class="eq-tok">incircle</span> has perspector <span class="g-tok">X_7</span>, while the extouch triangle has perspector <span class="g-tok">X_8</span>.</span>',
            "JOSEPH DIAZ GERGONNE (1818) & CHRISTIAN VON NAGEL (1836)",
            "Intouch triangle is the pedal triangle of X_1 and cevian triangle of X_7.",
        ),
        "s2": (
            "Symmetric Touch Segments: BT_a = CE_a = s−b  •  CT_a = BE_a = s−c",
            '<span class="clause-line"><b>Isotomic Touch Feet:</b> Intouch perspector <span class="g-tok">X_7 = 1/(s−a) : 1/(s−b) : 1/(s−c)</span> and extouch perspector <span class="coincide-tok">X_8 = s−a : s−b : s−c</span> are reciprocal in <span class="eq-tok">barycentrics</span>.</span>',
            "EQUAL AREA PROPERTY",
            "The intouch triangle T_a T_b T_c and extouch triangle E_a E_b E_c always have the exact same area: 2Δ²r / (abc).",
        ),
        "s3": (
            "Soddy Line {1, 7} • Nagel Line {1, 2, 8} • Mittenpunkt Line {2, 7, 9}",
            '<span class="clause-line"><b>Contact Central Lines:</b> Soddy axis <span class="g-tok">{1, 7}</span>, Nagel axis <span class="coincide-tok">{1, 2, 8}</span>, and Gergonne–Centroid–Mittenpunkt line <span class="eq-tok">{2, 7, 9}</span>.</span>',
            "COMPLEMENT OF GERGONNE POINT IS MITTENPUNKT X_9",
            "Under homothety at X_2, X_1 maps to X_8 (anticomplement), while X_9 is the complement of X_7.",
        ),
        "s4": (
            "X_7 ↔ X_8 • X_1 • X_2 • X_9",
            '<span class="clause-line"><b>Contact Quartet:</b> Gergonne <span class="g-tok">X_7</span> and Nagel <span class="coincide-tok">X_8</span> pair across <span class="eq-tok">X_1</span>, <span class="eq-tok">X_2</span>, and <span class="eq-tok">X_9</span>.</span>',
            "SPLITTER SEGMENTS",
            "The cevians through X_8 bisect the perimeter of △ABC and are called the splitters of the triangle.",
        ),
    },
    {
        "num": 23,
        "code": "T_23",
        "slug": "incentral-and-excentral-triangles",
        "category": "Derived Central Triangles",
        "title": "Incentral & Excentral Triangles",
        "short_title": "INCENTRAL & EXCENTRAL TRIANGLES",
        "enunciation": "The Incentral Triangle I_a I_b I_c (cevian triangle of X_1) formed by the interior angle-bisector feet and the Excentral Triangle J_a J_b J_c (anticevian triangle of X_1) formed by the three excenters.",
        "primary_center": 1,
        "centers": [1, 3, 4, 6, 9],
        "pairs": [(1, 9), (1, 3), (4, 9)],
        "lines": [(1, 6, 9), (1, 3), (4, 9)],
        "circles": ["incircle", "circumcircle"],
        "triangles": [],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> the Incentral Triangle I a I b I c and the Excentral Triangle J a J b J c are the cevian and anticevian triangles of the Incenter X one. <pause> Their six vertices are the harmonic bisector feet and the three excenters of triangle A B C.

[bell:construction]
Because the interior and exterior angle bisectors at each vertex A, B, and C are strictly perpendicular, <pause> the vertices A, B, C are the altitude feet of the excentral triangle, <pause> and the Incenter X one is the orthocenter of the excentral triangle!

[bell:insight]
This makes reference triangle A B C the orthic triangle of its own excentral triangle, <pause> and the circumcircle of A B C is the nine-point circle of the excentral triangle. <pause> Meanwhile, <pause> connecting the excenters through the side midpoints produces the Mittenpunkt X nine, <pause> the symmedian point of the excentral triangle.
""",
        "s1": (
            "Incentral Triangle I_a I_b I_c (Cevian of X_1) • Excentral Triangle J_a J_b J_c (Anticevian of X_1)",
            '<span class="clause-line"><b>Bisector Triangles:</b> Interior angle bisectors through <span class="g-tok">X_1</span> form the incentral feet <span class="g-tok">I_a, I_b, I_c</span>, while the <span class="coincide-tok">incircle</span> and <span class="eq-tok">circumcircle</span> govern the excentral duality.</span>',
            "ORTHOCENTRIC SYSTEM {X_1, J_a, J_b, J_c}",
            "X_1 and the three excenters form an orthocentric system: each point is the orthocenter of the other three.",
        ),
        "s2": (
            "△ABC is the Orthic Triangle of the Excentral Triangle • Mittenpunkt X_9 is its Symmedian Point",
            '<span class="clause-line"><b>Excentral Shift:</b> <span class="g-tok">X_1</span> is the orthocenter of the excentral triangle, the <span class="coincide-tok">circumcircle</span> is its nine-point circle, and <span class="eq-tok">X_9</span> is its symmedian point.</span>',
            "BEVAN CIRCLE (RADIUS 2R)",
            "Since △ABC is the orthic triangle of J_a J_b J_c, the circumcircle of J_a J_b J_c (the Bevan circle) has radius 2R.",
        ),
        "s3": (
            "Incenter–Symmedian–Mittenpunkt Line {1, 6, 9} • OI Line {1, 3} • Fuhrmann Axis {4, 9}",
            '<span class="clause-line"><b>Excentral Axes:</b> Symmedian–Mittenpunkt line <span class="g-tok">{1, 6, 9}</span>, OI line <span class="coincide-tok">{1, 3}</span>, and orthocenter–Mittenpunkt axis <span class="eq-tok">{4, 9}</span>.</span>',
            "MITTENPUNKT CONCURRENCE",
            "Lines from the excenters to the side midpoints M_a, M_b, M_c concur at Mittenpunkt X_9.",
        ),
        "s4": (
            "X_1 • X_9 • X_6 • X_3 • X_4",
            '<span class="clause-line"><b>Excentral Network:</b> <span class="g-tok">X_1</span> and <span class="coincide-tok">X_9</span> link <span class="coincide-tok">X_6</span>, <span class="eq-tok">X_3</span>, and <span class="eq-tok">X_4</span>.</span>',
            "EXCENTRAL ↔ ORTHIC ISOMORPHISM",
            "Every theorem about the orthic triangle of △ABC has a dual theorem about △ABC inside the excentral triangle.",
        ),
    },
    {
        "num": 24,
        "code": "T_24",
        "slug": "isogonic-and-napoleon-triangles",
        "category": "Derived Central Triangles",
        "title": "Equilateral, Isogonic & Napoleon Triangles",
        "short_title": "ISOGONIC & NAPOLEON TRIANGLES",
        "enunciation": "The outer and inner equilateral triangles erected on sides BC, CA, AB, whose apexes form the Isogonic Triangles (perspectors X_13, X_14) and whose centers form the equilateral Napoleon Triangles (perspectors X_17, X_18).",
        "primary_center": 17,
        "centers": [13, 14, 15, 16, 17, 18, 2, 3, 4],
        "pairs": [(13, 17), (14, 18), (17, 18)],
        "lines": [(2, 13, 17), (4, 13, 18), (3, 17, 18)],
        "circles": ["circumcircle"],
        "triangles": [],
        "script": """[bell:proposition]
In the Encyclopedia of Triangle Centers, <pause> erecting equilateral triangles outward and inward on the three sides of triangle A B C generates two celebrated pairs of central triangles: <pause> the outer and inner Isogonic Triangles, <pause> and the outer and inner Napoleon Triangles.

[bell:construction]
Connecting the three outer equilateral apexes to the opposite vertices A, B, C yields three equal segments concurring at the First Fermat Point X thirteen at sixty-degree angles; <pause> the inner apexes concur at the Second Fermat Point X fourteen. <pause> Meanwhile, <pause> by Napoleon's Theorem, <pause> the centroids of the three outer equilateral triangles form a strictly equilateral triangle—the Outer Napoleon Triangle—and the inner centroids form the Inner Napoleon Triangle.

[bell:insight]
Both Napoleon triangles share the exact same centroid X two as reference triangle A B C, <pause> their area difference equals the area of A B C, <pause> and their perspectors with A B C are the First and Second Napoleon Points X seventeen and X eighteen.
""",
        "s1": (
            "Isogonic Triangles (Perspectors X_13, X_14) • Napoleon Triangles (Perspectors X_17, X_18)",
            '<span class="clause-line"><b>Equilateral Constructions:</b> Outer and inner equilateral apexes yield Fermat points <span class="g-tok">X_13, X_14</span>, while their centroids form equilateral triangles with perspectors <span class="g-tok">X_17</span>, <span class="g-tok">X_18</span> on the <span class="coincide-tok">circumcircle</span> stage.</span>',
            "NAPOLEON'S THEOREM",
            "For any triangle ABC, the centers of outer (or inner) equilateral triangles on its sides form an equilateral triangle.",
        ),
        "s2": (
            "Area(Outer Napoleon) − Area(Inner Napoleon) = Area(△ABC)  •  Shared Centroid X_2",
            '<span class="clause-line"><b>Area & Centroid Invariance:</b> Both Napoleon triangles have centroid <span class="g-tok">X_2</span>, while <span class="coincide-tok">X_13, X_14</span> and <span class="eq-tok">X_17, X_18</span> correspond to Kiepert angles <span class="eq-tok">±60° and ±30°</span>.</span>',
            "TORRICELLI CIRCLES",
            "The circumcircles of the three outer equilateral triangles concur at the 1st Fermat point X_13.",
        ),
        "s3": (
            "Kiepert Chords {2, 13, 17} • {4, 13, 18} • {3, 17, 18}",
            '<span class="clause-line"><b>Napoleon Central Lines:</b> Centroid axis <span class="g-tok">{2, 13, 17}</span>, orthocenter axis <span class="coincide-tok">{4, 13, 18}</span>, and circumcenter axis <span class="eq-tok">{3, 17, 18}</span>.</span>',
            "COLLINEAR EQUILATERAL CENTERS",
            "X_17 and X_18 are isogonal conjugates of each other's pedal/circumcircle partners on the Kiepert hyperbola.",
        ),
        "s4": (
            "X_17 • X_18 • X_13 • X_14 • X_15 • X_16",
            '<span class="clause-line"><b>Equilateral Six-Center Family:</b> Napoleon points <span class="g-tok">X_17</span>, <span class="coincide-tok">X_18</span>, Fermat points <span class="eq-tok">X_13, X_14</span>, and Isodynamic points <span class="coincide-tok">X_15, X_16</span>.</span>',
            "COLLECTION 1 CAPSTONE",
            "Completes the equilateral geometry of Collection 1 before Clawson point X_19.",
        ),
    },
]


# ---------------------------------------------------------------------------
# SVG Builders for Topic Videos
# ---------------------------------------------------------------------------


def build_topic_model(
    topic: dict[str, Any],
    reg: CenterRegistry,
    include_all_lines: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for `topic` with tiny-dotted lines, solid segments, and exact element IDs."""
    ctx = reg.ctx
    model = Model(f"{topic['code']}: {topic['title']}")

    A = _add_point(model, 0.0, 0.0, ID="A", classes=["given", "vertex"])
    B = _add_point(model, 1.0, 0.0, ID="B", classes=["given", "vertex"])
    C = _add_point(model, ctx.C_xy[0], ctx.C_xy[1], ID="C", classes=["vertex"])

    _add_line(model, A, B, ID="[ A B ]", classes=["given", "sideline"])
    _add_line(model, B, C, ID="[ B C ]", classes=["sideline"])
    _add_line(model, C, A, ID="[ C A ]", classes=["sideline"])
    _add_polygon(model, [A, B, C], ID="< A B C >", classes=["reference"])

    # Derived triangles requested by the topic
    tri_kinds = topic.get("triangles") or []
    if "medial" in tri_kinds:
        Ma = _add_point(model, 0.5 * (1.0 + ctx.C_xy[0]), 0.5 * ctx.C_xy[1], ID="M_a", classes=["guide"], guide=True)
        Mb = _add_point(model, 0.5 * ctx.C_xy[0], 0.5 * ctx.C_xy[1], ID="M_b", classes=["guide"], guide=True)
        Mc = _add_point(model, 0.5, 0.0, ID="M_c", classes=["guide"], guide=True)
        _add_polygon(model, [Ma, Mb, Mc], ID="< M_a M_b M_c >", classes=["secondary"])
        if topic["slug"] in ("isotomic-conjugate", "complement-and-anticomplement", "medial-and-anticomplementary-triangles"):
            _add_line(model, A, Ma, ID="[ A M_a ]", classes=["bisector"])
            _add_line(model, B, Mb, ID="[ B M_b ]", classes=["bisector"])
            _add_line(model, C, Mc, ID="[ C M_c ]", classes=["bisector"])

    if "orthic" in tri_kinds:
        # Altitude feet H_a, H_b, H_c
        def _proj(px: float, py: float, x1: float, y1: float, x2: float, y2: float) -> tuple[float, float]:
            dx, dy = x2 - x1, y2 - y1
            t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)
            return x1 + t * dx, y1 + t * dy

        hax, hay = _proj(0.0, 0.0, 1.0, 0.0, ctx.C_xy[0], ctx.C_xy[1])
        hbx, hby = _proj(1.0, 0.0, ctx.C_xy[0], ctx.C_xy[1], 0.0, 0.0)
        hcx, hcy = _proj(ctx.C_xy[0], ctx.C_xy[1], 0.0, 0.0, 1.0, 0.0)
        Ha = _add_point(model, hax, hay, ID="H_a", classes=["guide"], guide=True)
        Hb = _add_point(model, hbx, hby, ID="H_b", classes=["guide"], guide=True)
        Hc = _add_point(model, hcx, hcy, ID="H_c", classes=["guide"], guide=True)
        _add_polygon(model, [Ha, Hb, Hc], ID="< H_a H_b H_c >", classes=["secondary"])
        _add_line(model, A, Ha, ID="[ A H_a ]", classes=["bisector"])
        _add_line(model, B, Hb, ID="[ B H_b ]", classes=["bisector"])
        _add_line(model, C, Hc, ID="[ C H_c ]", classes=["bisector"])

    if "intouch" in tri_kinds:
        x1_xy = reg.xy_cache.get(1, (0.5, 0.2))
        def _proj_in(px: float, py: float, x1: float, y1: float, x2: float, y2: float) -> tuple[float, float]:
            dx, dy = x2 - x1, y2 - y1
            t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)
            return x1 + t * dx, y1 + t * dy

        tax, tay = _proj_in(x1_xy[0], x1_xy[1], 1.0, 0.0, ctx.C_xy[0], ctx.C_xy[1])
        tbx, tby = _proj_in(x1_xy[0], x1_xy[1], ctx.C_xy[0], ctx.C_xy[1], 0.0, 0.0)
        tcx, tcy = _proj_in(x1_xy[0], x1_xy[1], 0.0, 0.0, 1.0, 0.0)
        Ta = _add_point(model, tax, tay, ID="T_a", classes=["guide"], guide=True)
        Tb = _add_point(model, tbx, tby, ID="T_b", classes=["guide"], guide=True)
        Tc = _add_point(model, tcx, tcy, ID="T_c", classes=["guide"], guide=True)
        _add_polygon(model, [Ta, Tb, Tc], ID="< T_a T_b T_c >", classes=["secondary"])
        _add_line(model, A, Ta, ID="[ A T_a ]", classes=["bisector"])
        _add_line(model, B, Tb, ID="[ B T_b ]", classes=["bisector"])
        _add_line(model, C, Tc, ID="[ C T_c ]", classes=["bisector"])

    if topic["slug"] in ("isogonal-conjugate", "incentral-and-excentral-triangles"):
        # Interior angle bisector feet I_a, I_b, I_c
        a_l, b_l, c_l = ctx.raw_a, ctx.raw_b, ctx.raw_c
        ia_x = (b_l * 1.0 + c_l * ctx.C_xy[0]) / (b_l + c_l)
        ia_y = (c_l * ctx.C_xy[1]) / (b_l + c_l)
        ib_x = (c_l * ctx.C_xy[0]) / (a_l + c_l)
        ib_y = (c_l * ctx.C_xy[1]) / (a_l + c_l)
        ic_x = b_l / (a_l + b_l)
        Ia = _add_point(model, ia_x, ia_y, ID="I_a", classes=["guide"], guide=True)
        Ib = _add_point(model, ib_x, ib_y, ID="I_b", classes=["guide"], guide=True)
        Ic = _add_point(model, ic_x, 0.0, ID="I_c", classes=["guide"], guide=True)
        _add_line(model, A, Ia, ID="[ A I_a ]", classes=["bisector"])
        _add_line(model, B, Ib, ID="[ B I_b ]", classes=["bisector"])
        _add_line(model, C, Ic, ID="[ C I_c ]", classes=["bisector"])

    pts_by_num: dict[int, Any] = {}

    def ensure_c_pt(k: int, is_primary: bool = False) -> Any:
        if k in pts_by_num:
            return pts_by_num[k]
        xy = reg.xy_cache.get(k)
        if xy is None:
            return None
        cls = ["selected", "target"] if is_primary else ["center"]
        pt = _add_point(model, xy[0], xy[1], ID=f"X_{k}", classes=cls)
        pts_by_num[k] = pt
        return pt

    primary_c = int(topic.get("primary_center", 1))
    for k in topic.get("centers", [1, 2, 3, 4, 5, 6]):
        ensure_c_pt(k, is_primary=(k == primary_c))

    # Named circles requested by the topic
    cir_kinds = topic.get("circles") or []
    if "incircle" in cir_kinds:
        p1 = ensure_c_pt(1, is_primary=(primary_c == 1))
        if p1 is not None:
            _add_circle(model, p1, ctx.r * ctx.scale, ID="incircle", classes=["incircle"])
    if "circumcircle" in cir_kinds:
        p3 = ensure_c_pt(3, is_primary=(primary_c == 3))
        if p3 is not None:
            _add_circle(model, p3, A, ID="circumcircle", classes=["circumcircle"])
    if "nine_point_circle" in cir_kinds:
        p5 = ensure_c_pt(5, is_primary=(primary_c == 5))
        if p5 is not None:
            _add_circle(model, p5, 0.5 * ctx.R * ctx.scale, ID="nine_point_circle", classes=["nine_point_circle"])
    if "spieker_circle" in cir_kinds:
        p10 = ensure_c_pt(10, is_primary=(primary_c == 10))
        if p10 is not None:
            _add_circle(model, p10, 0.5 * ctx.r * ctx.scale, ID="spieker_circle", classes=["secondary_circle"])
    if "brocard_circle" in cir_kinds:
        xy3 = reg.xy_cache.get(3)
        xy6 = reg.xy_cache.get(6)
        if xy3 and xy6:
            mx, my = 0.5 * (xy3[0] + xy6[0]), 0.5 * (xy3[1] + xy6[1])
            r_br = 0.5 * math.hypot(xy6[0] - xy3[0], xy6[1] - xy3[1])
            p_br = _add_point(model, mx, my, ID="X_182", classes=["guide"], guide=True)
            _add_circle(model, p_br, r_br, ID="brocard_circle", classes=["secondary_circle"])
    if "orthocentroidal_circle" in cir_kinds:
        xy2 = reg.xy_cache.get(2)
        xy4 = reg.xy_cache.get(4)
        if xy2 and xy4:
            mx, my = 0.5 * (xy2[0] + xy4[0]), 0.5 * (xy2[1] + xy4[1])
            r_oc = 0.5 * math.hypot(xy4[0] - xy2[0], xy4[1] - xy2[1])
            p_oc = _add_point(model, mx, my, ID="X_381", classes=["guide"], guide=True)
            _add_circle(model, p_oc, r_oc, ID="orthocentroidal_circle", classes=["nine_point_circle"])
    if "apollonian_circles" in cir_kinds:
        # C-Apollonian circle: PA / PB = b / a on baseline AB
        ratio = ctx.raw_b / ctx.raw_a
        if abs(ratio - 1.0) > 1e-4:
            x_in = ratio / (1.0 + ratio)
            x_ex = ratio / (ratio - 1.0)
            cx_ap = 0.5 * (x_in + x_ex)
            r_ap = 0.5 * abs(x_ex - x_in)
            p_ap = _add_point(model, cx_ap, 0.0, ID="O_C", classes=["guide"], guide=True)
            _add_circle(model, p_ap, r_ap, ID="apollonian_circle", classes=["secondary_circle"])

    # Central lines
    existing_line_ids: set[str] = set()
    for l_tuple in topic.get("lines", []):
        valid = [k for k in l_tuple if k in reg.xy_cache]
        if len(valid) >= 2:
            for k in valid:
                ensure_c_pt(k, is_primary=(k == primary_c))
            c1, c2 = valid[0], valid[1]
            p1, p2 = pts_by_num[c1], pts_by_num[c2]
            i_min, i_max = min(c1, c2), max(c1, c2)
            lid = f"{{ {i_min}, {i_max} }}"
            if lid not in existing_line_ids:
                _add_line(model, p1, p2, ID=lid, classes=["central_line"])
                existing_line_ids.add(lid)

    if include_all_lines:
        # Also parse brace sets {a, b, ...} in s3_clause
        s3_clause = topic.get("s3", ("", ""))[1]
        for m in re.finditer(r"\{([\d,\s]+)\}", s3_clause):
            bnums = [int(x) for x in re.findall(r"\d+", m.group(1)) if int(x) in reg.xy_cache]
            if len(bnums) >= 2:
                for k in bnums:
                    ensure_c_pt(k, is_primary=(k == primary_c))
                c1, c2 = bnums[0], bnums[1]
                i_min, i_max = min(c1, c2), max(c1, c2)
                lid = f"{{ {i_min}, {i_max} }}"
                if lid not in existing_line_ids:
                    _add_line(model, pts_by_num[c1], pts_by_num[c2], ID=lid, classes=["central_line"])
                    existing_line_ids.add(lid)

        # Also add lines for pairs and s4 partner tokens
        extra_pairs = list(topic.get("pairs", []))
        s4_clause = topic.get("s4", ("", ""))[1]
        for m in re.finditer(r"X_(\d+)\b", s4_clause):
            k = int(m.group(1))
            if k != primary_c:
                extra_pairs.append((primary_c, k))

        for p1_num, p2_num in extra_pairs:
            if p1_num in reg.xy_cache and p2_num in reg.xy_cache and p1_num != p2_num:
                pt1 = ensure_c_pt(p1_num, is_primary=(p1_num == primary_c))
                pt2 = ensure_c_pt(p2_num, is_primary=(p2_num == primary_c))
                i_min, i_max = min(p1_num, p2_num), max(p1_num, p2_num)
                lid = f"{{ {i_min}, {i_max} }}"
                if lid not in existing_line_ids:
                    _add_line(model, pt1, pt2, ID=lid, classes=["central_line"])
                    existing_line_ids.add(lid)

    # Promote primary center to top
    if primary_c in pts_by_num:
        t_pt = pts_by_num[primary_c]
        if t_pt in model:
            tdata = model.pop(t_pt)
            model[t_pt] = tdata

    return model


def generate_topic_overview_svg(topic: dict[str, Any], reg: CenterRegistry) -> str:
    """Render a dark-mode diagram card for Step 3 (`02_overview.svg`) illustrating the algebraic & geometric action of `topic`."""
    ctx = reg.ctx
    Ax, Ay = 0.0, 0.0
    Bx, By = 1.0, 0.0
    Cx, Cy = ctx.C_xy

    scale = 480.0
    ox = 500.0 - 0.5 * scale
    oy = 425.0

    def to_svg(x: float, y: float) -> tuple[float, float]:
        return (ox + x * scale, oy - y * scale)

    As = to_svg(Ax, Ay)
    Bs = to_svg(Bx, By)
    Cs = to_svg(Cx, Cy)

    p_num = int(topic.get("primary_center", 1))
    px, py = reg.xy_cache.get(p_num, (0.5, 0.2))
    Ps = to_svg(px, py)

    pairs = topic.get("pairs") or [(1, 2)]
    pair_colors = ["#e8b85a", "#38bdf8", "#5ec27e"]
    pair_lines_svg: list[str] = []
    pts_svg: list[str] = []
    drawn_nums: set[int] = set()

    for idx, (c1, c2) in enumerate(pairs[:3]):
        col = pair_colors[idx % len(pair_colors)]
        xy1 = reg.xy_cache.get(c1)
        xy2 = reg.xy_cache.get(c2)
        if xy1 and xy2:
            s1 = to_svg(*xy1)
            s2 = to_svg(*xy2)
            dx, dy = s2[0] - s1[0], s2[1] - s1[1]
            L = math.hypot(dx, dy)
            if L > 1e-3:
                ux, uy = dx / L, dy / L
                pair_lines_svg.append(
                    f'<line x1="{s1[0] - 280*ux:.1f}" y1="{s1[1] - 280*uy:.1f}" '
                    f'x2="{s2[0] + 280*ux:.1f}" y2="{s2[1] + 280*uy:.1f}" '
                    f'stroke="{col}" stroke-width="2.4" stroke-dasharray="2, 4.5" stroke-linecap="round" opacity="0.7" />'
                )
                pair_lines_svg.append(
                    f'<line x1="{s1[0]:.1f}" y1="{s1[1]:.1f}" x2="{s2[0]:.1f}" y2="{s2[1]:.1f}" '
                    f'stroke="{col}" stroke-width="4.2" stroke-linecap="round" />'
                )
            for cn, sc in ((c1, s1), (c2, s2)):
                if cn not in drawn_nums:
                    drawn_nums.add(cn)
                    pts_svg.append(
                        f'<circle cx="{sc[0]:.1f}" cy="{sc[1]:.1f}" r="7.5" fill="{col}" stroke="#0b0e15" stroke-width="2.2" />'
                        f'<text x="{sc[0] + 12:.1f}" y="{sc[1] - 10:.1f}" fill="{col}" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">'
                        f'X<tspan dy="4" font-size="12">{cn}</tspan></text>'
                    )

    s1_sym = html.escape(topic["s1"][0][:58])
    s2_sym = html.escape(topic["s2"][0][:58])
    s3_sym = html.escape(topic["s3"][0][:58])

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 760" width="100%" height="100%">
  <defs>
    <filter id="glow-topic" filterUnits="userSpaceOnUse" x="-100" y="-100" width="1200" height="960">
      <feGaussianBlur stdDeviation="3.5" result="blur" />
      <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
    </filter>
  </defs>

  <polygon points="{As[0]:.1f},{As[1]:.1f} {Bs[0]:.1f},{Bs[1]:.1f} {Cs[0]:.1f},{Cs[1]:.1f}" fill="rgba(54, 102, 204, 0.14)" stroke="#3b82f6" stroke-width="4.2" stroke-linejoin="round" />

  {"".join(pair_lines_svg)}
  {"".join(pts_svg)}

  <circle cx="{As[0]:.1f}" cy="{As[1]:.1f}" r="6.5" fill="#66ff66" stroke="#0d111a" stroke-width="2" />
  <circle cx="{Bs[0]:.1f}" cy="{Bs[1]:.1f}" r="6.5" fill="#66ff66" stroke="#0d111a" stroke-width="2" />
  <circle cx="{Cs[0]:.1f}" cy="{Cs[1]:.1f}" r="6.5" fill="#f8f6f0" stroke="#0d111a" stroke-width="2" />
  <text x="{As[0] - 24:.1f}" y="{As[1] + 22:.1f}" fill="#88ff88" font-family="JetBrains Mono, monospace" font-size="20" font-weight="bold">A</text>
  <text x="{Bs[0] + 12:.1f}" y="{Bs[1] + 22:.1f}" fill="#88ff88" font-family="JetBrains Mono, monospace" font-size="20" font-weight="bold">B</text>
  <text x="{Cs[0] - 8:.1f}" y="{Cs[1] - 16:.1f}" fill="#f8f6f0" font-family="JetBrains Mono, monospace" font-size="20" font-weight="bold">C</text>

  <circle cx="{Ps[0]:.1f}" cy="{Ps[1]:.1f}" r="9.5" fill="#ffd700" stroke="#00ffff" stroke-width="2.8" filter="url(#glow-topic)" />

  <!-- Bottom Summary Cards -->
  <g transform="translate(42, 548)">
    <rect x="0" y="0" width="916" height="184" rx="14" fill="rgba(11, 14, 21, 0.94)" stroke="rgba(232, 184, 90, 0.45)" stroke-width="1.5" />
    <text x="24" y="34" fill="#94a3b8" font-family="JetBrains Mono, monospace" font-size="14" font-weight="bold" letter-spacing="0.8">{html.escape(topic["category"].upper())} • {html.escape(topic["code"])}</text>
    <text x="892" y="34" text-anchor="end" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="15" font-weight="bold">{html.escape(topic["short_title"])}</text>

    <rect x="24" y="52" width="12" height="24" rx="3" fill="#e8b85a" />
    <text x="48" y="70" fill="#e8b85a" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">{s1_sym}</text>

    <rect x="24" y="94" width="12" height="24" rx="3" fill="#38bdf8" />
    <text x="48" y="112" fill="#38bdf8" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">{s2_sym}</text>

    <rect x="24" y="136" width="12" height="24" rx="3" fill="#5ec27e" />
    <text x="48" y="154" fill="#5ec27e" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">{s3_sym}</text>
  </g>
</svg>"""


def build_topic_video_package(
    topic: dict[str, Any],
    svgs_dir: Path,
    acute_reg: CenterRegistry,
    regs_by_preset: dict[str, tuple[str, TriangleContext, CenterRegistry]],
) -> tuple[str, list[dict[str, Any]]]:
    """Generate the 5 SVGs, `script.txt`, and 7-subslide `scenes.json` for `topic` with sequenced line/circle highlights."""
    svgs_dir.mkdir(parents=True, exist_ok=True)
    primary_c = int(topic.get("primary_center", 1))

    # 1. Primary model SVG (with tiny-dotted lines and solid segments)
    m_primary = build_topic_model(topic, acute_reg, include_all_lines=False)
    svg_primary = render_model_svg(m_primary)
    (svgs_dir / "01_primary.svg").write_text(svg_primary, encoding="utf-8")

    # 2. Overview coordinate/mapping SVG
    svg_overview = generate_topic_overview_svg(topic, acute_reg)
    (svgs_dir / "02_coordinates.svg").write_text(svg_overview, encoding="utf-8")

    # 3. Central lines SVG (all lines & pairs visible)
    m_lines = build_topic_model(topic, acute_reg, include_all_lines=True)
    svg_lines = render_model_svg(m_lines).replace(
        'class="geometor-etc-drawing"',
        'class="geometor-etc-drawing show-lines"',
        1,
    )
    (svgs_dir / "03_central_lines.svg").write_text(svg_lines, encoding="utf-8")
    (svgs_dir / "04_relations.svg").write_text(svg_lines, encoding="utf-8")

    # 4. Four-triangle invariance SVG
    svg_four = generate_four_triangles_svg(primary_c, regs_by_preset)
    (svgs_dir / "05_four_triangles.svg").write_text(svg_four, encoding="utf-8")

    # Parse primary SVG IDs for Step 1 & Step 2 sequencing
    from .video import (
        _normalize_relations_clause,
        _parse_primary_svg_elements,
        _sequence_central_lines_clause,
    )

    s1_sym, s1_clause, s1_jid, s1_jtitle = topic["s1"]
    s2_sym, s2_clause, s2_jid, s2_jtitle = topic["s2"]
    s3_sym, s3_clause, s3_jid, s3_jtitle = topic["s3"]
    s4_sym, s4_clause, s4_jid, s4_jtitle = topic["s4"]

    construction_ids, secondary_poly_ids, circle_ids = _parse_primary_svg_elements(
        svgs_dir / "01_primary.svg", primary_c, s1_clause
    )
    for k in topic.get("centers", [])[:3]:
        if f"X_{k}" not in construction_ids:
            construction_ids.append(f"X_{k}")

    s1a_clause = _mute_other_spans(s1_clause, {"g-tok"})
    s1b_clause = s1_clause

    s3a_clause, s3b_clause, l_active, l_coincide, l_equal = _sequence_central_lines_clause(
        s3_clause, primary_c, is_topic=True
    )
    s4_norm_clause, rel_active, rel_coincide, rel_equal = _normalize_relations_clause(
        s4_clause, primary_c, acute_reg, is_topic=True
    )

    common = {
        "prop_id": f"ETC • {topic['code']}",
        "short_code": topic["code"],
        "g_id": topic["short_title"],
        "folio": f"Kimberling ETC • {topic['category']}",
        "enunciation": topic["enunciation"],
        "step_total": 7,
        "visible_ids": ["*"],
    }

    scenes = [
        {
            "id": "act_1_definition",
            "title": f"{topic['code']} {topic['short_title']} — Geometric Definition",
            "subslides": [
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 1.0,
                    "step_num": 1,
                    "step_kind": "CONSTRUCT",
                    "svg_path": str(svgs_dir / "01_primary.svg"),
                    "symbolic": s1_sym,
                    "clause_html": s1a_clause,
                    "just_tag": "∵ DEFINITION",
                    "just_id": s1_jid,
                    "just_title": s1_jtitle,
                    "strict_step_ids": True,
                    "active_ids": construction_ids,
                    "coincide_ids": [],
                    "equal_ids": [],
                },
                {
                    **common,
                    "type": "euclid_step",
                    "is_punchline": True,
                    "weight": 1.0,
                    "step_num": 2,
                    "step_kind": "GOAL",
                    "svg_path": str(svgs_dir / "01_primary.svg"),
                    "symbolic": s1_sym,
                    "clause_html": s1b_clause,
                    "just_tag": "∵ STRUCTURE",
                    "just_id": s1_jid,
                    "just_title": s1_jtitle,
                    "strict_step_ids": True,
                    "active_ids": construction_ids,
                    "coincide_ids": secondary_poly_ids if secondary_poly_ids else circle_ids[:1],
                    "equal_ids": circle_ids if secondary_poly_ids else circle_ids[1:],
                },
            ],
        },
        {
            "id": "act_2_algebra_and_lines",
            "title": f"{topic['code']} Algebraic Action & Central Lines",
            "subslides": [
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 1.15,
                    "step_num": 3,
                    "step_kind": "ASSERT",
                    "svg_path": str(svgs_dir / "02_coordinates.svg"),
                    "symbolic": s2_sym,
                    "clause_html": s2_clause,
                    "just_tag": "∵ COORDINATE LAW",
                    "just_id": s2_jid,
                    "just_title": s2_jtitle,
                },
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 0.5,
                    "step_num": 4,
                    "step_kind": "INTERSECT",
                    "svg_path": str(svgs_dir / "03_central_lines.svg"),
                    "symbolic": s3_sym,
                    "clause_html": s3a_clause,
                    "just_tag": "∵ PRIMARY AXIS",
                    "just_id": s3_jid,
                    "just_title": s3_jtitle,
                    "strict_step_ids": True,
                    "active_ids": l_active,
                    "coincide_ids": [],
                    "equal_ids": [],
                },
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 0.55,
                    "step_num": 5,
                    "step_kind": "INTERSECT",
                    "svg_path": str(svgs_dir / "03_central_lines.svg"),
                    "symbolic": s3_sym,
                    "clause_html": s3b_clause,
                    "just_tag": "∵ COLLINEARITIES",
                    "just_id": s3_jid,
                    "just_title": s3_jtitle,
                    "strict_step_ids": True,
                    "active_ids": l_active,
                    "coincide_ids": l_coincide,
                    "equal_ids": l_equal,
                },
            ],
        },
        {
            "id": "act_3_collection_network",
            "title": f"{topic['code']} Collection 1 Network & Invariance",
            "subslides": [
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 1.1,
                    "step_num": 6,
                    "step_kind": "PROVE",
                    "svg_path": str(svgs_dir / "04_relations.svg"),
                    "symbolic": s4_sym,
                    "clause_html": s4_norm_clause,
                    "just_tag": "∵ COLLECTION 1",
                    "just_id": s4_jid,
                    "just_title": s4_jtitle,
                    "strict_step_ids": True,
                    "active_ids": rel_active,
                    "coincide_ids": rel_coincide,
                    "equal_ids": rel_equal,
                },
                {
                    **common,
                    "type": "euclid_step",
                    "weight": 0.95,
                    "step_num": 7,
                    "step_kind": "∴",
                    "svg_path": str(svgs_dir / "05_four_triangles.svg"),
                    "symbolic": "Invariance across Acute (5,6,7) • Right (3,4,5) • Kepler (1,√φ,φ) • Kimberling (6,9,13)",
                    "clause_html": (
                        f'<span class="clause-line"><b>Reference Triangle Invariance:</b> Across all four reference triangles, '
                        f'<b>{html.escape(topic["title"])}</b> preserves its exact projective incidences and harmonic ratios.</span>'
                    ),
                    "just_tag": "∵ INVARIANCE",
                    "just_id": "FOUR-TRIANGLE VERIFICATION",
                    "just_title": f"Verified across Collection 1 centers {', '.join('X_' + str(c) for c in topic.get('centers', [])[:6])}.",
                },
            ],
        },
    ]

    return topic["script"], scenes
