"""GEOMETOR construction model for X(757) = ISOGONAL CONJUGATE OF X(756)."""

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


def construct_x_00757(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(757) = ISOGONAL CONJUGATE OF X(756) on reference triangle ABC."""
    X_756 = eval_trilinear_point(model, A, B, C, '(b + c)**(2)', ID="X(756)", classes=["center"])
    X_757 = isogonal_conjugate(model, A, B, C, X_756, ID="X(757)", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X(86)", classes=["center", "incident"])
    central_line(model, X_58, X_86, 58, 86, incident=True)
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X(171)", classes=["center", "incident"])
    X_319 = eval_trilinear_point(model, A, B, C, '(1 + 2*cos(A))/a**(2)', ID="X(319)", classes=["center", "incident"])
    central_line(model, X_171, X_319, 171, 319, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X(662)", classes=["center", "incident"])
    central_line(model, X_6, X_662, 6, 662, incident=True)
    return promote_point_to_top(model, X_757)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(757) on the given reference triangle."""
    model = create_model('X(757) = ISOGONAL CONJUGATE OF X(756)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00757(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00757.json"))
    write_center_svg(
        model_acute,
        here / "x-00757.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
