"""GEOMETOR construction model for X_3660 = MIDPOINT OF {X_3513, X_3514}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03660(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3660 = MIDPOINT OF {X_3513, X_3514} on reference triangle ABC."""
    X_3660 = eval_barycentric_point(model, A, B, C, '(a*(a - b + c)*(a + b - c)*(b**(3) + c**(3) + a**(2)*b + a**(2)*c - 2*a*b**(2) - 2*a*c**(2) + 2*a*b*c - b**(2)*c - b*c**(2)))', ID="X_3660", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_222 = eval_trilinear_point(model, A, B, C, 'cos(A)*tan(A/2)', ID="X_222", classes=["center", "incident"])
    X_614 = eval_trilinear_point(model, A, B, C, 'a**(2) + b**(2) + c**(2) - 2*b*c', ID="X_614", classes=["center", "incident"])
    central_line(model, X_222, X_614, 222, 614, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_840 = point_from_barycentrics(model, A, B, C, 0.66666667, -0.32, 0.65333333, ID="X_840", classes=["center", "incident"])
    central_line(model, X_108, X_840, 108, 840, incident=True)
    return promote_point_to_top(model, X_3660)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3660 on the given reference triangle."""
    model = create_model('X_3660 = MIDPOINT OF {X_3513, X_3514}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03660(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03660.json"))
    write_center_svg(
        model_acute,
        here / "x-03660.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
