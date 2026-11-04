"""GEOMETOR construction model for X_2322 = X_2-ISOCONJUGATE OF X_1410."""

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
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02322(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2322 = X_2-ISOCONJUGATE OF X_1410 on reference triangle ABC."""
    X_2322 = eval_barycentric_point(model, A, B, C, '(b + c - a)**(2)/((b + c)*(b**(2) + c**(2) - a**(2)))', ID="X_2322", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    central_line(model, X_8, X_29, 8, 29, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    central_line(model, X_19, X_27, 19, 27, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_253 = eval_trilinear_point(model, A, B, C, '((csc(A))/(tan(B) + tan(C) - tan(A)))', ID="X_253", classes=["center", "incident"])
    central_line(model, X_2, X_253, 2, 253, incident=True)
    return promote_point_to_top(model, X_2322)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2322 on the given reference triangle."""
    model = create_model('X_2322 = X_2-ISOCONJUGATE OF X_1410')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02322(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02322.json"))
    write_center_svg(
        model_acute,
        here / "x-02322.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
