"""GEOMETOR construction model for X_1512 = ORTHOJOIN OF X_1."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    mittenpunkt_of,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01512(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1512 = ORTHOJOIN OF X_1 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center"])
    central_line(model, X_4, X_9, 4, 9)
    central_line(model, X_6, X_80, 6, 80)
    X_1512 = intersect_lines(model, X_4, X_9, X_6, X_80, ID="X_1512", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_392 = eval_trilinear_point(model, A, B, C, '(b + c)*(b**(2) + c**(2) - a**(2)) + 4*a*b*c', ID="X_392", classes=["center", "incident"])
    central_line(model, X_5, X_392, 5, 392, incident=True)
    return promote_point_to_top(model, X_1512)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1512 on the given reference triangle."""
    model = create_model('X_1512 = ORTHOJOIN OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01512(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01512.json"))
    write_center_svg(
        model_acute,
        here / "x-01512.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
