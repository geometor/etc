"""GEOMETOR construction model for X_365 = SQUARE ROOT POINT."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00365(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_365 = SQUARE ROOT POINT on reference triangle ABC."""
    X_365 = eval_trilinear_point(model, A, B, C, 'a**(1/2)', ID="X_365", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_364 = eval_trilinear_point(model, A, B, C, 'b**(1/2) + c**(1/2) - a**(1/2)', ID="X_364", classes=["center", "incident"])
    central_line(model, X_1, X_364, 1, 364, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_2068 = eval_trilinear_point(model, A, B, C, '(a + b**(1/2)*c**(1/2))', ID="X_2068", classes=["center", "incident"])
    central_line(model, X_43, X_2068, 43, 2068, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_2118 = eval_trilinear_point(model, A, B, C, '(a*(a + b + c)*(b*c)**(1/2) + (b*c + c*a + a*b)*(a - (a*b)**(1/2) - (a*c)**(1/2)))', ID="X_2118", classes=["center", "incident"])
    central_line(model, X_6, X_2118, 6, 2118, incident=True)
    return promote_point_to_top(model, X_365)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_365 on the given reference triangle."""
    model = create_model('X_365 = SQUARE ROOT POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00365(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00365.json"))
    write_center_svg(
        model_acute,
        here / "x-00365.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
