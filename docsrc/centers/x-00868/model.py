"""GEOMETOR construction model for X(868) = CROSSPOINT OF X(98) AND X(523)."""

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
    crosspoint,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00868(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(868) = CROSSPOINT OF X(98) AND X(523) on reference triangle ABC."""
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X(523)", classes=["center"])
    X_868 = crosspoint(model, A, B, C, X_98, X_523, ID="X(868)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X(125)", classes=["center", "incident"])
    central_line(model, X_115, X_125, 115, 125, incident=True)
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X(127)", classes=["center", "incident"])
    X_136 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2))/(a**(2) - b**(2) - c**(2))', ID="X(136)", classes=["center", "incident"])
    central_line(model, X_127, X_136, 127, 136, incident=True)
    return promote_point_to_top(model, X_868)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(868) on the given reference triangle."""
    model = create_model('X(868) = CROSSPOINT OF X(98) AND X(523)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00868(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00868.json"))
    write_center_svg(
        model_acute,
        here / "x-00868.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
