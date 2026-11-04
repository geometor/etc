"""GEOMETOR construction model for X_1534 = ORTHOJOIN OF X_40."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01534(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1534 = ORTHOJOIN OF X_40 on reference triangle ABC."""
    X_1534 = point_from_barycentrics(model, A, B, C, -0.19763461, -0.33953367, 1.5371683, ID="X_1534", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_937 = eval_trilinear_point(model, A, B, C, '1/(a**(3) - a**(2)*(b + c) - a*(b - c)**(2) + (b + c)**(3))', ID="X_937", classes=["center", "incident"])
    central_line(model, X_4, X_937, 4, 937, incident=True)
    return promote_point_to_top(model, X_1534)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1534 on the given reference triangle."""
    model = create_model('X_1534 = ORTHOJOIN OF X_40')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01534(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01534.json"))
    write_center_svg(
        model_acute,
        here / "x-01534.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
