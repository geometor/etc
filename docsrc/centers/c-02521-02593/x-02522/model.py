"""GEOMETOR construction model for X_2522 = RADICAL CENTER OF {NINE-POINT,BROCARD, APOLLONIUS} CIRCLES."""

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


def construct_x_02522(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2522 = RADICAL CENTER OF {NINE-POINT,BROCARD, APOLLONIUS} CIRCLES on reference triangle ABC."""
    X_2522 = eval_trilinear_point(model, A, B, C, '(b - c)*(b**(2) + c**(2) - a**(2))*(a**(2) + (b + c)**(2))', ID="X_2522", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_441 = point_from_barycentrics(model, A, B, C, 0.74590002, 0.58940921, -0.33530923, ID="X_441", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_441, X_525, 441, 525, incident=True)
    X_1021 = eval_trilinear_point(model, A, B, C, '((cos(B) - cos(C))/(cos(B) + cos(C)))', ID="X_1021", classes=["center", "incident"])
    X_1734 = eval_trilinear_point(model, A, B, C, '((b - c)*(b**(2) + c**(2) + b*c - a*b - a*c))', ID="X_1734", classes=["center", "incident"])
    central_line(model, X_1021, X_1734, 1021, 1734, incident=True)
    return promote_point_to_top(model, X_2522)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2522 on the given reference triangle."""
    model = create_model('X_2522 = RADICAL CENTER OF {NINE-POINT,BROCARD, APOLLONIUS} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02522(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02522.json"))
    write_center_svg(
        model_acute,
        here / "x-02522.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
