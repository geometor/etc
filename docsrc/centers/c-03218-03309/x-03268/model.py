"""GEOMETOR construction model for X_3268 = ISOTOMIC CONJUGATE OF X_476."""

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
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03268(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3268 = ISOTOMIC CONJUGATE OF X_476 on reference triangle ABC."""
    X_476 = eval_trilinear_point(model, A, B, C, '1/((1 + 2*cos(2*A))*sin(B - C))', ID="X_476", classes=["center"])
    X_3268 = isotomic_conjugate(model, A, B, C, X_476, ID="X_3268", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_99, X_110, 99, 110, incident=True)
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_325, X_523, 325, 523, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_1637 = eval_barycentric_point(model, A, B, C, 'tan(A)*(tan(B) - tan(C))*(tan(B) + tan(C) - 2*tan(A))', ID="X_1637", classes=["center", "incident"])
    central_line(model, X_2, X_1637, 2, 1637, incident=True)
    return promote_point_to_top(model, X_3268)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3268 on the given reference triangle."""
    model = create_model('X_3268 = ISOTOMIC CONJUGATE OF X_476')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03268(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03268.json"))
    write_center_svg(
        model_acute,
        here / "x-03268.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
