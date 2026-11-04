"""GEOMETOR construction model for X_1961 = CROSSSUM OF PU(31)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01961(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1961 = CROSSSUM OF PU(31) on reference triangle ABC."""
    X_846 = eval_trilinear_point(model, A, B, C, '(- a**(2) + b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_846", classes=["center"])
    X_1051 = eval_trilinear_point(model, A, B, C, '(3*a**(2) + b**(2) + c**(2) + b*c + 5*a*b + 5*a*c)', ID="X_1051", classes=["center"])
    X_1961 = cevapoint(model, A, B, C, X_846, X_1051, ID="X_1961", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    central_line(model, X_37, X_171, 37, 171, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_199 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) - a**(4) + (b**(2) + c**(2) - a**(2))*(b*c + c*a + a*b)))', ID="X_199", classes=["center", "incident"])
    central_line(model, X_35, X_199, 35, 199, incident=True)
    return promote_point_to_top(model, X_1961)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1961 on the given reference triangle."""
    model = create_model('X_1961 = CROSSSUM OF PU(31)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01961(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01961.json"))
    write_center_svg(
        model_acute,
        here / "x-01961.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
