"""GEOMETOR construction model for X_1231 = ISOTOMIC CONJUGATE OF X_1172."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    intersect_lines,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01231(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1231 = ISOTOMIC CONJUGATE OF X_1172 on reference triangle ABC."""
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center"])
    X_331 = eval_trilinear_point(model, A, B, C, '(sec(A/2))**(2)*csc(2*A)', ID="X_331", classes=["center"])
    central_line(model, X_7, X_8, 7, 8)
    central_line(model, X_76, X_331, 76, 331)
    X_1231 = intersect_lines(model, X_7, X_8, X_76, X_331, ID="X_1231", classes=["selected", "target"])
    X_201 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(B - C))', ID="X_201", classes=["center", "incident"])
    X_307 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*(b + c)*(cos(A))/(b + c - a)', ID="X_307", classes=["center", "incident"])
    central_line(model, X_201, X_307, 201, 307, incident=True)
    return promote_point_to_top(model, X_1231)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1231 on the given reference triangle."""
    model = create_model('X_1231 = ISOTOMIC CONJUGATE OF X_1172')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01231(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01231.json"))
    write_center_svg(
        model_acute,
        here / "x-01231.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
