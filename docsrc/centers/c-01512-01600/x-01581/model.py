"""GEOMETOR construction model for X_1581 = ISOGONAL CONJUGATE OF X_1580."""

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


def construct_x_01581(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1581 = ISOGONAL CONJUGATE OF X_1580 on reference triangle ABC."""
    X_1580 = eval_trilinear_point(model, A, B, C, 'a**(4) - b**(2)*c**(2)', ID="X_1580", classes=["center"])
    X_1581 = isogonal_conjugate(model, A, B, C, X_1580, ID="X_1581", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_257 = eval_trilinear_point(model, A, B, C, '1/(a**(3) + a*b*c)', ID="X_257", classes=["center", "incident"])
    central_line(model, X_10, X_257, 10, 257, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center", "incident"])
    central_line(model, X_37, X_256, 37, 256, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X_291", classes=["center", "incident"])
    central_line(model, X_65, X_291, 65, 291, incident=True)
    return promote_point_to_top(model, X_1581)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1581 on the given reference triangle."""
    model = create_model('X_1581 = ISOGONAL CONJUGATE OF X_1580')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01581(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01581.json"))
    write_center_svg(
        model_acute,
        here / "x-01581.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
