"""GEOMETOR construction model for X_2929 = TANGENTIAL-ISOGONAL CONJUGATE OF X_20."""

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


def construct_x_02929(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2929 = TANGENTIAL-ISOGONAL CONJUGATE OF X_20 on reference triangle ABC."""
    X_195 = eval_trilinear_point(model, A, B, C, 'a*(a**(8) + b**(8) + c**(8) - 4*a**(6)*(b**(2) + c**(2)) + a**(4)*(6*b**(4) + 6*c**(4) + 5*b**(2)*c**(2)) - a**(2)*(4*b**(6) + 4*c**(6) - b**(4)*c**(2) - b**(2)*c**(4)) - 2*b**(2)*c**(2)*(b**(4) + c**(4) - b**(2)*c**(2)))', ID="X_195", classes=["center"])
    X_389 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(2*A)*cos(B - C)', ID="X_389", classes=["center"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center"])
    X_1192 = point_from_barycentrics(model, A, B, C, 0.1436909, 0.29955674, 0.55675236, ID="X_1192", classes=["center"])
    central_line(model, X_195, X_389, 195, 389)
    central_line(model, X_24, X_1192, 24, 1192)
    X_2929 = intersect_lines(model, X_195, X_389, X_24, X_1192, ID="X_2929", classes=["selected", "target"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_1620 = point_from_barycentrics(model, A, B, C, -0.053323413, 0.23422619, 0.81909722, ID="X_1620", classes=["center", "incident"])
    central_line(model, X_22, X_1620, 22, 1620, incident=True)
    return promote_point_to_top(model, X_2929)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2929 on the given reference triangle."""
    model = create_model('X_2929 = TANGENTIAL-ISOGONAL CONJUGATE OF X_20')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02929(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02929.json"))
    write_center_svg(
        model_acute,
        here / "x-02929.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
