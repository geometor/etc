"""Exact symbolic GEOMETOR construction model for ``X_5 = NINE-POINT CENTER``."""

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
    exact_center_point,
    feuerbach_point,
    harmonic_feuerbach_point,
    incenter,
    nine_point_center,
    orthocenter,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00005(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_5 = NINE-POINT CENTER`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Medial midpoints ``M_a, M_b, M_c``, orthic feet ``H_a, H_b, H_c``, Euler midpoints
      ``Eu_a, Eu_b, Eu_c``, and the ``nine_point_circle``.
    - Incident central lines: Euler ``{ 2, 3 }`` (with ``X_2, X_3, X_4``),
      Feuerbach ``{ 1, 11 }`` (with ``X_1, X_11, X_12``), ``{ 39, 115 }``, and ``{ 54, 110 }``.
    """
    X_5 = nine_point_center(
        model,
        A,
        B,
        C,
        ID="X_5",
        classes=["selected", "target"],
        draw_nine_points=True,
    )

    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_3 = circumcenter(model, A, B, C, ID="X_3", classes=["center", "incident"])
    orthocenter(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_2, X_3, 2, 3, incident=True)

    X_1 = incenter(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_11 = feuerbach_point(model, A, B, C, ID="X_11", classes=["center", "incident"])
    harmonic_feuerbach_point(model, A, B, C, ID="X_12", classes=["center", "incident"])
    central_line(model, X_1, X_11, 1, 11, incident=True)

    X_39 = exact_center_point(
        model, A, B, C, 39, ID="X_39", classes=["center", "incident"]
    )
    X_115 = exact_center_point(
        model, A, B, C, 115, ID="X_115", classes=["center", "incident"]
    )
    central_line(model, X_39, X_115, 39, 115, incident=True)

    X_54 = exact_center_point(
        model, A, B, C, 54, ID="X_54", classes=["center", "incident"]
    )
    X_110 = exact_center_point(
        model, A, B, C, 110, ID="X_110", classes=["center", "incident"]
    )
    central_line(model, X_54, X_110, 54, 110, incident=True)

    return promote_point_to_top(model, X_5)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_5 = NINE-POINT CENTER``."""
    model = create_model("X_5 = NINE-POINT CENTER")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00005(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00005.svg", "Heronian (15, 13, 14) | Δ = 84, R_9 = 65/16"),
        ("right", "x-00005-right.svg", "Right (3, 4, 5) | Δ = 6, R_9 = 5/4"),
        ("kepler", "x-00005-kepler.svg", "Kepler (1, √φ, φ) | R_9 = φ / 4"),
        ("kimberling", "x-00005-kimberling.svg", "Kimberling (6, 9, 13) | R_9 = 39√35 / 70"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00005.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
