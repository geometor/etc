"""GEOMETOR construction model for X_3227 = SS(a → bc) OF X_106."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_03227(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3227 = SS(a → bc) OF X_106 on reference triangle ABC."""
    X_3227 = eval_trilinear_point(model, A, B, C, '(b*c/(2*b*c - a*b - a*c))', ID="X_3227", classes=["selected", "target"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    central_line(model, X_81, X_99, 81, 99, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_1, X_190, 1, 190, incident=True)
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    central_line(model, X_88, X_239, 88, 239, incident=True)
    return promote_point_to_top(model, X_3227)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3227 on the given reference triangle."""
    model = create_model('X_3227 = SS(a → bc) OF X_106')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03227(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03227.json"))
    write_center_svg(
        model_acute,
        here / "x-03227.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
