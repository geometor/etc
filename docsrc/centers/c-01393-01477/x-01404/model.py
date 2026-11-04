"""GEOMETOR construction model for X_1404 = X_44-BETH CONJUGATE OF X_44."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01404(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1404 = X_44-BETH CONJUGATE OF X_44 on reference triangle ABC."""
    X_1319 = eval_trilinear_point(model, A, B, C, '(b + c - 2*a)/ (b + c - a)', ID="X_1319", classes=["center"])
    X_902 = eval_trilinear_point(model, A, B, C, 'a*(b + c - 2*a)', ID="X_902", classes=["center"])
    X_1404 = ceva_conjugate(model, A, B, C, X_1319, X_902, ID="X_1404", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_6, X_41, 6, 41, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_89 = eval_trilinear_point(model, A, B, C, '1/(2*b + 2*c - a)', ID="X_89", classes=["center", "incident"])
    central_line(model, X_57, X_89, 57, 89, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_572 = eval_trilinear_point(model, A, B, C, '(cos(A - U))', ID="X_572", classes=["center", "incident"])
    central_line(model, X_35, X_572, 35, 572, incident=True)
    return promote_point_to_top(model, X_1404)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1404 on the given reference triangle."""
    model = create_model('X_1404 = X_44-BETH CONJUGATE OF X_44')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01404(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01404.json"))
    write_center_svg(
        model_acute,
        here / "x-01404.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
