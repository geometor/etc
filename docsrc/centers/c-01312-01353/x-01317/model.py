"""GEOMETOR construction model for X_1317 = REFLECTION OF X_11 IN X_1."""

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
    midpoint,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01317(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1317 = REFLECTION OF X_11 IN X_1 on reference triangle ABC."""
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center"])
    X_1317 = midpoint(model, X_100, X_145, ID="X_1317", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_56, X_100, 56, 100, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_55, X_104, 55, 104, incident=True)
    return promote_point_to_top(model, X_1317)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1317 on the given reference triangle."""
    model = create_model('X_1317 = REFLECTION OF X_11 IN X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01317(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01317.json"))
    write_center_svg(
        model_acute,
        here / "x-01317.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
