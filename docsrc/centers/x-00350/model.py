"""GEOMETOR construction model for X(350) = X(2)-HIRST INVERSE OF X(75)."""

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
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00350(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(350) = X(2)-HIRST INVERSE OF X(75) on reference triangle ABC."""
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X(291)", classes=["center"])
    X_350 = isotomic_conjugate(model, A, B, C, X_291, ID="X(350)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    central_line(model, X_2, X_37, 2, 37, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_1, X_76, 1, 76, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_36, X_99, 36, 99, incident=True)
    return promote_point_to_top(model, X_350)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(350) on the given reference triangle."""
    model = create_model('X(350) = X(2)-HIRST INVERSE OF X(75)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00350(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00350.json"))
    write_center_svg(
        model_acute,
        here / "x-00350.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
