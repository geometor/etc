"""GEOMETOR construction model for X(687) = TRILINEAR POLE OF LINE X(4)X(110)."""

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


def construct_x_00687(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(687) = TRILINEAR POLE OF LINE X(4)X(110) on reference triangle ABC."""
    X_686 = eval_trilinear_point(model, A, B, C, 'sec(B)*csc(A - B) + sec(C)*csc(A - C)', ID="X(686)", classes=["center"])
    X_687 = isogonal_conjugate(model, A, B, C, X_686, ID="X(687)", classes=["selected", "target"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X(107)", classes=["center", "incident"])
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X(250)", classes=["center", "incident"])
    central_line(model, X_107, X_250, 107, 250, incident=True)
    X_249 = eval_trilinear_point(model, A, B, C, '(csc(A))*(csc(B - C))**(2)', ID="X(249)", classes=["center", "incident"])
    X_648 = eval_trilinear_point(model, A, B, C, '1/(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2)))', ID="X(648)", classes=["center", "incident"])
    central_line(model, X_249, X_648, 249, 648, incident=True)
    return promote_point_to_top(model, X_687)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(687) on the given reference triangle."""
    model = create_model('X(687) = TRILINEAR POLE OF LINE X(4)X(110)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00687(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00687.json"))
    write_center_svg(
        model_acute,
        here / "x-00687.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
