"""GEOMETOR construction model for X(240) = X(1)-LINE CONJUGATE OF X(48)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00240(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(240) = X(1)-LINE CONJUGATE OF X(48) on reference triangle ABC."""
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A + omega )', ID="X(240)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    central_line(model, X_1, X_19, 1, 19, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X(38)", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center", "incident"])
    central_line(model, X_38, X_92, 38, 92, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    X_158 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(2*A))', ID="X(158)", classes=["center", "incident"])
    central_line(model, X_75, X_158, 75, 158, incident=True)
    return promote_point_to_top(model, X_240)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(240) on the given reference triangle."""
    model = create_model('X(240) = X(1)-LINE CONJUGATE OF X(48)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00240(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00240.json"))
    write_center_svg(
        model_acute,
        here / "x-00240.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
