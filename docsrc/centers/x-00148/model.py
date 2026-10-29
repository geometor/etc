"""GEOMETOR construction model for X(148) = STEINER POINT OF ANTICOMPLEMENTARY TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00148(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(148) = STEINER POINT OF ANTICOMPLEMENTARY TRIANGLE on reference triangle ABC."""
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center"])
    X_148 = anticomplement(model, A, B, C, X_99, ID="X(148)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_2, X_99, 2, 99, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    central_line(model, X_20, X_98, 20, 98, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_147 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(8) + (b**(2) + c**(2))*a**(6) - (2*b**(4) + 3*b**(2)*c**(2) + 2*c**(4))*a**(4) + (b**(6) + b**(4)*c**(2) + b**(2)*c**(4) + c**(6))*a**(2) - b**(8) + b**(6)*c**(2) + b**(2)*c**(6) - c**(8))', ID="X(147)", classes=["center", "incident"])
    central_line(model, X_4, X_147, 4, 147, incident=True)
    return promote_point_to_top(model, X_148)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(148) on the given reference triangle."""
    model = create_model('X(148) = STEINER POINT OF ANTICOMPLEMENTARY TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00148(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00148.json"))
    write_center_svg(
        model_acute,
        here / "x-00148.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
