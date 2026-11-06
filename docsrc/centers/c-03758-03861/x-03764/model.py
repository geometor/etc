"""GEOMETOR construction model for X_3764 = X_869com[T(bc, b²)]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03764(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3764 = X_869com[T(bc, b²)] on reference triangle ABC."""
    X_3764 = eval_barycentric_point(model, A, B, C, 'a**(2)*(b**(3) + c**(3) + a*b*c)', ID="X_3764", classes=["selected", "target"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center", "incident"])
    central_line(model, X_75, X_256, 75, 256, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_560 = eval_trilinear_point(model, A, B, C, 'a**(4)', ID="X_560", classes=["center", "incident"])
    central_line(model, X_6, X_560, 6, 560, incident=True)
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X_291", classes=["center", "incident"])
    X_751 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + 2*b*c)', ID="X_751", classes=["center", "incident"])
    central_line(model, X_291, X_751, 291, 751, incident=True)
    return promote_point_to_top(model, X_3764)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3764 on the given reference triangle."""
    model = create_model('X_3764 = X_869com[T(bc, b²)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03764(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03764.json"))
    write_center_svg(
        model_acute,
        here / "x-03764.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
