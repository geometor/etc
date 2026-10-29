"""GEOMETOR construction model for X(91) = ISOGONAL CONJUGATE OF X(47)."""

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


def construct_x_00091(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(91) = ISOGONAL CONJUGATE OF X(47) on reference triangle ABC."""
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center"])
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X(68)", classes=["center"])
    central_line(model, X_65, X_68, 65, 68)
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X(47)", classes=["center"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center"])
    central_line(model, X_47, X_92, 47, 92)
    X_91 = isogonal_conjugate(model, A, B, C, X_47, ID="X(91)", classes=["selected", "target"])
    return promote_point_to_top(model, X_91)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(91) on the given reference triangle."""
    model = create_model('X(91) = ISOGONAL CONJUGATE OF X(47)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00091(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00091.json"))
    write_center_svg(
        model_acute,
        here / "x-00091.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
