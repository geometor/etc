"""GEOMETOR construction model for X(122) = X(107)-OF-MEDIAL-TRIANGLE."""

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
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00122(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(122) = X(107)-OF-MEDIAL-TRIANGLE on reference triangle ABC."""
    X_122 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(a**(2) - b**(2) - c**(2))**(2)*(3*a**(4) - 2*a**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2))', ID="X(122)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X(107)", classes=["center", "incident"])
    central_line(model, X_2, X_107, 2, 107, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X(113)", classes=["center", "incident"])
    central_line(model, X_3, X_113, 3, 113, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_133 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sin(2*B) - sin(2*C))**(2) + (sin(2*A))*(sin(2*B)) + (sin(2*A))*(sin(2*C)) - 2*(sin(2*B))*(sin(2*C)))*(2*sin(2*A) - sin(2*B) - sin(2*C))', ID="X(133)", classes=["center", "incident"])
    central_line(model, X_5, X_133, 5, 133, incident=True)
    return promote_point_to_top(model, X_122)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(122) on the given reference triangle."""
    model = create_model('X(122) = X(107)-OF-MEDIAL-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00122(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00122.json"))
    write_center_svg(
        model_acute,
        here / "x-00122.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
