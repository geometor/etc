"""GEOMETOR construction model for X_1691 = RADICAL TRACE OF CIRCUMCIRCLE AND 1st LEMOINE CIRCLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01691(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1691 = RADICAL TRACE OF CIRCUMCIRCLE AND 1st LEMOINE CIRCLE on reference triangle ABC."""
    X_1691 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(4) - b**(2)*c**(2))', ID="X_1691", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X_98", classes=["center", "incident"])
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    central_line(model, X_98, X_230, 98, 230, incident=True)
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center", "incident"])
    X_316 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2)))', ID="X_316", classes=["center", "incident"])
    central_line(model, X_83, X_316, 83, 316, incident=True)
    return promote_point_to_top(model, X_1691)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1691 on the given reference triangle."""
    model = create_model('X_1691 = RADICAL TRACE OF CIRCUMCIRCLE AND 1st LEMOINE CIRCLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01691(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01691.json"))
    write_center_svg(
        model_acute,
        here / "x-01691.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
