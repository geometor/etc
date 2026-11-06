"""GEOMETOR construction model for X_3147 = X_254-CEVA CONJUGATE OF X_4."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03147(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3147 = X_254-CEVA CONJUGATE OF X_4 on reference triangle ABC."""
    X_254 = eval_trilinear_point(model, A, B, C, '(sec(A))/((cos(B))**(2) + (cos(C))**(2) - (cos(A))**(2))', ID="X_254", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_3147 = ceva_conjugate(model, A, B, C, X_254, X_4, ID="X_3147", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_1068 = eval_trilinear_point(model, A, B, C, '(1 - sec(A)*(cos(B) + cos(C)))', ID="X_1068", classes=["center", "incident"])
    X_1940 = eval_trilinear_point(model, A, B, C, '((sec(A))**(2) + sec(B)*sec(C))', ID="X_1940", classes=["center", "incident"])
    central_line(model, X_1068, X_1940, 1068, 1940, incident=True)
    X_323 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*(csc(A))**(2)', ID="X_323", classes=["center", "incident"])
    X_2904 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2))*(a**(6) - 3*a**(4)*(b**(2) + c**(2)) + 3*a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))/(b**(2) + c**(2) - a**(2))', ID="X_2904", classes=["center", "incident"])
    central_line(model, X_323, X_2904, 323, 2904, incident=True)
    return promote_point_to_top(model, X_3147)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3147 on the given reference triangle."""
    model = create_model('X_3147 = X_254-CEVA CONJUGATE OF X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03147(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03147.json"))
    write_center_svg(
        model_acute,
        here / "x-03147.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
