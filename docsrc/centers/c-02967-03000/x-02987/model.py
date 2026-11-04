"""GEOMETOR construction model for X_2987 = DC(X_98)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02987(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2987 = DC(X_98) on reference triangle ABC."""
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center"])
    X_2987 = isogonal_conjugate(model, A, B, C, X_230, ID="X_2987", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_25, X_110, 25, 110, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_323 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*(csc(A))**(2)', ID="X_323", classes=["center", "incident"])
    central_line(model, X_111, X_323, 111, 323, incident=True)
    X_193 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cot(B) + cot(C) - cot(A))', ID="X_193", classes=["center", "incident"])
    X_317 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)*(csc(A))**(2)', ID="X_317", classes=["center", "incident"])
    central_line(model, X_193, X_317, 193, 317, incident=True)
    return promote_point_to_top(model, X_2987)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2987 on the given reference triangle."""
    model = create_model('X_2987 = DC(X_98)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02987(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02987.json"))
    write_center_svg(
        model_acute,
        here / "x-02987.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
