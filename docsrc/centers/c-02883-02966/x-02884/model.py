"""GEOMETOR construction model for X_2884 = COMPLEMENTARY CONJUGATE OF X_7."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02884(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2884 = COMPLEMENTARY CONJUGATE OF X_7 on reference triangle ABC."""
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center"])
    X_1538 = point_from_barycentrics(model, A, B, C, -1.0625, -0.625, 2.6875, ID="X_1538", classes=["center"])
    X_857 = eval_trilinear_point(model, A, B, C, '((sin(C))**(2)*sin(2*B)*sin(C - A) + (sin(B))**(2)*sin(2*C)*sin(B - A))', ID="X_857", classes=["center"])
    X_948 = point_from_barycentrics(model, A, B, C, 0.23303835, 0.29498525, 0.4719764, ID="X_948", classes=["center"])
    central_line(model, X_142, X_1538, 142, 1538)
    central_line(model, X_857, X_948, 857, 948)
    X_2884 = intersect_lines(model, X_142, X_1538, X_857, X_948, ID="X_2884", classes=["selected", "target"])
    return promote_point_to_top(model, X_2884)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2884 on the given reference triangle."""
    model = create_model('X_2884 = COMPLEMENTARY CONJUGATE OF X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02884(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02884.json"))
    write_center_svg(
        model_acute,
        here / "x-02884.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
