"""GEOMETOR construction model for X_1284 = 8th SHARYGIN POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01284(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1284 = 8th SHARYGIN POINT on reference triangle ABC."""
    X_1284 = eval_trilinear_point(model, A, B, C, '((b + c)*(b*c - a**(2))/(b + c - a))', ID="X_1284", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_7, X_21, 7, 21, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_37, X_65, 37, 65, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center", "incident"])
    central_line(model, X_1, X_256, 1, 256, incident=True)
    return promote_point_to_top(model, X_1284)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1284 on the given reference triangle."""
    model = create_model('X_1284 = 8th SHARYGIN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01284(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01284.json"))
    write_center_svg(
        model_acute,
        here / "x-01284.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
