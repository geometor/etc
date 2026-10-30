"""GEOMETOR construction model for X(988) = INTERSECTION OF LINES X(1)X(3) AND X(9)X(39)."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00988(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(988) = INTERSECTION OF LINES X(1)X(3) AND X(9)X(39) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center"])
    central_line(model, X_1, X_3, 1, 3)
    central_line(model, X_9, X_39, 9, 39)
    X_988 = intersect_lines(model, X_1, X_3, X_9, X_39, ID="X(988)", classes=["selected", "target"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X(38)", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X(78)", classes=["center", "incident"])
    central_line(model, X_38, X_78, 38, 78, incident=True)
    return promote_point_to_top(model, X_988)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(988) on the given reference triangle."""
    model = create_model('X(988) = INTERSECTION OF LINES X(1)X(3) AND X(9)X(39)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00988(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00988.json"))
    write_center_svg(
        model_acute,
        here / "x-00988.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
