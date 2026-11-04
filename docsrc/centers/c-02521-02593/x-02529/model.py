"""GEOMETOR construction model for X_2529 = RADICAL CENTER OF {ORTHOCENTROIDAL, SPIEKER, BEVAN} CIRCLES."""

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


def construct_x_02529(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2529 = RADICAL CENTER OF {ORTHOCENTROIDAL, SPIEKER, BEVAN} CIRCLES on reference triangle ABC."""
    X_2529 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(7*a**(2) + a*b + a*c + 2*(b + c)**(2)))', ID="X_2529", classes=["selected", "target"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    X_2487 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*((b - c)**(2) + a*b + a*c - 4*a**(2)))', ID="X_2487", classes=["center", "incident"])
    central_line(model, X_514, X_2487, 514, 2487, incident=True)
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center", "incident"])
    X_2457 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2) - c**(2))*(2*a**(3) + a**(2)*(b + c) - (b + c)*(b - c)**(2) - 2*a*(b**(2) - b*c + c**(2))))', ID="X_2457", classes=["center", "incident"])
    central_line(model, X_650, X_2457, 650, 2457, incident=True)
    return promote_point_to_top(model, X_2529)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2529 on the given reference triangle."""
    model = create_model('X_2529 = RADICAL CENTER OF {ORTHOCENTROIDAL, SPIEKER, BEVAN} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02529(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02529.json"))
    write_center_svg(
        model_acute,
        here / "x-02529.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
