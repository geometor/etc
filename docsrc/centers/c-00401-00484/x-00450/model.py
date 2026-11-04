"""GEOMETOR construction model for X_450 = X_3-HIRST INVERSE OF X_4."""

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


def construct_x_00450(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_450 = X_3-HIRST INVERSE OF X_4 on reference triangle ABC."""
    X_450 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(4) - (cos(B)*cos(C))**(2))', ID="X_450", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_107, X_511, 107, 511, incident=True)
    X_155 = eval_trilinear_point(model, A, B, C, '(cos(A))*((cos(B))**(2) + (cos(C))**(2) - (cos(A))**(2))', ID="X_155", classes=["center", "incident"])
    X_1075 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sec(B))**(2) + (sec(C))**(2) - (sec(A))**(2))', ID="X_1075", classes=["center", "incident"])
    central_line(model, X_155, X_1075, 155, 1075, incident=True)
    return promote_point_to_top(model, X_450)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_450 on the given reference triangle."""
    model = create_model('X_450 = X_3-HIRST INVERSE OF X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00450(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00450.json"))
    write_center_svg(
        model_acute,
        here / "x-00450.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
