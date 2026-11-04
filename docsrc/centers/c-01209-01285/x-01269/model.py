"""GEOMETOR construction model for X_1269 = ISOTOMIC CONJUGATE OF X_1126."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    isotomic_conjugate,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01269(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1269 = ISOTOMIC CONJUGATE OF X_1126 on reference triangle ABC."""
    X_1126 = eval_trilinear_point(model, A, B, C, 'a/(2*a+b+c)', ID="X_1126", classes=["center"])
    X_1269 = isotomic_conjugate(model, A, B, C, X_1126, ID="X_1269", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_10, X_75, 10, 75, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_349 = eval_trilinear_point(model, A, B, C, '(cos(B) + cos(C))*(csc(A))**(3)', ID="X_349", classes=["center", "incident"])
    central_line(model, X_7, X_349, 7, 349, incident=True)
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center", "incident"])
    X_314 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2)*(b + c - a)/(b + c))', ID="X_314", classes=["center", "incident"])
    central_line(model, X_79, X_314, 79, 314, incident=True)
    return promote_point_to_top(model, X_1269)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1269 on the given reference triangle."""
    model = create_model('X_1269 = ISOTOMIC CONJUGATE OF X_1126')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01269(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01269.json"))
    write_center_svg(
        model_acute,
        here / "x-01269.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
