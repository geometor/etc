"""GEOMETOR construction model for X(584) = ORTHOHARMONIC OF X(500)."""

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
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00584(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(584) = ORTHOHARMONIC OF X(500) on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    central_line(model, X_37, X_41, 37, 41)
    X_584 = intersect_lines(model, X_3, X_6, X_37, X_41, ID="X(584)", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center", "incident"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X(354)", classes=["center", "incident"])
    central_line(model, X_48, X_354, 48, 354, incident=True)
    return promote_point_to_top(model, X_584)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(584) on the given reference triangle."""
    model = create_model('X(584) = ORTHOHARMONIC OF X(500)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00584(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00584.json"))
    write_center_svg(
        model_acute,
        here / "x-00584.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
