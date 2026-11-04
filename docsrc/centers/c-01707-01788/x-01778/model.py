"""GEOMETOR construction model for X_1778 = MIMOSA TRANSFORM OF X_1171."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01778(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1778 = MIMOSA TRANSFORM OF X_1171 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center"])
    central_line(model, X_6, X_21, 6, 21)
    central_line(model, X_9, X_58, 9, 58)
    X_1778 = intersect_lines(model, X_6, X_21, X_9, X_58, ID="X_1778", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    central_line(model, X_37, X_81, 37, 81, incident=True)
    return promote_point_to_top(model, X_1778)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1778 on the given reference triangle."""
    model = create_model('X_1778 = MIMOSA TRANSFORM OF X_1171')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01778(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01778.json"))
    write_center_svg(
        model_acute,
        here / "x-01778.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
