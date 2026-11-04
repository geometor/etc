"""GEOMETOR construction model for X_2124 = EIGENTRANSFORM OF X_9."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02124(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2124 = EIGENTRANSFORM OF X_9 on reference triangle ABC."""
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_279 = eval_trilinear_point(model, A, B, C, 'csc(A)*(tan(A/2))**(2)', ID="X_279", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_971 = eval_trilinear_point(model, A, B, C, 'a**(4)*(b + c) - 2*a**(3)*(b**(2) + c**(2) - b*c) + 2*a*(b - c)**(2)*(b**(2) + c**(2) + b*c) - (b - c)**(2)*(b + c)**(3)', ID="X_971", classes=["center"])
    central_line(model, X_57, X_279, 57, 279)
    central_line(model, X_1, X_971, 1, 971)
    X_2124 = intersect_lines(model, X_57, X_279, X_1, X_971, ID="X_2124", classes=["selected", "target"])
    X_664 = eval_trilinear_point(model, A, B, C, '1/(a*(b - c)*(b + c - a))', ID="X_664", classes=["center", "incident"])
    X_728 = eval_trilinear_point(model, A, B, C, '((b + c - a)**(3))', ID="X_728", classes=["center", "incident"])
    central_line(model, X_664, X_728, 664, 728, incident=True)
    return promote_point_to_top(model, X_2124)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2124 on the given reference triangle."""
    model = create_model('X_2124 = EIGENTRANSFORM OF X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02124(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02124.json"))
    write_center_svg(
        model_acute,
        here / "x-02124.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
