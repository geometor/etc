"""GEOMETOR construction model for X_2991 = DC(X_105)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02991(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2991 = DC(X_105) on reference triangle ABC."""
    X_1332 = eval_trilinear_point(model, A, B, C, '(b**(2) + c**(2) - a**(2))/(b - c)', ID="X_1332", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_2991 = reflection_in_point(model, X_1332, X_6, ID="X_2991", classes=["selected", "target"], guide=False)
    X_344 = eval_trilinear_point(model, A, B, C, '((csc(A/2))**(2))*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4))', ID="X_344", classes=["center", "incident"])
    central_line(model, X_6, X_344, 6, 344, incident=True)
    X_294 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b**(2) + c**(2) - a*b - a*c))', ID="X_294", classes=["center", "incident"])
    X_335 = eval_trilinear_point(model, A, B, C, 'b*c/(a**(2) - b*c)', ID="X_335", classes=["center", "incident"])
    central_line(model, X_294, X_335, 294, 335, incident=True)
    X_193 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cot(B) + cot(C) - cot(A))', ID="X_193", classes=["center", "incident"])
    X_608 = eval_trilinear_point(model, A, B, C, 'a*(1 - sec(A))', ID="X_608", classes=["center", "incident"])
    central_line(model, X_193, X_608, 193, 608, incident=True)
    return promote_point_to_top(model, X_2991)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2991 on the given reference triangle."""
    model = create_model('X_2991 = DC(X_105)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02991(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02991.json"))
    write_center_svg(
        model_acute,
        here / "x-02991.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
