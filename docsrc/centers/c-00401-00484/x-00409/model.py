"""GEOMETOR construction model for X_409 = EULER X_21-1st-SUBSTITUTION POINT."""

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
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00409(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_409 = EULER X_21-1st-SUBSTITUTION POINT on reference triangle ABC."""
    X_409 = eval_barycentric_point(model, A, B, C, 'a*(a + b) * (a + c) * (a**(4) - a**(3)*b + a*b**(3) - b**(4) - a**(3)*c + a**(2)*b*c + a*b**(2)*c + b**(3)*c + a*b*c**(2) + 4*b**(2)*c**(2) + a*c**(3) + b*c**(3) - c**(4))', ID="X_409", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_1098 = eval_trilinear_point(model, A, B, C, '(1/(cos(B) + cos(C))**(2))', ID="X_1098", classes=["center", "incident"])
    central_line(model, X_65, X_1098, 65, 1098, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1247 = point_from_barycentrics(model, A, B, C, 0.47979502, 0.29838347, 0.22182151, ID="X_1247", classes=["center", "incident"])
    central_line(model, X_1, X_1247, 1, 1247, incident=True)
    return promote_point_to_top(model, X_409)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_409 on the given reference triangle."""
    model = create_model('X_409 = EULER X_21-1st-SUBSTITUTION POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00409(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00409.json"))
    write_center_svg(
        model_acute,
        here / "x-00409.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
