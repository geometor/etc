"""GEOMETOR construction model for X_1823 = ISOGONAL CONJUGATE OF X_2589."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01823(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1823 = ISOGONAL CONJUGATE OF X_2589 on reference triangle ABC."""
    X_1101 = eval_trilinear_point(model, A, B, C, '((csc(B - C))**(2))', ID="X_1101", classes=["center"])
    X_1822 = point_from_barycentrics(model, A, B, C, -0.19858607, 0.24538924, 0.95319683, ID="X_1822", classes=["center"])
    X_1823 = ceva_conjugate(model, A, B, C, X_1101, X_1822, ID="X_1823", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_1114 = eval_trilinear_point(model, A, B, C, '(R + d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1114", classes=["center", "incident"])
    central_line(model, X_109, X_1114, 109, 1114, incident=True)
    return promote_point_to_top(model, X_1823)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1823 on the given reference triangle."""
    model = create_model('X_1823 = ISOGONAL CONJUGATE OF X_2589')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01823(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01823.json"))
    write_center_svg(
        model_acute,
        here / "x-01823.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
