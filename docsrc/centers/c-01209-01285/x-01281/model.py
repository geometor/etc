"""GEOMETOR construction model for X_1281 = 3rd SHARYGIN POINT."""

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


def construct_x_01281(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1281 = 3rd SHARYGIN POINT on reference triangle ABC."""
    X_1281 = eval_trilinear_point(model, A, B, C, '(b*c*(a**(2) - b*c)*(b**(3) + c**(3) - a**(3) - a*b*c))', ID="X_1281", classes=["selected", "target"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    central_line(model, X_21, X_99, 21, 99, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X_98", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_98, X_100, 98, 100, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_147 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(8) + (b**(2) + c**(2))*a**(6) - (2*b**(4) + 3*b**(2)*c**(2) + 2*c**(4))*a**(4) + (b**(6) + b**(4)*c**(2) + b**(2)*c**(4) + c**(6))*a**(2) - b**(8) + b**(6)*c**(2) + b**(2)*c**(6) - c**(8))', ID="X_147", classes=["center", "incident"])
    central_line(model, X_63, X_147, 63, 147, incident=True)
    return promote_point_to_top(model, X_1281)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1281 on the given reference triangle."""
    model = create_model('X_1281 = 3rd SHARYGIN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01281(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01281.json"))
    write_center_svg(
        model_acute,
        here / "x-01281.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
