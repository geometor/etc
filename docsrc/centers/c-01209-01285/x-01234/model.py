"""GEOMETOR construction model for X_1234 = ISOTOMIC CONJUGATE OF X_1175."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01234(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1234 = ISOTOMIC CONJUGATE OF X_1175 on reference triangle ABC."""
    X_1175 = point_from_barycentrics(model, A, B, C, 0.23759272, 0.33745259, 0.42495468, ID="X_1175", classes=["center"])
    X_1234 = isotomic_conjugate(model, A, B, C, X_1175, ID="X_1234", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_4, X_69, 4, 69, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_313 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(3)*c**(3)', ID="X_313", classes=["center", "incident"])
    central_line(model, X_12, X_313, 12, 313, incident=True)
    X_312 = eval_trilinear_point(model, A, B, C, '(b + c - a)*b**(2)*c**(2)', ID="X_312", classes=["center", "incident"])
    X_1230 = eval_trilinear_point(model, A, B, C, '(b**(3)*c**(3)*(b + c)*(2*a + b + c))', ID="X_1230", classes=["center", "incident"])
    central_line(model, X_312, X_1230, 312, 1230, incident=True)
    return promote_point_to_top(model, X_1234)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1234 on the given reference triangle."""
    model = create_model('X_1234 = ISOTOMIC CONJUGATE OF X_1175')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01234(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01234.json"))
    write_center_svg(
        model_acute,
        here / "x-01234.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
