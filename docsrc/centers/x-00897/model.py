"""GEOMETOR construction model for X(897) = ISOGONAL CONJUGATE OF X(896)."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00897(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(897) = ISOGONAL CONJUGATE OF X(896) on reference triangle ABC."""
    X_896 = eval_trilinear_point(model, A, B, C, '2*a**(2) - b**(2) - c**(2)', ID="X(896)", classes=["center"])
    X_897 = isogonal_conjugate(model, A, B, C, X_896, ID="X(897)", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    central_line(model, X_37, X_100, 37, 100, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X(162)", classes=["center", "incident"])
    central_line(model, X_19, X_162, 19, 162, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    central_line(model, X_10, X_190, 10, 190, incident=True)
    return promote_point_to_top(model, X_897)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(897) on the given reference triangle."""
    model = create_model('X(897) = ISOGONAL CONJUGATE OF X(896)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00897(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00897.json"))
    write_center_svg(
        model_acute,
        here / "x-00897.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
