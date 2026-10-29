"""GEOMETOR construction model for X(748) = INTERSECTION OF LINES X(2)X(31) AND X(9)X(38)."""

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
    feuerbach_point_of,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00748(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(748) = INTERSECTION OF LINES X(2)X(31) AND X(9)X(38) on reference triangle ABC."""
    X_748 = eval_trilinear_point(model, A, B, C, 'a**(2) - 2*b*c', ID="X(748)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    central_line(model, X_2, X_31, 2, 31, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X(38)", classes=["center", "incident"])
    central_line(model, X_9, X_38, 9, 38, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center", "incident"])
    X_212 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(A))', ID="X(212)", classes=["center", "incident"])
    central_line(model, X_11, X_212, 11, 212, incident=True)
    return promote_point_to_top(model, X_748)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(748) on the given reference triangle."""
    model = create_model('X(748) = INTERSECTION OF LINES X(2)X(31) AND X(9)X(38)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00748(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00748.json"))
    write_center_svg(
        model_acute,
        here / "x-00748.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
