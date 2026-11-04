"""GEOMETOR construction model for X_1841 = ZOSMA TRANSFORM OF X_71."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01841(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1841 = ZOSMA TRANSFORM OF X_71 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    central_line(model, X_6, X_19, 6, 19)
    central_line(model, X_4, X_37, 4, 37)
    X_1841 = intersect_lines(model, X_6, X_19, X_4, X_37, ID="X_1841", classes=["selected", "target"])
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    central_line(model, X_53, X_225, 53, 225, incident=True)
    return promote_point_to_top(model, X_1841)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1841 on the given reference triangle."""
    model = create_model('X_1841 = ZOSMA TRANSFORM OF X_71')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01841(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01841.json"))
    write_center_svg(
        model_acute,
        here / "x-01841.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
