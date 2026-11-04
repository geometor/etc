"""GEOMETOR construction model for X_1532 = ORTHOJOIN OF X_37."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01532(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1532 = ORTHOJOIN OF X_37 on reference triangle ABC."""
    X_1532 = eval_trilinear_point(model, A, B, C, '(b*c*(2*a*b*c - (b + c)*(a - b + c)*(a + b - c))*(a*(b + c)*(a + b - c)*(a - b + c) - (a + b + c)*(a - b - c)*(b - c)**(2)))', ID="X_1532", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center", "incident"])
    central_line(model, X_11, X_515, 11, 515, incident=True)
    X_119 = eval_trilinear_point(model, A, B, C, '(csc(A))*(-1 + cos(B) + cos(C))*(sin(2*B) + sin(2*C) + 2*(-1 + cos(A))*(sin(B) + sin(C)))', ID="X_119", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_119, X_517, 119, 517, incident=True)
    return promote_point_to_top(model, X_1532)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1532 on the given reference triangle."""
    model = create_model('X_1532 = ORTHOJOIN OF X_37')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01532(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01532.json"))
    write_center_svg(
        model_acute,
        here / "x-01532.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
