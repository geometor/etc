"""GEOMETOR construction model for X_1405 = X_45-BETH CONJUGATE OF X_45."""

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


def construct_x_01405(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1405 = X_45-BETH CONJUGATE OF X_45 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center"])
    central_line(model, X_6, X_41, 6, 41)
    central_line(model, X_31, X_51, 31, 51)
    X_1405 = intersect_lines(model, X_6, X_41, X_31, X_51, ID="X_1405", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_44, X_65, 44, 65, incident=True)
    return promote_point_to_top(model, X_1405)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1405 on the given reference triangle."""
    model = create_model('X_1405 = X_45-BETH CONJUGATE OF X_45')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01405(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01405.json"))
    write_center_svg(
        model_acute,
        here / "x-01405.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
