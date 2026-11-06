"""GEOMETOR construction model for X_3503 = ISOGONAL CONJUGATE OF X_3495."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03503(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3503 = ISOGONAL CONJUGATE OF X_3495 on reference triangle ABC."""
    X_3495 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b**(2)*c**(2) + c**(2)*a**(2) + a**(2)*b**(2) - a*b*c*(b + c - a)))', ID="X_3495", classes=["center"])
    X_3503 = isogonal_conjugate(model, A, B, C, X_3495, ID="X_3503", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_1923 = eval_trilinear_point(model, A, B, C, 'a**(4)*(b**(2) + c**(2))', ID="X_1923", classes=["center", "incident"])
    central_line(model, X_109, X_1923, 109, 1923, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_3501 = eval_trilinear_point(model, A, B, C, '(a - b)*(a - c)*(b + c) + a*b*c', ID="X_3501", classes=["center", "incident"])
    central_line(model, X_76, X_3501, 76, 3501, incident=True)
    return promote_point_to_top(model, X_3503)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3503 on the given reference triangle."""
    model = create_model('X_3503 = ISOGONAL CONJUGATE OF X_3495')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03503(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03503.json"))
    write_center_svg(
        model_acute,
        here / "x-03503.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
