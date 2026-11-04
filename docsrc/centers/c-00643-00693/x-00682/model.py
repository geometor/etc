"""GEOMETOR construction model for X_682 = POINT ARNEB."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00682(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_682 = POINT ARNEB on reference triangle ABC."""
    X_682 = eval_trilinear_point(model, A, B, C, '(sec(B)*(csc(C))**(3) + sec(C)*(csc(B))**(3))', ID="X_682", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_3, X_69, 3, 69, incident=True)
    X_154 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(B)*cos(C))*a**(2)', ID="X_154", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X_237", classes=["center", "incident"])
    central_line(model, X_154, X_237, 154, 237, incident=True)
    X_248 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*sec(A + omega )', ID="X_248", classes=["center", "incident"])
    X_695 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) + b**(2)*c**(2))', ID="X_695", classes=["center", "incident"])
    central_line(model, X_248, X_695, 248, 695, incident=True)
    return promote_point_to_top(model, X_682)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_682 on the given reference triangle."""
    model = create_model('X_682 = POINT ARNEB')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00682(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00682.json"))
    write_center_svg(
        model_acute,
        here / "x-00682.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
