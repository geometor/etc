"""GEOMETOR construction model for X_1973 = TRILINEAR PRODUCT OF PU(39)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01973(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1973 = TRILINEAR PRODUCT OF PU(39) on reference triangle ABC."""
    X_304 = eval_trilinear_point(model, A, B, C, '(cot(A))*(csc(A))**(2)', ID="X_304", classes=["center"])
    X_1973 = isogonal_conjugate(model, A, B, C, X_304, ID="X_1973", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_1, X_19, 1, 19, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_25, X_41, 25, 41, incident=True)
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    central_line(model, X_47, X_163, 47, 163, incident=True)
    return promote_point_to_top(model, X_1973)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1973 on the given reference triangle."""
    model = create_model('X_1973 = TRILINEAR PRODUCT OF PU(39)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01973(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01973.json"))
    write_center_svg(
        model_acute,
        here / "x-01973.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
