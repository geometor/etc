"""GEOMETOR construction model for X_416 = X_3-HIRST INVERSE OF X_21."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00416(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_416 = X_3-HIRST INVERSE OF X_21 on reference triangle ABC."""
    X_416 = eval_barycentric_point(model, A, B, C, 'a*(a + b) * (a + c) * (a**(7)*b**(2) - a**(6)*b**(3) - 2*a**(5)*b**(4) + 2*a**(4)*b**(5) + a**(3)*b**(6) - a**(2)*b**(7) + a**(7)*b*c - a**(6)*b**(2)*c - a**(5)*b**(3)*c + 2*a**(4)*b**(4)*c - a**(3)*b**(5)*c - a**(2)*b**(6)*c + a*b**(7)*c + a**(7)*c**(2) - a**(6)*b*c**(2) + a**(5)*b**(2)*c**(2) - a**(4)*b**(3)*c**(2) - a**(3)*b**(4)*c**(2) + a**(2)*b**(5)*c**(2) - a*b**(6)*c**(2) + b**(7)*c**(2) - a**(6)*c**(3) - a**(5)*b*c**(3) - a**(4)*b**(2)*c**(3) + 2*a**(3)*b**(3)*c**(3) + a**(2)*b**(4)*c**(3) - a*b**(5)*c**(3) + b**(6)*c**(3) - 2*a**(5)*c**(4) + 2*a**(4)*b*c**(4) - a**(3)*b**(2)*c**(4) + a**(2)*b**(3)*c**(4) + 2*a*b**(4)*c**(4) - 2*b**(5)*c**(4) + 2*a**(4)*c**(5) - a**(3)*b*c**(5) + a**(2)*b**(2)*c**(5) - a*b**(3)*c**(5) - 2*b**(4)*c**(5) + a**(3)*c**(6) - a**(2)*b*c**(6) - a*b**(2)*c**(6) + b**(3)*c**(6) - a**(2)*c**(7) + a*b*c**(7) + b**(2)*c**(7))', ID="X_416", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center", "incident"])
    X_1248 = point_from_barycentrics(model, A, B, C, -0.013970382, -0.017899094, 1.0318695, ID="X_1248", classes=["center", "incident"])
    central_line(model, X_255, X_1248, 255, 1248, incident=True)
    X_296 = eval_trilinear_point(model, A, B, C, '(cos(A))/((cos(A))**(2) - cos(B)*cos(C))', ID="X_296", classes=["center", "incident"])
    X_2651 = eval_trilinear_point(model, A, B, C, '(1/((cos(A) + cos(B))*(cos(A) + cos(C))) - 1/(cos(B) + cos(C))**(2))', ID="X_2651", classes=["center", "incident"])
    central_line(model, X_296, X_2651, 296, 2651, incident=True)
    return promote_point_to_top(model, X_416)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_416 on the given reference triangle."""
    model = create_model('X_416 = X_3-HIRST INVERSE OF X_21')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00416(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00416.json"))
    write_center_svg(
        model_acute,
        here / "x-00416.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
