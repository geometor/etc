"""GEOMETOR construction model for X_1832 = ZOSMA TRANSFORM OF X_15."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01832(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1832 = ZOSMA TRANSFORM OF X_15 on reference triangle ABC."""
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1251 = eval_trilinear_point(model, A, B, C, '(cos(A/2))*csc(A/2 -  pi  /3)', ID="X_1251", classes=["center"])
    central_line(model, X_12, X_37, 12, 37)
    central_line(model, X_4, X_1251, 4, 1251)
    X_1832 = intersect_lines(model, X_12, X_37, X_4, X_1251, ID="X_1832", classes=["selected", "target"])
    return promote_point_to_top(model, X_1832)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1832 on the given reference triangle."""
    model = create_model('X_1832 = ZOSMA TRANSFORM OF X_15')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01832(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01832.json"))
    write_center_svg(
        model_acute,
        here / "x-01832.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
