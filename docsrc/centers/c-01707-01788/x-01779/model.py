"""GEOMETOR construction model for X_1779 = MIMOSA TRANSFORM OF X_1172."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01779(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1779 = MIMOSA TRANSFORM OF X_1172 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center"])
    central_line(model, X_4, X_46, 4, 46)
    central_line(model, X_35, X_47, 35, 47)
    X_1779 = intersect_lines(model, X_4, X_46, X_35, X_47, ID="X_1779", classes=["selected", "target"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_43, X_165, 43, 165, incident=True)
    return promote_point_to_top(model, X_1779)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1779 on the given reference triangle."""
    model = create_model('X_1779 = MIMOSA TRANSFORM OF X_1172')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01779(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01779.json"))
    write_center_svg(
        model_acute,
        here / "x-01779.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
