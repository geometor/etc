"""GEOMETOR construction model for X_840 = ISOGONAL CONJUGATE OF X_528."""

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


def construct_x_00840(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_840 = ISOGONAL CONJUGATE OF X_528 on reference triangle ABC."""
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center"])
    central_line(model, X_36, X_101, 36, 101)
    central_line(model, X_100, X_518, 100, 518)
    X_840 = intersect_lines(model, X_36, X_101, X_100, X_518, ID="X_840", classes=["selected", "target"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_105, X_513, 105, 513, incident=True)
    return promote_point_to_top(model, X_840)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_840 on the given reference triangle."""
    model = create_model('X_840 = ISOGONAL CONJUGATE OF X_528')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00840(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00840.json"))
    write_center_svg(
        model_acute,
        here / "x-00840.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
