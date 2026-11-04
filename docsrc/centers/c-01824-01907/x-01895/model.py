"""GEOMETOR construction model for X_1895 = ZOSMA TRANSFORM OF X_1044."""

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
    gergonne_point_of,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01895(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1895 = ZOSMA TRANSFORM OF X_1044 on reference triangle ABC."""
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center"])
    X_1895 = ceva_conjugate(model, A, B, C, X_75, X_92, ID="X_1895", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_4, X_7, 4, 7, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    central_line(model, X_1, X_29, 1, 29, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_280 = eval_trilinear_point(model, A, B, C, '((csc(A/2))**(2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X_280", classes=["center", "incident"])
    central_line(model, X_2, X_280, 2, 280, incident=True)
    return promote_point_to_top(model, X_1895)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1895 on the given reference triangle."""
    model = create_model('X_1895 = ZOSMA TRANSFORM OF X_1044')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01895(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01895.json"))
    write_center_svg(
        model_acute,
        here / "x-01895.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
