"""GEOMETOR construction model for X_1355 = BRISSE TRANSFORM OF X_98."""

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


def construct_x_01355(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1355 = BRISSE TRANSFORM OF X_98 on reference triangle ABC."""
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_741 = eval_trilinear_point(model, A, B, C, '(1/(a **(-2)*(b**(1) + c**(1)) - a**(0)*(b **(-1) + c **(-1))))', ID="X_741", classes=["center"])
    X_222 = eval_trilinear_point(model, A, B, C, 'cos(A)*tan(A/2)', ID="X_222", classes=["center"])
    X_1363 = point_from_barycentrics(model, A, B, C, 0.39605447, 0.60045962, 0.0034859063, ID="X_1363", classes=["center"])
    central_line(model, X_56, X_741, 56, 741)
    central_line(model, X_222, X_1363, 222, 1363)
    X_1355 = intersect_lines(model, X_56, X_741, X_222, X_1363, ID="X_1355", classes=["selected", "target"])
    return promote_point_to_top(model, X_1355)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1355 on the given reference triangle."""
    model = create_model('X_1355 = BRISSE TRANSFORM OF X_98')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01355(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01355.json"))
    write_center_svg(
        model_acute,
        here / "x-01355.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
