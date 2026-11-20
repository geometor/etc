"""Exact symbolic GEOMETOR construction model for ``X_7 = GERGONNE POINT``."""

from __future__ import annotations

from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid,
    construct_baseline_triangle,
    construct_reference_triangle,
    create_model,
    de_longchamps_point,
    exact_center_point,
    gergonne_point,
    incenter,
    mittenpunkt,
    nagel_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00007(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_7 = GERGONNE POINT`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Incircle, intouch triangle ``< T_a T_b T_c >``, and Gergonne cevians
      ``[ A T_a ]``, ``[ B T_b ]``, ``[ C T_c ]`` concurring at ``X_7``.
    - Incident central lines: Centroid-Mittenpunkt ``{ 2, 9 }``, Soddy ``{ 1, 20 }``,
      and Nagel-Intouch-Orthocenter ``{ 8, 65 }``.
    """
    X_7 = gergonne_point(
        model,
        A,
        B,
        C,
        ID="X_7",
        classes=["selected", "target"],
        draw_cevians=True,
        draw_intouch=True,
    )

    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_9 = mittenpunkt(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_2, X_9, 2, 9, incident=True)

    X_1 = incenter(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_20 = de_longchamps_point(
        model, A, B, C, ID="X_20", classes=["center", "incident"]
    )
    central_line(model, X_1, X_20, 1, 20, incident=True)

    X_8 = nagel_point(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_65 = exact_center_point(
        model, A, B, C, 65, ID="X_65", classes=["center", "incident"]
    )
    central_line(model, X_8, X_65, 8, 65, incident=True)

    return promote_point_to_top(model, X_7)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_7 = GERGONNE POINT``."""
    model = create_model("X_7 = GERGONNE POINT")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00007(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00007.svg", "Heronian (15, 13, 14) | Δ = 84, 7 : 9 : 8"),
        ("right", "x-00007-right.svg", "Right (3, 4, 5) | Δ = 6, 2 : 3 : 6"),
        ("kepler", "x-00007-kepler.svg", "Kepler (1, √φ, φ) | Δ = √φ / 2"),
        ("kimberling", "x-00007-kimberling.svg", "Kimberling (6, 9, 13) | 1 : 4 : 8"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00007.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
