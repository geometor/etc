"""GEOMETOR construction model for X(218) = X(7)-CEVA CONJUGATE OF X(55)."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00218(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(218) = X(7)-CEVA CONJUGATE OF X(55) on reference triangle ABC."""
    X_218 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(2) + b**(2) + c**(2) - 2*a*b - 2*a*c)', ID="X(218)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["center", "incident"])
    central_line(model, X_3, X_41, 3, 41, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_56, X_101, 56, 101, incident=True)
    return promote_point_to_top(model, X_218)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(218) on the given reference triangle."""
    model = create_model('X(218) = X(7)-CEVA CONJUGATE OF X(55)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00218(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00218.json"))
    write_center_svg(
        model_acute,
        here / "x-00218.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
