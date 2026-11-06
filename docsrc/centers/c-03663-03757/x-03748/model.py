"""GEOMETOR construction model for X_3748 = X_1621com[n(MEDIAL)*n(INCENTRAL)]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03748(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3748 = X_1621com[n(MEDIAL)*n(INCENTRAL)] on reference triangle ABC."""
    X_3748 = eval_barycentric_point(model, A, B, C, '(a*(2*a**(2) + b**(2) + c**(2) - 3*a*b - 3*a*c - 2*b*c))', ID="X_3748", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    X_1001 = eval_trilinear_point(model, A, B, C, 'a**(2) - a*(b + c) - 2*b*c', ID="X_1001", classes=["center", "incident"])
    central_line(model, X_210, X_1001, 210, 1001, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_1279 = eval_trilinear_point(model, A, B, C, '((b - c)**(2) - a*(b + c - 2*a))', ID="X_1279", classes=["center", "incident"])
    central_line(model, X_42, X_1279, 42, 1279, incident=True)
    return promote_point_to_top(model, X_3748)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3748 on the given reference triangle."""
    model = create_model('X_3748 = X_1621com[n(MEDIAL)*n(INCENTRAL)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03748(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03748.json"))
    write_center_svg(
        model_acute,
        here / "x-03748.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
