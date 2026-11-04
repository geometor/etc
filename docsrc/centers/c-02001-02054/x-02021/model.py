"""GEOMETOR construction model for X_2021 = RADICAL TRACE OF GALLATLY CIRCLE AND CIRCUMCIRCLE."""

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
    midpoint,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02021(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2021 = RADICAL TRACE OF GALLATLY CIRCLE AND CIRCUMCIRCLE on reference triangle ABC."""
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center"])
    X_2021 = midpoint(model, X_39, X_187, ID="X_2021", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_620 = point_from_barycentrics(model, A, B, C, 0.40242494, 0.16743649, 0.43013857, ID="X_620", classes=["center", "incident"])
    X_736 = eval_trilinear_point(model, A, B, C, '(a **(-3)*(b**(4) + c**(4)) - a**(3)*(b **(-2) + c **(-2)))', ID="X_736", classes=["center", "incident"])
    central_line(model, X_620, X_736, 620, 736, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_1513 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))*(3*a**(4) + (b**(2) - c**(2))**(2)))', ID="X_1513", classes=["center", "incident"])
    central_line(model, X_115, X_1513, 115, 1513, incident=True)
    return promote_point_to_top(model, X_2021)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2021 on the given reference triangle."""
    model = create_model('X_2021 = RADICAL TRACE OF GALLATLY CIRCLE AND CIRCUMCIRCLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02021(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02021.json"))
    write_center_svg(
        model_acute,
        here / "x-02021.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
