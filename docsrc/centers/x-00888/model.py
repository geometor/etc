"""GEOMETOR construction model for X(888) = ISOTOMIC CONJUGATE OF X(886)."""

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
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00888(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(888) = ISOTOMIC CONJUGATE OF X(886) on reference triangle ABC."""
    X_886 = eval_barycentric_point(model, A, B, C, 'b**(2)*c**(2)/((b**(2) - c**(2))*(a**(2)*b**(2) + a**(2)*c**(2) - 2*b**(2)*c**(2)))', ID="X(886)", classes=["center"])
    X_888 = isotomic_conjugate(model, A, B, C, X_886, ID="X(888)", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_351 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)- c**(2))*(b**(2)+ c**(2)- 2*a**(2))', ID="X(351)", classes=["center", "incident"])
    X_865 = point_from_barycentrics(model, A, B, C, 2.2741668, 1.5379886, -2.8121554, ID="X(865)", classes=["center", "incident"])
    central_line(model, X_351, X_865, 351, 865, incident=True)
    X_694 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) - b**(2)*c**(2))', ID="X(694)", classes=["center", "incident"])
    X_882 = point_from_barycentrics(model, A, B, C, 0.023590899, 1.0060979, -0.02968882, ID="X(882)", classes=["center", "incident"])
    central_line(model, X_694, X_882, 694, 882, incident=True)
    return promote_point_to_top(model, X_888)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(888) on the given reference triangle."""
    model = create_model('X(888) = ISOTOMIC CONJUGATE OF X(886)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00888(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00888.json"))
    write_center_svg(
        model_acute,
        here / "x-00888.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
