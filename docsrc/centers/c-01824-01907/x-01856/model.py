"""GEOMETOR construction model for X_1856 = ZOSMA TRANSFORM OF X_222."""

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


def construct_x_01856(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1856 = ZOSMA TRANSFORM OF X_222 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center"])
    central_line(model, X_4, X_57, 4, 57)
    central_line(model, X_33, X_42, 33, 42)
    X_1856 = intersect_lines(model, X_4, X_57, X_33, X_42, ID="X_1856", classes=["selected", "target"])
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    X_235 = eval_trilinear_point(model, A, B, C, 'sec(A) - cos(B - C)', ID="X_235", classes=["center", "incident"])
    central_line(model, X_225, X_235, 225, 235, incident=True)
    return promote_point_to_top(model, X_1856)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1856 on the given reference triangle."""
    model = create_model('X_1856 = ZOSMA TRANSFORM OF X_222')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01856(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01856.json"))
    write_center_svg(
        model_acute,
        here / "x-01856.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
