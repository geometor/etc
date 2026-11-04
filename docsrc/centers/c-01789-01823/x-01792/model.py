"""GEOMETOR construction model for X_1792 = INVERSE MIMOSA TRANSFORM OF X_20."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01792(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1792 = INVERSE MIMOSA TRANSFORM OF X_20 on reference triangle ABC."""
    X_1426 = point_from_barycentrics(model, A, B, C, 0.035969128, 0.11183923, 0.85219164, ID="X_1426", classes=["center"])
    X_1792 = isogonal_conjugate(model, A, B, C, X_1426, ID="X_1792", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_8, X_21, 8, 21, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_3, X_69, 3, 69, incident=True)
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    X_212 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(A))', ID="X_212", classes=["center", "incident"])
    central_line(model, X_78, X_212, 78, 212, incident=True)
    return promote_point_to_top(model, X_1792)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1792 on the given reference triangle."""
    model = create_model('X_1792 = INVERSE MIMOSA TRANSFORM OF X_20')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01792(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01792.json"))
    write_center_svg(
        model_acute,
        here / "x-01792.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
