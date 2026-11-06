"""GEOMETOR construction model for X_1358 = BRISSE TRANSFORM OF X_101."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01358(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1358 = BRISSE TRANSFORM OF X_101 on reference triangle ABC."""
    X_1358 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)*(sin(B/2 - C/2))**(2)', ID="X_1358", classes=["selected", "target"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    central_line(model, X_12, X_85, 12, 85, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_56, X_105, 56, 105, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_528 = point_from_barycentrics(model, A, B, C, -0.26726124, 0.80178373, -0.53452248, ID="X_528", classes=["center", "incident"])
    central_line(model, X_7, X_528, 7, 528, incident=True)
    return promote_point_to_top(model, X_1358)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1358 on the given reference triangle."""
    model = create_model('X_1358 = BRISSE TRANSFORM OF X_101')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01358(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01358.json"))
    write_center_svg(
        model_acute,
        here / "x-01358.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
