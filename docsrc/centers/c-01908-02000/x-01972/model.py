"""GEOMETOR construction model for X_1972 = TRILINEAR POLE OF PU(38)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01972(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1972 = TRILINEAR POLE OF PU(38) on reference triangle ABC."""
    X_648 = eval_trilinear_point(model, A, B, C, '1/(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2)))', ID="X_648", classes=["center"])
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X_216", classes=["center"])
    X_1972 = reflection_in_point(model, X_648, X_216, ID="X_1972", classes=["selected", "target"], guide=False)
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X_95", classes=["center", "incident"])
    central_line(model, X_95, X_216, 95, 216, incident=True)
    X_287 = eval_trilinear_point(model, A, B, C, 'cot(A)*sec(A + omega )', ID="X_287", classes=["center", "incident"])
    X_401 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))*(csc(A))', ID="X_401", classes=["center", "incident"])
    central_line(model, X_287, X_401, 287, 401, incident=True)
    X_925 = eval_trilinear_point(model, A, B, C, '(sin(A))/(sec(2*B) - sec(2*C))', ID="X_925", classes=["center", "incident"])
    X_1298 = point_from_barycentrics(model, A, B, C, 0.54395477, 1.0720972, -0.61605193, ID="X_1298", classes=["center", "incident"])
    central_line(model, X_925, X_1298, 925, 1298, incident=True)
    return promote_point_to_top(model, X_1972)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1972 on the given reference triangle."""
    model = create_model('X_1972 = TRILINEAR POLE OF PU(38)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01972(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01972.json"))
    write_center_svg(
        model_acute,
        here / "x-01972.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
