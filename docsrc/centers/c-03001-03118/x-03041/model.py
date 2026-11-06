"""GEOMETOR construction model for X_3041 = COMPLEMENT OF X_1362."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    mittenpunkt_of,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03041(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3041 = COMPLEMENT OF X_1362 on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_3022 = eval_trilinear_point(model, A, B, C, '(a*(b - c)**(2)*(b + c - a)**(3))', ID="X_3022", classes=["center"])
    X_3041 = midpoint(model, X_8, X_3022, ID="X_3041", classes=["selected", "target"], guide=False)
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center", "incident"])
    X_124 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)*(b - c)**(2)*((b + c)*(b**(2) + c**(2) - a**(2) - b*c) + a*b*c))', ID="X_124", classes=["center", "incident"])
    central_line(model, X_118, X_124, 118, 124, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_958 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(a**(2) + a*b + a*c + 2*b*c)', ID="X_958", classes=["center", "incident"])
    central_line(model, X_101, X_958, 101, 958, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_1282 = point_from_barycentrics(model, A, B, C, 0.61507937, -0.97619048, 1.3611111, ID="X_1282", classes=["center", "incident"])
    central_line(model, X_9, X_1282, 9, 1282, incident=True)
    return promote_point_to_top(model, X_3041)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3041 on the given reference triangle."""
    model = create_model('X_3041 = COMPLEMENT OF X_1362')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03041(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03041.json"))
    write_center_svg(
        model_acute,
        here / "x-03041.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
