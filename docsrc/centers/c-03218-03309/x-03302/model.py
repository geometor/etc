"""GEOMETOR construction model for X_3302 = ISOGONAL CONJUGATE OF X_3301."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03302(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3302 = ISOGONAL CONJUGATE OF X_3301 on reference triangle ABC."""
    X_3301 = eval_trilinear_point(model, A, B, C, '1 - 2*sin(A)', ID="X_3301", classes=["center"])
    X_3302 = isogonal_conjugate(model, A, B, C, X_3301, ID="X_3302", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_590 = eval_trilinear_point(model, A, B, C, '(a**(2) + 4*area )/a', ID="X_590", classes=["center", "incident"])
    central_line(model, X_1, X_590, 1, 590, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_1374 = eval_trilinear_point(model, A, B, C, '1 - 8*( area )/(a*(b + c - a))', ID="X_1374", classes=["center", "incident"])
    central_line(model, X_57, X_1374, 57, 1374, incident=True)
    X_498 = eval_trilinear_point(model, A, B, C, '1 + 2*sin(B)*sin(C)', ID="X_498", classes=["center", "incident"])
    X_1123 = eval_trilinear_point(model, A, B, C, '1/(1 +sin(A))', ID="X_1123", classes=["center", "incident"])
    central_line(model, X_498, X_1123, 498, 1123, incident=True)
    return promote_point_to_top(model, X_3302)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3302 on the given reference triangle."""
    model = create_model('X_3302 = ISOGONAL CONJUGATE OF X_3301')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03302(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03302.json"))
    write_center_svg(
        model_acute,
        here / "x-03302.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
