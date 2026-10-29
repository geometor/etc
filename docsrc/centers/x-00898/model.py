"""GEOMETOR construction model for X(898) = ISOGONAL CONJUGATE OF X(891)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00898(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(898) = ISOGONAL CONJUGATE OF X(891) on reference triangle ABC."""
    X_891 = eval_trilinear_point(model, A, B, C, '(b - c)*(a*b + a*c - 2*b*c)', ID="X(891)", classes=["center"])
    X_898 = isogonal_conjugate(model, A, B, C, X_891, ID="X(898)", classes=["selected", "target"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X(106)", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X(238)", classes=["center", "incident"])
    central_line(model, X_106, X_238, 106, 238, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_667 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b - c)', ID="X(667)", classes=["center", "incident"])
    central_line(model, X_100, X_667, 100, 667, incident=True)
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X(105)", classes=["center", "incident"])
    X_666 = eval_trilinear_point(model, A, B, C, 'b*c/((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X(666)", classes=["center", "incident"])
    central_line(model, X_105, X_666, 105, 666, incident=True)
    return promote_point_to_top(model, X_898)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(898) on the given reference triangle."""
    model = create_model('X(898) = ISOGONAL CONJUGATE OF X(891)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00898(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00898.json"))
    write_center_svg(
        model_acute,
        here / "x-00898.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
