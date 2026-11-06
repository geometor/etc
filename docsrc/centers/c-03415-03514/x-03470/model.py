"""GEOMETOR construction model for X_3470 = TRILINEAR PRODUCT X_74*X_1749."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03470(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3470 = TRILINEAR PRODUCT X_74*X_1749 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_1117 = eval_barycentric_point(model, A, B, C, '(a**(2)-a*b+b**(2)-c**(2))*(a**(2)+a*b+b**(2)-c**(2))*(a**(2)-b**(2)-a*c+c**(2))*(a**(2)-b**(2)+a*c+c**(2))*(a**(6)-a**(4)*b**(2)-a**(2)*b**(4)+b**(6)-3*a**(4)*c**(2)+a**(2)*b**(2)*c**(2)-3*b**(4)*c**(2)+3*a**(2)*c**(4)+3*b**(2)*c**(4)-c**(6))*(a**(6)-3*a**(4)*b**(2)+3*a**(2)*b**(4)-b**(6)-a**(4)*c**(2)+a**(2)*b**(2)*c**(2)+3*b**(4)*c**(2)-a**(2)*c**(4)-3*b**(2)*c**(4)+c**(6))*(a**(8)-4*a**(6)*b**(2)+6*a**(4)*b**(4)-4*a**(2)*b**(6)+b**(8)-4*a**(6)*c**(2)+a**(4)*b**(2)*c**(2)+a**(2)*b**(4)*c**(2)+2*b**(6)*c**(2)+6*a**(4)*c**(4)+a**(2)*b**(2)*c**(4)-6*b**(4)*c**(4)-4*a**(2)*c**(6)+2*b**(2)*c**(6)+c**(8))', ID="X_1117", classes=["center"])
    central_line(model, X_3, X_74, 3, 74)
    central_line(model, X_5, X_1117, 5, 1117)
    X_3470 = intersect_lines(model, X_3, X_74, X_5, X_1117, ID="X_3470", classes=["selected", "target"])
    X_1138 = eval_trilinear_point(model, A, B, C, '(1/(5*cos(A) - 4*cos(B)*cos(C) - 8*(cos(A))**(2)*sin(B)*sin(C)))', ID="X_1138", classes=["center", "incident"])
    X_2132 = point_from_barycentrics(model, A, B, C, -0.58419421, 0.77475873, 0.80943548, ID="X_2132", classes=["center", "incident"])
    central_line(model, X_1138, X_2132, 1138, 2132, incident=True)
    return promote_point_to_top(model, X_3470)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3470 on the given reference triangle."""
    model = create_model('X_3470 = TRILINEAR PRODUCT X_74*X_1749')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03470(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03470.json"))
    write_center_svg(
        model_acute,
        here / "x-03470.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
