"""GEOMETOR construction model for X(248) = X(4)-LINE CONJUGATE OF X(132)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00248(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(248) = X(4)-LINE CONJUGATE OF X(132) on reference triangle ABC."""
    X_248 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*sec(A + omega )', ID="X(248)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    central_line(model, X_4, X_32, 4, 32, incident=True)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    central_line(model, X_39, X_54, 39, 54, incident=True)
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X(50)", classes=["center", "incident"])
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(67)", classes=["center", "incident"])
    central_line(model, X_50, X_67, 50, 67, incident=True)
    return promote_point_to_top(model, X_248)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(248) on the given reference triangle."""
    model = create_model('X(248) = X(4)-LINE CONJUGATE OF X(132)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00248(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00248.json"))
    write_center_svg(
        model_acute,
        here / "x-00248.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
