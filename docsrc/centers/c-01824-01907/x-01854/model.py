"""GEOMETOR construction model for X_1854 = ZOSMA TRANSFORM OF X_208."""

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
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01854(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1854 = ZOSMA TRANSFORM OF X_208 on reference triangle ABC."""
    X_221 = eval_trilinear_point(model, A, B, C, '((sin(A/2))**(2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_221", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1854 = reflection_in_point(model, X_221, X_1, ID="X_1854", classes=["selected", "target"], guide=False)
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center", "incident"])
    central_line(model, X_1, X_84, 1, 84, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    central_line(model, X_33, X_64, 33, 64, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_774 = eval_trilinear_point(model, A, B, C, '(cos(B))**(2) + (cos(C))**(2)', ID="X_774", classes=["center", "incident"])
    central_line(model, X_56, X_774, 56, 774, incident=True)
    return promote_point_to_top(model, X_1854)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1854 on the given reference triangle."""
    model = create_model('X_1854 = ZOSMA TRANSFORM OF X_208')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01854(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01854.json"))
    write_center_svg(
        model_acute,
        here / "x-01854.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
