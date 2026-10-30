"""GEOMETOR construction model for X(840) = ISOGONAL CONJUGATE OF X(528)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00840(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(840) = ISOGONAL CONJUGATE OF X(528) on reference triangle ABC."""
    X_528 = point_from_barycentrics(model, A, B, C, -0.26726124, 0.80178373, -0.53452248, ID="X(528)", classes=["center"])
    X_840 = isogonal_conjugate(model, A, B, C, X_528, ID="X(840)", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_36, X_101, 36, 101, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_518 = point_from_barycentrics(model, A, B, C, -0.66389881, -0.079667858, 0.74356667, ID="X(518)", classes=["center", "incident"])
    central_line(model, X_100, X_518, 100, 518, incident=True)
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X(105)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_105, X_513, 105, 513, incident=True)
    return promote_point_to_top(model, X_840)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(840) on the given reference triangle."""
    model = create_model('X(840) = ISOGONAL CONJUGATE OF X(528)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00840(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00840.json"))
    write_center_svg(
        model_acute,
        here / "x-00840.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
