"""GEOMETOR construction model for X(969) = INTERSECTION OF LINES X(10)X(69) AND X(19)X(81)."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00969(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(969) = INTERSECTION OF LINES X(10)X(69) AND X(19)X(81) on reference triangle ABC."""
    X_968 = eval_trilinear_point(model, A, B, C, 'a**(2) - 2*a*(b + c) - (b + c)**(2)', ID="X(968)", classes=["center"])
    X_969 = isogonal_conjugate(model, A, B, C, X_968, ID="X(969)", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    central_line(model, X_10, X_69, 10, 69, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X(81)", classes=["center", "incident"])
    central_line(model, X_19, X_81, 19, 81, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X(63)", classes=["center", "incident"])
    central_line(model, X_37, X_63, 37, 63, incident=True)
    return promote_point_to_top(model, X_969)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(969) on the given reference triangle."""
    model = create_model('X(969) = INTERSECTION OF LINES X(10)X(69) AND X(19)X(81)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00969(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00969.json"))
    write_center_svg(
        model_acute,
        here / "x-00969.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
