"""GEOMETOR construction model for X(280) = X(1)-CROSS CONJUGATE OF X(8)."""

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
    gergonne_point_of,
    isogonal_conjugate,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00280(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(280) = X(1)-CROSS CONJUGATE OF X(8) on reference triangle ABC."""
    X_221 = eval_trilinear_point(model, A, B, C, '(1 - cos(A))*(1 + cos(A) - cos(B) - cos(C))', ID="X(221)", classes=["center"])
    X_280 = isogonal_conjugate(model, A, B, C, X_221, ID="X(280)", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    central_line(model, X_8, X_20, 8, 20, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_253 = eval_barycentric_point(model, A, B, C, '1/(3*a**(4) - 2*a**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2))', ID="X(253)", classes=["center", "incident"])
    central_line(model, X_7, X_253, 7, 253, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    X_268 = point_from_barycentrics(model, A, B, C, -0.78436965, -0.82915003, 2.6135197, ID="X(268)", classes=["center", "incident"])
    central_line(model, X_21, X_268, 21, 268, incident=True)
    return promote_point_to_top(model, X_280)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(280) on the given reference triangle."""
    model = create_model('X(280) = X(1)-CROSS CONJUGATE OF X(8)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00280(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00280.json"))
    write_center_svg(
        model_acute,
        here / "x-00280.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
