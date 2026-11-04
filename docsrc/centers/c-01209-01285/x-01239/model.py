"""GEOMETOR construction model for X_1239 = ISOTOMIC CONJUGATE OF X_1180."""

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
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01239(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1239 = ISOTOMIC CONJUGATE OF X_1180 on reference triangle ABC."""
    X_1180 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) + b**(2)*c**(2) + c**(2)*a**(2) + a**(2)*b**(2))', ID="X_1180", classes=["center"])
    X_1239 = isotomic_conjugate(model, A, B, C, X_1180, ID="X_1239", classes=["selected", "target"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_251 = eval_trilinear_point(model, A, B, C, 'a**(2)*csc(A + omega )', ID="X_251", classes=["center", "incident"])
    central_line(model, X_76, X_251, 76, 251, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_1235 = eval_barycentric_point(model, A, B, C, '(csc(A))*(csc(2*A))*sin(A + omega )', ID="X_1235", classes=["center", "incident"])
    central_line(model, X_25, X_1235, 25, 1235, incident=True)
    return promote_point_to_top(model, X_1239)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1239 on the given reference triangle."""
    model = create_model('X_1239 = ISOTOMIC CONJUGATE OF X_1180')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01239(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01239.json"))
    write_center_svg(
        model_acute,
        here / "x-01239.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
