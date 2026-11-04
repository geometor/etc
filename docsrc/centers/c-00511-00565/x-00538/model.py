"""GEOMETOR construction model for X_538 = DIRECTION OF VECTOR AX + BX + CX, where X = X_39."""

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


def construct_x_00538(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_538 = DIRECTION OF VECTOR AX + BX + CX, where X = X_39 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center"])
    central_line(model, X_2, X_39, 2, 39)
    central_line(model, X_99, X_187, 99, 187)
    X_538 = intersect_lines(model, X_2, X_39, X_99, X_187, ID="X_538", classes=["selected", "target"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    central_line(model, X_115, X_325, 115, 325, incident=True)
    return promote_point_to_top(model, X_538)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_538 on the given reference triangle."""
    model = create_model('X_538 = DIRECTION OF VECTOR AX + BX + CX, where X = X_39')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00538(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00538.json"))
    write_center_svg(
        model_acute,
        here / "x-00538.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
