"""GEOMETOR construction model for X_919 = ISOGONAL CONJUGATE OF X_918."""

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


def construct_x_00919(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_919 = ISOGONAL CONJUGATE OF X_918 on reference triangle ABC."""
    X_918 = eval_barycentric_point(model, A, B, C, '((b - c)*(b**(2) + c**(2) -a*b - a*c))', ID="X_918", classes=["center"])
    X_919 = isogonal_conjugate(model, A, B, C, X_918, ID="X_919", classes=["selected", "target"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_294 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b**(2) + c**(2) - a*b - a*c))', ID="X_294", classes=["center", "incident"])
    central_line(model, X_104, X_294, 104, 294, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center", "incident"])
    central_line(model, X_100, X_650, 100, 650, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center", "incident"])
    central_line(model, X_109, X_649, 109, 649, incident=True)
    return promote_point_to_top(model, X_919)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_919 on the given reference triangle."""
    model = create_model('X_919 = ISOGONAL CONJUGATE OF X_918')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00919(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00919.json"))
    write_center_svg(
        model_acute,
        here / "x-00919.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
