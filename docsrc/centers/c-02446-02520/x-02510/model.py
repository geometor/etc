"""GEOMETOR construction model for X_2510 = RADICAL CENTER OF {NINE-POINT, BROCARD, MOSES} CIRCLES."""

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


def construct_x_02510(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2510 = RADICAL CENTER OF {NINE-POINT, BROCARD, MOSES} CIRCLES on reference triangle ABC."""
    X_2510 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - a**(2))*(b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 3*b**(2)*c**(2)))', ID="X_2510", classes=["selected", "target"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_804 = eval_trilinear_point(model, A, B, C, 'a **(-3)*(b**(2) - c**(2)) + a**(1)*(b **(-2) - c **(-2))', ID="X_804", classes=["center", "incident"])
    central_line(model, X_115, X_804, 115, 804, incident=True)
    X_441 = point_from_barycentrics(model, A, B, C, 0.74590002, 0.58940921, -0.33530923, ID="X_441", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_441, X_525, 441, 525, incident=True)
    X_248 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*sec(A +  omega  )', ID="X_248", classes=["center", "incident"])
    X_878 = point_from_barycentrics(model, A, B, C, -0.14706477, 1.0752646, 0.071800149, ID="X_878", classes=["center", "incident"])
    central_line(model, X_248, X_878, 248, 878, incident=True)
    return promote_point_to_top(model, X_2510)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2510 on the given reference triangle."""
    model = create_model('X_2510 = RADICAL CENTER OF {NINE-POINT, BROCARD, MOSES} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02510(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02510.json"))
    write_center_svg(
        model_acute,
        here / "x-02510.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
