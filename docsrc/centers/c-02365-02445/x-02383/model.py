"""GEOMETOR construction model for X_2383 = CIR(X_539)."""

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
    isogonal_conjugate,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02383(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2383 = CIR(X_539) on reference triangle ABC."""
    X_539 = eval_barycentric_point(model, A, B, C, '(a**(2) - b**(2) - c**(2))*(2*a**(8) - 4*a**(6)*(b**(2) + c**(2)) + 3*a**(4)*(b**(4) + c**(4)) - 2*a**(2)*(b**(2) - c**(2))**(2)*(b**(2) + c**(2)) + (b**(2) - c**(2))**(4))', ID="X_539", classes=["center"])
    X_2383 = isogonal_conjugate(model, A, B, C, X_539, ID="X_2383", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_128 = eval_trilinear_point(model, A, B, C, '((sec(A))*(cos(2*B) + cos(2*C))*(1 + 2*cos(2*A))*(cos(2*A) + 2*cos(2*B)*cos(2*C)))', ID="X_128", classes=["center", "incident"])
    central_line(model, X_4, X_128, 4, 128, incident=True)
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_52, X_110, 52, 110, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_925 = eval_trilinear_point(model, A, B, C, '(sin(A))/(sec(2*B) - sec(2*C))', ID="X_925", classes=["center", "incident"])
    central_line(model, X_5, X_925, 5, 925, incident=True)
    return promote_point_to_top(model, X_2383)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2383 on the given reference triangle."""
    model = create_model('X_2383 = CIR(X_539)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02383(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02383.json"))
    write_center_svg(
        model_acute,
        here / "x-02383.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
