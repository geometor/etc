"""GEOMETOR construction model for X_422 = X_4-HIRST INVERSE OF X_28."""

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
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00422(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_422 = X_4-HIRST INVERSE OF X_28 on reference triangle ABC."""
    X_422 = eval_barycentric_point(model, A, B, C, '(a + b) * (a + c) * (a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2)) * (a**(3) + a*b*c - b**(2)*c - b*c**(2))', ID="X_422", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X_162", classes=["center", "incident"])
    X_242 = eval_trilinear_point(model, A, B, C, '((sec(A))*((sin(A))**(2) - sin(B)*sin(C)))', ID="X_242", classes=["center", "incident"])
    central_line(model, X_162, X_242, 162, 242, incident=True)
    return promote_point_to_top(model, X_422)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_422 on the given reference triangle."""
    model = create_model('X_422 = X_4-HIRST INVERSE OF X_28')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00422(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00422.json"))
    write_center_svg(
        model_acute,
        here / "x-00422.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
