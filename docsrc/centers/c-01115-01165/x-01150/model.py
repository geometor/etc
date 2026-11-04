"""GEOMETOR construction model for X_1150 = INTERSECTION OF LINES X_2X_6 AND X_3X_8."""

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
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01150(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1150 = INTERSECTION OF LINES X_2X_6 AND X_3X_8 on reference triangle ABC."""
    X_1150 = eval_trilinear_point(model, A, B, C, '((b**(2) + c**(2) - a**(2)) + b*c*(b + c)/a)', ID="X_1150", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    central_line(model, X_3, X_8, 3, 8, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_63, X_321, 63, 321, incident=True)
    return promote_point_to_top(model, X_1150)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1150 on the given reference triangle."""
    model = create_model('X_1150 = INTERSECTION OF LINES X_2X_6 AND X_3X_8')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01150(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01150.json"))
    write_center_svg(
        model_acute,
        here / "x-01150.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
