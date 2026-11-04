"""GEOMETOR construction model for X_1515 = ORTHOJOIN OF X_4."""

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
    intersect_lines,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01515(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1515 = ORTHOJOIN OF X_4 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_1294 = eval_barycentric_point(model, A, B, C, '1/(a**(6)*(b**(2) + c**(2)) - a**(4)*(3*b**(4) - 4*b**(2)*c**(2) + 3*c**(4)) + 3*a**(2)*(b**(2) - c**(2))**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2)*(b**(4) + 4*b**(2)*c**(2) + c**(4)))', ID="X_1294", classes=["center"])
    central_line(model, X_4, X_6, 4, 6)
    central_line(model, X_30, X_1294, 30, 1294)
    X_1515 = intersect_lines(model, X_4, X_6, X_30, X_1294, ID="X_1515", classes=["selected", "target"])
    X_133 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sin(2*B) - sin(2*C))**(2) + (sin(2*A))*(sin(2*B)) + (sin(2*A))*(sin(2*C)) - 2*(sin(2*B))*(sin(2*C)))*(2*sin(2*A) - sin(2*B) - sin(2*C))', ID="X_133", classes=["center", "incident"])
    X_1559 = point_from_barycentrics(model, A, B, C, 0.2024927, 0.25212191, 0.54538539, ID="X_1559", classes=["center", "incident"])
    central_line(model, X_133, X_1559, 133, 1559, incident=True)
    return promote_point_to_top(model, X_1515)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1515 on the given reference triangle."""
    model = create_model('X_1515 = ORTHOJOIN OF X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01515(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01515.json"))
    write_center_svg(
        model_acute,
        here / "x-01515.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
