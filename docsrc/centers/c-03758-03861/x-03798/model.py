"""GEOMETOR construction model for X_3798 = X_3239com[INVERSE(nT(a², a² - c²))]."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03798(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3798 = X_3239com[INVERSE(nT(a², a² - c²))] on reference triangle ABC."""
    X_3798 = eval_barycentric_point(model, A, B, C, '((b - c)*(b**(2) + c**(2) - 3*a**(2)))', ID="X_3798", classes=["selected", "target"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_239, X_514, 239, 514, incident=True)
    X_900 = eval_trilinear_point(model, A, B, C, '(b - c)*(b + c - 2*a)/a', ID="X_900", classes=["center", "incident"])
    X_2487 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*((b - c)**(2) + a*b + a*c - 4*a**(2)))', ID="X_2487", classes=["center", "incident"])
    central_line(model, X_900, X_2487, 900, 2487, incident=True)
    X_812 = eval_trilinear_point(model, A, B, C, 'a **(-2)*(b**(1) - c**(1)) + a**(0)*(b **(-1) - c **(-1))', ID="X_812", classes=["center", "incident"])
    X_3676 = eval_barycentric_point(model, A, B, C, '(b - c)/(b + c - a)', ID="X_3676", classes=["center", "incident"])
    central_line(model, X_812, X_3676, 812, 3676, incident=True)
    return promote_point_to_top(model, X_3798)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3798 on the given reference triangle."""
    model = create_model('X_3798 = X_3239com[INVERSE(nT(a², a² - c²))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03798(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03798.json"))
    write_center_svg(
        model_acute,
        here / "x-03798.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
