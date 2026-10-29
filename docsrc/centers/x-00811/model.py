"""GEOMETOR construction model for X(811) = ISOGONAL CONJUGATE OF X(810)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00811(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(811) = ISOGONAL CONJUGATE OF X(810) on reference triangle ABC."""
    X_810 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X(810)", classes=["center"])
    X_811 = isogonal_conjugate(model, A, B, C, X_810, ID="X(811)", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X(108)", classes=["center", "incident"])
    central_line(model, X_99, X_108, 99, 108, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_336 = eval_trilinear_point(model, A, B, C, 'csc(A)*cot(A)*sec(A + omega )', ID="X(336)", classes=["center", "incident"])
    central_line(model, X_1, X_336, 1, 336, incident=True)
    X_350 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c)*b**(2)*c**(2)', ID="X(350)", classes=["center", "incident"])
    X_447 = point_from_barycentrics(model, A, B, C, -0.43131573, -0.14127643, 1.5725922, ID="X(447)", classes=["center", "incident"])
    central_line(model, X_350, X_447, 350, 447, incident=True)
    return promote_point_to_top(model, X_811)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(811) on the given reference triangle."""
    model = create_model('X(811) = ISOGONAL CONJUGATE OF X(810)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00811(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00811.json"))
    write_center_svg(
        model_acute,
        here / "x-00811.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
