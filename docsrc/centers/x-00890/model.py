"""GEOMETOR construction model for X(890) = ISOGONAL CONJUGATE OF X(889)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00890(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(890) = ISOGONAL CONJUGATE OF X(889) on reference triangle ABC."""
    X_889 = eval_barycentric_point(model, A, B, C, 'b*c/((b - c)*(a*b + a*c - 2*b*c))', ID="X(889)", classes=["center"])
    X_890 = isogonal_conjugate(model, A, B, C, X_889, ID="X(890)", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    central_line(model, X_100, X_190, 100, 190, incident=True)
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X(237)", classes=["center", "incident"])
    central_line(model, X_187, X_237, 187, 237, incident=True)
    return promote_point_to_top(model, X_890)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(890) on the given reference triangle."""
    model = create_model('X(890) = ISOGONAL CONJUGATE OF X(889)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00890(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00890.json"))
    write_center_svg(
        model_acute,
        here / "x-00890.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
