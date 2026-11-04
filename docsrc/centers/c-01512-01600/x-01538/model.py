"""GEOMETOR construction model for X_1538 = ORTHOJOIN OF X_45."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01538(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1538 = ORTHOJOIN OF X_45 on reference triangle ABC."""
    X_119 = eval_trilinear_point(model, A, B, C, '(csc(A))*(-1 + cos(B) + cos(C))*(sin(2*B) + sin(2*C) + 2*(-1 + cos(A))*(sin(B) + sin(C)))', ID="X_119", classes=["center"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center"])
    X_971 = eval_trilinear_point(model, A, B, C, 'a**(4)*(b + c) - 2*a**(3)*(b**(2) + c**(2) - b*c) + 2*a*(b - c)**(2)*(b**(2) + c**(2) + b*c) - (b - c)**(2)*(b + c)**(3)', ID="X_971", classes=["center"])
    central_line(model, X_119, X_517, 119, 517)
    central_line(model, X_11, X_971, 11, 971)
    X_1538 = intersect_lines(model, X_119, X_517, X_11, X_971, ID="X_1538", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_1385 = eval_trilinear_point(model, A, B, C, '16*( area )**(2) + a*(a + b + c)*(b**(2) + c**(2) - a**(2))', ID="X_1385", classes=["center", "incident"])
    central_line(model, X_4, X_1385, 4, 1385, incident=True)
    return promote_point_to_top(model, X_1538)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1538 on the given reference triangle."""
    model = create_model('X_1538 = ORTHOJOIN OF X_45')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01538(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01538.json"))
    write_center_svg(
        model_acute,
        here / "x-01538.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
