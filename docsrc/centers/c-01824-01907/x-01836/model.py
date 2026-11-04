"""GEOMETOR construction model for X_1836 = ZOSMA TRANSFORM OF X_33."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01836(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1836 = ZOSMA TRANSFORM OF X_33 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_1836 = crosspoint(model, A, B, C, X_4, X_7, ID="X_1836", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    central_line(model, X_1, X_30, 1, 30, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_5, X_46, 5, 46, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    central_line(model, X_12, X_40, 12, 40, incident=True)
    return promote_point_to_top(model, X_1836)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1836 on the given reference triangle."""
    model = create_model('X_1836 = ZOSMA TRANSFORM OF X_33')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01836(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01836.json"))
    write_center_svg(
        model_acute,
        here / "x-01836.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
