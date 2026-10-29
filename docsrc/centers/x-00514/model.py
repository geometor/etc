"""GEOMETOR construction model for X(514) = ISOGONAL CONJUGATE OF X(101)."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00514(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(514) = ISOGONAL CONJUGATE OF X(101) on reference triangle ABC."""
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center"])
    X_514 = isogonal_conjugate(model, A, B, C, X_101, ID="X(514)", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X(663)", classes=["center", "incident"])
    central_line(model, X_1, X_663, 1, 663, incident=True)
    X_664 = eval_trilinear_point(model, A, B, C, '1/(a*(b - c)*(b + c - a))', ID="X(664)", classes=["center", "incident"])
    central_line(model, X_101, X_664, 101, 664, incident=True)
    return promote_point_to_top(model, X_514)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(514) on the given reference triangle."""
    model = create_model('X(514) = ISOGONAL CONJUGATE OF X(101)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00514(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00514.json"))
    write_center_svg(
        model_acute,
        here / "x-00514.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
