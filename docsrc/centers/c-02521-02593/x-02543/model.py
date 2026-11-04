"""GEOMETOR construction model for X_2543 = EXSIMILICENTER(BROCARD CIRCLE, (X_4,2R))."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02543(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2543 = EXSIMILICENTER(BROCARD CIRCLE, (X_4,2R)) on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_1340 = point_from_barycentrics(model, A, B, C, 0.34709524, 0.36700624, 0.28589852, ID="X_1340", classes=["center"])
    central_line(model, X_4, X_83, 4, 83)
    central_line(model, X_2, X_1340, 2, 1340)
    X_2543 = intersect_lines(model, X_4, X_83, X_2, X_1340, ID="X_2543", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_1341 = point_from_barycentrics(model, A, B, C, 0.30653192, 0.35355532, 0.33991277, ID="X_1341", classes=["center", "incident"])
    central_line(model, X_20, X_1341, 20, 1341, incident=True)
    return promote_point_to_top(model, X_2543)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2543 on the given reference triangle."""
    model = create_model('X_2543 = EXSIMILICENTER(BROCARD CIRCLE, (X_4,2R))')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02543(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02543.json"))
    write_center_svg(
        model_acute,
        here / "x-02543.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
