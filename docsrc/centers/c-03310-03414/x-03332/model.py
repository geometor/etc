"""GEOMETOR construction model for X_3332 = INTERSECTION OF LINES X_1X_7 AND X_4X_6."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03332(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3332 = INTERSECTION OF LINES X_1X_7 AND X_4X_6 on reference triangle ABC."""
    X_3332 = eval_trilinear_point(model, A, B, C, '((cos(C))*(1 + cos(B))*(cos(C) - cos(A))*(sin(2*A) - sin(2*B)) - (cos(B))*(1 + cos(C))*(cos(A) - cos(B))*(sin(2*C) - sin(2*A)))', ID="X_3332", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_278 = eval_trilinear_point(model, A, B, C, 'sec(A)*tan(A/2)', ID="X_278", classes=["center", "incident"])
    X_1456 = point_from_barycentrics(model, A, B, C, -0.40740741, -0.35555556, 1.762963, ID="X_1456", classes=["center", "incident"])
    central_line(model, X_278, X_1456, 278, 1456, incident=True)
    return promote_point_to_top(model, X_3332)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3332 on the given reference triangle."""
    model = create_model('X_3332 = INTERSECTION OF LINES X_1X_7 AND X_4X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03332(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03332.json"))
    write_center_svg(
        model_acute,
        here / "x-03332.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
