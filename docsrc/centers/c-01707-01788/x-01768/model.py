"""GEOMETOR construction model for X_1768 = MIMOSA TRANSFORM OF X_521."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01768(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1768 = MIMOSA TRANSFORM OF X_521 on reference triangle ABC."""
    X_1768 = eval_trilinear_point(model, A, B, C, 'a**(5) - a**(4)*(b + c) - a**(3)*(2*b**(2) - 5*b*c + 2*c**(2)) + 2*a**(2)*(b - c)**(2)*(b + c) + a*(b - c)**(2)*(b**(2) - b*c + c**(2)) - b**(5) + b**(4)*c + b*c**(4) - c**(5)', ID="X_1768", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_11, X_57, 11, 57, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_1, X_104, 1, 104, incident=True)
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_46, X_80, 46, 80, incident=True)
    return promote_point_to_top(model, X_1768)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1768 on the given reference triangle."""
    model = create_model('X_1768 = MIMOSA TRANSFORM OF X_521')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01768(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01768.json"))
    write_center_svg(
        model_acute,
        here / "x-01768.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
