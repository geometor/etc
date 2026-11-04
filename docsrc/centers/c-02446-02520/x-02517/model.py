"""GEOMETOR construction model for X_2517 = RADICAL CENTER OF {CIRCUMCIRCLE, FUHRMANN CIRCLE, (X_4,2R)}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02517(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2517 = RADICAL CENTER OF {CIRCUMCIRCLE, FUHRMANN CIRCLE, (X_4,2R)} on reference triangle ABC."""
    X_1310 = point_from_barycentrics(model, A, B, C, 0.51256281, -0.33145729, 0.81889447, ID="X_1310", classes=["center"])
    X_2517 = isotomic_conjugate(model, A, B, C, X_1310, ID="X_2517", classes=["selected", "target"])
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A +  omega  )', ID="X_240", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_240, X_522, 240, 522, incident=True)
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_325, X_523, 325, 523, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_2533 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2) - c**(2))*(a**(2) + b*c))', ID="X_2533", classes=["center", "incident"])
    central_line(model, X_513, X_2533, 513, 2533, incident=True)
    return promote_point_to_top(model, X_2517)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2517 on the given reference triangle."""
    model = create_model('X_2517 = RADICAL CENTER OF {CIRCUMCIRCLE, FUHRMANN CIRCLE, (X_4,2R)}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02517(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02517.json"))
    write_center_svg(
        model_acute,
        here / "x-02517.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
