"""GEOMETOR construction model for X_2036 = EXSIMILICENTER(MOSES CIRCLE, 1st LEMOINE CIRCLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02036(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2036 = EXSIMILICENTER(MOSES CIRCLE, 1st LEMOINE CIRCLE) on reference triangle ABC."""
    X_2036 = eval_trilinear_point(model, A, B, C, '(sin(A) - sin(A +  omega  ) - sin(A - 2*omega  ))', ID="X_2036", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_1015 = eval_trilinear_point(model, A, B, C, 'a*(b - c)**(2)', ID="X_1015", classes=["center", "incident"])
    X_1673 = eval_trilinear_point(model, A, B, C, '1 - cos(A -  omega  )', ID="X_1673", classes=["center", "incident"])
    central_line(model, X_1015, X_1673, 1015, 1673, incident=True)
    X_1500 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)', ID="X_1500", classes=["center", "incident"])
    X_1672 = eval_trilinear_point(model, A, B, C, '1 + cos(A -  omega  )', ID="X_1672", classes=["center", "incident"])
    central_line(model, X_1500, X_1672, 1500, 1672, incident=True)
    return promote_point_to_top(model, X_2036)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2036 on the given reference triangle."""
    model = create_model('X_2036 = EXSIMILICENTER(MOSES CIRCLE, 1st LEMOINE CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02036(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02036.json"))
    write_center_svg(
        model_acute,
        here / "x-02036.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
