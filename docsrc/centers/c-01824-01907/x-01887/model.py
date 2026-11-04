"""GEOMETOR construction model for X_1887 = ZOSMA TRANSFORM OF X_946."""

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


def construct_x_01887(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1887 = ZOSMA TRANSFORM OF X_946 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    central_line(model, X_4, X_65, 4, 65)
    central_line(model, X_33, X_56, 33, 56)
    X_1887 = intersect_lines(model, X_4, X_65, X_33, X_56, ID="X_1887", classes=["selected", "target"])
    X_318 = eval_trilinear_point(model, A, B, C, '(1 + sec(A))/a**(2)', ID="X_318", classes=["center", "incident"])
    X_518 = eval_trilinear_point(model, A, B, C, '(a*b + a*c - b**(2) - c**(2))', ID="X_518", classes=["center", "incident"])
    central_line(model, X_318, X_518, 318, 518, incident=True)
    return promote_point_to_top(model, X_1887)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1887 on the given reference triangle."""
    model = create_model('X_1887 = ZOSMA TRANSFORM OF X_946')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01887(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01887.json"))
    write_center_svg(
        model_acute,
        here / "x-01887.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
