"""GEOMETOR construction model for X(279) = ISOGONAL CONJUGATE OF X(220)."""

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
    gergonne_point_of,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00279(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(279) = ISOGONAL CONJUGATE OF X(220) on reference triangle ABC."""
    X_220 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)**(2)', ID="X(220)", classes=["center"])
    X_279 = isogonal_conjugate(model, A, B, C, X_220, ID="X(279)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X(85)", classes=["center", "incident"])
    central_line(model, X_2, X_85, 2, 85, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X(105)", classes=["center", "incident"])
    central_line(model, X_56, X_105, 56, 105, incident=True)
    return promote_point_to_top(model, X_279)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(279) on the given reference triangle."""
    model = create_model('X(279) = ISOGONAL CONJUGATE OF X(220)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00279(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00279.json"))
    write_center_svg(
        model_acute,
        here / "x-00279.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
