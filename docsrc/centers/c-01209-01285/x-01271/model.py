"""GEOMETOR construction model for X_1271 = ISOTOMIC CONJUGATE OF X_1132."""

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
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01271(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1271 = ISOTOMIC CONJUGATE OF X_1132 on reference triangle ABC."""
    X_1132 = eval_trilinear_point(model, A, B, C, '1/(sin(A) - 2*cos(A))', ID="X_1132", classes=["center"])
    X_1271 = isotomic_conjugate(model, A, B, C, X_1132, ID="X_1271", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_176 = eval_trilinear_point(model, A, B, C, '1 + sec(A/2)*cos(B/2)*cos(C/2)', ID="X_176", classes=["center", "incident"])
    central_line(model, X_8, X_176, 8, 176, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_487 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 - csc(A)*sin(B)*sin(C)))', ID="X_487", classes=["center", "incident"])
    central_line(model, X_20, X_487, 20, 487, incident=True)
    return promote_point_to_top(model, X_1271)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1271 on the given reference triangle."""
    model = create_model('X_1271 = ISOTOMIC CONJUGATE OF X_1132')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01271(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01271.json"))
    write_center_svg(
        model_acute,
        here / "x-01271.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
