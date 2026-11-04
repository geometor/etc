"""GEOMETOR construction model for X_2941 = EXCENTRAL-ISOGONAL CONJUGATE OF X_6."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02941(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2941 = EXCENTRAL-ISOGONAL CONJUGATE OF X_6 on reference triangle ABC."""
    X_2321 = point_from_barycentrics(model, A, B, C, 0.47272727, 0.32727273, 0.2, ID="X_2321", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2941 = ceva_conjugate(model, A, B, C, X_2321, X_1, ID="X_2941", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    central_line(model, X_30, X_40, 30, 40, incident=True)
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    X_846 = eval_trilinear_point(model, A, B, C, '(- a**(2) + b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_846", classes=["center", "incident"])
    central_line(model, X_165, X_846, 165, 846, incident=True)
    X_1412 = eval_trilinear_point(model, A, B, C, 'a/((b + c)*(a - b - c))', ID="X_1412", classes=["center", "incident"])
    central_line(model, X_1, X_1412, 1, 1412, incident=True)
    return promote_point_to_top(model, X_2941)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2941 on the given reference triangle."""
    model = create_model('X_2941 = EXCENTRAL-ISOGONAL CONJUGATE OF X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02941(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02941.json"))
    write_center_svg(
        model_acute,
        here / "x-02941.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
