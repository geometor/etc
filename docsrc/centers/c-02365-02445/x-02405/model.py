"""GEOMETOR construction model for X_2405 = GIBERT-SIMSON TRANSFORM OF X_108."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02405(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2405 = GIBERT-SIMSON TRANSFORM OF X_108 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center"])
    X_653 = eval_trilinear_point(model, A, B, C, '1/(sec(B) - sec(C))', ID="X_653", classes=["center"])
    X_934 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(b + c - a)**(2))', ID="X_934", classes=["center"])
    central_line(model, X_2, X_92, 2, 92)
    central_line(model, X_653, X_934, 653, 934)
    X_2405 = intersect_lines(model, X_2, X_92, X_653, X_934, ID="X_2405", classes=["selected", "target"])
    return promote_point_to_top(model, X_2405)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2405 on the given reference triangle."""
    model = create_model('X_2405 = GIBERT-SIMSON TRANSFORM OF X_108')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02405(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02405.json"))
    write_center_svg(
        model_acute,
        here / "x-02405.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
