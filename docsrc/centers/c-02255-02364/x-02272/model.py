"""GEOMETOR construction model for X_2272 = X_2-ISOCONJUGATE OF X_972."""

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


def construct_x_02272(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2272 = X_2-ISOCONJUGATE OF X_972 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    central_line(model, X_19, X_57, 19, 57)
    central_line(model, X_48, X_55, 48, 55)
    X_2272 = intersect_lines(model, X_19, X_57, X_48, X_55, ID="X_2272", classes=["selected", "target"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_71, X_165, 71, 165, incident=True)
    return promote_point_to_top(model, X_2272)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2272 on the given reference triangle."""
    model = create_model('X_2272 = X_2-ISOCONJUGATE OF X_972')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02272(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02272.json"))
    write_center_svg(
        model_acute,
        here / "x-02272.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
