"""Exact symbolic GEOMETOR construction model for ``X_15 = 1ST ISODYNAMIC POINT``."""

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
    first_isodynamic_point,
    first_napoleon_point,
    orthocenter,
    promote_point_to_top,
    second_isodynamic_point,
    second_isogonic_center,
    symmedian_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00015(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_15 = 1ST ISODYNAMIC POINT`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Circumcircle, coaxial Apollonian circles ``apollonian_a``, ``apollonian_b``,
      ``apollonian_c``, and equilateral pedal triangle ``< Pd_a Pd_b Pd_c >``.
    - Incident central lines: Brocard axis ``{ 3, 6 }`` (with ``X_3, X_6, X_16``),
      ``{ 2, 14 }``, and ``{ 4, 17 }``.
    """
    X_15 = first_isodynamic_point(
        model,
        A,
        B,
        C,
        ID="X_15",
        classes=["selected", "target"],
        draw_apollonian=True,
        draw_pedal=True,
    )

    X_3 = circumcenter(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point(model, A, B, C, ID="X_6", classes=["center", "incident"])
    second_isodynamic_point(model, A, B, C, ID="X_16", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)

    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_14 = second_isogonic_center(
        model, A, B, C, ID="X_14", classes=["center", "incident"]
    )
    central_line(model, X_2, X_14, 2, 14, incident=True)

    X_4 = orthocenter(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_17 = first_napoleon_point(
        model, A, B, C, ID="X_17", classes=["center", "incident"]
    )
    central_line(model, X_4, X_17, 4, 17, incident=True)

    return promote_point_to_top(model, X_15)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_15 = 1ST ISODYNAMIC POINT``."""
    model = create_model("X_15 = 1ST ISODYNAMIC POINT")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00015(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00015.svg", "Heronian (15, 13, 14) | ℚ(√3) | Δ = 84"),
        ("right", "x-00015-right.svg", "Right (3, 4, 5) | ℚ(√3) | Δ = 6"),
        ("kepler", "x-00015-kepler.svg", "Kepler (1, √φ, φ) | ℚ(φ, √φ, √3)"),
        ("kimberling", "x-00015-kimberling.svg", "Kimberling (6, 9, 13) | ℚ(√35, √3)"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00015.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
