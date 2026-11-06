"""GEOMETOR construction model for X_3992 = X_1149com[INVERSE(n(INCENTRAL TRIANGLE))]."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03992(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3992 = X_1149com[INVERSE(n(INCENTRAL TRIANGLE))] on reference triangle ABC."""
    X_3992 = eval_barycentric_point(model, A, B, C, '(b*c*(b + c)*(b + c - 2*a))', ID="X_3992", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_10, X_321, 10, 321, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_341 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*(b + c - a)**(2)', ID="X_341", classes=["center", "incident"])
    central_line(model, X_1, X_341, 1, 341, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center", "incident"])
    central_line(model, X_190, X_484, 190, 484, incident=True)
    return promote_point_to_top(model, X_3992)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3992 on the given reference triangle."""
    model = create_model('X_3992 = X_1149com[INVERSE(n(INCENTRAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03992(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03992.json"))
    write_center_svg(
        model_acute,
        here / "x-03992.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
