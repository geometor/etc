"""GEOMETOR construction model for X_2259 = X_2-ISOCONJUGATE OF X_942."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02259(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2259 = X_2-ISOCONJUGATE OF X_942 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    central_line(model, X_19, X_41, 19, 41)
    central_line(model, X_48, X_57, 48, 57)
    X_2259 = intersect_lines(model, X_19, X_41, X_48, X_57, ID="X_2259", classes=["selected", "target"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    central_line(model, X_35, X_71, 35, 71, incident=True)
    return promote_point_to_top(model, X_2259)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2259 on the given reference triangle."""
    model = create_model('X_2259 = X_2-ISOCONJUGATE OF X_942')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02259(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02259.json"))
    write_center_svg(
        model_acute,
        here / "x-02259.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
