"""GEOMETOR construction model for X_1020 = POINT ALGEDI."""

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


def construct_x_01020(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1020 = POINT ALGEDI on reference triangle ABC."""
    X_1020 = eval_trilinear_point(model, A, B, C, '(cos(B) + cos(C))/(cos(B) - cos(C))', ID="X_1020", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center", "incident"])
    central_line(model, X_1, X_185, 1, 185, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_108, X_109, 108, 109, incident=True)
    X_269 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)', ID="X_269", classes=["center", "incident"])
    X_292 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) - b*c)', ID="X_292", classes=["center", "incident"])
    central_line(model, X_269, X_292, 269, 292, incident=True)
    return promote_point_to_top(model, X_1020)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1020 on the given reference triangle."""
    model = create_model('X_1020 = POINT ALGEDI')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01020(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01020.json"))
    write_center_svg(
        model_acute,
        here / "x-01020.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
