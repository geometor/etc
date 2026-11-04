"""GEOMETOR construction model for X_1470 = X_997-BETH CONJUGATE OF X_997."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01470(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1470 = X_997-BETH CONJUGATE OF X_997 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_474 = eval_trilinear_point(model, A, B, C, 'cos(A) - (a + b + c)/a', ID="X_474", classes=["center"])
    central_line(model, X_1, X_3, 1, 3)
    central_line(model, X_12, X_474, 12, 474)
    X_1470 = intersect_lines(model, X_1, X_3, X_12, X_474, ID="X_1470", classes=["selected", "target"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_378 = eval_trilinear_point(model, A, B, C, 'sec(A) + 2*cos(A)', ID="X_378", classes=["center", "incident"])
    central_line(model, X_108, X_378, 108, 378, incident=True)
    return promote_point_to_top(model, X_1470)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1470 on the given reference triangle."""
    model = create_model('X_1470 = X_997-BETH CONJUGATE OF X_997')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01470(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01470.json"))
    write_center_svg(
        model_acute,
        here / "x-01470.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
