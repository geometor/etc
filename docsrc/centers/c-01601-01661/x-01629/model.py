"""GEOMETOR construction model for X_1629 = TCC-PERSPECTOR OF X_275."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_01629(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1629 = TCC-PERSPECTOR OF X_275 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X_98", classes=["center"])
    central_line(model, X_4, X_54, 4, 54)
    central_line(model, X_25, X_98, 25, 98)
    X_1629 = intersect_lines(model, X_4, X_54, X_25, X_98, ID="X_1629", classes=["selected", "target"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center", "incident"])
    central_line(model, X_22, X_264, 22, 264, incident=True)
    return promote_point_to_top(model, X_1629)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1629 on the given reference triangle."""
    model = create_model('X_1629 = TCC-PERSPECTOR OF X_275')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01629(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01629.json"))
    write_center_svg(
        model_acute,
        here / "x-01629.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
