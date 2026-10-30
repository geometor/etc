"""GEOMETOR construction model for X(612) = INTERSECTION OF LINES X(1)X(2) AND X(9)X(31)."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00612(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(612) = INTERSECTION OF LINES X(1)X(2) AND X(9)X(31) on reference triangle ABC."""
    X_612 = eval_trilinear_point(model, A, B, C, 'a**(2) + b**(2) + c**(2) + 2*b*c', ID="X(612)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    central_line(model, X_9, X_31, 9, 31, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    central_line(model, X_19, X_25, 19, 25, incident=True)
    return promote_point_to_top(model, X_612)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(612) on the given reference triangle."""
    model = create_model('X(612) = INTERSECTION OF LINES X(1)X(2) AND X(9)X(31)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00612(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00612.json"))
    write_center_svg(
        model_acute,
        here / "x-00612.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
