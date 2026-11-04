"""GEOMETOR construction model for X_1732 = MIMOSA TRANSFORM OF X_89."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01732(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1732 = MIMOSA TRANSFORM OF X_89 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    central_line(model, X_19, X_46, 19, 46)
    central_line(model, X_44, X_56, 44, 56)
    X_1732 = intersect_lines(model, X_19, X_46, X_44, X_56, ID="X_1732", classes=["selected", "target"])
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X_45", classes=["center", "incident"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center", "incident"])
    central_line(model, X_45, X_354, 45, 354, incident=True)
    return promote_point_to_top(model, X_1732)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1732 on the given reference triangle."""
    model = create_model('X_1732 = MIMOSA TRANSFORM OF X_89')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01732(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01732.json"))
    write_center_svg(
        model_acute,
        here / "x-01732.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
