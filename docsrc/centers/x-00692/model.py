"""GEOMETOR construction model for X(692) = X(110)-CEVA CONJUGATE OF X(101)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00692(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(692) = X(110)-CEVA CONJUGATE OF X(101) on reference triangle ABC."""
    X_692 = eval_trilinear_point(model, A, B, C, 'a**(2)/(b - c)', ID="X(692)", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_100, X_110, 100, 110, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X(184)", classes=["center", "incident"])
    central_line(model, X_55, X_184, 55, 184, incident=True)
    X_154 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(B)*cos(C))*a**(2)', ID="X(154)", classes=["center", "incident"])
    X_197 = eval_trilinear_point(model, A, B, C, 'a*(-a**(2)*tan(A/2) + b**(2)*tan(B/2) + c**(2)*tan(C/2))', ID="X(197)", classes=["center", "incident"])
    central_line(model, X_154, X_197, 154, 197, incident=True)
    return promote_point_to_top(model, X_692)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(692) on the given reference triangle."""
    model = create_model('X(692) = X(110)-CEVA CONJUGATE OF X(101)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00692(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00692.json"))
    write_center_svg(
        model_acute,
        here / "x-00692.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
