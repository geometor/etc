"""GEOMETOR construction model for X(762) = TRILINEAR CUBE OF X(37)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00762(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(762) = TRILINEAR CUBE OF X(37) on reference triangle ABC."""
    X_762 = eval_trilinear_point(model, A, B, C, '(b + c)**(3)', ID="X(762)", classes=["selected", "target"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X(210)", classes=["center", "incident"])
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X(213)", classes=["center", "incident"])
    central_line(model, X_210, X_213, 210, 213, incident=True)
    return promote_point_to_top(model, X_762)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(762) on the given reference triangle."""
    model = create_model('X(762) = TRILINEAR CUBE OF X(37)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00762(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00762.json"))
    write_center_svg(
        model_acute,
        here / "x-00762.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
