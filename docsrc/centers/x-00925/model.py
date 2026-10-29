"""GEOMETOR construction model for X(925) = ANTICOMPLEMENT OF X(136)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00925(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(925) = ANTICOMPLEMENT OF X(136) on reference triangle ABC."""
    X_924 = eval_trilinear_point(model, A, B, C, 'b*cos(A - B) - c*cos(A - C)', ID="X(924)", classes=["center"])
    X_925 = isogonal_conjugate(model, A, B, C, X_924, ID="X(925)", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X(68)", classes=["center", "incident"])
    central_line(model, X_20, X_68, 20, 68, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X(22)", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    central_line(model, X_22, X_98, 22, 98, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_131 = point_from_barycentrics(model, A, B, C, 0.57236082, 0.12379803, 0.30384114, ID="X(131)", classes=["center", "incident"])
    central_line(model, X_4, X_131, 4, 131, incident=True)
    return promote_point_to_top(model, X_925)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(925) on the given reference triangle."""
    model = create_model('X(925) = ANTICOMPLEMENT OF X(136)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00925(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00925.json"))
    write_center_svg(
        model_acute,
        here / "x-00925.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
