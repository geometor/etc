"""GEOMETOR construction model for X_1569 = MOSES-CIRCLE ANTIPODE OF X_115."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01569(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1569 = MOSES-CIRCLE ANTIPODE OF X_115 on reference triangle ABC."""
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center"])
    X_1569 = midpoint(model, X_99, X_194, ID="X_1569", classes=["selected", "target"], guide=False)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_5, X_39, 5, 39, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_32, X_99, 32, 99, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X_98", classes=["center", "incident"])
    X_574 = eval_trilinear_point(model, A, B, C, 'a*(a**(2) - 2*b**(2) - 2*c**(2))', ID="X_574", classes=["center", "incident"])
    central_line(model, X_98, X_574, 98, 574, incident=True)
    return promote_point_to_top(model, X_1569)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1569 on the given reference triangle."""
    model = create_model('X_1569 = MOSES-CIRCLE ANTIPODE OF X_115')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01569(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01569.json"))
    write_center_svg(
        model_acute,
        here / "x-01569.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
