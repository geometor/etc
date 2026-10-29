"""GEOMETOR construction model for X(581) = ORTHOHARMONIC OF X(284)."""

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
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00581(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(581) = ORTHOHARMONIC OF X(284) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    central_line(model, X_1, X_4, 1, 4)
    central_line(model, X_3, X_6, 3, 6)
    X_581 = intersect_lines(model, X_1, X_4, X_3, X_6, ID="X(581)", classes=["selected", "target"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X(35)", classes=["center", "incident"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X(47)", classes=["center", "incident"])
    central_line(model, X_35, X_47, 35, 47, incident=True)
    return promote_point_to_top(model, X_581)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(581) on the given reference triangle."""
    model = create_model('X(581) = ORTHOHARMONIC OF X(284)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00581(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00581.json"))
    write_center_svg(
        model_acute,
        here / "x-00581.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
