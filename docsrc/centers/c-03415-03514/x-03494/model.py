"""GEOMETOR construction model for X_3494 = INTERSECTION OF LINES X_1X_87 AND X_3X_2053."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03494(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3494 = INTERSECTION OF LINES X_1X_87 AND X_3X_2053 on reference triangle ABC."""
    X_3494 = eval_trilinear_point(model, A, B, C, '((a**(2) + b**(2) + c**(2) - a*b - a*c + b*c)/(a*b + a*c - b*c))', ID="X_3494", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X_87", classes=["center", "incident"])
    central_line(model, X_1, X_87, 1, 87, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_2053 = eval_trilinear_point(model, A, B, C, '(a*(b + c - a)/(a*b + a*c - b*c))', ID="X_2053", classes=["center", "incident"])
    central_line(model, X_3, X_2053, 3, 2053, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_2319 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(a*b + a*c - b*c))', ID="X_2319", classes=["center", "incident"])
    central_line(model, X_32, X_2319, 32, 2319, incident=True)
    return promote_point_to_top(model, X_3494)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3494 on the given reference triangle."""
    model = create_model('X_3494 = INTERSECTION OF LINES X_1X_87 AND X_3X_2053')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03494(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03494.json"))
    write_center_svg(
        model_acute,
        here / "x-03494.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
