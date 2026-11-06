"""GEOMETOR construction model for X_3769 = X_3705com[T(-bc, b²)]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03769(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3769 = X_3705com[T(-bc, b²)] on reference triangle ABC."""
    X_3769 = eval_barycentric_point(model, A, B, C, '(2*a**(3) + a*b*c - b**(2)*c - b*c**(2))', ID="X_3769", classes=["selected", "target"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    central_line(model, X_75, X_171, 75, 171, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_312 = eval_trilinear_point(model, A, B, C, '(b + c - a)*b**(2)*c**(2)', ID="X_312", classes=["center", "incident"])
    central_line(model, X_31, X_312, 31, 312, incident=True)
    X_333 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)/(b + c)', ID="X_333", classes=["center", "incident"])
    X_612 = eval_trilinear_point(model, A, B, C, 'a**(2) + b**(2) + c**(2) + 2*b*c', ID="X_612", classes=["center", "incident"])
    central_line(model, X_333, X_612, 333, 612, incident=True)
    return promote_point_to_top(model, X_3769)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3769 on the given reference triangle."""
    model = create_model('X_3769 = X_3705com[T(-bc, b²)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03769(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03769.json"))
    write_center_svg(
        model_acute,
        here / "x-03769.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
