"""GEOMETOR construction model for X(344) = ISOTOMIC CONJUGATE OF X(277)."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00344(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(344) = ISOTOMIC CONJUGATE OF X(277) on reference triangle ABC."""
    X_277 = eval_barycentric_point(model, A, B, C, '1/(a**(2) + b**(2) + c**(2) - 2*a*b - 2*a*c)', ID="X(277)", classes=["center"])
    X_344 = isotomic_conjugate(model, A, B, C, X_277, ID="X(344)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    central_line(model, X_2, X_37, 2, 37, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    central_line(model, X_9, X_69, 9, 69, incident=True)
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X(45)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_45, X_141, 45, 141, incident=True)
    return promote_point_to_top(model, X_344)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(344) on the given reference triangle."""
    model = create_model('X(344) = ISOTOMIC CONJUGATE OF X(277)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00344(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00344.json"))
    write_center_svg(
        model_acute,
        here / "x-00344.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
