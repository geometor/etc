"""Exact symbolic GEOMETOR construction model for ``X_12 = {X_1, X_5}-HARMONIC CONJUGATE OF X_11``."""

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
    spieker_center,
)
from geometor.etc.render import write_center_svg


def construct_x_00012(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_12`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Incircle, nine-point circle, Feuerbach triangle ``< F_a F_b F_c >``, and
      perspectivity lines ``[ A F_a ]``, ``[ B F_b ]``, ``[ C F_c ]`` concurring at ``X_12``.
    - Incident central lines: Feuerbach ``{ 1, 5 }`` (with ``X_1, X_5, X_11``),
      Centroid-Exsimilicenter ``{ 2, 56 }``, Orthocenter-Insimilicenter ``{ 4, 55 }``,
      and ``{ 10, 65 }``.
    """
    X_12 = harmonic_feuerbach_point(
        model,
        A,
        B,
        C,
        ID="X_12",
        classes=["selected", "target"],
        draw_feuerbach=True,
    )

    X_1 = incenter(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_5 = nine_point_center(model, A, B, C, ID="X_5", classes=["center", "incident"])
    feuerbach_point(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)

    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_56 = exact_center_point(
        model, A, B, C, 56, ID="X_56", classes=["center", "incident"]
    )
    central_line(model, X_2, X_56, 2, 56, incident=True)

    X_4 = orthocenter(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_55 = exact_center_point(
        model, A, B, C, 55, ID="X_55", classes=["center", "incident"]
    )
    central_line(model, X_4, X_55, 4, 55, incident=True)

    X_10 = spieker_center(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_65 = exact_center_point(
        model, A, B, C, 65, ID="X_65", classes=["center", "incident"]
    )
    central_line(model, X_10, X_65, 10, 65, incident=True)

    return promote_point_to_top(model, X_12)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_12``."""
    model = create_model("X_12 = {X_1, X_5}-HARMONIC CONJUGATE OF X_11")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00012(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00012.svg", "Heronian (15, 13, 14) | Δ = 84, (X_1, X_5; X_11, X_12) = -1"),
        ("right", "x-00012-right.svg", "Right (3, 4, 5) | Δ = 6, 81 : 96 : 98"),
        ("kepler", "x-00012-kepler.svg", "Kepler (1, √φ, φ) | Δ = √φ / 2"),
        ("kimberling", "x-00012-kimberling.svg", "Kimberling (6, 9, 13) | 242 : 724 : 900"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00012.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
