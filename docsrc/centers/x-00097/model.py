"""GEOMETOR construction model for X(97) = ISOGONAL CONJUGATE OF X(53)."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00097(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(97) = ISOGONAL CONJUGATE OF X(53) on reference triangle ABC."""
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X(53)", classes=["center"])
    X_97 = isogonal_conjugate(model, A, B, C, X_53, ID="X(97)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    central_line(model, X_3, X_54, 3, 54, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X(95)", classes=["center", "incident"])
    central_line(model, X_2, X_95, 2, 95, incident=True)
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X(216)", classes=["center", "incident"])
    X_288 = eval_trilinear_point(model, A, B, C, '(sec(B - C))/(b*cos(C - A) + c*cos(B - A))', ID="X(288)", classes=["center", "incident"])
    central_line(model, X_216, X_288, 216, 288, incident=True)
    return promote_point_to_top(model, X_97)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(97) on the given reference triangle."""
    model = create_model('X(97) = ISOGONAL CONJUGATE OF X(53)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00097(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00097.json"))
    write_center_svg(
        model_acute,
        here / "x-00097.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
