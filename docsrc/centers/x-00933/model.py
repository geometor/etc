"""GEOMETOR construction model for X(933) = X(4)-CROSS CONJUGATE OF X(250)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00933(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(933) = X(4)-CROSS CONJUGATE OF X(250) on reference triangle ABC."""
    X_933 = eval_trilinear_point(model, A, B, C, 'sec(A)*csc(2*B - 2*C)', ID="X(933)", classes=["selected", "target"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center", "incident"])
    central_line(model, X_54, X_74, 54, 74, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_137 = point_from_barycentrics(model, A, B, C, 0.1354431, 0.64976082, 0.21479608, ID="X(137)", classes=["center", "incident"])
    central_line(model, X_4, X_137, 4, 137, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    X_275 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*sec(B - C)', ID="X(275)", classes=["center", "incident"])
    central_line(model, X_98, X_275, 98, 275, incident=True)
    return promote_point_to_top(model, X_933)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(933) on the given reference triangle."""
    model = create_model('X(933) = X(4)-CROSS CONJUGATE OF X(250)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00933(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00933.json"))
    write_center_svg(
        model_acute,
        here / "x-00933.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
