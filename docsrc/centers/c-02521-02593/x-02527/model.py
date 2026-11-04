"""GEOMETOR construction model for X_2527 = RADICAL CENTER OF {NINE-POINT, SPIEKER, BEVAN} CIRCLES."""

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


def construct_x_02527(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2527 = RADICAL CENTER OF {NINE-POINT, SPIEKER, BEVAN} CIRCLES on reference triangle ABC."""
    X_2527 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(6*a**(2) - a*b - a*c + (b + c)**(2)))', ID="X_2527", classes=["selected", "target"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center", "incident"])
    X_900 = eval_trilinear_point(model, A, B, C, '(b - c)*(b + c - 2*a)/a', ID="X_900", classes=["center", "incident"])
    central_line(model, X_649, X_900, 649, 900, incident=True)
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    X_2487 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*((b - c)**(2) + a*b + a*c - 4*a**(2)))', ID="X_2487", classes=["center", "incident"])
    central_line(model, X_514, X_2487, 514, 2487, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_2490 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(4*a**(2) - 3*a*b - 3*a*c + (b + c)**(2)))', ID="X_2490", classes=["center", "incident"])
    central_line(model, X_513, X_2490, 513, 2490, incident=True)
    return promote_point_to_top(model, X_2527)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2527 on the given reference triangle."""
    model = create_model('X_2527 = RADICAL CENTER OF {NINE-POINT, SPIEKER, BEVAN} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02527(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02527.json"))
    write_center_svg(
        model_acute,
        here / "x-02527.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
