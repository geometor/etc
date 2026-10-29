"""GEOMETOR construction model for X(129) = X(98)-OF-ORTHIC-TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00129(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(129) = X(98)-OF-ORTHIC-TRIANGLE on reference triangle ABC."""
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_130 = eval_trilinear_point(model, A, B, C, '(sin(A))*(sin(2*B) + sin(2*C))*((sin(2*B) - sin(2*C))**(2))*((sin(2*A))**(2) + sin(2*B)*sin(2*C))', ID="X(130)", classes=["center"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center"])
    X_137 = point_from_barycentrics(model, A, B, C, 0.1354431, 0.64976082, 0.21479608, ID="X(137)", classes=["center"])
    central_line(model, X_5, X_130, 5, 130)
    central_line(model, X_51, X_137, 51, 137)
    X_129 = intersect_lines(model, X_5, X_130, X_51, X_137, ID="X(129)", classes=["selected", "target"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X(52)", classes=["center", "incident"])
    X_139 = point_from_barycentrics(model, A, B, C, 0.0028749347, 0.23097013, 0.76615493, ID="X(139)", classes=["center", "incident"])
    central_line(model, X_52, X_139, 52, 139, incident=True)
    return promote_point_to_top(model, X_129)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(129) on the given reference triangle."""
    model = create_model('X(129) = X(98)-OF-ORTHIC-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00129(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00129.json"))
    write_center_svg(
        model_acute,
        here / "x-00129.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
