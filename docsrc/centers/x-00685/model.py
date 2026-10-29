"""GEOMETOR construction model for X(685) = TRILINEAR POLE OF LINE X(4)X(98)."""

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


def construct_x_00685(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(685) = TRILINEAR POLE OF LINE X(4)X(98) on reference triangle ABC."""
    X_684 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a**(2))*(b**(2) - c**(2))*(a**(2)*b**(2) + a**(2)*c**(2) - b**(4) - c**(4))', ID="X(684)", classes=["center"])
    X_685 = isogonal_conjugate(model, A, B, C, X_684, ID="X(685)", classes=["selected", "target"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    X_468 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cot(B) + cot(C) - 2*cot(A))', ID="X(468)", classes=["center", "incident"])
    central_line(model, X_98, X_468, 98, 468, incident=True)
    X_287 = eval_trilinear_point(model, A, B, C, 'cot(A)*sec(A + omega )', ID="X(287)", classes=["center", "incident"])
    X_297 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*cos(A + omega )', ID="X(297)", classes=["center", "incident"])
    central_line(model, X_287, X_297, 287, 297, incident=True)
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X(250)", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X(523)", classes=["center", "incident"])
    central_line(model, X_250, X_523, 250, 523, incident=True)
    return promote_point_to_top(model, X_685)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(685) on the given reference triangle."""
    model = create_model('X(685) = TRILINEAR POLE OF LINE X(4)X(98)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00685(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00685.json"))
    write_center_svg(
        model_acute,
        here / "x-00685.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
