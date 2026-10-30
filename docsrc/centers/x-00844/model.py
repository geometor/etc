"""GEOMETOR construction model for X(844) = INTERSECTION OF LINES X(166)X(167) AND X(173)X(503)."""

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


def construct_x_00844(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(844) = INTERSECTION OF LINES X(166)X(167) AND X(173)X(503) on reference triangle ABC."""
    X_166 = point_from_barycentrics(model, A, B, C, 0.22766017, 0.3221551, 0.45018473, ID="X(166)", classes=["center"])
    X_167 = point_from_barycentrics(model, A, B, C, 0.58849841, 0.49152493, -0.080023337, ID="X(167)", classes=["center"])
    X_173 = eval_trilinear_point(model, A, B, C, 'cos(B/2) + cos(C/2) - cos(A/2)', ID="X(173)", classes=["center"])
    X_503 = point_from_barycentrics(model, A, B, C, 0.32695379, 0.35836943, 0.31467678, ID="X(503)", classes=["center"])
    central_line(model, X_166, X_167, 166, 167)
    central_line(model, X_173, X_503, 173, 503)
    X_844 = intersect_lines(model, X_166, X_167, X_173, X_503, ID="X(844)", classes=["selected", "target"])
    return promote_point_to_top(model, X_844)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(844) on the given reference triangle."""
    model = create_model('X(844) = INTERSECTION OF LINES X(166)X(167) AND X(173)X(503)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00844(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00844.json"))
    write_center_svg(
        model_acute,
        here / "x-00844.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
