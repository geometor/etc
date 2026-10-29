"""GEOMETOR construction model for X(751) = ISOGONAL CONJUGATE OF X(750)."""

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


def construct_x_00751(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(751) = ISOGONAL CONJUGATE OF X(750) on reference triangle ABC."""
    X_750 = eval_trilinear_point(model, A, B, C, 'a**(2) + 2*b*c', ID="X(750)", classes=["center"])
    X_751 = isogonal_conjugate(model, A, B, C, X_750, ID="X(751)", classes=["selected", "target"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X(519)", classes=["center", "incident"])
    X_984 = eval_trilinear_point(model, A, B, C, 'b**(2) + b*c + c**(2)', ID="X(984)", classes=["center", "incident"])
    central_line(model, X_519, X_984, 519, 984, incident=True)
    return promote_point_to_top(model, X_751)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(751) on the given reference triangle."""
    model = create_model('X(751) = ISOGONAL CONJUGATE OF X(750)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00751(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00751.json"))
    write_center_svg(
        model_acute,
        here / "x-00751.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
