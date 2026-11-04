"""GEOMETOR construction model for X_2341 = X_2-ISOCONJUGATE OF X_1464."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02341(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2341 = X_2-ISOCONJUGATE OF X_1464 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_2173 = eval_trilinear_point(model, A, B, C, 'a*(cos(A) - 2*cos(B)*cos(C))', ID="X_2173", classes=["center"])
    X_2341 = crosspoint(model, A, B, C, X_6, X_2173, ID="X_2341", classes=["selected", "target"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_6, X_13, 6, 13, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_37, X_101, 37, 101, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_81, X_226, 81, 226, incident=True)
    return promote_point_to_top(model, X_2341)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2341 on the given reference triangle."""
    model = create_model('X_2341 = X_2-ISOCONJUGATE OF X_1464')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02341(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02341.json"))
    write_center_svg(
        model_acute,
        here / "x-02341.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
