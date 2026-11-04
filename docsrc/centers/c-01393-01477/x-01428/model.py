"""GEOMETOR construction model for X_1428 = X_238-BETH CONJUGATE OF X_238."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01428(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1428 = X_238-BETH CONJUGATE OF X_238 on reference triangle ABC."""
    X_1416 = point_from_barycentrics(model, A, B, C, 0.065359477, 1.254902, -0.32026144, ID="X_1416", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_1428 = ceva_conjugate(model, A, B, C, X_1416, X_56, ID="X_1428", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_6, X_41, 6, 41, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center", "incident"])
    central_line(model, X_65, X_82, 65, 82, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A- omega )', ID="X_182", classes=["center", "incident"])
    central_line(model, X_1, X_182, 1, 182, incident=True)
    return promote_point_to_top(model, X_1428)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1428 on the given reference triangle."""
    model = create_model('X_1428 = X_238-BETH CONJUGATE OF X_238')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01428(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01428.json"))
    write_center_svg(
        model_acute,
        here / "x-01428.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
