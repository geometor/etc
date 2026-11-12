"""Exact symbolic GEOMETOR construction model for ``X_18 = 2ND NAPOLEON POINT``."""

from __future__ import annotations

from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter,
    construct_baseline_triangle,
    construct_reference_triangle,
    create_model,
    fermat_point,
    first_napoleon_point,
    nine_point_center,
    orthocenter,
    promote_point_to_top,
    second_isodynamic_point,
    second_isogonic_center,
    second_napoleon_point,
    symmedian_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00018(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_18 = 2ND NAPOLEON POINT`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Inner equilateral triangles and inner Napoleon triangle ``< Nap'_a Nap'_b Nap'_c >``
      with perspectivity lines ``[ A Nap'_a ]``, ``[ B Nap'_b ]``, ``[ C Nap'_c ]``
      concurring at ``X_18``.
    - Incident central lines: ``{ 3, 14 }``, ``{ 5, 13 }``, ``{ 4, 16 }``, and
      Napoleon line ``{ 6, 17 }``.
    """
    X_18 = second_napoleon_point(
        model,
        A,
        B,
        C,
        ID="X_18",
        classes=["selected", "target"],
        draw_napoleon=True,
    )

    X_3 = circumcenter(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_14 = second_isogonic_center(
        model, A, B, C, ID="X_14", classes=["center", "incident"]
    )
    central_line(model, X_3, X_14, 3, 14, incident=True)

    X_5 = nine_point_center(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_13 = fermat_point(model, A, B, C, ID="X_13", classes=["center", "incident"])
    central_line(model, X_5, X_13, 5, 13, incident=True)

    X_4 = orthocenter(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_16 = second_isodynamic_point(
        model, A, B, C, ID="X_16", classes=["center", "incident"]
    )
    central_line(model, X_4, X_16, 4, 16, incident=True)

    X_6 = symmedian_point(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_17 = first_napoleon_point(
        model, A, B, C, ID="X_17", classes=["center", "incident"]
    )
    central_line(model, X_6, X_17, 6, 17, incident=True)

    return promote_point_to_top(model, X_18)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_18 = 2ND NAPOLEON POINT``."""
    model = create_model("X_18 = 2ND NAPOLEON POINT")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00018(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00018.svg", "Heronian (15, 13, 14) | ℚ(√3) | Δ = 84"),
        ("right", "x-00018-right.svg", "Right (3, 4, 5) | ℚ(√3) | Δ = 6"),
        ("kepler", "x-00018-kepler.svg", "Kepler (1, √φ, φ) | ℚ(φ, √φ, √3)"),
        ("kimberling", "x-00018-kimberling.svg", "Kimberling (6, 9, 13) | ℚ(√35, √3)"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00018.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
