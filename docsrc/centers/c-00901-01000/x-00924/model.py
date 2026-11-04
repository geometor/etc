"""GEOMETOR construction model for X_924 = CROSSDIFFERENCE OF X_5 AND X_6."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00924(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_924 = CROSSDIFFERENCE OF X_5 AND X_6 on reference triangle ABC."""
    X_924 = eval_trilinear_point(model, A, B, C, 'b*cos(A - B) - c*cos(A - C)', ID="X_924", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X_50", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X_647", classes=["center", "incident"])
    central_line(model, X_50, X_647, 50, 647, incident=True)
    X_66 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4))', ID="X_66", classes=["center", "incident"])
    X_879 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))/(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X_879", classes=["center", "incident"])
    central_line(model, X_66, X_879, 66, 879, incident=True)
    return promote_point_to_top(model, X_924)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_924 on the given reference triangle."""
    model = create_model('X_924 = CROSSDIFFERENCE OF X_5 AND X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00924(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00924.json"))
    write_center_svg(
        model_acute,
        here / "x-00924.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
