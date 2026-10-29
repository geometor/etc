"""GEOMETOR construction model for X(937) = ISOGONAL CONJUGATE OF X(936)."""

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


def construct_x_00937(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(937) = ISOGONAL CONJUGATE OF X(936) on reference triangle ABC."""
    X_936 = eval_trilinear_point(model, A, B, C, 'a**(3) - a**(2)*(b + c) - a*(b - c)**(2) + (b + c)**(3)', ID="X(936)", classes=["center"])
    X_937 = isogonal_conjugate(model, A, B, C, X_936, ID="X(937)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    central_line(model, X_6, X_40, 6, 40, incident=True)
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center", "incident"])
    X_196 = eval_trilinear_point(model, A, B, C, '(cos(B) + cos(C) - cos(A) - 1)*sec(A)*tan(A/2)', ID="X(196)", classes=["center", "incident"])
    central_line(model, X_34, X_196, 34, 196, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X(223)", classes=["center", "incident"])
    central_line(model, X_56, X_223, 56, 223, incident=True)
    return promote_point_to_top(model, X_937)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(937) on the given reference triangle."""
    model = create_model('X(937) = ISOGONAL CONJUGATE OF X(936)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00937(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00937.json"))
    write_center_svg(
        model_acute,
        here / "x-00937.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
