"""GEOMETOR construction model for X(998) = ISOGONAL CONJUGATE OF X(997)."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00998(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(998) = ISOGONAL CONJUGATE OF X(997) on reference triangle ABC."""
    X_997 = eval_trilinear_point(model, A, B, C, 'a**(3)- a**(2)*(b + c) - a*(b - c)**(2)+ (b + c)*(b**(2)+ c**(2))', ID="X(997)", classes=["center"])
    X_998 = isogonal_conjugate(model, A, B, C, X_997, ID="X(998)", classes=["selected", "target"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X(46)", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    central_line(model, X_46, X_58, 46, 58, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X(517)", classes=["center", "incident"])
    central_line(model, X_6, X_517, 6, 517, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X(106)", classes=["center", "incident"])
    X_614 = eval_trilinear_point(model, A, B, C, '(cot(B/2))**(2) + (cot(C/2))**(2)', ID="X(614)", classes=["center", "incident"])
    central_line(model, X_106, X_614, 106, 614, incident=True)
    return promote_point_to_top(model, X_998)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(998) on the given reference triangle."""
    model = create_model('X(998) = ISOGONAL CONJUGATE OF X(997)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00998(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00998.json"))
    write_center_svg(
        model_acute,
        here / "x-00998.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
