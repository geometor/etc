"""GEOMETOR construction model for X(939) = ISOGONAL CONJUGATE OF X(938)."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00939(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(939) = ISOGONAL CONJUGATE OF X(938) on reference triangle ABC."""
    X_938 = point_from_barycentrics(model, A, B, C, 0.2562724, 0.33333333, 0.41039427, ID="X(938)", classes=["center"])
    X_939 = isogonal_conjugate(model, A, B, C, X_938, ID="X(939)", classes=["selected", "target"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    central_line(model, X_34, X_55, 34, 55, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_212 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(A))', ID="X(212)", classes=["center", "incident"])
    central_line(model, X_56, X_212, 56, 212, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_269 = eval_trilinear_point(model, A, B, C, '(a**(2) - (b - c)**(2))**(2)', ID="X(269)", classes=["center", "incident"])
    central_line(model, X_3, X_269, 3, 269, incident=True)
    return promote_point_to_top(model, X_939)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(939) on the given reference triangle."""
    model = create_model('X(939) = ISOGONAL CONJUGATE OF X(938)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00939(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00939.json"))
    write_center_svg(
        model_acute,
        here / "x-00939.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
