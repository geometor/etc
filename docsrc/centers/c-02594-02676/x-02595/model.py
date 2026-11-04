"""GEOMETOR construction model for X_2595 = CROSSSUM OF PU(68)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02595(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2595 = CROSSSUM OF PU(68) on reference triangle ABC."""
    X_2595 = eval_trilinear_point(model, A, B, C, '(cos(A - B)*cos(A - C) + (cos(B - C))**(2))', ID="X_2595", classes=["selected", "target"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_1087 = eval_trilinear_point(model, A, B, C, '1 + cos(2*B - 2*C)', ID="X_1087", classes=["center", "incident"])
    central_line(model, X_54, X_1087, 54, 1087, incident=True)
    X_1048 = eval_trilinear_point(model, A, B, C, 'a**(7)*(b**(2) + b*c + c**(2)) + a**(6)*(b + c)*(b**(2) + b*c + c**(2)) - a**(5)*(2*b**(4) + b**(3)*c + b*c**(3) + 2*c**(4)) - 2*a**(4)*(b + c)**(3)*(b**(2) - b*c + c**(2)) + a**(3)*(b**(6) - b**(5)*c - 2*b**(4)*c**(2) - b**(3)*c**(3) - 2*b**(2)*c**(4) - b*c**(5) + c**(6)) + a**(2)*(b**(7) + 2*b**(6)*c - 2*b**(4)*c**(3) - 2*b**(3)*c**(4) + 2*b*c**(6) + c**(7)) + a*b*c*(b**(2) - c**(2))**(2)*(b**(2) + c**(2)) - b**(2)*c**(2)*(b - c)**(2)*(b + c)**(3)', ID="X_1048", classes=["center", "incident"])
    X_2594 = eval_trilinear_point(model, A, B, C, '(cos(C- A) + cos(B - A))', ID="X_2594", classes=["center", "incident"])
    central_line(model, X_1048, X_2594, 1048, 2594, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_2607 = eval_trilinear_point(model, A, B, C, 'sin(A - B)*sin(A - C) + (sin(B - C))**(2)', ID="X_2607", classes=["center", "incident"])
    central_line(model, X_12, X_2607, 12, 2607, incident=True)
    return promote_point_to_top(model, X_2595)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2595 on the given reference triangle."""
    model = create_model('X_2595 = CROSSSUM OF PU(68)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02595(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02595.json"))
    write_center_svg(
        model_acute,
        here / "x-02595.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
