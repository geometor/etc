"""GEOMETOR construction model for X_3099 = INTERSECTION OF LINES X_1X_32 AND X_846X_902."""

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


def construct_x_03099(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3099 = INTERSECTION OF LINES X_1X_32 AND X_846X_902 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_846 = eval_trilinear_point(model, A, B, C, '(- a**(2) + b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_846", classes=["center"])
    X_902 = eval_trilinear_point(model, A, B, C, 'a*(b + c - 2*a)', ID="X_902", classes=["center"])
    central_line(model, X_1, X_32, 1, 32)
    central_line(model, X_846, X_902, 846, 902)
    X_3099 = intersect_lines(model, X_1, X_32, X_846, X_902, ID="X_3099", classes=["selected", "target"])
    X_672 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c))', ID="X_672", classes=["center", "incident"])
    X_1282 = point_from_barycentrics(model, A, B, C, 0.61507937, -0.97619048, 1.3611111, ID="X_1282", classes=["center", "incident"])
    central_line(model, X_672, X_1282, 672, 1282, incident=True)
    return promote_point_to_top(model, X_3099)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3099 on the given reference triangle."""
    model = create_model('X_3099 = INTERSECTION OF LINES X_1X_32 AND X_846X_902')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03099(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03099.json"))
    write_center_svg(
        model_acute,
        here / "x-03099.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
