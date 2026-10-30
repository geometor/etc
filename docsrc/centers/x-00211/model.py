"""GEOMETOR construction model for X(211) = X(4)-CEVA CONJUGATE OF X(39)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00211(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(211) = X(4)-CEVA CONJUGATE OF X(39) on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center"])
    X_211 = ceva_conjugate(model, A, B, C, X_4, X_39, ID="X(211)", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_5, X_141, 5, 141, incident=True)
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X(52)", classes=["center", "incident"])
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B + omega ) + c*sec(C + omega ))', ID="X(114)", classes=["center", "incident"])
    central_line(model, X_52, X_114, 52, 114, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X(184)", classes=["center", "incident"])
    central_line(model, X_32, X_184, 32, 184, incident=True)
    return promote_point_to_top(model, X_211)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(211) on the given reference triangle."""
    model = create_model('X(211) = X(4)-CEVA CONJUGATE OF X(39)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00211(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00211.json"))
    write_center_svg(
        model_acute,
        here / "x-00211.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
