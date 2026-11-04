"""GEOMETOR construction model for X_2511 = RADICAL CENTER OF {NINE-POINT, APOLLONIUS, MOSES} CIRCLES."""

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


def construct_x_02511(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2511 = RADICAL CENTER OF {NINE-POINT, APOLLONIUS, MOSES} CIRCLES on reference triangle ABC."""
    X_2511 = eval_trilinear_point(model, A, B, C, '((b - c)*(b + c)**(2)*(a**(4) - a**(2)*(b - c)**(2) - b**(2)*c**(2)))', ID="X_2511", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_804 = eval_trilinear_point(model, A, B, C, 'a **(-3)*(b**(2) - c**(2)) + a**(1)*(b **(-2) - c **(-2))', ID="X_804", classes=["center", "incident"])
    central_line(model, X_115, X_804, 115, 804, incident=True)
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X_665", classes=["center", "incident"])
    X_1213 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c)*(2*a + b + c))', ID="X_1213", classes=["center", "incident"])
    central_line(model, X_665, X_1213, 665, 1213, incident=True)
    return promote_point_to_top(model, X_2511)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2511 on the given reference triangle."""
    model = create_model('X_2511 = RADICAL CENTER OF {NINE-POINT, APOLLONIUS, MOSES} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02511(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02511.json"))
    write_center_svg(
        model_acute,
        here / "x-02511.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
