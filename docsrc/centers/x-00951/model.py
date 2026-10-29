"""GEOMETOR construction model for X(951) = ISOGONAL CONJUGATE OF X(950)."""

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


def construct_x_00951(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(951) = ISOGONAL CONJUGATE OF X(950) on reference triangle ABC."""
    X_950 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)*(2*a**(3) + (b + c)*(a**(2) + (b - c)**(2)))', ID="X(950)", classes=["center"])
    X_951 = isogonal_conjugate(model, A, B, C, X_950, ID="X(951)", classes=["selected", "target"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X(78)", classes=["center", "incident"])
    central_line(model, X_57, X_78, 57, 78, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X(226)", classes=["center", "incident"])
    central_line(model, X_29, X_226, 29, 226, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X(219)", classes=["center", "incident"])
    central_line(model, X_56, X_219, 56, 219, incident=True)
    return promote_point_to_top(model, X_951)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(951) on the given reference triangle."""
    model = create_model('X(951) = ISOGONAL CONJUGATE OF X(950)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00951(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00951.json"))
    write_center_svg(
        model_acute,
        here / "x-00951.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
