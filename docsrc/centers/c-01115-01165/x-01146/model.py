"""GEOMETOR construction model for X_1146 = CENTER OF HYPERBOLA {{A,B,C,X_2,X_8}}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01146(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1146 = CENTER OF HYPERBOLA {{A,B,C,X_2,X_8}} on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_1121 = eval_trilinear_point(model, A, B, C, '(b*c/((b + c - a)*a - (a + b - c)*(a + c - b)))', ID="X_1121", classes=["center"])
    X_1146 = midpoint(model, X_2, X_1121, ID="X_1146", classes=["selected", "target"], guide=False)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_9, X_80, 9, 80, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_220 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)**(2)', ID="X_220", classes=["center", "incident"])
    central_line(model, X_8, X_220, 8, 220, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_124 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(b - c)**(2)*((b + c)*(b**(2) + c**(2) - a**(2) - b*c) + a*b*c))', ID="X_124", classes=["center", "incident"])
    central_line(model, X_115, X_124, 115, 124, incident=True)
    return promote_point_to_top(model, X_1146)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1146 on the given reference triangle."""
    model = create_model('X_1146 = CENTER OF HYPERBOLA {{A,B,C,X_2,X_8}}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01146(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01146.json"))
    write_center_svg(
        model_acute,
        here / "x-01146.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
