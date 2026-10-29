"""GEOMETOR construction model for X(253) = X(4)-CROSS CONJUGATE OF X(2)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    isogonal_conjugate,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00253(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(253) = X(4)-CROSS CONJUGATE OF X(2) on reference triangle ABC."""
    X_154 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(B)*cos(C))*a**(2)', ID="X(154)", classes=["center"])
    X_253 = isogonal_conjugate(model, A, B, C, X_154, ID="X(253)", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X(64)", classes=["center", "incident"])
    central_line(model, X_20, X_64, 20, 64, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_280 = point_from_barycentrics(model, A, B, C, -0.15770609, -0.1827957, 1.3405018, ID="X(280)", classes=["center", "incident"])
    central_line(model, X_7, X_280, 7, 280, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_307 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*(b + c)*(cos(A))/(b + c - a)', ID="X(307)", classes=["center", "incident"])
    central_line(model, X_8, X_307, 8, 307, incident=True)
    return promote_point_to_top(model, X_253)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(253) on the given reference triangle."""
    model = create_model('X(253) = X(4)-CROSS CONJUGATE OF X(2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00253(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00253.json"))
    write_center_svg(
        model_acute,
        here / "x-00253.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
