"""GEOMETOR construction model for X(693) = ISOTOMIC CONJUGATE OF X(100)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00693(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(693) = ISOTOMIC CONJUGATE OF X(100) on reference triangle ABC."""
    X_692 = eval_trilinear_point(model, A, B, C, 'a**(2)/(b - c)', ID="X(692)", classes=["center"])
    X_693 = isogonal_conjugate(model, A, B, C, X_692, ID="X(693)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X(650)", classes=["center", "incident"])
    central_line(model, X_2, X_650, 2, 650, incident=True)
    X_320 = eval_trilinear_point(model, A, B, C, '(1 - 2*cos(A))/a**(2)', ID="X(320)", classes=["center", "incident"])
    X_350 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c)*b**(2)*c**(2)', ID="X(350)", classes=["center", "incident"])
    central_line(model, X_320, X_350, 320, 350, incident=True)
    X_325 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X(325)", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X(523)", classes=["center", "incident"])
    central_line(model, X_325, X_523, 325, 523, incident=True)
    return promote_point_to_top(model, X_693)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(693) on the given reference triangle."""
    model = create_model('X(693) = ISOTOMIC CONJUGATE OF X(100)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00693(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00693.json"))
    write_center_svg(
        model_acute,
        here / "x-00693.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
