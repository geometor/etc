"""GEOMETOR construction model for X_1484 = REFLECTION OF X_5 IN X_11."""

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
    midpoint,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01484(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1484 = REFLECTION OF X_5 IN X_11 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_149 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(3) + c**(3) - a**(3) + (a**(2) - b*c)*(b + c) + a*(b*c - b**(2) - c**(2))))', ID="X_149", classes=["center"])
    X_1484 = midpoint(model, X_3, X_149, ID="X_1484", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_30, X_104, 30, 104, incident=True)
    central_line(model, X_3, X_149, 3, 149, incident=True)
    return promote_point_to_top(model, X_1484)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1484 on the given reference triangle."""
    model = create_model('X_1484 = REFLECTION OF X_5 IN X_11')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01484(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01484.json"))
    write_center_svg(
        model_acute,
        here / "x-01484.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
