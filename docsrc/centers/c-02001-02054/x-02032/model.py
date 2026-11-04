"""GEOMETOR construction model for X_2032 = RADICAL TRACE OF MOSES AND 1st LEMOINE CIRCLES."""

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


def construct_x_02032(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2032 = RADICAL TRACE OF MOSES AND 1st LEMOINE CIRCLES on reference triangle ABC."""
    X_2032 = eval_trilinear_point(model, A, B, C, '((3 + 5*cos(4*omega)  )*sin(A) + (2*sin(2*omega)  - 3*sin(4*omega)  )*cos(A))', ID="X_2032", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    return promote_point_to_top(model, X_2032)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2032 on the given reference triangle."""
    model = create_model('X_2032 = RADICAL TRACE OF MOSES AND 1st LEMOINE CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02032(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02032.json"))
    write_center_svg(
        model_acute,
        here / "x-02032.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
