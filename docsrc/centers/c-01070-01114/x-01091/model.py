"""GEOMETOR construction model for X_1091 = TRILINEAR SQUARE OF X_12."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01091(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1091 = TRILINEAR SQUARE OF X_12 on reference triangle ABC."""
    X_1091 = eval_trilinear_point(model, A, B, C, '((1 + cos(B - C))**(2))', ID="X_1091", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_1090 = eval_trilinear_point(model, A, B, C, '((1 - cos(B - C))**(2))', ID="X_1090", classes=["center", "incident"])
    central_line(model, X_5, X_1090, 5, 1090, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_1109 = eval_trilinear_point(model, A, B, C, '(sin(B - C))**(2)', ID="X_1109", classes=["center", "incident"])
    central_line(model, X_12, X_1109, 12, 1109, incident=True)
    return promote_point_to_top(model, X_1091)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1091 on the given reference triangle."""
    model = create_model('X_1091 = TRILINEAR SQUARE OF X_12')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01091(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01091.json"))
    write_center_svg(
        model_acute,
        here / "x-01091.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
