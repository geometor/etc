"""GEOMETOR construction model for X_2962 = TRILINEAR PRODUCT X_17*X_18."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02962(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2962 = TRILINEAR PRODUCT X_17*X_18 on reference triangle ABC."""
    X_2962 = eval_trilinear_point(model, A, B, C, '(csc(A +  pi  /6)*csc(A -  pi  /6))', ID="X_2962", classes=["selected", "target"])
    X_93 = eval_trilinear_point(model, A, B, C, 'sec(3*A)', ID="X_93", classes=["center", "incident"])
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    central_line(model, X_93, X_225, 93, 225, incident=True)
    X_759 = eval_trilinear_point(model, A, B, C, '(1/(a**(0)*(b**(3) + c**(3)) - a**(2)*(b**(1) + c**(1))))', ID="X_759", classes=["center", "incident"])
    X_930 = eval_barycentric_point(model, A, B, C, '1/((b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) - b**(2)*c**(2)))', ID="X_930", classes=["center", "incident"])
    central_line(model, X_759, X_930, 759, 930, incident=True)
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center", "incident"])
    X_1733 = point_from_barycentrics(model, A, B, C, -0.64449661, 0.38341158, 1.261085, ID="X_1733", classes=["center", "incident"])
    central_line(model, X_82, X_1733, 82, 1733, incident=True)
    return promote_point_to_top(model, X_2962)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2962 on the given reference triangle."""
    model = create_model('X_2962 = TRILINEAR PRODUCT X_17*X_18')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02962(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02962.json"))
    write_center_svg(
        model_acute,
        here / "x-02962.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
