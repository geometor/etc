"""GEOMETOR construction model for X_3645 = POINT ALKAID."""

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


def construct_x_03645(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3645 = POINT ALKAID on reference triangle ABC."""
    X_3645 = eval_trilinear_point(model, A, B, C, '(1 + cos(B/2) + cos(C/2) - cos(A/2))', ID="X_3645", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_168 = eval_trilinear_point(model, A, B, C, 'sin(A) - sin(B) - sin(C) + 2*(cos(A/2) + sin(B/2 - A/2) + sin(C/2 - A/2))', ID="X_168", classes=["center", "incident"])
    central_line(model, X_1, X_168, 1, 168, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_483 = eval_trilinear_point(model, A, B, C, '(sec(A/4))**(2)', ID="X_483", classes=["center", "incident"])
    central_line(model, X_40, X_483, 40, 483, incident=True)
    X_258 = eval_trilinear_point(model, A, B, C, '1/(cos(B/2) + cos(C/2) - cos(A/2))', ID="X_258", classes=["center", "incident"])
    X_1127 = eval_trilinear_point(model, A, B, C, '(sin(A/4))/sin(3*A/4)', ID="X_1127", classes=["center", "incident"])
    central_line(model, X_258, X_1127, 258, 1127, incident=True)
    return promote_point_to_top(model, X_3645)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3645 on the given reference triangle."""
    model = create_model('X_3645 = POINT ALKAID')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03645(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03645.json"))
    write_center_svg(
        model_acute,
        here / "x-03645.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
