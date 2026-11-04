"""GEOMETOR construction model for X_2519 = RADICAL CENTER OF {NINE-POINT, 2nd LEMOINE, BROCARD} CIRCLES."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_02519(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2519 = RADICAL CENTER OF {NINE-POINT, 2nd LEMOINE, BROCARD} CIRCLES on reference triangle ABC."""
    X_2519 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))*(a**(4) + b**(4) + c**(4) + 2*a**(2)*b**(2) + 2*a**(2)*c**(2) - 6*b**(2)*c**(2)))', ID="X_2519", classes=["selected", "target"])
    X_441 = point_from_barycentrics(model, A, B, C, 0.74590002, 0.58940921, -0.33530923, ID="X_441", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_441, X_525, 441, 525, incident=True)
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_1570 = eval_trilinear_point(model, A, B, C, 'a*(cot(A) + cot(omega)  - 4*tan(omega)  )', ID="X_1570", classes=["center", "incident"])
    central_line(model, X_512, X_1570, 512, 1570, incident=True)
    return promote_point_to_top(model, X_2519)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2519 on the given reference triangle."""
    model = create_model('X_2519 = RADICAL CENTER OF {NINE-POINT, 2nd LEMOINE, BROCARD} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02519(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02519.json"))
    write_center_svg(
        model_acute,
        here / "x-02519.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
