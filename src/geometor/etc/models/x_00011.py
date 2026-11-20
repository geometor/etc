"""Exact symbolic GEOMETOR construction model for ``X_11 = FEUERBACH POINT``."""

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
    exact_center_point,
    feuerbach_point,
    harmonic_feuerbach_point,
    incenter,
    nine_point_center,
    orthocenter,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00011(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_11 = FEUERBACH POINT`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - The ``incircle`` and ``nine_point_circle``, internally tangent at ``X_11``.
    - Incident central lines: Feuerbach ``{ 1, 5 }`` (with ``X_1, X_5, X_12``),
      Centroid-Insimilicenter ``{ 2, 55 }``, Orthocenter-Exsimilicenter ``{ 4, 56 }``,
      and ``{ 35, 140 }``.
    """
    X_11 = feuerbach_point(
        model,
        A,
        B,
        C,
        ID="X_11",
        classes=["selected", "target"],
        draw_circles=True,
    )

    X_1 = incenter(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_5 = nine_point_center(model, A, B, C, ID="X_5", classes=["center", "incident"])
    harmonic_feuerbach_point(model, A, B, C, ID="X_12", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)

    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_55 = exact_center_point(
        model, A, B, C, 55, ID="X_55", classes=["center", "incident"]
    )
    central_line(model, X_2, X_55, 2, 55, incident=True)

    X_4 = orthocenter(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_56 = exact_center_point(
        model, A, B, C, 56, ID="X_56", classes=["center", "incident"]
    )
    central_line(model, X_4, X_56, 4, 56, incident=True)

    X_35 = exact_center_point(
        model, A, B, C, 35, ID="X_35", classes=["center", "incident"]
    )
    X_140 = exact_center_point(
        model, A, B, C, 140, ID="X_140", classes=["center", "incident"]
    )
    central_line(model, X_35, X_140, 35, 140, incident=True)

    return promote_point_to_top(model, X_11)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_11 = FEUERBACH POINT``."""
    model = create_model("X_11 = FEUERBACH POINT")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00011(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00011.svg", "Heronian (15, 13, 14) | Δ = 84, 6 : 8 : 28"),
        ("right", "x-00011-right.svg", "Right (3, 4, 5) | Δ = 6, 3 : 8 : 1"),
        ("kepler", "x-00011-kepler.svg", "Kepler (1, √φ, φ) | Δ = √φ / 2"),
        ("kimberling", "x-00011-kimberling.svg", "Kimberling (6, 9, 13) | 128 : 245 : 9"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00011.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
