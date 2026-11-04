"""GEOMETOR construction model for X_468 = X_2-LINE CONJUGATE OF X_3."""

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


def construct_x_00468(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_468 = X_2-LINE CONJUGATE OF X_3 on reference triangle ABC."""
    X_468 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cot(B) + cot(C) - 2*cot(A))', ID="X_468", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_231 = eval_trilinear_point(model, A, B, C, '(cos(B))*(4*(sin(C))**(2) - 1)*(cos(A)*sin(B) - sin(A)*cos(B)) - (cos(C))*(4*(sin(B))**(2) - 1)*(cos(C)*sin(A) - sin(C)*cos(A))', ID="X_231", classes=["center", "incident"])
    central_line(model, X_230, X_231, 230, 231, incident=True)
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X_250", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    central_line(model, X_250, X_325, 250, 325, incident=True)
    return promote_point_to_top(model, X_468)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_468 on the given reference triangle."""
    model = create_model('X_468 = X_2-LINE CONJUGATE OF X_3')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00468(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00468.json"))
    write_center_svg(
        model_acute,
        here / "x-00468.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
