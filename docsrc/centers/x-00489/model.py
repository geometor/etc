"""GEOMETOR construction model for X(489) = CEVAPOINT OF X(20) AND X(487)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00489(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(489) = CEVAPOINT OF X(20) AND X(487) on reference triangle ABC."""
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center"])
    X_487 = point_from_barycentrics(model, A, B, C, -1.1839423, 1.1273575, 1.0565848, ID="X(487)", classes=["center"])
    X_489 = cevapoint(model, A, B, C, X_20, X_487, ID="X(489)", classes=["selected", "target"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X(64)", classes=["center", "incident"])
    central_line(model, X_20, X_64, 20, 64, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    central_line(model, X_4, X_487, 4, 487, incident=True)
    X_376 = eval_trilinear_point(model, A, B, C, '5*cos(A) - cos(B - C)', ID="X(376)", classes=["center", "incident"])
    X_488 = point_from_barycentrics(model, A, B, C, 0.48788658, 0.37148244, 0.14063098, ID="X(488)", classes=["center", "incident"])
    central_line(model, X_376, X_488, 376, 488, incident=True)
    return promote_point_to_top(model, X_489)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(489) on the given reference triangle."""
    model = create_model('X(489) = CEVAPOINT OF X(20) AND X(487)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00489(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00489.json"))
    write_center_svg(
        model_acute,
        here / "x-00489.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
