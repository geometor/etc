"""Exact symbolic GEOMETOR construction model for ``X_4 = ORTHOCENTER``."""

from __future__ import annotations

from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid,
    circumcenter,
    clawson_point,
    construct_baseline_triangle,
    construct_reference_triangle,
    create_model,
    exact_center_point,
    feuerbach_point,
    incenter,
    mittenpunkt,
    nagel_point,
    nine_point_center,
    orthocenter,
    promote_point_to_top,
    spieker_center,
)
from geometor.etc.render import write_center_svg


def construct_x_00004(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_4 = ORTHOCENTER`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Orthic triangle ``< H_a H_b H_c >`` and altitudes ``[ A H_a ]``, ``[ B H_b ]``,
      ``[ C H_c ]`` concurring at ``X_4``.
    - Incident central lines: Euler ``{ 2, 3 }`` (with ``X_2, X_3, X_5``),
      Mittenpunkt-Spieker-Clawson ``{ 9, 10 }`` (with ``X_9, X_10, X_19``),
      ``{ 1, 33 }``, ``{ 11, 56 }``, and ``{ 8, 72 }``.
    """
    X_4 = orthocenter(
        model,
        A,
        B,
        C,
        ID="X_4",
        classes=["selected", "target"],
        draw_altitudes=True,
    )

    X_2 = centroid(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_3 = circumcenter(model, A, B, C, ID="X_3", classes=["center", "incident"])
    nine_point_center(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_2, X_3, 2, 3, incident=True)

    X_9 = mittenpunkt(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_10 = spieker_center(model, A, B, C, ID="X_10", classes=["center", "incident"])
    clawson_point(model, A, B, C, ID="X_19", classes=["center", "incident"])
    central_line(model, X_9, X_10, 9, 10, incident=True)

    X_1 = incenter(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_33 = exact_center_point(
        model, A, B, C, 33, ID="X_33", classes=["center", "incident"]
    )
    central_line(model, X_1, X_33, 1, 33, incident=True)

    X_11 = feuerbach_point(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_56 = exact_center_point(
        model, A, B, C, 56, ID="X_56", classes=["center", "incident"]
    )
    central_line(model, X_11, X_56, 11, 56, incident=True)

    X_8 = nagel_point(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_72 = exact_center_point(
        model, A, B, C, 72, ID="X_72", classes=["center", "incident"]
    )
    central_line(model, X_8, X_72, 8, 72, incident=True)

    return promote_point_to_top(model, X_4)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_4 = ORTHOCENTER``."""
    model = create_model("X_4 = ORTHOCENTER")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00004(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00004.svg", "Heronian (15, 13, 14) | Δ = 84, X_4 = (5, 15/4)"),
        ("right", "x-00004-right.svg", "Right (3, 4, 5) | Δ = 6, X_4 = C = (16/5, 12/5)"),
        ("kepler", "x-00004-kepler.svg", "Kepler (1, √φ, φ) | X_4 = C"),
        ("kimberling", "x-00004-kimberling.svg", "Kimberling (6, 9, 13) | Δ = 3√35"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00004.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
