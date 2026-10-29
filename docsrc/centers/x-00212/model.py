"""GEOMETOR construction model for X(212) = X(9)-CEVA CONJUGATE OF X(41)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00212(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(212) = X(9)-CEVA CONJUGATE OF X(41) on reference triangle ABC."""
    X_212 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(A))', ID="X(212)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    central_line(model, X_6, X_31, 6, 31, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    central_line(model, X_9, X_33, 9, 33, incident=True)
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    central_line(model, X_34, X_40, 34, 40, incident=True)
    return promote_point_to_top(model, X_212)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(212) on the given reference triangle."""
    model = create_model('X(212) = X(9)-CEVA CONJUGATE OF X(41)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00212(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00212.json"))
    write_center_svg(
        model_acute,
        here / "x-00212.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
