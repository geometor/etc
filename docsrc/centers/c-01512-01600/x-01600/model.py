"""GEOMETOR construction model for X_1600 = POINT CHORT II."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01600(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1600 = POINT CHORT II on reference triangle ABC."""
    X_1592 = eval_trilinear_point(model, A, B, C, '(csc(A) - cos(B - C))', ID="X_1592", classes=["center"])
    X_1600 = anticomplement(model, A, B, C, X_1592, ID="X_1600", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_589 = eval_trilinear_point(model, A, B, C, '(a/(a**(2) - 4*area ))', ID="X_589", classes=["center", "incident"])
    central_line(model, X_6, X_589, 6, 589, incident=True)
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    X_1152 = eval_trilinear_point(model, A, B, C, 'sin(A) - 2*cos(A)', ID="X_1152", classes=["center", "incident"])
    central_line(model, X_394, X_1152, 394, 1152, incident=True)
    return promote_point_to_top(model, X_1600)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1600 on the given reference triangle."""
    model = create_model('X_1600 = POINT CHORT II')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01600(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01600.json"))
    write_center_svg(
        model_acute,
        here / "x-01600.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
