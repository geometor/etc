"""GEOMETOR construction model for X(958) = INTERSECTION OF LINES X(1)X(6) AND X(2)X(12)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00958(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(958) = INTERSECTION OF LINES X(1)X(6) AND X(2)X(12) on reference triangle ABC."""
    X_958 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(a**(2) + a*b + a*c + 2*b*c)', ID="X(958)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    central_line(model, X_3, X_10, 3, 10, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center", "incident"])
    central_line(model, X_2, X_12, 2, 12, incident=True)
    return promote_point_to_top(model, X_958)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(958) on the given reference triangle."""
    model = create_model('X(958) = INTERSECTION OF LINES X(1)X(6) AND X(2)X(12)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00958(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00958.json"))
    write_center_svg(
        model_acute,
        here / "x-00958.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
