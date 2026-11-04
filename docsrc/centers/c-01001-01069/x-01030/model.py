"""GEOMETOR construction model for X_1030 = ISOGONAL CONJUGATE OF X_1029."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01030(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1030 = ISOGONAL CONJUGATE OF X_1029 on reference triangle ABC."""
    X_1029 = eval_trilinear_point(model, A, B, C, '(1/(a + 2*(a + b + c)*cos(A)))', ID="X_1029", classes=["center"])
    X_1030 = isogonal_conjugate(model, A, B, C, X_1029, ID="X_1030", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_35, X_37, 35, 37, incident=True)
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X_45", classes=["center", "incident"])
    X_198 = eval_trilinear_point(model, A, B, C, '(a*(cos(B) + cos(C) - cos(A) - 1))', ID="X_198", classes=["center", "incident"])
    central_line(model, X_45, X_198, 45, 198, incident=True)
    return promote_point_to_top(model, X_1030)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1030 on the given reference triangle."""
    model = create_model('X_1030 = ISOGONAL CONJUGATE OF X_1029')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01030(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01030.json"))
    write_center_svg(
        model_acute,
        here / "x-01030.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
