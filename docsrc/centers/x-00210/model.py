"""GEOMETOR construction model for X(210) = X(10)-CEVA CONJUGATE OF X(37)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00210(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(210) = X(10)-CEVA CONJUGATE OF X(37) on reference triangle ABC."""
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center"])
    X_210 = ceva_conjugate(model, A, B, C, X_10, X_37, ID="X(210)", classes=["selected", "target"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center", "incident"])
    central_line(model, X_10, X_12, 10, 12, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    central_line(model, X_9, X_55, 9, 55, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    central_line(model, X_31, X_44, 31, 44, incident=True)
    return promote_point_to_top(model, X_210)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(210) on the given reference triangle."""
    model = create_model('X(210) = X(10)-CEVA CONJUGATE OF X(37)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00210(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00210.json"))
    write_center_svg(
        model_acute,
        here / "x-00210.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
