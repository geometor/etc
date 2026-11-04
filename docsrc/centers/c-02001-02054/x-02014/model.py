"""GEOMETOR construction model for X_2014 = EXSIMILICENTER(GALLATLY CIRCLE, SPIEKER CIRCLE)."""

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
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02014(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2014 = EXSIMILICENTER(GALLATLY CIRCLE, SPIEKER CIRCLE) on reference triangle ABC."""
    X_2014 = eval_trilinear_point(model, A, B, C, '((sin(B) + sin(C) - sin(A)*sin(A +  omega  ))*(csc(A)))', ID="X_2014", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_10, X_39, 10, 39, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_2007 = eval_trilinear_point(model, A, B, C, '(1 + sin(A +  omega  ))', ID="X_2007", classes=["center", "incident"])
    central_line(model, X_2, X_2007, 2, 2007, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_2008 = eval_trilinear_point(model, A, B, C, '(1 - sin(A +  omega  ))', ID="X_2008", classes=["center", "incident"])
    central_line(model, X_8, X_2008, 8, 2008, incident=True)
    return promote_point_to_top(model, X_2014)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2014 on the given reference triangle."""
    model = create_model('X_2014 = EXSIMILICENTER(GALLATLY CIRCLE, SPIEKER CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02014(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02014.json"))
    write_center_svg(
        model_acute,
        here / "x-02014.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
