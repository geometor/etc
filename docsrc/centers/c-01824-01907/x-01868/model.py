"""GEOMETOR construction model for X_1868 = ZOSMA TRANSFORM OF X_387."""

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
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01868(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1868 = ZOSMA TRANSFORM OF X_387 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    central_line(model, X_4, X_8, 4, 8)
    central_line(model, X_34, X_37, 34, 37)
    X_1868 = intersect_lines(model, X_4, X_8, X_34, X_37, ID="X_1868", classes=["selected", "target"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    X_429 = eval_barycentric_point(model, A, B, C, '(b + c) * (-a**(2) + b**(2) - c**(2)) * (a**(2) + b**(2) - c**(2)) * (a*b + b**(2) + a*c + c**(2))', ID="X_429", classes=["center", "incident"])
    central_line(model, X_226, X_429, 226, 429, incident=True)
    return promote_point_to_top(model, X_1868)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1868 on the given reference triangle."""
    model = create_model('X_1868 = ZOSMA TRANSFORM OF X_387')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01868(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01868.json"))
    write_center_svg(
        model_acute,
        here / "x-01868.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
