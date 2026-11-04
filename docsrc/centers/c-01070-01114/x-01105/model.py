"""GEOMETOR construction model for X_1105 = CEVAPOINT OF X_3 AND X_4."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01105(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1105 = CEVAPOINT OF X_3 AND X_4 on reference triangle ABC."""
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center"])
    X_1105 = isogonal_conjugate(model, A, B, C, X_185, ID="X_1105", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_393 = eval_trilinear_point(model, A, B, C, 'b*c*(tan(A))**(2)', ID="X_393", classes=["center", "incident"])
    central_line(model, X_20, X_393, 20, 393, incident=True)
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    X_412 = eval_barycentric_point(model, A, B, C, '(a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2)) * (a**(6) + a**(5)*b - 2*a**(4)*b**(2) - 2*a**(3)*b**(3) + a**(2)*b**(4) + a*b**(5) + a**(5)*c - a**(4)*b*c - a*b**(4)*c + b**(5)*c - 2*a**(4)*c**(2) + 2*a**(2)*b**(2)*c**(2) - 2*a**(3)*c**(3) - 2*b**(3)*c**(3) + a**(2)*c**(4) - a*b*c**(4) + a*c**(5) + b*c**(5))', ID="X_412", classes=["center", "incident"])
    central_line(model, X_225, X_412, 225, 412, incident=True)
    X_243 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(2) - cos(B)*cos(C))', ID="X_243", classes=["center", "incident"])
    X_411 = eval_trilinear_point(model, A, B, C, '(cos(B)*cos(C) - (cos(A) + cos(B) + cos(C))*cos(A))', ID="X_411", classes=["center", "incident"])
    central_line(model, X_243, X_411, 243, 411, incident=True)
    return promote_point_to_top(model, X_1105)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1105 on the given reference triangle."""
    model = create_model('X_1105 = CEVAPOINT OF X_3 AND X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01105(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01105.json"))
    write_center_svg(
        model_acute,
        here / "x-01105.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
