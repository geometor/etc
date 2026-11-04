"""GEOMETOR construction model for X_2920 = TANGENTIAL-ISOGONAL CONJUGATE OF X_8."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02920(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2920 = TANGENTIAL-ISOGONAL CONJUGATE OF X_8 on reference triangle ABC."""
    X_2920 = point_from_barycentrics(model, A, B, C, 0.42386012, 0.45683931, 0.11930058, ID="X_2920", classes=["selected", "target"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_1616 = eval_trilinear_point(model, A, B, C, '(a*((a + b + c)**(2) - 8*b*c))', ID="X_1616", classes=["center", "incident"])
    central_line(model, X_22, X_1616, 22, 1616, incident=True)
    return promote_point_to_top(model, X_2920)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2920 on the given reference triangle."""
    model = create_model('X_2920 = TANGENTIAL-ISOGONAL CONJUGATE OF X_8')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02920(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02920.json"))
    write_center_svg(
        model_acute,
        here / "x-02920.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
