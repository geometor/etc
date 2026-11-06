"""GEOMETOR construction model for X_3063 = CROSSDIFFERENCE OF X_7 AND X_8."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03063(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3063 = CROSSDIFFERENCE OF X_7 AND X_8 on reference triangle ABC."""
    X_798 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))', ID="X_798", classes=["center"])
    X_3049 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b*sin(A - B) - c*sin(A - C))', ID="X_3049", classes=["center"])
    X_3063 = cevapoint(model, A, B, C, X_798, X_3049, ID="X_3063", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_6, X_513, 6, 513, incident=True)
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X_59", classes=["center", "incident"])
    X_919 = point_from_barycentrics(model, A, B, C, -0.11560694, 0.83236994, 0.28323699, ID="X_919", classes=["center", "incident"])
    central_line(model, X_59, X_919, 59, 919, incident=True)
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center", "incident"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X_650", classes=["center", "incident"])
    central_line(model, X_521, X_650, 521, 650, incident=True)
    return promote_point_to_top(model, X_3063)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3063 on the given reference triangle."""
    model = create_model('X_3063 = CROSSDIFFERENCE OF X_7 AND X_8')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03063(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03063.json"))
    write_center_svg(
        model_acute,
        here / "x-03063.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
