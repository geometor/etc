"""GEOMETOR construction model for X_2336 = X_2-ISOCONJUGATE OF X_1453."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_02336(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2336 = X_2-ISOCONJUGATE OF X_1453 on reference triangle ABC."""
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center"])
    central_line(model, X_34, X_37, 34, 37)
    central_line(model, X_56, X_71, 56, 71)
    X_2336 = intersect_lines(model, X_34, X_37, X_56, X_71, ID="X_2336", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X_219", classes=["center", "incident"])
    central_line(model, X_58, X_219, 58, 219, incident=True)
    return promote_point_to_top(model, X_2336)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2336 on the given reference triangle."""
    model = create_model('X_2336 = X_2-ISOCONJUGATE OF X_1453')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02336(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02336.json"))
    write_center_svg(
        model_acute,
        here / "x-02336.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
