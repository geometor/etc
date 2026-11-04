"""GEOMETOR construction model for X_1988 = 2nd LEMOINE ANTIPARALLELS POINT."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01988(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1988 = 2nd LEMOINE ANTIPARALLELS POINT on reference triangle ABC."""
    X_1988 = eval_trilinear_point(model, A, B, C, '((sin(A))/(csc(2*B) + csc(2*C) - csc(2*A)))', ID="X_1988", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_436 = eval_barycentric_point(model, A, B, C, '(a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2)) * (a**(8) - 2*a**(6)*b**(2) + a**(4)*b**(4) - 2*a**(6)*c**(2) + 3*a**(4)*b**(2)*c**(2) - b**(6)*c**(2) + a**(4)*c**(4) + 2*b**(4)*c**(4) - b**(2)*c**(6))', ID="X_436", classes=["center", "incident"])
    central_line(model, X_6, X_436, 6, 436, incident=True)
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    X_401 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*sin(2*C) - (sin(2*A))**(2))*(csc(A))', ID="X_401", classes=["center", "incident"])
    central_line(model, X_394, X_401, 394, 401, incident=True)
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    X_1968 = eval_trilinear_point(model, A, B, C, 'a*((tan(A))**(2) + tan(B)*tan(C))', ID="X_1968", classes=["center", "incident"])
    central_line(model, X_184, X_1968, 184, 1968, incident=True)
    return promote_point_to_top(model, X_1988)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1988 on the given reference triangle."""
    model = create_model('X_1988 = 2nd LEMOINE ANTIPARALLELS POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01988(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01988.json"))
    write_center_svg(
        model_acute,
        here / "x-01988.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
