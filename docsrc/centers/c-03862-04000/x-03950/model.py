"""GEOMETOR construction model for X_3950 = X_9com[INVERSE(n(INCENTRAL TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03950(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3950 = X_9com[INVERSE(n(INCENTRAL TRIANGLE))] on reference triangle ABC."""
    X_3950 = eval_barycentric_point(model, A, B, C, '((b + c)*(b + c - 3*a))', ID="X_3950", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_10, X_37, 10, 37, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_346 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)**(2)', ID="X_346", classes=["center", "incident"])
    central_line(model, X_1, X_346, 1, 346, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_9, X_519, 9, 519, incident=True)
    return promote_point_to_top(model, X_3950)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3950 on the given reference triangle."""
    model = create_model('X_3950 = X_9com[INVERSE(n(INCENTRAL TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03950(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03950.json"))
    write_center_svg(
        model_acute,
        here / "x-03950.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
