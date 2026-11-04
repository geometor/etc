"""GEOMETOR construction model for X_2947 = EXCENTRAL-ISOGONAL CONJUGATE OF X_19."""

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
    incenter_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02947(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2947 = EXCENTRAL-ISOGONAL CONJUGATE OF X_19 on reference triangle ABC."""
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X_219", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2947 = ceva_conjugate(model, A, B, C, X_219, X_1, ID="X_2947", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_71, X_165, 71, 165, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_1754 = point_from_barycentrics(model, A, B, C, 0.042032164, 0.23903509, 0.71893275, ID="X_1754", classes=["center", "incident"])
    central_line(model, X_43, X_1754, 43, 1754, incident=True)
    return promote_point_to_top(model, X_2947)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2947 on the given reference triangle."""
    model = create_model('X_2947 = EXCENTRAL-ISOGONAL CONJUGATE OF X_19')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02947(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02947.json"))
    write_center_svg(
        model_acute,
        here / "x-02947.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
