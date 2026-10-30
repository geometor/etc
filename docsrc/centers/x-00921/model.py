"""GEOMETOR construction model for X(921) = ISOGONAL CONJUGATE OF X(920)."""

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


def construct_x_00921(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(921) = ISOGONAL CONJUGATE OF X(920) on reference triangle ABC."""
    X_920 = eval_trilinear_point(model, A, B, C, 'a**(6) - 3*a**(4)*(b**(2) + c**(2)) + a**(2)*(3*b**(4) - 2*b**(2)*c**(2) + 3*c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2))', ID="X(920)", classes=["center"])
    X_921 = isogonal_conjugate(model, A, B, C, X_920, ID="X(921)", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X(47)", classes=["center", "incident"])
    central_line(model, X_19, X_47, 19, 47, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X(63)", classes=["center", "incident"])
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X(91)", classes=["center", "incident"])
    central_line(model, X_63, X_91, 63, 91, incident=True)
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X(46)", classes=["center", "incident"])
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X(225)", classes=["center", "incident"])
    central_line(model, X_46, X_225, 46, 225, incident=True)
    return promote_point_to_top(model, X_921)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(921) on the given reference triangle."""
    model = create_model('X(921) = ISOGONAL CONJUGATE OF X(920)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00921(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00921.json"))
    write_center_svg(
        model_acute,
        here / "x-00921.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
