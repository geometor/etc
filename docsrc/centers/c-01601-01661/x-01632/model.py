"""GEOMETOR construction model for X_1632 = TCC-PERSPECTOR OF X_648."""

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
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01632(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1632 = TCC-PERSPECTOR OF X_648 on reference triangle ABC."""
    X_648 = eval_trilinear_point(model, A, B, C, '1/(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2)))', ID="X_648", classes=["center"])
    X_1576 = eval_trilinear_point(model, A, B, C, 'a**(3)/(b**(2) - c**(2))', ID="X_1576", classes=["center"])
    X_1632 = reflection_in_point(model, X_648, X_1576, ID="X_1632", classes=["selected", "target"], guide=False)
    X_157 = eval_trilinear_point(model, A, B, C, '(a*(b**(3)*cos(B) + c**(3)*cos(C) - a**(3)*cos(A)))', ID="X_157", classes=["center", "incident"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center", "incident"])
    central_line(model, X_157, X_264, 157, 264, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X_98", classes=["center", "incident"])
    X_338 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)/a**(3)', ID="X_338", classes=["center", "incident"])
    central_line(model, X_98, X_338, 98, 338, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_670 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(2) - c**(2)))', ID="X_670", classes=["center", "incident"])
    central_line(model, X_99, X_670, 99, 670, incident=True)
    return promote_point_to_top(model, X_1632)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1632 on the given reference triangle."""
    model = create_model('X_1632 = TCC-PERSPECTOR OF X_648')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01632(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01632.json"))
    write_center_svg(
        model_acute,
        here / "x-01632.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
