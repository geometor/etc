"""GEOMETOR construction model for X_358 = 2nd MORLEY-TAYLOR-MARR CENTER."""

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


def construct_x_00358(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_358 = 2nd MORLEY-TAYLOR-MARR CENTER on reference triangle ABC."""
    X_357 = eval_trilinear_point(model, A, B, C, 'sec(A/3)', ID="X_357", classes=["center"])
    X_358 = isogonal_conjugate(model, A, B, C, X_357, ID="X_358", classes=["selected", "target"])
    X_356 = eval_trilinear_point(model, A, B, C, 'cos(A/3) + 2*cos(B/3)*cos(C/3)', ID="X_356", classes=["center", "incident"])
    central_line(model, X_356, X_357, 356, 357, incident=True)
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A- pi /3)', ID="X_16", classes=["center", "incident"])
    X_1135 = eval_trilinear_point(model, A, B, C, 'cos(A/3 - pi /3)', ID="X_1135", classes=["center", "incident"])
    central_line(model, X_16, X_1135, 16, 1135, incident=True)
    return promote_point_to_top(model, X_358)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_358 on the given reference triangle."""
    model = create_model('X_358 = 2nd MORLEY-TAYLOR-MARR CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00358(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00358.json"))
    write_center_svg(
        model_acute,
        here / "x-00358.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
