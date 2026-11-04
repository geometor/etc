"""GEOMETOR construction model for X_1634 = TCC-PERSPECTOR OF X_662."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01634(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1634 = TCC-PERSPECTOR OF X_662 on reference triangle ABC."""
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center"])
    X_1634 = crosspoint(model, A, B, C, X_99, X_110, ID="X_1634", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_67", classes=["center", "incident"])
    central_line(model, X_3, X_67, 3, 67, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_160 = eval_trilinear_point(model, A, B, C, '(a*((b**(2) + c**(2))*sin(2*A) + (c**(2) - a**(2))*sin(2*B) + (b**(2) - a**(2))*sin(2*C)))', ID="X_160", classes=["center", "incident"])
    central_line(model, X_69, X_160, 69, 160, incident=True)
    X_351 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(2) + c**(2) - 2*a**(2)))', ID="X_351", classes=["center", "incident"])
    central_line(model, X_110, X_351, 110, 351, incident=True)
    return promote_point_to_top(model, X_1634)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1634 on the given reference triangle."""
    model = create_model('X_1634 = TCC-PERSPECTOR OF X_662')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01634(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01634.json"))
    write_center_svg(
        model_acute,
        here / "x-01634.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
