"""GEOMETOR construction model for X(152) = REFLECTION OF X(20) IN X(101)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00152(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(152) = REFLECTION OF X(20) IN X(101) on reference triangle ABC."""
    X_152 = eval_barycentric_point(model, A, B, C, 'a**(8) - a**(7)*(b + c) + a**(6)*(2*b**(2) + b*c + 2*c**(2)) - a**(5)*(5*b**(3) - b**(2)*c - b*c**(2) + 5*c**(3)) - a**(4)*b*c*(b**(2) - 6*b*c + c**(2)) + a**(3)*(5*b**(5) + b**(4)*c - 6*b**(3)*c**(2) - 6*b**(2)*c**(3) + b*c**(4) + 5*c**(5)) - a**(2)*(2*b**(6) + b**(5)*c + 2*b**(4)*c**(2) - 10*b**(3)*c**(3) + 2*b**(2)*c**(4) + b*c**(5) + 2*c**(6)) + a*(b**(7) - b**(6)*c - 3*b**(5)*c**(2) + 3*b**(4)*c**(3) + 3*b**(3)*c**(4) - 3*b**(2)*c**(5) - b*c**(6) + c**(7)) - b**(8) + b**(7)*c + 2*b**(6)*c**(2) - b**(5)*c**(3) - 2*b**(4)*c**(4) - b**(3)*c**(5) + 2*b**(2)*c**(6) + b*c**(7) - c**(8)', ID="X(152)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X(103)", classes=["center", "incident"])
    central_line(model, X_2, X_103, 2, 103, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_20, X_101, 20, 101, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_150 = point_from_barycentrics(model, A, B, C, 0.10714286, 1.6428571, -0.75, ID="X(150)", classes=["center", "incident"])
    central_line(model, X_4, X_150, 4, 150, incident=True)
    return promote_point_to_top(model, X_152)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(152) on the given reference triangle."""
    model = create_model('X(152) = REFLECTION OF X(20) IN X(101)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00152(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00152.json"))
    write_center_svg(
        model_acute,
        here / "x-00152.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
