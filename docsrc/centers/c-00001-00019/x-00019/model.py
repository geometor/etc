"""Exact symbolic GEOMETOR construction model for ``X_19 = CLAWSON POINT``."""

from __future__ import annotations

from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    clawson_point,
    construct_baseline_triangle,
    construct_reference_triangle,
    create_model,
    exact_center_point,
    incenter,
    mittenpunkt,
    orthocenter,
    promote_point_to_top,
    spieker_center,
    symmedian_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00019(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct ``X_19 = CLAWSON POINT`` and its classical incident central lines on ``ABC``.

    Constructed elements include:

    - Orthic triangle ``< H_a H_b H_c >``, Clawson cevian triangle ``< P_a P_b P_c >``,
      and cevians ``[ A P_a ]``, ``[ B P_b ]``, ``[ C P_c ]`` concurring at ``X_19``.
    - Incident central lines: Orthocenter-Mittenpunkt-Spieker ``{ 4, 9 }``
      (with ``X_4, X_9, X_10``), ``{ 1, 28 }``, and ``{ 6, 34 }``.
    """
    X_19 = clawson_point(
        model,
        A,
        B,
        C,
        ID="X_19",
        classes=["selected", "target"],
        draw_cevians=True,
    )

    X_4 = orthocenter(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt(model, A, B, C, ID="X_9", classes=["center", "incident"])
    spieker_center(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)

    X_1 = incenter(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_28 = exact_center_point(
        model, A, B, C, 28, ID="X_28", classes=["center", "incident"]
    )
    central_line(model, X_1, X_28, 1, 28, incident=True)

    X_6 = symmedian_point(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_34 = exact_center_point(
        model, A, B, C, 34, ID="X_34", classes=["center", "incident"]
    )
    central_line(model, X_6, X_34, 6, 34, incident=True)

    return promote_point_to_top(model, X_19)


def build_model(
    preset: str | tuple[sp.Expr | int, sp.Expr | int, sp.Expr | int] = "heronian",
    show_guides: bool = False,
) -> Model:
    """Build an exact symbolic :class:`geometor.model.Model` for ``X_19 = CLAWSON POINT``."""
    model = create_model("X_19 = CLAWSON POINT")
    if isinstance(preset, str):
        A, B, C = construct_reference_triangle(model, preset, show_guides=show_guides)
    else:
        A, B, C = construct_baseline_triangle(model, *preset, show_guides=show_guides)
    construct_x_00019(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    plate_specs = [
        ("heronian", "x-00019.svg", "Heronian (15, 13, 14) | Δ = 84, 33 : 60 : 65"),
        ("right", "x-00019-right.svg", "Right (3, 4, 5) | Δ = 6, X_19 = C = (16/5, 12/5)"),
        ("kepler", "x-00019-kepler.svg", "Kepler (1, √φ, φ) | X_19 = C"),
        ("kimberling", "x-00019-kimberling.svg", "Kimberling (6, 9, 13) | 60 : 99 : -65"),
    ]
    for preset_key, svg_name, sub_text in plate_specs:
        mdl = build_model(preset_key)
        if preset_key == "heronian":
            mdl.save(str(here / "x-00019.json"))
        write_center_svg(mdl, here / svg_name, subtitle=sub_text)
