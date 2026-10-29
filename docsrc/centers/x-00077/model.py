"""GEOMETOR construction model for X(77) = ISOGONAL CONJUGATE OF X(33)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcircle,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00077(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(77) = ISOGONAL CONJUGATE OF X(33) on reference triangle ABC."""
    circumcircle(model, A, B, C)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center"])
    central_line(model, X_1, X_7, 1, 7)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center"])
    central_line(model, X_29, X_34, 29, 34)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X(73)", classes=["center"])
    central_line(model, X_69, X_73, 69, 73)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center"])
    X_77 = isogonal_conjugate(model, A, B, C, X_33, ID="X(77)", classes=["selected", "target"])
    return promote_point_to_top(model, X_77)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(77) on the given reference triangle."""
    model = create_model('X(77) = ISOGONAL CONJUGATE OF X(33)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00077(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00077.json"))
    write_center_svg(
        model_acute,
        here / "x-00077.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
