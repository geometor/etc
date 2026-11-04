"""GEOMETOR construction model for X_459 = X_253-CEVA CONJUGATE OF X_4."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00459(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_459 = X_253-CEVA CONJUGATE OF X_4 on reference triangle ABC."""
    X_253 = eval_trilinear_point(model, A, B, C, '((csc(A))/(tan(B) + tan(C) - tan(A)))', ID="X_253", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_459 = ceva_conjugate(model, A, B, C, X_253, X_4, ID="X_459", classes=["selected", "target"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    central_line(model, X_4, X_64, 4, 64, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_253, 2, 253, incident=True)
    X_196 = eval_trilinear_point(model, A, B, C, '((cos(B) + cos(C) - cos(A) - 1)*sec(A)*tan(A/2))', ID="X_196", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_196, X_226, 196, 226, incident=True)
    return promote_point_to_top(model, X_459)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_459 on the given reference triangle."""
    model = create_model('X_459 = X_253-CEVA CONJUGATE OF X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00459(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00459.json"))
    write_center_svg(
        model_acute,
        here / "x-00459.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
