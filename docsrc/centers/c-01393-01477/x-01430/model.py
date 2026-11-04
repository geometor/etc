"""GEOMETOR construction model for X_1430 = X_243-BETH CONJUGATE OF X_243."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01430(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1430 = X_243-BETH CONJUGATE OF X_243 on reference triangle ABC."""
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center"])
    central_line(model, X_25, X_34, 25, 34)
    central_line(model, X_27, X_58, 27, 58)
    X_1430 = intersect_lines(model, X_25, X_34, X_27, X_58, ID="X_1430", classes=["selected", "target"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    central_line(model, X_92, X_171, 92, 171, incident=True)
    return promote_point_to_top(model, X_1430)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1430 on the given reference triangle."""
    model = create_model('X_1430 = X_243-BETH CONJUGATE OF X_243')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01430(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01430.json"))
    write_center_svg(
        model_acute,
        here / "x-01430.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
