"""GEOMETOR construction model for X_3187 = X_27-CEVA CONJUGATE OF X_2."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03187(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3187 = X_27-CEVA CONJUGATE OF X_2 on reference triangle ABC."""
    X_306 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2))*(b + c)*cos(A)', ID="X_306", classes=["center"])
    X_3187 = anticomplement(model, A, B, C, X_306, ID="X_3187", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    central_line(model, X_75, X_81, 75, 81, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_740 = eval_trilinear_point(model, A, B, C, 'a **(-2)*(b**(1) + c**(1)) - a**(0)*(b **(-1) + c **(-1))', ID="X_740", classes=["center", "incident"])
    central_line(model, X_31, X_740, 31, 740, incident=True)
    return promote_point_to_top(model, X_3187)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3187 on the given reference triangle."""
    model = create_model('X_3187 = X_27-CEVA CONJUGATE OF X_2')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03187(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03187.json"))
    write_center_svg(
        model_acute,
        here / "x-03187.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
