"""GEOMETOR construction model for X_1360 = BRISSE TRANSFORM OF X_103."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01360(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1360 = BRISSE TRANSFORM OF X_103 on reference triangle ABC."""
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center"])
    central_line(model, X_11, X_57, 11, 57)
    central_line(model, X_56, X_105, 56, 105)
    X_1360 = intersect_lines(model, X_11, X_57, X_56, X_105, ID="X_1360", classes=["selected", "target"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    central_line(model, X_55, X_108, 55, 108, incident=True)
    return promote_point_to_top(model, X_1360)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1360 on the given reference triangle."""
    model = create_model('X_1360 = BRISSE TRANSFORM OF X_103')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01360(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01360.json"))
    write_center_svg(
        model_acute,
        here / "x-01360.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
