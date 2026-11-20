"""Exact symbolic GEOMETOR construction model for ``X_14 = 2ND ISOGONIC CENTER``."""

from __future__ import annotations

from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid,
    circumcenter,
    construct_baseline_triangle,
    construct_reference_triangle,
    create_model,
    fermat_point,
    first_isodynamic_point,
    first_napoleon_point,
    nine_point_center,
    promote_point_to_top,
    second_isogonic_center,
    second_napoleon_point,
    symmedian_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00014(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_14 = 2ND ISOGONIC CENTER`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Inner equilateral triangles ``< B C A'' >``, ``< C A B'' >``, ``< A B C'' >``
      and isogonic lines ``[ A A'' ]``, ``[ B B'' ]``, ``[ C C'' ]`` concurring at ``X_14``.
    - Incident central lines: Fermat axis ``{ 6, 13 }``, ``{ 2, 15 }``, ``{ 3, 18 }``,
      and ``{ 5, 17 }``.
    """
    X_14 = second_isogonic_center(
        model,
        A,
        B,
        C,
        ID="X_14",
        classes=["selected", "target"],
        draw_equilaterals=True,
    )

    X_6 = symmedian_point(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_13 = fermat_point(model, A, B, C, ID="X_13", classes=["center", "incident"])
    central_line(model, X_6, X_13, 6, 13, incident=True)

    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_15 = first_isodynamic_point(
        model, A, B, C, ID="X_15", classes=["center", "incident"]
    )
    central_line(model, X_2, X_15, 2, 15, incident=True)

    X_3 = circumcenter(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_18 = second_napoleon_point(
        model, A, B, C, ID="X_18", classes=["center", "incident"]
    )
    central_line(model, X_3, X_18, 3, 18, incident=True)

    X_5 = nine_point_center(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_17 = first_napoleon_point(
        model, A, B, C, ID="X_17", classes=["center", "incident"]
    )
    central_line(model, X_5, X_17, 5, 17, incident=True)

    return promote_point_to_top(model, X_14)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_14 = 2ND ISOGONIC CENTER``."""
    model = create_model("X_14 = 2ND ISOGONIC CENTER")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00014(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00014.svg", "Heronian (15, 13, 14) | ℚ(√3) | Δ = 84"),
        ("right", "x-00014-right.svg", "Right (3, 4, 5) | ℚ(√3) | Δ = 6"),
        ("kepler", "x-00014-kepler.svg", "Kepler (1, √φ, φ) | ℚ(φ, √φ, √3)"),
        ("kimberling", "x-00014-kimberling.svg", "Kimberling (6, 9, 13) | ℚ(√35, √3)"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00014.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
