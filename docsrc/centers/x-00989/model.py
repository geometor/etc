"""GEOMETOR construction model for X(989) = ISOGONAL CONJUGATE OF X(988)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00989(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(989) = ISOGONAL CONJUGATE OF X(988) on reference triangle ABC."""
    X_988 = point_from_barycentrics(model, A, B, C, 0.30315849, 0.34348562, 0.35335589, ID="X(988)", classes=["center"])
    X_989 = isogonal_conjugate(model, A, B, C, X_988, ID="X(989)", classes=["selected", "target"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X(84)", classes=["center", "incident"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X(171)", classes=["center", "incident"])
    central_line(model, X_84, X_171, 84, 171, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center", "incident"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X(256)", classes=["center", "incident"])
    central_line(model, X_40, X_256, 40, 256, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    X_612 = eval_trilinear_point(model, A, B, C, 'a**(2) + b**(2) + c**(2) + 2*b*c', ID="X(612)", classes=["center", "incident"])
    central_line(model, X_21, X_612, 21, 612, incident=True)
    return promote_point_to_top(model, X_989)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(989) on the given reference triangle."""
    model = create_model('X(989) = ISOGONAL CONJUGATE OF X(988)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00989(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00989.json"))
    write_center_svg(
        model_acute,
        here / "x-00989.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
