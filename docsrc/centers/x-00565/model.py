"""GEOMETOR construction model for X(565) = INTERSECTION OF LINES X(49)X(93) AND X(143,324)."""

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


def construct_x_00565(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(565) = INTERSECTION OF LINES X(49)X(93) AND X(143,324) on reference triangle ABC."""
    X_565 = eval_trilinear_point(model, A, B, C, 'cos(3*B - 3*C)', ID="X(565)", classes=["selected", "target"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X(49)", classes=["center", "incident"])
    X_93 = eval_trilinear_point(model, A, B, C, 'sec(3*A)', ID="X(93)", classes=["center", "incident"])
    central_line(model, X_49, X_93, 49, 93, incident=True)
    X_143 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(2*C - 2*A) + cos(2*A - 2*B))', ID="X(143)", classes=["center", "incident"])
    X_324 = eval_trilinear_point(model, A, B, C, 'b*c*sec(A)*cos(B - C)', ID="X(324)", classes=["center", "incident"])
    central_line(model, X_143, X_324, 143, 324, incident=True)
    return promote_point_to_top(model, X_565)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(565) on the given reference triangle."""
    model = create_model('X(565) = INTERSECTION OF LINES X(49)X(93) AND X(143,324)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00565(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00565.json"))
    write_center_svg(
        model_acute,
        here / "x-00565.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
