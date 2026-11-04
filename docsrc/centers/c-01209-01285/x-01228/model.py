"""GEOMETOR construction model for X_1228 = ISOTOMIC CONJUGATE OF X_1169."""

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
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01228(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1228 = ISOTOMIC CONJUGATE OF X_1169 on reference triangle ABC."""
    X_1169 = point_from_barycentrics(model, A, B, C, 0.19529243, 0.31300293, 0.49170465, ID="X_1169", classes=["center"])
    X_1228 = isotomic_conjugate(model, A, B, C, X_1169, ID="X_1228", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_2, X_39, 2, 39, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_313 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(3)*c**(3)', ID="X_313", classes=["center", "incident"])
    central_line(model, X_12, X_313, 12, 313, incident=True)
    X_312 = eval_trilinear_point(model, A, B, C, '(b + c - a)*b**(2)*c**(2)', ID="X_312", classes=["center", "incident"])
    X_857 = eval_trilinear_point(model, A, B, C, '((sin(C))**(2)*sin(2*B)*sin(C - A) + (sin(B))**(2)*sin(2*C)*sin(B - A))', ID="X_857", classes=["center", "incident"])
    central_line(model, X_312, X_857, 312, 857, incident=True)
    return promote_point_to_top(model, X_1228)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1228 on the given reference triangle."""
    model = create_model('X_1228 = ISOTOMIC CONJUGATE OF X_1169')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01228(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01228.json"))
    write_center_svg(
        model_acute,
        here / "x-01228.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
