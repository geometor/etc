"""GEOMETOR construction model for X_2954 = EXCENTRAL-ISOGONAL CONJUGATE OF X_71."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02954(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2954 = EXCENTRAL-ISOGONAL CONJUGATE OF X_71 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_201 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(B - C))', ID="X_201", classes=["center"])
    central_line(model, X_19, X_165, 19, 165)
    central_line(model, X_1, X_201, 1, 201)
    X_2954 = intersect_lines(model, X_19, X_165, X_1, X_201, ID="X_2954", classes=["selected", "target"])
    X_228 = eval_trilinear_point(model, A, B, C, '(sin(2*A))*(sin(B) + sin(C))', ID="X_228", classes=["center", "incident"])
    X_1282 = point_from_barycentrics(model, A, B, C, 0.61507937, -0.97619048, 1.3611111, ID="X_1282", classes=["center", "incident"])
    central_line(model, X_228, X_1282, 228, 1282, incident=True)
    return promote_point_to_top(model, X_2954)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2954 on the given reference triangle."""
    model = create_model('X_2954 = EXCENTRAL-ISOGONAL CONJUGATE OF X_71')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02954(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02954.json"))
    write_center_svg(
        model_acute,
        here / "x-02954.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
