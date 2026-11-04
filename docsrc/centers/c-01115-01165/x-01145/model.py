"""GEOMETOR construction model for X_1145 = 3rd EHRMANN POINT."""

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
    feuerbach_point_of,
    midpoint,
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01145(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1145 = 3rd EHRMANN POINT on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center"])
    X_1145 = midpoint(model, X_8, X_100, ID="X_1145", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_3, X_8, 3, 8, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_10, X_11, 10, 11, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_9, X_80, 9, 80, incident=True)
    return promote_point_to_top(model, X_1145)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1145 on the given reference triangle."""
    model = create_model('X_1145 = 3rd EHRMANN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01145(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01145.json"))
    write_center_svg(
        model_acute,
        here / "x-01145.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
