"""GEOMETOR construction model for X_1647 = TRIPOLAR CENTROID OF X_514."""

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
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01647(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1647 = TRIPOLAR CENTROID OF X_514 on reference triangle ABC."""
    X_1644 = point_from_barycentrics(model, A, B, C, 0.70710678, 0, -0.70710678, ID="X_1644", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_1647 = reflection_in_point(model, X_1644, X_2, ID="X_1647", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    central_line(model, X_80, X_106, 80, 106, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_11, X_244, 11, 244, incident=True)
    return promote_point_to_top(model, X_1647)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1647 on the given reference triangle."""
    model = create_model('X_1647 = TRIPOLAR CENTROID OF X_514')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01647(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01647.json"))
    write_center_svg(
        model_acute,
        here / "x-01647.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
