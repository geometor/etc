"""GEOMETOR construction model for X_3777 = X_1577com[INVERSE(nT(-bc, c²))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03777(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3777 = X_1577com[INVERSE(nT(-bc, c²))] on reference triangle ABC."""
    X_3777 = eval_barycentric_point(model, A, B, C, '(a*(b - c)*(b**(2) + c**(2) - b*c))', ID="X_3777", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_10, X_514, 10, 514, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X_663", classes=["center", "incident"])
    central_line(model, X_513, X_663, 513, 663, incident=True)
    X_659 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c)*(b - c)', ID="X_659", classes=["center", "incident"])
    X_905 = eval_trilinear_point(model, A, B, C, '(b - c)*cot(A)', ID="X_905", classes=["center", "incident"])
    central_line(model, X_659, X_905, 659, 905, incident=True)
    return promote_point_to_top(model, X_3777)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3777 on the given reference triangle."""
    model = create_model('X_3777 = X_1577com[INVERSE(nT(-bc, c²))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03777(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03777.json"))
    write_center_svg(
        model_acute,
        here / "x-03777.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
