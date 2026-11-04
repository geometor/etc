"""GEOMETOR construction model for X_2866 = SM(X_105, X_109)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02866(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2866 = SM(X_105, X_109) on reference triangle ABC."""
    X_312 = eval_trilinear_point(model, A, B, C, '(b + c - a)*b**(2)*c**(2)', ID="X_312", classes=["center"])
    X_919 = point_from_barycentrics(model, A, B, C, -0.11560694, 0.83236994, 0.28323699, ID="X_919", classes=["center"])
    X_561 = eval_trilinear_point(model, A, B, C, 'a **(- 4)', ID="X_561", classes=["center"])
    X_927 = point_from_barycentrics(model, A, B, C, -0.12244898, 0.81632653, 0.30612245, ID="X_927", classes=["center"])
    central_line(model, X_312, X_919, 312, 919)
    central_line(model, X_561, X_927, 561, 927)
    X_2866 = intersect_lines(model, X_312, X_919, X_561, X_927, ID="X_2866", classes=["selected", "target"])
    return promote_point_to_top(model, X_2866)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2866 on the given reference triangle."""
    model = create_model('X_2866 = SM(X_105, X_109)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02866(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02866.json"))
    write_center_svg(
        model_acute,
        here / "x-02866.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
