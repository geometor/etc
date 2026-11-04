"""GEOMETOR construction model for X_1485 = PERSPECTOR OF ABC AND TANGENTIAL-OF-TANGENTIAL TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01485(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1485 = PERSPECTOR OF ABC AND TANGENTIAL-OF-TANGENTIAL TRIANGLE on reference triangle ABC."""
    X_1485 = eval_trilinear_point(model, A, B, C, '(a/(b**(3)*cos(B) + c**(3)*cos(C) - a**(3)*cos(A)))', ID="X_1485", classes=["selected", "target"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_160 = eval_trilinear_point(model, A, B, C, '(a*((b**(2) + c**(2))*sin(2*A) + (c**(2) - a**(2))*sin(2*B) + (b**(2) - a**(2))*sin(2*C)))', ID="X_160", classes=["center", "incident"])
    central_line(model, X_22, X_160, 22, 160, incident=True)
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_26", classes=["center", "incident"])
    X_206 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(4) + c**(4) - a**(4))', ID="X_206", classes=["center", "incident"])
    central_line(model, X_26, X_206, 26, 206, incident=True)
    X_157 = eval_trilinear_point(model, A, B, C, '(a*(b**(3)*cos(B) + c**(3)*cos(C) - a**(3)*cos(A)))', ID="X_157", classes=["center", "incident"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center", "incident"])
    central_line(model, X_157, X_264, 157, 264, incident=True)
    return promote_point_to_top(model, X_1485)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1485 on the given reference triangle."""
    model = create_model('X_1485 = PERSPECTOR OF ABC AND TANGENTIAL-OF-TANGENTIAL TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01485(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01485.json"))
    write_center_svg(
        model_acute,
        here / "x-01485.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
