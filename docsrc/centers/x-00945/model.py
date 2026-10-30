"""GEOMETOR construction model for X(945) = ISOGONAL CONJUGATE OF X(944)."""

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


def construct_x_00945(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(945) = ISOGONAL CONJUGATE OF X(944) on reference triangle ABC."""
    X_944 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a**(4) - 2*a**(3)*(b + c) + (b - c)**(2)*(2*a*b + 2*a*c - 2*b*c - b**(2) - c**(2) - 2*a**(2)))', ID="X(944)", classes=["center"])
    X_945 = isogonal_conjugate(model, A, B, C, X_944, ID="X(945)", classes=["selected", "target"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X(78)", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X(517)", classes=["center", "incident"])
    central_line(model, X_78, X_517, 78, 517, incident=True)
    X_283 = eval_trilinear_point(model, A, B, C, '(cos(A))/(cos(B) + cos(C))', ID="X(283)", classes=["center", "incident"])
    X_859 = point_from_barycentrics(model, A, B, C, -1.2557078, -0.65296804, 2.9086758, ID="X(859)", classes=["center", "incident"])
    central_line(model, X_283, X_859, 283, 859, incident=True)
    return promote_point_to_top(model, X_945)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(945) on the given reference triangle."""
    model = create_model('X(945) = ISOGONAL CONJUGATE OF X(944)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00945(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00945.json"))
    write_center_svg(
        model_acute,
        here / "x-00945.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
