"""GEOMETOR construction model for X(505) = 3rd ISOSCELIZER POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00505(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(505) = 3rd ISOSCELIZER POINT on reference triangle ABC."""
    X_164 = eval_trilinear_point(model, A, B, C, 'sin(B/2) + sin(C/2) - sin(A/2)', ID="X(164)", classes=["center"])
    X_505 = isogonal_conjugate(model, A, B, C, X_164, ID="X(505)", classes=["selected", "target"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    central_line(model, X_40, X_164, 40, 164, incident=True)
    return promote_point_to_top(model, X_505)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(505) on the given reference triangle."""
    model = create_model('X(505) = 3rd ISOSCELIZER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00505(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00505.json"))
    write_center_svg(
        model_acute,
        here / "x-00505.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
