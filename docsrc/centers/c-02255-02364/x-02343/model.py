"""GEOMETOR construction model for X_2343 = X_2-ISOCONJUGATE OF X_1467."""

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


def construct_x_02343(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2343 = X_2-ISOCONJUGATE OF X_1467 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_220 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)**(2)', ID="X_220", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X_219", classes=["center"])
    central_line(model, X_19, X_220, 19, 220)
    central_line(model, X_57, X_219, 57, 219)
    X_2343 = intersect_lines(model, X_19, X_220, X_57, X_219, ID="X_2343", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_939 = eval_trilinear_point(model, A, B, C, '(a/(a**(4) - 2*a**(3)*(b + c) - 4*a**(2)*b*c + (b - c)*(b**(2) - c**(2))*(2*a - b - c)))', ID="X_939", classes=["center", "incident"])
    central_line(model, X_6, X_939, 6, 939, incident=True)
    return promote_point_to_top(model, X_2343)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2343 on the given reference triangle."""
    model = create_model('X_2343 = X_2-ISOCONJUGATE OF X_1467')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02343(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02343.json"))
    write_center_svg(
        model_acute,
        here / "x-02343.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
