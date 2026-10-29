"""GEOMETOR construction model for X(232) = X(2)-CEVA CONJUGATE OF X(132)."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00232(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(232) = X(2)-CEVA CONJUGATE OF X(132) on reference triangle ABC."""
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A + omega )', ID="X(232)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    central_line(model, X_6, X_25, 6, 25, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    central_line(model, X_4, X_39, 4, 39, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X(24)", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    central_line(model, X_24, X_32, 24, 32, incident=True)
    return promote_point_to_top(model, X_232)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(232) on the given reference triangle."""
    model = create_model('X(232) = X(2)-CEVA CONJUGATE OF X(132)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00232(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00232.json"))
    write_center_svg(
        model_acute,
        here / "x-00232.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
