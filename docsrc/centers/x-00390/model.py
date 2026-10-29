"""GEOMETOR construction model for X(390) = REFLECTION OF GERGONNE POINT IN INCENTER."""

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
    feuerbach_point_of,
    gergonne_point_of,
    incenter_of,
    midpoint,
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00390(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(390) = REFLECTION OF GERGONNE POINT IN INCENTER on reference triangle ABC."""
    X_144 = eval_trilinear_point(model, A, B, C, '(csc(A))*(tan(B/2) + tan(C/2) - tan(A/2))', ID="X(144)", classes=["center"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X(145)", classes=["center"])
    X_390 = midpoint(model, X_144, X_145, ID="X(390)", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center", "incident"])
    central_line(model, X_2, X_11, 2, 11, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    central_line(model, X_8, X_9, 8, 9, incident=True)
    return promote_point_to_top(model, X_390)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(390) on the given reference triangle."""
    model = create_model('X(390) = REFLECTION OF GERGONNE POINT IN INCENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00390(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00390.json"))
    write_center_svg(
        model_acute,
        here / "x-00390.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
