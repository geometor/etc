"""GEOMETOR construction model for X(301) = ISOTOMIC CONJUGATE OF 2nd ISODYNAMIC CENTER."""

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


def construct_x_00301(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(301) = ISOTOMIC CONJUGATE OF 2nd ISODYNAMIC CENTER on reference triangle ABC."""
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A- pi /3)', ID="X(16)", classes=["center"])
    X_301 = isotomic_conjugate(model, A, B, C, X_16, ID="X(301)", classes=["selected", "target"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X(14)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_14, X_76, 14, 76, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X(94)", classes=["center", "incident"])
    central_line(model, X_2, X_94, 2, 94, incident=True)
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X(264)", classes=["center", "incident"])
    X_303 = eval_barycentric_point(model, A, B, C, 'csc(A)*sin(A - pi /6)', ID="X(303)", classes=["center", "incident"])
    central_line(model, X_264, X_303, 264, 303, incident=True)
    return promote_point_to_top(model, X_301)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(301) on the given reference triangle."""
    model = create_model('X(301) = ISOTOMIC CONJUGATE OF 2nd ISODYNAMIC CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00301(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00301.json"))
    write_center_svg(
        model_acute,
        here / "x-00301.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
