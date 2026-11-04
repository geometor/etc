"""GEOMETOR construction model for X_2531 = RADICAL CENTER OF {BROCARD, (X_4,2R), 2nd BROCARD} CIRCLES."""

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


def construct_x_02531(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2531 = RADICAL CENTER OF {BROCARD, (X_4,2R), 2nd BROCARD} CIRCLES on reference triangle ABC."""
    X_2531 = eval_trilinear_point(model, A, B, C, '(a**(3)*(b**(2) - c**(2))*(b**(2) + c**(2))**(2))', ID="X_2531", classes=["selected", "target"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_39, X_512, 39, 512, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_783 = eval_trilinear_point(model, A, B, C, '(1/(a **(-5)*(b**(4) - c**(4)) + a**(3)*(b **(-4) - c **(-4))))', ID="X_783", classes=["center", "incident"])
    central_line(model, X_99, X_783, 99, 783, incident=True)
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    X_2513 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(a**(2)*(2*b**(4) + 3*b**(2)*c**(2) + 2*c**(4)) + b**(2)*c**(2)*(b**(2) + c**(2))))', ID="X_2513", classes=["center", "incident"])
    central_line(model, X_525, X_2513, 525, 2513, incident=True)
    return promote_point_to_top(model, X_2531)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2531 on the given reference triangle."""
    model = create_model('X_2531 = RADICAL CENTER OF {BROCARD, (X_4,2R), 2nd BROCARD} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02531(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02531.json"))
    write_center_svg(
        model_acute,
        here / "x-02531.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
