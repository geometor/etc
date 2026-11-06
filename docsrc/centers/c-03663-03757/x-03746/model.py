"""GEOMETOR construction model for X_3746 = X_191com[n(MEDIAL)*n(INCENTRAL)]."""

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


def construct_x_03746(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3746 = X_191com[n(MEDIAL)*n(INCENTRAL)] on reference triangle ABC."""
    X_3746 = eval_trilinear_point(model, A, B, C, '3 + 2*cos(A)', ID="X_3746", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_21, X_519, 21, 519, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_546 = eval_trilinear_point(model, A, B, C, '3*cos(B - C) - 2*cos(A)', ID="X_546", classes=["center", "incident"])
    central_line(model, X_12, X_546, 12, 546, incident=True)
    return promote_point_to_top(model, X_3746)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3746 on the given reference triangle."""
    model = create_model('X_3746 = X_191com[n(MEDIAL)*n(INCENTRAL)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03746(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03746.json"))
    write_center_svg(
        model_acute,
        here / "x-03746.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
