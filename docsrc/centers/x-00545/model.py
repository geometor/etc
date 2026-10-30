"""GEOMETOR construction model for X(545) = DIRECTION OF VECTOR AX + BX + CX, where X = X(190)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00545(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(545) = DIRECTION OF VECTOR AX + BX + CX, where X = X(190) on reference triangle ABC."""
    X_545 = eval_barycentric_point(model, A, B, C, '2*a**(2) - b**(2) - c**(2) - 2*a*b - 2*a*c + 4*b*c', ID="X(545)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X(45)", classes=["center", "incident"])
    central_line(model, X_2, X_45, 2, 45, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X(30)", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A + omega )', ID="X(511)", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    return promote_point_to_top(model, X_545)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(545) on the given reference triangle."""
    model = create_model('X(545) = DIRECTION OF VECTOR AX + BX + CX, where X = X(190)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00545(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00545.json"))
    write_center_svg(
        model_acute,
        here / "x-00545.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
