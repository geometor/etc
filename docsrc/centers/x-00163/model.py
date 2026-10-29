"""GEOMETOR construction model for X(163) = TRILINEAR PRODUCT X(6)*X(110)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00163(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(163) = TRILINEAR PRODUCT X(6)*X(110) on reference triangle ABC."""
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X(163)", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_101, X_110, 101, 110, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X(112)", classes=["center", "incident"])
    central_line(model, X_109, X_112, 109, 112, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_293 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(A + omega )', ID="X(293)", classes=["center", "incident"])
    central_line(model, X_1, X_293, 1, 293, incident=True)
    return promote_point_to_top(model, X_163)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(163) on the given reference triangle."""
    model = create_model('X(163) = TRILINEAR PRODUCT X(6)*X(110)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00163(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00163.json"))
    write_center_svg(
        model_acute,
        here / "x-00163.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
