"""GEOMETOR construction model for X_2237 = X_2-ISOCONJUGATE OF X_735."""

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


def construct_x_02237(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2237 = X_2-ISOCONJUGATE OF X_735 on reference triangle ABC."""
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    central_line(model, X_32, X_75, 32, 75)
    central_line(model, X_44, X_513, 44, 513)
    X_2237 = intersect_lines(model, X_32, X_75, X_44, X_513, ID="X_2237", classes=["selected", "target"])
    X_1740 = eval_trilinear_point(model, A, B, C, '(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_1740", classes=["center", "incident"])
    X_1759 = eval_trilinear_point(model, A, B, C, '(a**(3) - b**(3) - c**(3))', ID="X_1759", classes=["center", "incident"])
    central_line(model, X_1740, X_1759, 1740, 1759, incident=True)
    return promote_point_to_top(model, X_2237)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2237 on the given reference triangle."""
    model = create_model('X_2237 = X_2-ISOCONJUGATE OF X_735')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02237(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02237.json"))
    write_center_svg(
        model_acute,
        here / "x-02237.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
