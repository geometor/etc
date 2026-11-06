"""GEOMETOR construction model for X_3554 = INTERSECTION OF LINES X_1X_6 AND X_19X_604."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03554(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3554 = INTERSECTION OF LINES X_1X_6 AND X_19X_604 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1422 = point_from_barycentrics(model, A, B, C, -0.022661722, -0.056036259, 1.078698, ID="X_1422", classes=["center"])
    X_3554 = crosspoint(model, A, B, C, X_1, X_1422, ID="X_3554", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    X_393 = eval_trilinear_point(model, A, B, C, 'b*c*(tan(A))**(2)', ID="X_393", classes=["center", "incident"])
    central_line(model, X_34, X_393, 34, 393, incident=True)
    X_198 = eval_trilinear_point(model, A, B, C, '(a*(cos(B) + cos(C) - cos(A) - 1))', ID="X_198", classes=["center", "incident"])
    X_319 = eval_trilinear_point(model, A, B, C, '(1 + 2*cos(A))/a**(2)', ID="X_319", classes=["center", "incident"])
    central_line(model, X_198, X_319, 198, 319, incident=True)
    return promote_point_to_top(model, X_3554)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3554 on the given reference triangle."""
    model = create_model('X_3554 = INTERSECTION OF LINES X_1X_6 AND X_19X_604')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03554(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03554.json"))
    write_center_svg(
        model_acute,
        here / "x-03554.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
