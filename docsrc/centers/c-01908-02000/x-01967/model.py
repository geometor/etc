"""GEOMETOR construction model for X_1967 = TRILINEAR POLE OF PU(36)."""

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


def construct_x_01967(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1967 = TRILINEAR POLE OF PU(36) on reference triangle ABC."""
    X_1966 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*(a**(4) - b**(2)*c**(2))', ID="X_1966", classes=["center"])
    X_1967 = isogonal_conjugate(model, A, B, C, X_1966, ID="X_1967", classes=["selected", "target"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center", "incident"])
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X_291", classes=["center", "incident"])
    central_line(model, X_256, X_291, 256, 291, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_694 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) - b**(2)*c**(2))', ID="X_694", classes=["center", "incident"])
    central_line(model, X_42, X_694, 42, 694, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_799 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)/((cos(B))**(2) - (cos(C))**(2))', ID="X_799", classes=["center", "incident"])
    central_line(model, X_38, X_799, 38, 799, incident=True)
    return promote_point_to_top(model, X_1967)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1967 on the given reference triangle."""
    model = create_model('X_1967 = TRILINEAR POLE OF PU(36)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01967(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01967.json"))
    write_center_svg(
        model_acute,
        here / "x-01967.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
