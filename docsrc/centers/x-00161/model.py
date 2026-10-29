"""GEOMETOR construction model for X(161) = X(63)-OF-TANGENTIAL-TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00161(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(161) = X(63)-OF-TANGENTIAL-TRIANGLE on reference triangle ABC."""
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X(68)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_161 = ceva_conjugate(model, A, B, C, X_68, X_6, ID="X(161)", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    central_line(model, X_6, X_25, 6, 25, incident=True)
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X(26)", classes=["center", "incident"])
    central_line(model, X_26, X_68, 26, 68, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X(22)", classes=["center", "incident"])
    X_343 = eval_trilinear_point(model, A, B, C, 'cot(A)*cos(B - C)', ID="X(343)", classes=["center", "incident"])
    central_line(model, X_22, X_343, 22, 343, incident=True)
    return promote_point_to_top(model, X_161)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(161) on the given reference triangle."""
    model = create_model('X(161) = X(63)-OF-TANGENTIAL-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00161(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00161.json"))
    write_center_svg(
        model_acute,
        here / "x-00161.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
