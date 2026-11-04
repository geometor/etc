"""GEOMETOR construction model for X_1840 = ZOSMA TRANSFORM OF X_39."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01840(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1840 = ZOSMA TRANSFORM OF X_39 on reference triangle ABC."""
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_318 = eval_trilinear_point(model, A, B, C, '(1 + sec(A))/a**(2)', ID="X_318", classes=["center"])
    central_line(model, X_12, X_37, 12, 37)
    central_line(model, X_19, X_318, 19, 318)
    X_1840 = intersect_lines(model, X_12, X_37, X_19, X_318, ID="X_1840", classes=["selected", "target"])
    X_419 = eval_barycentric_point(model, A, B, C, '(a**(2) - b*c) * (a**(2) + b*c) * (a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2))', ID="X_419", classes=["center", "incident"])
    X_1215 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c)*(a**(2) + b*c))', ID="X_1215", classes=["center", "incident"])
    central_line(model, X_419, X_1215, 419, 1215, incident=True)
    return promote_point_to_top(model, X_1840)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1840 on the given reference triangle."""
    model = create_model('X_1840 = ZOSMA TRANSFORM OF X_39')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01840(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01840.json"))
    write_center_svg(
        model_acute,
        here / "x-01840.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
