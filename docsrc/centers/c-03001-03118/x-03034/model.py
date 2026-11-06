"""GEOMETOR construction model for X_3034 = INTERSECTION X_10X_116∩X_105X_386."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03034(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3034 = INTERSECTION X_10X_116∩X_105X_386 on reference triangle ABC."""
    X_3034 = eval_trilinear_point(model, A, B, C, '(b**(3) - b**(2)*c + b*a**(2) - a*b*c + a**(2)*c - a*c**(2))*(c**(3) - c**(2)*b + c*a**(2) - a*b*c + a**(2)*b - a*b**(2))', ID="X_3034", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X_116", classes=["center", "incident"])
    central_line(model, X_10, X_116, 10, 116, incident=True)
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    X_386 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_386", classes=["center", "incident"])
    central_line(model, X_105, X_386, 105, 386, incident=True)
    X_528 = point_from_barycentrics(model, A, B, C, -0.26726124, 0.80178373, -0.53452248, ID="X_528", classes=["center", "incident"])
    X_3032 = eval_trilinear_point(model, A, B, C, '(b**(3) + b**(2)*c - b*a**(2) + a*b*c - a**(2)*c - a*c**(2))*(c**(3) + c**(2)*b - c*a**(2) + a*b*c - a**(2)*b - a*b**(2))', ID="X_3032", classes=["center", "incident"])
    central_line(model, X_528, X_3032, 528, 3032, incident=True)
    return promote_point_to_top(model, X_3034)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3034 on the given reference triangle."""
    model = create_model('X_3034 = INTERSECTION X_10X_116∩X_105X_386')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03034(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03034.json"))
    write_center_svg(
        model_acute,
        here / "x-03034.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
