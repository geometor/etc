"""GEOMETOR construction model for X_1834 = ZOSMA TRANSFORM OF X_28."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01834(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1834 = ZOSMA TRANSFORM OF X_28 on reference triangle ABC."""
    X_1043 = eval_trilinear_point(model, A, B, C, '(1/((1 - cos(A))*(cos(B) + cos(C))))', ID="X_1043", classes=["center"])
    X_1834 = complement(model, A, B, C, X_1043, ID="X_1834", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_10, X_37, 10, 37, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    central_line(model, X_12, X_42, 12, 42, incident=True)
    return promote_point_to_top(model, X_1834)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1834 on the given reference triangle."""
    model = create_model('X_1834 = ZOSMA TRANSFORM OF X_28')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01834(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01834.json"))
    write_center_svg(
        model_acute,
        here / "x-01834.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
