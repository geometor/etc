"""GEOMETOR construction model for X(688) = CROSSDIFFERENCE OF X(6) AND X(76)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00688(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(688) = CROSSDIFFERENCE OF X(6) AND X(76) on reference triangle ABC."""
    X_688 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(4)- c**(4))', ID="X(688)", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_882 = point_from_barycentrics(model, A, B, C, 0.023590899, 1.0060979, -0.02968882, ID="X(882)", classes=["center", "incident"])
    central_line(model, X_6, X_882, 6, 882, incident=True)
    X_669 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(2) - c**(2))', ID="X(669)", classes=["center", "incident"])
    X_864 = point_from_barycentrics(model, A, B, C, -0.32864548, -0.077550067, 1.4061955, ID="X(864)", classes=["center", "incident"])
    central_line(model, X_669, X_864, 669, 864, incident=True)
    return promote_point_to_top(model, X_688)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(688) on the given reference triangle."""
    model = create_model('X(688) = CROSSDIFFERENCE OF X(6) AND X(76)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00688(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00688.json"))
    write_center_svg(
        model_acute,
        here / "x-00688.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
