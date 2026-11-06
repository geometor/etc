"""GEOMETOR construction model for X_3029 = INTERSECTION X_10X_115∩X_98X_573."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_03029(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3029 = INTERSECTION X_10X_115∩X_98X_573 on reference triangle ABC."""
    X_3029 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c)**(2)*(a**(3) + a**(2)*c - a*b**(2) - b**(3))*(a**(3) + a**(2)*b - a*c**(2) - c**(3)))', ID="X_3029", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    central_line(model, X_10, X_115, 10, 115, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_386 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_386", classes=["center", "incident"])
    central_line(model, X_99, X_386, 99, 386, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_573 = eval_trilinear_point(model, A, B, C, 'cos(A + U)', ID="X_573", classes=["center", "incident"])
    central_line(model, X_98, X_573, 98, 573, incident=True)
    return promote_point_to_top(model, X_3029)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3029 on the given reference triangle."""
    model = create_model('X_3029 = INTERSECTION X_10X_115∩X_98X_573')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03029(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03029.json"))
    write_center_svg(
        model_acute,
        here / "x-03029.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
