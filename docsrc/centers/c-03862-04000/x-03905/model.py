"""GEOMETOR construction model for X_3905 = X_626com[INVERSE(n(3rd EULER TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03905(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3905 = X_626com[INVERSE(n(3rd EULER TRIANGLE))] on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_712 = eval_trilinear_point(model, A, B, C, '(a **(-4)*(b **(-2) + c **(-2)) - a **(-3)*(b **(-3) + c **(-3)))', ID="X_712", classes=["center"])
    central_line(model, X_1, X_75, 1, 75)
    central_line(model, X_32, X_712, 32, 712)
    X_3905 = intersect_lines(model, X_1, X_75, X_32, X_712, ID="X_3905", classes=["selected", "target"])
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X_192", classes=["center", "incident"])
    X_2329 = point_from_barycentrics(model, A, B, C, 0.35982814, 0.34317938, 0.29699248, ID="X_2329", classes=["center", "incident"])
    central_line(model, X_192, X_2329, 192, 2329, incident=True)
    return promote_point_to_top(model, X_3905)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3905 on the given reference triangle."""
    model = create_model('X_3905 = X_626com[INVERSE(n(3rd EULER TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03905(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03905.json"))
    write_center_svg(
        model_acute,
        here / "x-03905.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
