"""GEOMETOR construction model for X(207) = X(1)-CEVA CONJUGATE OF X(34)."""

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


def construct_x_00207(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(207) = X(1)-CEVA CONJUGATE OF X(34) on reference triangle ABC."""
    X_207 = eval_trilinear_point(model, A, B, C, '(1 - sec(A))*(sec(B) + sec(C) - sec(A) - 1)', ID="X(207)", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    central_line(model, X_19, X_56, 19, 56, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X(64)", classes=["center", "incident"])
    central_line(model, X_33, X_64, 33, 64, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X(108)", classes=["center", "incident"])
    central_line(model, X_40, X_108, 40, 108, incident=True)
    return promote_point_to_top(model, X_207)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(207) on the given reference triangle."""
    model = create_model('X(207) = X(1)-CEVA CONJUGATE OF X(34)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00207(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00207.json"))
    write_center_svg(
        model_acute,
        here / "x-00207.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
