"""GEOMETOR construction model for X_2898 = ORTHIC-ISOGONAL CONJUGATE OF X_7."""

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
    gergonne_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02898(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2898 = ORTHIC-ISOGONAL CONJUGATE OF X_7 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_2898 = ceva_conjugate(model, A, B, C, X_4, X_7, ID="X_2898", classes=["selected", "target"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center", "incident"])
    central_line(model, X_7, X_354, 7, 354, incident=True)
    X_857 = eval_trilinear_point(model, A, B, C, '((sin(C))**(2)*sin(2*B)*sin(C - A) + (sin(B))**(2)*sin(2*C)*sin(B - A))', ID="X_857", classes=["center", "incident"])
    X_948 = point_from_barycentrics(model, A, B, C, 0.23303835, 0.29498525, 0.4719764, ID="X_948", classes=["center", "incident"])
    central_line(model, X_857, X_948, 857, 948, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_1996 = point_from_barycentrics(model, A, B, C, 0.23108952, 0.29424011, 0.47467037, ID="X_1996", classes=["center", "incident"])
    central_line(model, X_55, X_1996, 55, 1996, incident=True)
    return promote_point_to_top(model, X_2898)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2898 on the given reference triangle."""
    model = create_model('X_2898 = ORTHIC-ISOGONAL CONJUGATE OF X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02898(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02898.json"))
    write_center_svg(
        model_acute,
        here / "x-02898.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
