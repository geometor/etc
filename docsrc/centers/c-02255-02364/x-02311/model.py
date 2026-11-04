"""GEOMETOR construction model for X_2311 = X_2-ISOCONJUGATE OF X_1284."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02311(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2311 = X_2-ISOCONJUGATE OF X_1284 on reference triangle ABC."""
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    central_line(model, X_41, X_60, 41, 60)
    central_line(model, X_58, X_101, 58, 101)
    X_2311 = intersect_lines(model, X_41, X_60, X_58, X_101, ID="X_2311", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_261 = eval_trilinear_point(model, A, B, C, '(((csc(A))*(sec(B/2 - C/2)))**(2))', ID="X_261", classes=["center", "incident"])
    central_line(model, X_9, X_261, 9, 261, incident=True)
    return promote_point_to_top(model, X_2311)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2311 on the given reference triangle."""
    model = create_model('X_2311 = X_2-ISOCONJUGATE OF X_1284')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02311(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02311.json"))
    write_center_svg(
        model_acute,
        here / "x-02311.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
