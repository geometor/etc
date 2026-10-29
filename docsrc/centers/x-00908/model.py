"""GEOMETOR construction model for X(908) = POINT ACUBENS."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    gergonne_point_of,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00908(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(908) = POINT ACUBENS on reference triangle ABC."""
    X_908 = eval_barycentric_point(model, A, B, C, 'cos(B) + cos(C) - 1', ID="X(908)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X(72)", classes=["center", "incident"])
    central_line(model, X_5, X_72, 5, 72, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X(78)", classes=["center", "incident"])
    central_line(model, X_4, X_78, 4, 78, incident=True)
    return promote_point_to_top(model, X_908)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(908) on the given reference triangle."""
    model = create_model('X(908) = POINT ACUBENS')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00908(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00908.json"))
    write_center_svg(
        model_acute,
        here / "x-00908.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
