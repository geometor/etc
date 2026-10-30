"""GEOMETOR construction model for X(217) = X(6)-CEVA CONJUGATE OF X(51)."""

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
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00217(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(217) = X(6)-CEVA CONJUGATE OF X(51) on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X(112)", classes=["center"])
    central_line(model, X_4, X_6, 4, 6)
    central_line(model, X_54, X_112, 54, 112)
    X_217 = intersect_lines(model, X_4, X_6, X_54, X_112, ID="X(217)", classes=["selected", "target"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X(184)", classes=["center", "incident"])
    central_line(model, X_32, X_184, 32, 184, incident=True)
    return promote_point_to_top(model, X_217)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(217) on the given reference triangle."""
    model = create_model('X(217) = X(6)-CEVA CONJUGATE OF X(51)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00217(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00217.json"))
    write_center_svg(
        model_acute,
        here / "x-00217.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
