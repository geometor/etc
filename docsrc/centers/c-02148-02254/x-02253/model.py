"""GEOMETOR construction model for X_2253 = X_2-ISOCONJUGATE OF X_917."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02253(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2253 = X_2-ISOCONJUGATE OF X_917 on reference triangle ABC."""
    X_911 = eval_barycentric_point(model, A, B, C, 'a**(3) / (2*a**(3) - a**(2)*(b + c) - (b - c)**(2)*(b + c))', ID="X_911", classes=["center"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    X_2253 = ceva_conjugate(model, A, B, C, X_911, X_48, ID="X_2253", classes=["selected", "target"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_48, X_184, 48, 184, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_1708 = point_from_barycentrics(model, A, B, C, -0.046554935, 0.23836127, 0.80819367, ID="X_1708", classes=["center", "incident"])
    central_line(model, X_19, X_1708, 19, 1708, incident=True)
    return promote_point_to_top(model, X_2253)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2253 on the given reference triangle."""
    model = create_model('X_2253 = X_2-ISOCONJUGATE OF X_917')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02253(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02253.json"))
    write_center_svg(
        model_acute,
        here / "x-02253.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
