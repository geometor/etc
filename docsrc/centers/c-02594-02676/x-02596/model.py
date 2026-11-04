"""GEOMETOR construction model for X_2596 = CROSSDIFFERENCE OF PU(68)."""

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
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02596(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2596 = CROSSDIFFERENCE OF PU(68) on reference triangle ABC."""
    X_2596 = eval_trilinear_point(model, A, B, C, 'cos(A - B)*cos(A - C) - (cos(B - C))**(2)', ID="X_2596", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_1087 = eval_trilinear_point(model, A, B, C, '1 + cos(2*B - 2*C)', ID="X_1087", classes=["center", "incident"])
    central_line(model, X_54, X_1087, 54, 1087, incident=True)
    X_654 = eval_trilinear_point(model, A, B, C, 'cos(A - B) - cos(C - A)', ID="X_654", classes=["center", "incident"])
    X_1021 = eval_trilinear_point(model, A, B, C, '((cos(B) - cos(C))/(cos(B) + cos(C)))', ID="X_1021", classes=["center", "incident"])
    central_line(model, X_654, X_1021, 654, 1021, incident=True)
    return promote_point_to_top(model, X_2596)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2596 on the given reference triangle."""
    model = create_model('X_2596 = CROSSDIFFERENCE OF PU(68)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02596(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02596.json"))
    write_center_svg(
        model_acute,
        here / "x-02596.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
