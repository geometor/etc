"""GEOMETOR construction model for X(178) = 2nd MID-ARC POINT."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00178(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(178) = 2nd MID-ARC POINT on reference triangle ABC."""
    X_178 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*csc(A)', ID="X(178)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_188 = eval_trilinear_point(model, A, B, C, 'csc(A/2)', ID="X(188)", classes=["center", "incident"])
    central_line(model, X_2, X_188, 2, 188, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_236 = eval_trilinear_point(model, A, B, C, '(csc(A/2))*(cos(B/2) + cos(C/2) - cos(A/2))', ID="X(236)", classes=["center", "incident"])
    central_line(model, X_8, X_236, 8, 236, incident=True)
    return promote_point_to_top(model, X_178)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(178) on the given reference triangle."""
    model = create_model('X(178) = 2nd MID-ARC POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00178(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00178.json"))
    write_center_svg(
        model_acute,
        here / "x-00178.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
