"""GEOMETOR construction model for X(604) = X(56)-CEVA CONJUGATE OF X(31)."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00604(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(604) = X(56)-CEVA CONJUGATE OF X(31) on reference triangle ABC."""
    X_312 = eval_trilinear_point(model, A, B, C, '(b + c - a)*b**(2)*c**(2)', ID="X(312)", classes=["center"])
    X_604 = isogonal_conjugate(model, A, B, C, X_312, ID="X(604)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["center", "incident"])
    central_line(model, X_6, X_41, 6, 41, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X(77)", classes=["center", "incident"])
    central_line(model, X_57, X_77, 57, 77, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X(184)", classes=["center", "incident"])
    central_line(model, X_31, X_184, 31, 184, incident=True)
    return promote_point_to_top(model, X_604)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(604) on the given reference triangle."""
    model = create_model('X(604) = X(56)-CEVA CONJUGATE OF X(31)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00604(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00604.json"))
    write_center_svg(
        model_acute,
        here / "x-00604.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
