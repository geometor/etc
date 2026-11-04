"""GEOMETOR construction model for X_1406 = X_46-BETH CONJUGATE OF X_46."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01406(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1406 = X_46-BETH CONJUGATE OF X_46 on reference triangle ABC."""
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_1406 = ceva_conjugate(model, A, B, C, X_34, X_56, ID="X_1406", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_31, X_56, 31, 56, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_222 = eval_trilinear_point(model, A, B, C, 'cos(A)*tan(A/2)', ID="X_222", classes=["center", "incident"])
    central_line(model, X_65, X_222, 65, 222, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1066 = eval_trilinear_point(model, A, B, C, '(1 - cos(A)*(cos(B) + cos(C)))', ID="X_1066", classes=["center", "incident"])
    central_line(model, X_55, X_1066, 55, 1066, incident=True)
    return promote_point_to_top(model, X_1406)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1406 on the given reference triangle."""
    model = create_model('X_1406 = X_46-BETH CONJUGATE OF X_46')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01406(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01406.json"))
    write_center_svg(
        model_acute,
        here / "x-01406.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
