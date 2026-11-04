"""GEOMETOR construction model for X_1167 = 1st SARAGOSSA POINT OF X_34."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01167(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1167 = 1st SARAGOSSA POINT OF X_34 on reference triangle ABC."""
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center"])
    X_269 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)', ID="X_269", classes=["center"])
    central_line(model, X_34, X_40, 34, 40)
    central_line(model, X_255, X_269, 255, 269)
    X_1167 = intersect_lines(model, X_34, X_40, X_255, X_269, ID="X_1167", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_580 = point_from_barycentrics(model, A, B, C, 0.002197609, 0.25263713, 0.74516526, ID="X_580", classes=["center", "incident"])
    central_line(model, X_56, X_580, 56, 580, incident=True)
    return promote_point_to_top(model, X_1167)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1167 on the given reference triangle."""
    model = create_model('X_1167 = 1st SARAGOSSA POINT OF X_34')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01167(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01167.json"))
    write_center_svg(
        model_acute,
        here / "x-01167.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
