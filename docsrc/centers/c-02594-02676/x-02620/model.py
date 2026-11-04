"""GEOMETOR construction model for X_2620 = CROSSDIFFERENCE OF PU(72)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02620(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2620 = CROSSDIFFERENCE OF PU(72) on reference triangle ABC."""
    X_2620 = eval_trilinear_point(model, A, B, C, '(tan(A - B)*tan(A - C) + (tan(B - C))**(2))', ID="X_2620", classes=["selected", "target"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_47, X_48, 47, 48, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2616 = eval_trilinear_point(model, A, B, C, 'tan(B - C)', ID="X_2616", classes=["center", "incident"])
    central_line(model, X_1, X_2616, 1, 2616, incident=True)
    X_2617 = eval_trilinear_point(model, A, B, C, 'cot(B - C)', ID="X_2617", classes=["center", "incident"])
    X_2619 = eval_trilinear_point(model, A, B, C, '(tan(A - B)*tan(A - C) - (tan(B - C))**(2))', ID="X_2619", classes=["center", "incident"])
    central_line(model, X_2617, X_2619, 2617, 2619, incident=True)
    return promote_point_to_top(model, X_2620)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2620 on the given reference triangle."""
    model = create_model('X_2620 = CROSSDIFFERENCE OF PU(72)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02620(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02620.json"))
    write_center_svg(
        model_acute,
        here / "x-02620.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
