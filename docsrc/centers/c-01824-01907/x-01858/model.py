"""GEOMETOR construction model for X_1858 = ZOSMA TRANSFORM OF X_225."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01858(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1858 = ZOSMA TRANSFORM OF X_225 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center"])
    X_1858 = crosspoint(model, A, B, C, X_4, X_21, ID="X_1858", classes=["selected", "target"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_4, X_65, 4, 65, incident=True)
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_21, X_60, 21, 60, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_90 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A))', ID="X_90", classes=["center", "incident"])
    central_line(model, X_1, X_90, 1, 90, incident=True)
    return promote_point_to_top(model, X_1858)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1858 on the given reference triangle."""
    model = create_model('X_1858 = ZOSMA TRANSFORM OF X_225')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01858(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01858.json"))
    write_center_svg(
        model_acute,
        here / "x-01858.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
