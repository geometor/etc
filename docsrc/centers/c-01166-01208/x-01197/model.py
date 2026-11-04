"""GEOMETOR construction model for X_1197 = 3rd SARAGOSSA POINT OF X_31."""

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


def construct_x_01197(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1197 = 3rd SARAGOSSA POINT OF X_31 on reference triangle ABC."""
    X_1197 = eval_trilinear_point(model, A, B, C, '(a**(2)*(a*b**(2) + a*c**(2) + b**(2)*c + b*c**(2)))', ID="X_1197", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    central_line(model, X_6, X_43, 6, 43, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_31, X_32, 31, 32, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    central_line(model, X_81, X_239, 81, 239, incident=True)
    return promote_point_to_top(model, X_1197)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1197 on the given reference triangle."""
    model = create_model('X_1197 = 3rd SARAGOSSA POINT OF X_31')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01197(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01197.json"))
    write_center_svg(
        model_acute,
        here / "x-01197.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
