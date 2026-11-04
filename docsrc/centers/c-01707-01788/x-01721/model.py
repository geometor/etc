"""GEOMETOR construction model for X_1721 = MIMOSA TRANSFORM OF X_55."""

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
    incenter_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01721(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1721 = MIMOSA TRANSFORM OF X_55 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_990 = eval_trilinear_point(model, A, B, C, '(a**(5) - a**(4)*(b + c) - 2*a**(3)*b*c - a*(b - c)**(2)*(b**(2) + c**(2)) + (b - c)**(2)*(b + c)**(3))', ID="X_990", classes=["center"])
    X_1721 = reflection_in_point(model, X_1, X_990, ID="X_1721", classes=["selected", "target"], guide=False)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    X_846 = eval_trilinear_point(model, A, B, C, '(- a**(2) + b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_846", classes=["center", "incident"])
    central_line(model, X_165, X_846, 165, 846, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_984 = eval_trilinear_point(model, A, B, C, 'b**(2) + b*c + c**(2)', ID="X_984", classes=["center", "incident"])
    central_line(model, X_40, X_984, 40, 984, incident=True)
    return promote_point_to_top(model, X_1721)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1721 on the given reference triangle."""
    model = create_model('X_1721 = MIMOSA TRANSFORM OF X_55')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01721(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01721.json"))
    write_center_svg(
        model_acute,
        here / "x-01721.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
