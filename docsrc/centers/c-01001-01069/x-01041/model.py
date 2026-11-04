"""GEOMETOR construction model for X_1041 = ISOGONAL CONJUGATE OF X_1040."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    isogonal_conjugate,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01041(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1041 = ISOGONAL CONJUGATE OF X_1040 on reference triangle ABC."""
    X_1040 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(A)*cos(B)*cos(C)', ID="X_1040", classes=["center"])
    X_1041 = isogonal_conjugate(model, A, B, C, X_1040, ID="X_1041", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    central_line(model, X_7, X_33, 7, 33, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_8, X_34, 8, 34, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_294 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b**(2) + c**(2) - a*b - a*c))', ID="X_294", classes=["center", "incident"])
    central_line(model, X_19, X_294, 19, 294, incident=True)
    return promote_point_to_top(model, X_1041)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1041 on the given reference triangle."""
    model = create_model('X_1041 = ISOGONAL CONJUGATE OF X_1040')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01041(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01041.json"))
    write_center_svg(
        model_acute,
        here / "x-01041.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
