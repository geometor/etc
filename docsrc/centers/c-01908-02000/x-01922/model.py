"""GEOMETOR construction model for X_1922 = TRILINEAR POLE OF PU(12)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01922(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1922 = TRILINEAR POLE OF PU(12) on reference triangle ABC."""
    X_1921 = eval_trilinear_point(model, A, B, C, '(b**(3)*c**(3)*(a**(2) - b*c))', ID="X_1921", classes=["center"])
    X_1922 = isogonal_conjugate(model, A, B, C, X_1921, ID="X_1922", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_58, X_101, 58, 101, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X_291", classes=["center", "incident"])
    central_line(model, X_6, X_291, 6, 291, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_335 = eval_trilinear_point(model, A, B, C, 'b*c/(a**(2) - b*c)', ID="X_335", classes=["center", "incident"])
    central_line(model, X_81, X_335, 81, 335, incident=True)
    return promote_point_to_top(model, X_1922)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1922 on the given reference triangle."""
    model = create_model('X_1922 = TRILINEAR POLE OF PU(12)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01922(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01922.json"))
    write_center_svg(
        model_acute,
        here / "x-01922.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
