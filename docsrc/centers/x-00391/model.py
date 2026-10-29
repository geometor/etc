"""GEOMETOR construction model for X(391) = INTERSECTION OF LINES X(2,6) AND X(8,9)."""

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
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00391(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(391) = INTERSECTION OF LINES X(2,6) AND X(8,9) on reference triangle ABC."""
    X_391 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a + b + c)*(b + c - a)', ID="X(391)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    central_line(model, X_8, X_9, 8, 9, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X(145)", classes=["center", "incident"])
    central_line(model, X_37, X_145, 37, 145, incident=True)
    return promote_point_to_top(model, X_391)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(391) on the given reference triangle."""
    model = create_model('X(391) = INTERSECTION OF LINES X(2,6) AND X(8,9)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00391(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00391.json"))
    write_center_svg(
        model_acute,
        here / "x-00391.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
