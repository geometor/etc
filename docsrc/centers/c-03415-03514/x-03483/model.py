"""GEOMETOR construction model for X_3483 = INTERSECTION OF LINES X_1X_1157 and X_4X_484."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03483(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3483 = INTERSECTION OF LINES X_1X_1157 and X_4X_484 on reference triangle ABC."""
    X_3483 = eval_barycentric_point(model, A, B, C, '(a*(a**(6)+a**(5)*b-a**(4)*b**(2)-2*a**(3)*b**(3)-a**(2)*b**(4)+a*b**(5)+b**(6)+a**(5)*c+a**(4)*b*c-a*b**(4)*c-b**(5)*c-a**(4)*c**(2)+2*a**(2)*b**(2)*c**(2)-b**(4)*c**(2)-2*a**(3)*c**(3)+2*b**(3)*c**(3)-a**(2)*c**(4)-a*b*c**(4)-b**(2)*c**(4)+a*c**(5)-b*c**(5)+c**(6)))/(-a**(3)-a**(2)*b+a*b**(2)+b**(3)-a**(2)*c-a*b*c-b**(2)*c+a*c**(2)-b*c**(2)+c**(3))', ID="X_3483", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center", "incident"])
    central_line(model, X_4, X_484, 4, 484, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1157 = eval_trilinear_point(model, A, B, C, '4*cos(A) + cos(3*A)*sec(A)*sec(B - C)', ID="X_1157", classes=["center", "incident"])
    central_line(model, X_1, X_1157, 1, 1157, incident=True)
    X_399 = eval_trilinear_point(model, A, B, C, '5*cos(A) - 4*cos(B)*cos(C) - 8*sin(B)*sin(C)*(cos(A))**(2)', ID="X_399", classes=["center", "incident"])
    X_3466 = point_from_barycentrics(model, A, B, C, 0.75049052, 1.2119032, -0.96239372, ID="X_3466", classes=["center", "incident"])
    central_line(model, X_399, X_3466, 399, 3466, incident=True)
    return promote_point_to_top(model, X_3483)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3483 on the given reference triangle."""
    model = create_model('X_3483 = INTERSECTION OF LINES X_1X_1157 and X_4X_484')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03483(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03483.json"))
    write_center_svg(
        model_acute,
        here / "x-03483.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
