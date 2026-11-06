"""GEOMETOR construction model for X_3032 = INTERSECTION X_10X_11∩X_100X_386."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03032(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3032 = INTERSECTION X_10X_11∩X_100X_386 on reference triangle ABC."""
    X_3032 = eval_trilinear_point(model, A, B, C, '(b**(3) + b**(2)*c - b*a**(2) + a*b*c - a**(2)*c - a*c**(2))*(c**(3) + c**(2)*b - c*a**(2) + a*b*c - a**(2)*b - a*b**(2))', ID="X_3032", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_10, X_11, 10, 11, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_386 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_386", classes=["center", "incident"])
    central_line(model, X_100, X_386, 100, 386, incident=True)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_573 = eval_trilinear_point(model, A, B, C, 'cos(A + U)', ID="X_573", classes=["center", "incident"])
    central_line(model, X_104, X_573, 104, 573, incident=True)
    return promote_point_to_top(model, X_3032)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3032 on the given reference triangle."""
    model = create_model('X_3032 = INTERSECTION X_10X_11∩X_100X_386')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03032(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03032.json"))
    write_center_svg(
        model_acute,
        here / "x-03032.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
