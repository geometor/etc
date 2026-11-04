"""GEOMETOR construction model for X_2934 = TANGENTIAL-ISOGONAL CONJUGATE OF X_184."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02934(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2934 = TANGENTIAL-ISOGONAL CONJUGATE OF X_184 on reference triangle ABC."""
    X_311 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*cos(B - C)', ID="X_311", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_2934 = ceva_conjugate(model, A, B, C, X_311, X_6, ID="X_2934", classes=["selected", "target"])
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_26", classes=["center", "incident"])
    X_157 = eval_trilinear_point(model, A, B, C, '(a*(b**(3)*cos(B) + c**(3)*cos(C) - a**(3)*cos(A)))', ID="X_157", classes=["center", "incident"])
    central_line(model, X_26, X_157, 26, 157, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_1225 = point_from_barycentrics(model, A, B, C, 0.48769872, 0.29467347, 0.2176278, ID="X_1225", classes=["center", "incident"])
    central_line(model, X_22, X_1225, 22, 1225, incident=True)
    X_159 = eval_trilinear_point(model, A, B, C, '(a*((a**(2) + b**(2) + c**(2))*sin(2*A) + (c**(2) - b**(2) - a**(2))*sin(2*B) + (b**(2) - c**(2) - a**(2))*sin(2*C)))', ID="X_159", classes=["center", "incident"])
    X_2917 = point_from_barycentrics(model, A, B, C, 0.88332649, 0.90409967, -0.78742616, ID="X_2917", classes=["center", "incident"])
    central_line(model, X_159, X_2917, 159, 2917, incident=True)
    return promote_point_to_top(model, X_2934)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2934 on the given reference triangle."""
    model = create_model('X_2934 = TANGENTIAL-ISOGONAL CONJUGATE OF X_184')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02934(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02934.json"))
    write_center_svg(
        model_acute,
        here / "x-02934.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
