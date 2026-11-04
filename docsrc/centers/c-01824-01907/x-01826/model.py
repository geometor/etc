"""GEOMETOR construction model for X_1826 = ZOSMA TRANSFORM OF X_6."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01826(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1826 = ZOSMA TRANSFORM OF X_6 on reference triangle ABC."""
    X_1790 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a**(2))/(b + c)', ID="X_1790", classes=["center"])
    X_1826 = isogonal_conjugate(model, A, B, C, X_1790, ID="X_1826", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_12, X_37, 12, 37, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    central_line(model, X_33, X_42, 33, 42, incident=True)
    return promote_point_to_top(model, X_1826)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1826 on the given reference triangle."""
    model = create_model('X_1826 = ZOSMA TRANSFORM OF X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01826(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01826.json"))
    write_center_svg(
        model_acute,
        here / "x-01826.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
