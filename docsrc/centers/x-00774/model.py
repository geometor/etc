"""GEOMETOR construction model for X(774) = CROSSPOINT OF X(1) AND X(158)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00774(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(774) = CROSSPOINT OF X(1) AND X(158) on reference triangle ABC."""
    X_774 = eval_trilinear_point(model, A, B, C, '1 - cos(A)*cos(B - C)', ID="X(774)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    X_201 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(B - C))', ID="X(201)", classes=["center", "incident"])
    central_line(model, X_55, X_201, 55, 201, incident=True)
    X_821 = point_from_barycentrics(model, A, B, C, 0.10320788, 0.13043402, 0.76635811, ID="X(821)", classes=["center", "incident"])
    X_823 = eval_trilinear_point(model, A, B, C, '1/(csc(B/2) - csc(C/2))', ID="X(823)", classes=["center", "incident"])
    central_line(model, X_821, X_823, 821, 823, incident=True)
    return promote_point_to_top(model, X_774)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(774) on the given reference triangle."""
    model = create_model('X(774) = CROSSPOINT OF X(1) AND X(158)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00774(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00774.json"))
    write_center_svg(
        model_acute,
        here / "x-00774.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
