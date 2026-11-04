"""GEOMETOR construction model for X_1598 = POINT CHERTAN II."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_01598(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1598 = POINT CHERTAN II on reference triangle ABC."""
    X_1598 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*sec(A)', ID="X_1598", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_154 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(B)*cos(C))*a**(2)', ID="X_154", classes=["center", "incident"])
    X_578 = eval_trilinear_point(model, A, B, C, 'cos(A) + sin(A)*(tan(A) + tan(B) + tan(C))', ID="X_578", classes=["center", "incident"])
    central_line(model, X_154, X_578, 154, 578, incident=True)
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    X_999 = eval_trilinear_point(model, A, B, C, '2 - cos(A)', ID="X_999", classes=["center", "incident"])
    central_line(model, X_34, X_999, 34, 999, incident=True)
    return promote_point_to_top(model, X_1598)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1598 on the given reference triangle."""
    model = create_model('X_1598 = POINT CHERTAN II')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01598(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01598.json"))
    write_center_svg(
        model_acute,
        here / "x-01598.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
