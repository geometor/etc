"""GEOMETOR construction model for X_1583 = POINT CAPELLA I."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01583(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1583 = POINT CAPELLA I on reference triangle ABC."""
    X_1583 = eval_trilinear_point(model, A, B, C, '(csc(A) + cos(A))', ID="X_1583", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_493 = eval_trilinear_point(model, A, B, C, '1/(sin(A) + sin(B)*sin(C))', ID="X_493", classes=["center", "incident"])
    central_line(model, X_6, X_493, 6, 493, incident=True)
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A - pi /4)', ID="X_371", classes=["center", "incident"])
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    central_line(model, X_371, X_394, 371, 394, incident=True)
    return promote_point_to_top(model, X_1583)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1583 on the given reference triangle."""
    model = create_model('X_1583 = POINT CAPELLA I')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01583(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01583.json"))
    write_center_svg(
        model_acute,
        here / "x-01583.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
