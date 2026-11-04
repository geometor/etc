"""GEOMETOR construction model for X_209 = X_4-CEVA CONJUGATE OF X_37."""

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
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00209(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_209 = X_4-CEVA CONJUGATE OF X_37 on reference triangle ABC."""
    X_209 = eval_trilinear_point(model, A, B, C, '((sin(B) + sin(C))*(sin(A) + sin(A - B) + sin(A - C)))', ID="X_209", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    central_line(model, X_10, X_12, 10, 12, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_6, X_31, 6, 31, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_44, X_51, 44, 51, incident=True)
    return promote_point_to_top(model, X_209)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_209 on the given reference triangle."""
    model = create_model('X_209 = X_4-CEVA CONJUGATE OF X_37')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00209(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00209.json"))
    write_center_svg(
        model_acute,
        here / "x-00209.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
