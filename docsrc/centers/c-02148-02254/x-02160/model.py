"""GEOMETOR construction model for X_2160 = X_2-ISOCONJUGATE OF X_35."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_02160(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2160 = X_2-ISOCONJUGATE OF X_35 on reference triangle ABC."""
    X_2160 = eval_trilinear_point(model, A, B, C, '(sin(A))/(1 + 2*cos(A))', ID="X_2160", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_9, X_46, 9, 46, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_199 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) - a**(4) + (b**(2) + c**(2) - a**(2))*(b*c + c*a + a*b)))', ID="X_199", classes=["center", "incident"])
    central_line(model, X_55, X_199, 55, 199, incident=True)
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    X_501 = eval_trilinear_point(model, A, B, C, '(a*(a**(3) - b**(3) - c**(3) - b*c*(a + b + c) + a*b*(a - b) + a*c*(a - c))/(b + c))', ID="X_501", classes=["center", "incident"])
    central_line(model, X_284, X_501, 284, 501, incident=True)
    return promote_point_to_top(model, X_2160)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2160 on the given reference triangle."""
    model = create_model('X_2160 = X_2-ISOCONJUGATE OF X_35')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02160(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02160.json"))
    write_center_svg(
        model_acute,
        here / "x-02160.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
