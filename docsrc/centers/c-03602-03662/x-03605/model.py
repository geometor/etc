"""GEOMETOR construction model for X_3605 = ISOGONAL CONJUGATE OF X_356."""

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


def construct_x_03605(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3605 = ISOGONAL CONJUGATE OF X_356 on reference triangle ABC."""
    X_3605 = eval_trilinear_point(model, A, B, C, '(1/(cos(A/3) + 2*cos(B/3)*cos(C/3)))', ID="X_3605", classes=["selected", "target"])
    X_1507 = eval_trilinear_point(model, A, B, C, '(1 + 2*(cos(B/3) + cos(C/3) - cos(A/3)))', ID="X_1507", classes=["center", "incident"])
    X_1508 = eval_trilinear_point(model, A, B, C, '(2 - sec(A/3) + sec(B/3) + sec(C/3))', ID="X_1508", classes=["center", "incident"])
    central_line(model, X_1507, X_1508, 1507, 1508, incident=True)
    X_358 = eval_trilinear_point(model, A, B, C, 'cos(A/3)', ID="X_358", classes=["center", "incident"])
    X_3279 = eval_trilinear_point(model, A, B, C, '(cos(B/3)*cos(C/3) + sin(A/3)*sin(2*A/3))', ID="X_3279", classes=["center", "incident"])
    central_line(model, X_358, X_3279, 358, 3279, incident=True)
    return promote_point_to_top(model, X_3605)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3605 on the given reference triangle."""
    model = create_model('X_3605 = ISOGONAL CONJUGATE OF X_356')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03605(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03605.json"))
    write_center_svg(
        model_acute,
        here / "x-03605.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
