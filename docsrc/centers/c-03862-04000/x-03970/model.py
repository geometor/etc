"""GEOMETOR construction model for X_3970 = X_1334com[INVERSE(n(INCENTRAL TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03970(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3970 = X_1334com[INVERSE(n(INCENTRAL TRIANGLE))] on reference triangle ABC."""
    X_3970 = eval_barycentric_point(model, A, B, C, '(a*(b + c)*(b**(2) + c**(2) - b*c - c*a - a*b))', ID="X_3970", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_1018 = eval_trilinear_point(model, A, B, C, '((b + c)/(b - c))', ID="X_1018", classes=["center", "incident"])
    central_line(model, X_65, X_1018, 65, 1018, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1759 = eval_trilinear_point(model, A, B, C, '(a**(3) - b**(3) - c**(3))', ID="X_1759", classes=["center", "incident"])
    central_line(model, X_55, X_1759, 55, 1759, incident=True)
    return promote_point_to_top(model, X_3970)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3970 on the given reference triangle."""
    model = create_model('X_3970 = X_1334com[INVERSE(n(INCENTRAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03970(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03970.json"))
    write_center_svg(
        model_acute,
        here / "x-03970.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
