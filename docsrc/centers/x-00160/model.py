"""GEOMETOR construction model for X(160) = X(37)-OF-TANGENTIAL-TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00160(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(160) = X(37)-OF-TANGENTIAL-TRIANGLE on reference triangle ABC."""
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X(95)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_160 = ceva_conjugate(model, A, B, C, X_95, X_6, ID="X(160)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_66 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4))', ID="X(66)", classes=["center", "incident"])
    central_line(model, X_3, X_66, 3, 66, incident=True)
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X(237)", classes=["center", "incident"])
    central_line(model, X_6, X_237, 6, 237, incident=True)
    X_206 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(4) + c**(4) - a**(4))', ID="X(206)", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    central_line(model, X_206, X_57, 206, 57, incident=True)
    return promote_point_to_top(model, X_160)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(160) on the given reference triangle."""
    model = create_model('X(160) = X(37)-OF-TANGENTIAL-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00160(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00160.json"))
    write_center_svg(
        model_acute,
        here / "x-00160.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
