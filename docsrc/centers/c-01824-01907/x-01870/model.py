"""GEOMETOR construction model for X_1870 = ZOSMA TRANSFORM OF X_484."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01870(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1870 = ZOSMA TRANSFORM OF X_484 on reference triangle ABC."""
    X_1807 = eval_trilinear_point(model, A, B, C, '1/(2 - sec(A))', ID="X_1807", classes=["center"])
    X_1870 = isogonal_conjugate(model, A, B, C, X_1807, ID="X_1870", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_24, X_56, 24, 56, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_28, X_60, 28, 60, incident=True)
    return promote_point_to_top(model, X_1870)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1870 on the given reference triangle."""
    model = create_model('X_1870 = ZOSMA TRANSFORM OF X_484')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01870(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01870.json"))
    write_center_svg(
        model_acute,
        here / "x-01870.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
