"""GEOMETOR construction model for X(652) = CROSSDIFFERENCE OF X(1) AND X(4)."""

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


def construct_x_00652(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(652) = CROSSDIFFERENCE OF X(1) AND X(4) on reference triangle ABC."""
    X_652 = eval_trilinear_point(model, A, B, C, 'sec(B) - sec(C)', ID="X(652)", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_243 = eval_barycentric_point(model, A, B, C, '(a - b - c)*(a**(4) - a**(2)*(b**(2) - b*c + c**(2)) - b*c*(b - c)**(2))/(a**(2) - b**(2) - c**(2))', ID="X(243)", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X(522)", classes=["center", "incident"])
    central_line(model, X_243, X_522, 243, 522, incident=True)
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X(520)", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X(647)", classes=["center", "incident"])
    central_line(model, X_520, X_647, 520, 647, incident=True)
    return promote_point_to_top(model, X_652)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(652) on the given reference triangle."""
    model = create_model('X(652) = CROSSDIFFERENCE OF X(1) AND X(4)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00652(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00652.json"))
    write_center_svg(
        model_acute,
        here / "x-00652.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
