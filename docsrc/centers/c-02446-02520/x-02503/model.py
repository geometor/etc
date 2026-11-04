"""GEOMETOR construction model for X_2503 = RADICAL CENTER OF {CIRCUMCIRCLE, PARRY CIRCLE, BEVAN CIRCLE}."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02503(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2503 = RADICAL CENTER OF {CIRCUMCIRCLE, PARRY CIRCLE, BEVAN CIRCLE} on reference triangle ABC."""
    X_842 = eval_barycentric_point(model, A, B, C, 'a**(2)/(2*a**(6) - 2*a**(4)*(b**(2) + c**(2)) + a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X_842", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    X_2503 = ceva_conjugate(model, A, B, C, X_842, X_55, ID="X_2503", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_6, X_110, 6, 110, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_2611 = point_from_barycentrics(model, A, B, C, 0.21464646, 0.68065268, 0.10470085, ID="X_2611", classes=["center", "incident"])
    central_line(model, X_37, X_2611, 37, 2611, incident=True)
    return promote_point_to_top(model, X_2503)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2503 on the given reference triangle."""
    model = create_model('X_2503 = RADICAL CENTER OF {CIRCUMCIRCLE, PARRY CIRCLE, BEVAN CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02503(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02503.json"))
    write_center_svg(
        model_acute,
        here / "x-02503.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
