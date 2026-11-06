"""GEOMETOR construction model for X_3446 = X_513-VERTEX CONJUGATE OF X_513."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03446(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3446 = X_513-VERTEX CONJUGATE OF X_513 on reference triangle ABC."""
    X_149 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(3) + c**(3) - a**(3) + (a**(2) - b*c)*(b + c) + a*(b*c - b**(2) - c**(2))))', ID="X_149", classes=["center"])
    X_3446 = isogonal_conjugate(model, A, B, C, X_149, ID="X_3446", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    central_line(model, X_36, X_518, 36, 518, incident=True)
    X_840 = point_from_barycentrics(model, A, B, C, 0.66666667, -0.32, 0.65333333, ID="X_840", classes=["center", "incident"])
    X_1618 = point_from_barycentrics(model, A, B, C, 0.50925926, -0.68888889, 1.1796296, ID="X_1618", classes=["center", "incident"])
    central_line(model, X_840, X_1618, 840, 1618, incident=True)
    return promote_point_to_top(model, X_3446)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3446 on the given reference triangle."""
    model = create_model('X_3446 = X_513-VERTEX CONJUGATE OF X_513')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03446(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03446.json"))
    write_center_svg(
        model_acute,
        here / "x-03446.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
