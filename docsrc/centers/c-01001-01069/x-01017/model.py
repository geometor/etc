"""GEOMETOR construction model for X_1017 = POINT ALFIRK."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01017(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1017 = POINT ALFIRK on reference triangle ABC."""
    X_1017 = eval_trilinear_point(model, A, B, C, 'a*(b + c - 2*a)**(2)', ID="X_1017", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_6, X_101, 6, 101, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_214 = eval_trilinear_point(model, A, B, C, '(b + c - 2*a)*(b**(2) + c**(2) - a**(2) - b*c)', ID="X_214", classes=["center", "incident"])
    central_line(model, X_44, X_214, 44, 214, incident=True)
    return promote_point_to_top(model, X_1017)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1017 on the given reference triangle."""
    model = create_model('X_1017 = POINT ALFIRK')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01017(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01017.json"))
    write_center_svg(
        model_acute,
        here / "x-01017.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
