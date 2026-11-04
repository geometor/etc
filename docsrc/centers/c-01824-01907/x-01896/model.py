"""GEOMETOR construction model for X_1896 = ZOSMA TRANSFORM OF X_1047."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01896(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1896 = ZOSMA TRANSFORM OF X_1047 on reference triangle ABC."""
    X_1896 = eval_trilinear_point(model, A, B, C, '(sec(A))/(sec(B) + sec(C))', ID="X_1896", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    central_line(model, X_1, X_29, 1, 29, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_4, X_51, 4, 51, incident=True)
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center", "incident"])
    central_line(model, X_27, X_84, 27, 84, incident=True)
    return promote_point_to_top(model, X_1896)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1896 on the given reference triangle."""
    model = create_model('X_1896 = ZOSMA TRANSFORM OF X_1047')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01896(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01896.json"))
    write_center_svg(
        model_acute,
        here / "x-01896.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
