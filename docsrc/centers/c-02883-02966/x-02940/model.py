"""GEOMETOR construction model for X_2940 = EXCENTRAL-ISOGONAL CONJUGATE OF X_5."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02940(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2940 = EXCENTRAL-ISOGONAL CONJUGATE OF X_5 on reference triangle ABC."""
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_191 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(b*c + c*a + a*b) + b**(3) + c**(3) - a**(3)', ID="X_191", classes=["center"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center"])
    central_line(model, X_35, X_37, 35, 37)
    central_line(model, X_191, X_210, 191, 210)
    X_2940 = intersect_lines(model, X_35, X_37, X_191, X_210, ID="X_2940", classes=["selected", "target"])
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center", "incident"])
    X_1046 = point_from_barycentrics(model, A, B, C, 0.13236391, 0.3064877, 0.5611484, ID="X_1046", classes=["center", "incident"])
    central_line(model, X_484, X_1046, 484, 1046, incident=True)
    return promote_point_to_top(model, X_2940)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2940 on the given reference triangle."""
    model = create_model('X_2940 = EXCENTRAL-ISOGONAL CONJUGATE OF X_5')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02940(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02940.json"))
    write_center_svg(
        model_acute,
        here / "x-02940.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
