"""GEOMETOR construction model for X_2445 = ISOGONAL CONJUGATE OF X_2419."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02445(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2445 = ISOGONAL CONJUGATE OF X_2419 on reference triangle ABC."""
    X_2419 = point_from_barycentrics(model, A, B, C, -80.557045, 75.491805, 6.0652396, ID="X_2419", classes=["center"])
    X_2445 = isogonal_conjugate(model, A, B, C, X_2419, ID="X_2445", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_6, X_25, 6, 25, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_1301 = point_from_barycentrics(model, A, B, C, -0.036707118, 0.057047829, 0.97965929, ID="X_1301", classes=["center", "incident"])
    central_line(model, X_110, X_1301, 110, 1301, incident=True)
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X_250", classes=["center", "incident"])
    X_2421 = eval_trilinear_point(model, A, B, C, '(sin(A))*(sin(2*B) + sin(2*C) - 2*(cot(A))*((sin(B))**(2) + (sin(C))**(2)))/(cot(B) - cot(C))', ID="X_2421", classes=["center", "incident"])
    central_line(model, X_250, X_2421, 250, 2421, incident=True)
    return promote_point_to_top(model, X_2445)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2445 on the given reference triangle."""
    model = create_model('X_2445 = ISOGONAL CONJUGATE OF X_2419')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02445(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02445.json"))
    write_center_svg(
        model_acute,
        here / "x-02445.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
