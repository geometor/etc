"""GEOMETOR construction model for X(842) = ISOGONAL CONJUGATE OF X(542)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00842(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(842) = ISOGONAL CONJUGATE OF X(542) on reference triangle ABC."""
    X_691 = eval_trilinear_point(model, A, B, C, 'a/((b**(2) - c**(2))*(2*a**(2) - b**(2) - c**(2)))', ID="X(691)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_842 = reflection_in_point(model, X_691, X_3, ID="X(842)", classes=["selected", "target"], guide=False)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_30, X_99, 30, 99, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(23)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_23, X_110, 23, 110, incident=True)
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X(112)", classes=["center", "incident"])
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X(186)", classes=["center", "incident"])
    central_line(model, X_112, X_186, 112, 186, incident=True)
    return promote_point_to_top(model, X_842)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(842) on the given reference triangle."""
    model = create_model('X(842) = ISOGONAL CONJUGATE OF X(542)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00842(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00842.json"))
    write_center_svg(
        model_acute,
        here / "x-00842.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
