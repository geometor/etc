"""GEOMETOR construction model for X_2316 = X_2-ISOCONJUGATE OF X_1319."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02316(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2316 = X_2-ISOCONJUGATE OF X_1319 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center"])
    central_line(model, X_6, X_101, 6, 101)
    central_line(model, X_57, X_88, 57, 88)
    X_2316 = intersect_lines(model, X_6, X_101, X_57, X_88, ID="X_2316", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_44, X_517, 44, 517, incident=True)
    return promote_point_to_top(model, X_2316)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2316 on the given reference triangle."""
    model = create_model('X_2316 = X_2-ISOCONJUGATE OF X_1319')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02316(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02316.json"))
    write_center_svg(
        model_acute,
        here / "x-02316.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
