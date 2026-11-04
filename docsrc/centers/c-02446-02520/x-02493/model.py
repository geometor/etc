"""GEOMETOR construction model for X_2493 = RADICAL CENTER OF {CIRCUMCIRCLE,NINE-POINT-CIRCLE, PARRY CIRCLE}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_barycentric_point,
    eval_trilinear_point,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02493(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2493 = RADICAL CENTER OF {CIRCUMCIRCLE,NINE-POINT-CIRCLE, PARRY CIRCLE} on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_842 = eval_barycentric_point(model, A, B, C, 'a**(2)/(2*a**(6) - 2*a**(4)*(b**(2) + c**(2)) + a**(2)*(b**(4) + c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X_842", classes=["center"])
    X_2493 = crosspoint(model, A, B, C, X_2, X_842, ID="X_2493", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_5, X_39, 5, 39, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X_50", classes=["center", "incident"])
    central_line(model, X_23, X_50, 23, 50, incident=True)
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X_94", classes=["center", "incident"])
    central_line(model, X_2, X_94, 2, 94, incident=True)
    return promote_point_to_top(model, X_2493)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2493 on the given reference triangle."""
    model = create_model('X_2493 = RADICAL CENTER OF {CIRCUMCIRCLE,NINE-POINT-CIRCLE, PARRY CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02493(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02493.json"))
    write_center_svg(
        model_acute,
        here / "x-02493.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
