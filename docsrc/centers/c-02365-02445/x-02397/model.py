"""GEOMETOR construction model for X_2397 = GIBERT-SIMSON TRANSFORM OF X_100."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02397(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2397 = GIBERT-SIMSON TRANSFORM OF X_100 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center"])
    X_644 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b - c))', ID="X_644", classes=["center"])
    central_line(model, X_2, X_37, 2, 37)
    central_line(model, X_190, X_644, 190, 644)
    X_2397 = intersect_lines(model, X_2, X_37, X_190, X_644, ID="X_2397", classes=["selected", "target"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    X_1026 = eval_trilinear_point(model, A, B, C, '((b**(2) + c**(2) - a*(b + c))/(b - c))', ID="X_1026", classes=["center", "incident"])
    central_line(model, X_522, X_1026, 522, 1026, incident=True)
    return promote_point_to_top(model, X_2397)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2397 on the given reference triangle."""
    model = create_model('X_2397 = GIBERT-SIMSON TRANSFORM OF X_100')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02397(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02397.json"))
    write_center_svg(
        model_acute,
        here / "x-02397.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
