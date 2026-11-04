"""GEOMETOR construction model for X_1249 = ISOGONAL CONJUGATE OF X_1073."""

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
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01249(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1249 = ISOGONAL CONJUGATE OF X_1073 on reference triangle ABC."""
    X_1073 = eval_trilinear_point(model, A, B, C, '((cot(A))/(cos(A) - cos(B)*cos(C)))', ID="X_1073", classes=["center"])
    X_1249 = isogonal_conjugate(model, A, B, C, X_1073, ID="X_1249", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_19, X_57, 19, 57, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_253 = eval_trilinear_point(model, A, B, C, '((csc(A))/(tan(B) + tan(C) - tan(A)))', ID="X_253", classes=["center", "incident"])
    central_line(model, X_2, X_253, 2, 253, incident=True)
    return promote_point_to_top(model, X_1249)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1249 on the given reference triangle."""
    model = create_model('X_1249 = ISOGONAL CONJUGATE OF X_1073')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01249(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01249.json"))
    write_center_svg(
        model_acute,
        here / "x-01249.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
