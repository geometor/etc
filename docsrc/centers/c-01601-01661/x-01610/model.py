"""GEOMETOR construction model for X_1610 = TCC-PERSPECTOR OF X_21."""

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
    intersect_lines,
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01610(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1610 = TCC-PERSPECTOR OF X_21 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_197 = eval_trilinear_point(model, A, B, C, 'a*(-a**(2)*tan(A/2) + b**(2)*tan(B/2) + c**(2)*tan(C/2))', ID="X_197", classes=["center"])
    central_line(model, X_1, X_19, 1, 19)
    central_line(model, X_8, X_197, 8, 197)
    X_1610 = intersect_lines(model, X_1, X_19, X_8, X_197, ID="X_1610", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_959 = eval_trilinear_point(model, A, B, C, '(1/((b + c - a)*(a**(2) + a*b + a*c + 2*b*c)))', ID="X_959", classes=["center", "incident"])
    central_line(model, X_6, X_959, 6, 959, incident=True)
    return promote_point_to_top(model, X_1610)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1610 on the given reference triangle."""
    model = create_model('X_1610 = TCC-PERSPECTOR OF X_21')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01610(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01610.json"))
    write_center_svg(
        model_acute,
        here / "x-01610.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
