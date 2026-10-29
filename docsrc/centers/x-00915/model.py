"""GEOMETOR construction model for X(915) = ISOGONAL CONJUGATE OF X(912)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00915(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(915) = ISOGONAL CONJUGATE OF X(912) on reference triangle ABC."""
    X_912 = eval_trilinear_point(model, A, B, C, '(a**(2) - b**(2) - c**(2))*(a**(3)*(b + c) - a**(2)*(b**(2) + c**(2)) - a*(b - c)**(2)*(b + c) + (b**(2) - c**(2))**(2))', ID="X(912)", classes=["center"])
    X_915 = isogonal_conjugate(model, A, B, C, X_912, ID="X(915)", classes=["selected", "target"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X(46)", classes=["center", "incident"])
    central_line(model, X_34, X_46, 34, 46, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_19, X_101, 19, 101, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X(24)", classes=["center", "incident"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X(108)", classes=["center", "incident"])
    central_line(model, X_24, X_108, 24, 108, incident=True)
    return promote_point_to_top(model, X_915)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(915) on the given reference triangle."""
    model = create_model('X(915) = ISOGONAL CONJUGATE OF X(912)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00915(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00915.json"))
    write_center_svg(
        model_acute,
        here / "x-00915.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
