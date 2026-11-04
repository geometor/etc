"""GEOMETOR construction model for X_1783 = MIMOSA TRANSFORM OF X_1262."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01783(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1783 = MIMOSA TRANSFORM OF X_1262 on reference triangle ABC."""
    X_905 = eval_trilinear_point(model, A, B, C, '(b - c)*cot(A)', ID="X_905", classes=["center"])
    X_1783 = isogonal_conjugate(model, A, B, C, X_905, ID="X_1783", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    central_line(model, X_101, X_108, 101, 108, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_100, X_112, 100, 112, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_218 = eval_trilinear_point(model, A, B, C, '((cos(A/2))**(2)*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4)))', ID="X_218", classes=["center", "incident"])
    central_line(model, X_4, X_218, 4, 218, incident=True)
    return promote_point_to_top(model, X_1783)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1783 on the given reference triangle."""
    model = create_model('X_1783 = MIMOSA TRANSFORM OF X_1262')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01783(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01783.json"))
    write_center_svg(
        model_acute,
        here / "x-01783.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
