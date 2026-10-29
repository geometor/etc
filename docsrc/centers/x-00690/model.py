"""GEOMETOR construction model for X(690) = CROSSDIFFERENCE OF LINE X(6) AND X(110)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00690(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(690) = CROSSDIFFERENCE OF LINE X(6) AND X(110) on reference triangle ABC."""
    X_690 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))*(2*a**(2) - b**(2) - c**(2))', ID="X(690)", classes=["selected", "target"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    central_line(model, X_74, X_98, 74, 98, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_99, X_110, 99, 110, incident=True)
    X_113 = eval_trilinear_point(model, A, B, C, 'sin(B)*sin(C)*((sin(C))/(cos(C) - 2*cos(A)*cos(B)) + (sin(B))/(cos(B) - 2*cos(A)*cos(C)))', ID="X(113)", classes=["center", "incident"])
    X_114 = point_from_barycentrics(model, A, B, C, 0.37082211, -0.060960354, 0.69013825, ID="X(114)", classes=["center", "incident"])
    central_line(model, X_113, X_114, 113, 114, incident=True)
    return promote_point_to_top(model, X_690)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(690) on the given reference triangle."""
    model = create_model('X(690) = CROSSDIFFERENCE OF LINE X(6) AND X(110)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00690(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00690.json"))
    write_center_svg(
        model_acute,
        here / "x-00690.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
