"""GEOMETOR construction model for X_1766 = MIMOSA TRANSFORM OF X_345."""

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
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01766(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1766 = MIMOSA TRANSFORM OF X_345 on reference triangle ABC."""
    X_990 = eval_trilinear_point(model, A, B, C, '(a**(5) - a**(4)*(b + c) - 2*a**(3)*b*c - a*(b - c)**(2)*(b**(2) + c**(2)) + (b - c)**(2)*(b + c)**(3))', ID="X_990", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_1766 = reflection_in_point(model, X_990, X_3, ID="X_1766", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_3, X_37, 3, 37, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_346 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)**(2)', ID="X_346", classes=["center", "incident"])
    central_line(model, X_20, X_346, 20, 346, incident=True)
    return promote_point_to_top(model, X_1766)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1766 on the given reference triangle."""
    model = create_model('X_1766 = MIMOSA TRANSFORM OF X_345')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01766(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01766.json"))
    write_center_svg(
        model_acute,
        here / "x-01766.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
