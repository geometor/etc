"""GEOMETOR construction model for X_1612 = TCC-PERSPECTOR OF X_28."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01612(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1612 = TCC-PERSPECTOR OF X_28 on reference triangle ABC."""
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center"])
    X_765 = eval_trilinear_point(model, A, B, C, '(b - c) **(-2)', ID="X_765", classes=["center"])
    X_1612 = crosspoint(model, A, B, C, X_107, X_765, ID="X_1612", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_387 = eval_trilinear_point(model, A, B, C, 'b*c*(-a**(4) + 2*a**(2)*(a + b + c)**(2) + (b**(2) - c**(2))**(2))', ID="X_387", classes=["center", "incident"])
    central_line(model, X_55, X_387, 55, 387, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_943 = eval_trilinear_point(model, A, B, C, '(1/(2*a*b*c + (b + c)*(a - b + c)*(a + b - c)))', ID="X_943", classes=["center", "incident"])
    central_line(model, X_6, X_943, 6, 943, incident=True)
    return promote_point_to_top(model, X_1612)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1612 on the given reference triangle."""
    model = create_model('X_1612 = TCC-PERSPECTOR OF X_28')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01612(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01612.json"))
    write_center_svg(
        model_acute,
        here / "x-01612.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
