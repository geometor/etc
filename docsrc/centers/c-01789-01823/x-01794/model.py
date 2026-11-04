"""GEOMETOR construction model for X_1794 = INVERSE MIMOSA TRANSFORM OF X_35."""

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
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01794(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1794 = INVERSE MIMOSA TRANSFORM OF X_35 on reference triangle ABC."""
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center"])
    central_line(model, X_10, X_29, 10, 29)
    central_line(model, X_35, X_71, 35, 71)
    X_1794 = intersect_lines(model, X_10, X_29, X_35, X_71, ID="X_1794", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_201 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(B - C))', ID="X_201", classes=["center", "incident"])
    central_line(model, X_1, X_201, 1, 201, incident=True)
    return promote_point_to_top(model, X_1794)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1794 on the given reference triangle."""
    model = create_model('X_1794 = INVERSE MIMOSA TRANSFORM OF X_35')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01794(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01794.json"))
    write_center_svg(
        model_acute,
        here / "x-01794.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
