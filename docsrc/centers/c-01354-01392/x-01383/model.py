"""GEOMETOR construction model for X_1383 = 1st GRINBERG HOMOTHETIC CENTER."""

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
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01383(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1383 = 1st GRINBERG HOMOTHETIC CENTER on reference triangle ABC."""
    X_599 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - 2*b**(2) - 2*c**(2))', ID="X_599", classes=["center"])
    X_1383 = isogonal_conjugate(model, A, B, C, X_599, ID="X_1383", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    central_line(model, X_6, X_23, 6, 23, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    central_line(model, X_32, X_111, 32, 111, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center", "incident"])
    central_line(model, X_2, X_187, 2, 187, incident=True)
    return promote_point_to_top(model, X_1383)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1383 on the given reference triangle."""
    model = create_model('X_1383 = 1st GRINBERG HOMOTHETIC CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01383(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01383.json"))
    write_center_svg(
        model_acute,
        here / "x-01383.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
