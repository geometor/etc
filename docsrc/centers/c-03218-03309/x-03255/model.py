"""GEOMETOR construction model for X_3255 = INTERSECTION OF X_104X_551 AND X_390X_1392."""

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


def construct_x_03255(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3255 = INTERSECTION OF X_104X_551 AND X_390X_1392 on reference triangle ABC."""
    X_3255 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)/(b*c + (b + c - a)**(2)))', ID="X_3255", classes=["selected", "target"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    X_551 = eval_trilinear_point(model, A, B, C, '(4*a + b + c)/a', ID="X_551", classes=["center", "incident"])
    central_line(model, X_105, X_551, 105, 551, incident=True)
    X_758 = eval_trilinear_point(model, A, B, C, 'a**(0)*(b**(3) + c**(3)) - a**(2)*(b**(1) + c**(1))', ID="X_758", classes=["center", "incident"])
    X_1000 = eval_trilinear_point(model, A, B, C, '1/(a*(a**(2) + 4*b*c - b**(2) - c**(2)))', ID="X_1000", classes=["center", "incident"])
    central_line(model, X_758, X_1000, 758, 1000, incident=True)
    X_390 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)*(3*a**(2) + (b - c)**(2))', ID="X_390", classes=["center", "incident"])
    X_1392 = eval_trilinear_point(model, A, B, C, '((a - b -c)/(3*a - 2*b - 2*c))', ID="X_1392", classes=["center", "incident"])
    central_line(model, X_390, X_1392, 390, 1392, incident=True)
    return promote_point_to_top(model, X_3255)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3255 on the given reference triangle."""
    model = create_model('X_3255 = INTERSECTION OF X_104X_551 AND X_390X_1392')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03255(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03255.json"))
    write_center_svg(
        model_acute,
        here / "x-03255.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
