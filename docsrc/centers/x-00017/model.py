"""GEOMETOR construction model for X(17) = 1st NAPOLEON POINT."""

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
    nine_point_center_of,
    orthocenter_of,
    outer_napoleon_triangle,
    perspector,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00017(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(17) = 1st NAPOLEON POINT on reference triangle ABC."""
    Na, Nb, Nc = outer_napoleon_triangle(model, A, B, C)
    X_17 = perspector(model, A, B, C, Na, Nb, Nc, ID="X(17)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center", "incident"])
    central_line(model, X_3, X_13, 3, 13, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A + pi /3)', ID="X(15)", classes=["center", "incident"])
    central_line(model, X_4, X_15, 4, 15, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X(14)", classes=["center", "incident"])
    central_line(model, X_5, X_14, 5, 14, incident=True)
    return promote_point_to_top(model, X_17)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(17) on the given reference triangle."""
    model = create_model('X(17) = 1st NAPOLEON POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00017(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00017.json"))
    write_center_svg(
        model_acute,
        here / "x-00017.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
