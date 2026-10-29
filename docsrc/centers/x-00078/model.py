"""GEOMETOR construction model for X(78) = ISOGONAL CONJUGATE OF X(34)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00078(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(78) = ISOGONAL CONJUGATE OF X(34) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    central_line(model, X_1, X_2, 1, 2)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center"])
    central_line(model, X_9, X_21, 9, 21)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center"])
    central_line(model, X_29, X_33, 29, 33)
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center"])
    X_78 = isogonal_conjugate(model, A, B, C, X_34, ID="X(78)", classes=["selected", "target"])
    return promote_point_to_top(model, X_78)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(78) on the given reference triangle."""
    model = create_model('X(78) = ISOGONAL CONJUGATE OF X(34)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00078(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00078.json"))
    write_center_svg(
        model_acute,
        here / "x-00078.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
