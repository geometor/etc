"""GEOMETOR construction model for X_1798 = INVERSE MIMOSA TRANSFORM OF X_58."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01798(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1798 = INVERSE MIMOSA TRANSFORM OF X_58 on reference triangle ABC."""
    X_429 = eval_barycentric_point(model, A, B, C, '(b + c) * (-a**(2) + b**(2) - c**(2)) * (a**(2) + b**(2) - c**(2)) * (a*b + b**(2) + a*c + c**(2))', ID="X_429", classes=["center"])
    X_1798 = isogonal_conjugate(model, A, B, C, X_429, ID="X_1798", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_6, X_60, 6, 60, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    central_line(model, X_65, X_81, 65, 81, incident=True)
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_283 = eval_trilinear_point(model, A, B, C, '(cos(A))/(cos(B) + cos(C))', ID="X_283", classes=["center", "incident"])
    central_line(model, X_71, X_283, 71, 283, incident=True)
    return promote_point_to_top(model, X_1798)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1798 on the given reference triangle."""
    model = create_model('X_1798 = INVERSE MIMOSA TRANSFORM OF X_58')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01798(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01798.json"))
    write_center_svg(
        model_acute,
        here / "x-01798.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
