"""GEOMETOR construction model for X(745) = EVEN (- 1, 3) CIRCUMCIRCLE POINT."""

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


def construct_x_00745(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(745) = EVEN (- 1, 3) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_744 = eval_trilinear_point(model, A, B, C, 'a**(-2)*(b**(3)+ c**(3)) - a**(2)*(b**(-1)+ c**(-1))', ID="X(744)", classes=["center"])
    X_745 = isogonal_conjugate(model, A, B, C, X_744, ID="X(745)", classes=["selected", "target"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X(38)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_38, X_99, 38, 99, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    X_689 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(4) - c**(4)))', ID="X(689)", classes=["center", "incident"])
    central_line(model, X_75, X_689, 75, 689, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_827 = eval_trilinear_point(model, A, B, C, '1/(a**(-1)*(b**(4) - c**(4)) + a**(3)*(b**(0) - c**(0)))', ID="X(827)", classes=["center", "incident"])
    central_line(model, X_31, X_827, 31, 827, incident=True)
    return promote_point_to_top(model, X_745)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(745) on the given reference triangle."""
    model = create_model('X(745) = EVEN (- 1, 3) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00745(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00745.json"))
    write_center_svg(
        model_acute,
        here / "x-00745.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
