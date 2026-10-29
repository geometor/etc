"""GEOMETOR construction model for X(561) = ISOGONAL CONJUGATE OF 4th POWER POINT."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00561(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(561) = ISOGONAL CONJUGATE OF 4th POWER POINT on reference triangle ABC."""
    X_560 = eval_trilinear_point(model, A, B, C, 'a**(4)', ID="X(560)", classes=["center"])
    X_561 = isogonal_conjugate(model, A, B, C, X_560, ID="X(561)", classes=["selected", "target"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X(38)", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    central_line(model, X_38, X_75, 38, 75, incident=True)
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center", "incident"])
    X_304 = eval_trilinear_point(model, A, B, C, 'cos(A)*csc(A - omega )', ID="X(304)", classes=["center", "incident"])
    central_line(model, X_92, X_304, 92, 304, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X(321)", classes=["center", "incident"])
    central_line(model, X_76, X_321, 76, 321, incident=True)
    return promote_point_to_top(model, X_561)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(561) on the given reference triangle."""
    model = create_model('X(561) = ISOGONAL CONJUGATE OF 4th POWER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00561(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00561.json"))
    write_center_svg(
        model_acute,
        here / "x-00561.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
