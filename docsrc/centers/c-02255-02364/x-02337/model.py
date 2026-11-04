"""GEOMETOR construction model for X_2337 = X_2-ISOCONJUGATE OF X_1454."""

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


def construct_x_02337(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2337 = X_2-ISOCONJUGATE OF X_1454 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center"])
    central_line(model, X_19, X_24, 19, 24)
    central_line(model, X_6, X_47, 6, 47)
    X_2337 = intersect_lines(model, X_19, X_24, X_6, X_47, ID="X_2337", classes=["selected", "target"])
    return promote_point_to_top(model, X_2337)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2337 on the given reference triangle."""
    model = create_model('X_2337 = X_2-ISOCONJUGATE OF X_1454')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02337(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02337.json"))
    write_center_svg(
        model_acute,
        here / "x-02337.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
