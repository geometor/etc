"""GEOMETOR construction model for X_3460 = X_5-CEVA CONJUGATE OF X_1."""

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
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03460(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3460 = X_5-CEVA CONJUGATE OF X_1 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center"])
    central_line(model, X_1, X_54, 1, 54)
    central_line(model, X_4, X_484, 4, 484)
    X_3460 = intersect_lines(model, X_1, X_54, X_4, X_484, ID="X_3460", classes=["selected", "target"])
    X_655 = eval_trilinear_point(model, A, B, C, '1/(cos(A - B) - cos(C- A))', ID="X_655", classes=["center", "incident"])
    X_1087 = eval_trilinear_point(model, A, B, C, '1 + cos(2*B - 2*C)', ID="X_1087", classes=["center", "incident"])
    central_line(model, X_655, X_1087, 655, 1087, incident=True)
    return promote_point_to_top(model, X_3460)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3460 on the given reference triangle."""
    model = create_model('X_3460 = X_5-CEVA CONJUGATE OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03460(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03460.json"))
    write_center_svg(
        model_acute,
        here / "x-03460.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
