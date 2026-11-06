"""GEOMETOR construction model for X_3724 = X_908com(INCENTRAL TRIANGLE)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03724(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3724 = X_908com(INCENTRAL TRIANGLE) on reference triangle ABC."""
    X_3724 = eval_barycentric_point(model, A, B, C, 'a**(3)*(b+c) * (a**(2)-b**(2)+b*c-c**(2))', ID="X_3724", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_31, X_48, 31, 48, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X_181", classes=["center", "incident"])
    central_line(model, X_42, X_181, 42, 181, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_214 = eval_trilinear_point(model, A, B, C, '(b + c - 2*a)*(b**(2) + c**(2) - a**(2) - b*c)', ID="X_214", classes=["center", "incident"])
    central_line(model, X_36, X_214, 36, 214, incident=True)
    return promote_point_to_top(model, X_3724)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3724 on the given reference triangle."""
    model = create_model('X_3724 = X_908com(INCENTRAL TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03724(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03724.json"))
    write_center_svg(
        model_acute,
        here / "x-03724.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
