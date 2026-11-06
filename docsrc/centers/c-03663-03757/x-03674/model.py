"""GEOMETOR construction model for X_3674 = X_2329com(INTOUCH TRIANGLE)."""

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
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03674(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3674 = X_2329com(INTOUCH TRIANGLE) on reference triangle ABC."""
    X_3674 = eval_barycentric_point(model, A, B, C, '((b**(2) + c**(2) + a*b + a*c)/(b + c - a))', ID="X_3674", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    central_line(model, X_76, X_85, 76, 85, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_348 = eval_trilinear_point(model, A, B, C, 'cot(A)*(sec(A/2))**(2)', ID="X_348", classes=["center", "incident"])
    central_line(model, X_57, X_348, 57, 348, incident=True)
    return promote_point_to_top(model, X_3674)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3674 on the given reference triangle."""
    model = create_model('X_3674 = X_2329com(INTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03674(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03674.json"))
    write_center_svg(
        model_acute,
        here / "x-03674.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
