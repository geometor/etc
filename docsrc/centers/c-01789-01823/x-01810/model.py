"""GEOMETOR construction model for X_1810 = INVERSE MIMOSA TRANSFORM OF X_518."""

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


def construct_x_01810(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1810 = INVERSE MIMOSA TRANSFORM OF X_518 on reference triangle ABC."""
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_222 = eval_trilinear_point(model, A, B, C, 'cos(A)*tan(A/2)', ID="X_222", classes=["center"])
    X_1331 = eval_trilinear_point(model, A, B, C, '(cos(A))/(b - c)', ID="X_1331", classes=["center"])
    central_line(model, X_57, X_100, 57, 100)
    central_line(model, X_222, X_1331, 222, 1331)
    X_1810 = intersect_lines(model, X_57, X_100, X_222, X_1331, ID="X_1810", classes=["selected", "target"])
    return promote_point_to_top(model, X_1810)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1810 on the given reference triangle."""
    model = create_model('X_1810 = INVERSE MIMOSA TRANSFORM OF X_518')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01810(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01810.json"))
    write_center_svg(
        model_acute,
        here / "x-01810.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
