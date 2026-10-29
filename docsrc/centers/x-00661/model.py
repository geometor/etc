"""GEOMETOR construction model for X(661) = CROSSDIFFERENCE OF X(1) AND X(21)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00661(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(661) = CROSSDIFFERENCE OF X(1) AND X(21) on reference triangle ABC."""
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X(661)", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X(514)", classes=["center", "incident"])
    X_693 = eval_trilinear_point(model, A, B, C, '(b - c)/a**(2)', ID="X(693)", classes=["center", "incident"])
    central_line(model, X_514, X_693, 514, 693, incident=True)
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X(663)", classes=["center", "incident"])
    X_810 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X(810)", classes=["center", "incident"])
    central_line(model, X_663, X_810, 663, 810, incident=True)
    return promote_point_to_top(model, X_661)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(661) on the given reference triangle."""
    model = create_model('X(661) = CROSSDIFFERENCE OF X(1) AND X(21)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00661(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00661.json"))
    write_center_svg(
        model_acute,
        here / "x-00661.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
