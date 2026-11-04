"""GEOMETOR construction model for X_2613 = CROSSDIFFERENCE OF PU(70)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02613(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2613 = CROSSDIFFERENCE OF PU(70) on reference triangle ABC."""
    X_2612 = eval_trilinear_point(model, A, B, C, '(csc(A - B)*csc(A - C) - (csc(B - C))**(2))', ID="X_2612", classes=["center"])
    X_1101 = eval_trilinear_point(model, A, B, C, '((csc(B - C))**(2))', ID="X_1101", classes=["center"])
    X_2613 = reflection_in_point(model, X_2612, X_1101, ID="X_2613", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_1, X_60, 1, 60, incident=True)
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_523, X_1101, 523, 1101, incident=True)
    X_1983 = eval_trilinear_point(model, A, B, C, '(sin(C - A) - sin(A - B))/sin(B - C)', ID="X_1983", classes=["center", "incident"])
    X_2610 = point_from_barycentrics(model, A, B, C, -2.9137931, 0.99310345, 2.9206897, ID="X_2610", classes=["center", "incident"])
    central_line(model, X_1983, X_2610, 1983, 2610, incident=True)
    return promote_point_to_top(model, X_2613)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2613 on the given reference triangle."""
    model = create_model('X_2613 = CROSSDIFFERENCE OF PU(70)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02613(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02613.json"))
    write_center_svg(
        model_acute,
        here / "x-02613.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
