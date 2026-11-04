"""GEOMETOR construction model for X_1727 = MIMOSA TRANSFORM OF X_80."""

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


def construct_x_01727(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1727 = MIMOSA TRANSFORM OF X_80 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center"])
    central_line(model, X_4, X_46, 4, 46)
    central_line(model, X_35, X_72, 35, 72)
    X_1727 = intersect_lines(model, X_4, X_46, X_35, X_72, ID="X_1727", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_30, X_80, 30, 80, incident=True)
    return promote_point_to_top(model, X_1727)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1727 on the given reference triangle."""
    model = create_model('X_1727 = MIMOSA TRANSFORM OF X_80')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01727(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01727.json"))
    write_center_svg(
        model_acute,
        here / "x-01727.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
