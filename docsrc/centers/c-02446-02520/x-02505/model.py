"""GEOMETOR construction model for X_2505 = RADICAL CENTER OF {INCIRCLE, NINE-POINT CIRCLE, SPIEKER CIRCLE}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02505(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2505 = RADICAL CENTER OF {INCIRCLE, NINE-POINT CIRCLE, SPIEKER CIRCLE} on reference triangle ABC."""
    X_2505 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(2*a**(3) - 5*(b + c)*a**(2) - (b + c)**(3) + 8*a*(b**(2) + c**(2))))', ID="X_2505", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_11, X_244, 11, 244, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_2490 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(4*a**(2) - 3*a*b - 3*a*c + (b + c)**(2)))', ID="X_2490", classes=["center", "incident"])
    central_line(model, X_513, X_2490, 513, 2490, incident=True)
    X_2487 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*((b - c)**(2) + a*b + a*c - 4*a**(2)))', ID="X_2487", classes=["center", "incident"])
    X_2496 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(7*a**(3) - 4*a**(2)*(b + c) - 2*(b + c)*(b - c)**(2) + a*(3*b**(2) - 2*b*c + 3*c**(2))))', ID="X_2496", classes=["center", "incident"])
    central_line(model, X_2487, X_2496, 2487, 2496, incident=True)
    return promote_point_to_top(model, X_2505)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2505 on the given reference triangle."""
    model = create_model('X_2505 = RADICAL CENTER OF {INCIRCLE, NINE-POINT CIRCLE, SPIEKER CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02505(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02505.json"))
    write_center_svg(
        model_acute,
        here / "x-02505.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
