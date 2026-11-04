"""GEOMETOR construction model for X_1473 = X_1040-BETH CONJUGATE OF X_1040."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01473(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1473 = X_1040-BETH CONJUGATE OF X_1040 on reference triangle ABC."""
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center"])
    X_1459 = eval_trilinear_point(model, A, B, C, '(b - c)*cos(A)', ID="X_1459", classes=["center"])
    X_1473 = ceva_conjugate(model, A, B, C, X_101, X_1459, ID="X_1473", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_3, X_63, 3, 63, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_25, X_57, 25, 57, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_31, X_56, 31, 56, incident=True)
    return promote_point_to_top(model, X_1473)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1473 on the given reference triangle."""
    model = create_model('X_1473 = X_1040-BETH CONJUGATE OF X_1040')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01473(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01473.json"))
    write_center_svg(
        model_acute,
        here / "x-01473.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
