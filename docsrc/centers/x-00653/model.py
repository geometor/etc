"""GEOMETOR construction model for X(653) = TRILINEAR POLE OF LINE X(1)X(4)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00653(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(653) = TRILINEAR POLE OF LINE X(1)X(4) on reference triangle ABC."""
    X_652 = eval_trilinear_point(model, A, B, C, 'sec(B) - sec(C)', ID="X(652)", classes=["center"])
    X_653 = isogonal_conjugate(model, A, B, C, X_652, ID="X(653)", classes=["selected", "target"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center", "incident"])
    central_line(model, X_29, X_65, 29, 65, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center", "incident"])
    central_line(model, X_57, X_92, 57, 92, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_196 = point_from_barycentrics(model, A, B, C, 0.56369983, 0.76788831, -0.33158813, ID="X(196)", classes=["center", "incident"])
    central_line(model, X_2, X_196, 2, 196, incident=True)
    return promote_point_to_top(model, X_653)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(653) on the given reference triangle."""
    model = create_model('X(653) = TRILINEAR POLE OF LINE X(1)X(4)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00653(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00653.json"))
    write_center_svg(
        model_acute,
        here / "x-00653.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
