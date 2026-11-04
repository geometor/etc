"""GEOMETOR construction model for X_1399 = X_35-BETH CONJUGATE OF X_35."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01399(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1399 = X_35-BETH CONJUGATE OF X_35 on reference triangle ABC."""
    X_1399 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(2*A))', ID="X_1399", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    central_line(model, X_3, X_47, 3, 47, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_31, X_56, 31, 56, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_58, X_65, 58, 65, incident=True)
    return promote_point_to_top(model, X_1399)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1399 on the given reference triangle."""
    model = create_model('X_1399 = X_35-BETH CONJUGATE OF X_35')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01399(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01399.json"))
    write_center_svg(
        model_acute,
        here / "x-01399.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
