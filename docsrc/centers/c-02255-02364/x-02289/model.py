"""GEOMETOR construction model for X_2289 = X_2-ISOCONJUGATE OF X_1118."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02289(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2289 = X_2-ISOCONJUGATE OF X_1118 on reference triangle ABC."""
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center"])
    X_2289 = ceva_conjugate(model, A, B, C, X_394, X_255, ID="X_2289", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_9, X_21, 9, 21, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_3, X_48, 3, 48, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_610 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C) - tan(A)', ID="X_610", classes=["center", "incident"])
    central_line(model, X_101, X_610, 101, 610, incident=True)
    return promote_point_to_top(model, X_2289)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2289 on the given reference triangle."""
    model = create_model('X_2289 = X_2-ISOCONJUGATE OF X_1118')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02289(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02289.json"))
    write_center_svg(
        model_acute,
        here / "x-02289.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
