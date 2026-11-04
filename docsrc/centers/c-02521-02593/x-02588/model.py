"""GEOMETOR construction model for X_2588 = X_3-ISOCONJUGATE OF X_1113."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02588(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2588 = X_3-ISOCONJUGATE OF X_1113 on reference triangle ABC."""
    X_1822 = point_from_barycentrics(model, A, B, C, -0.19858607, 0.24538924, 0.95319683, ID="X_1822", classes=["center"])
    X_2588 = isogonal_conjugate(model, A, B, C, X_1822, ID="X_2588", classes=["selected", "target"])
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A +  omega  )', ID="X_240", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_240, X_522, 240, 522, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_1313 = eval_trilinear_point(model, A, B, C, '(J + 1)*cos(A) + 2*(J - 1)*cos(B)*cos(C)', ID="X_1313", classes=["center", "incident"])
    central_line(model, X_11, X_1313, 11, 1313, incident=True)
    X_759 = eval_trilinear_point(model, A, B, C, '(1/(a**(0)*(b**(3) + c**(3)) - a**(2)*(b**(1) + c**(1))))', ID="X_759", classes=["center", "incident"])
    X_1114 = eval_trilinear_point(model, A, B, C, '(R + d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1114", classes=["center", "incident"])
    central_line(model, X_759, X_1114, 759, 1114, incident=True)
    return promote_point_to_top(model, X_2588)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2588 on the given reference triangle."""
    model = create_model('X_2588 = X_3-ISOCONJUGATE OF X_1113')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02588(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02588.json"))
    write_center_svg(
        model_acute,
        here / "x-02588.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
