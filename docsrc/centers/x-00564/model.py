"""GEOMETOR construction model for X(564) = INTERSECTION OF LINES X(1)X(1048) AND X(47,91)."""

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


def construct_x_00564(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(564) = INTERSECTION OF LINES X(1)X(1048) AND X(47,91) on reference triangle ABC."""
    X_564 = eval_trilinear_point(model, A, B, C, 'cos(2*B - 2*C)', ID="X(564)", classes=["selected", "target"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X(47)", classes=["center", "incident"])
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X(91)", classes=["center", "incident"])
    central_line(model, X_47, X_91, 47, 91, incident=True)
    return promote_point_to_top(model, X_564)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(564) on the given reference triangle."""
    model = create_model('X(564) = INTERSECTION OF LINES X(1)X(1048) AND X(47,91)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00564(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00564.json"))
    write_center_svg(
        model_acute,
        here / "x-00564.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
