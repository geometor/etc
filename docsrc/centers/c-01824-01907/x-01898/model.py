"""GEOMETOR construction model for X_1898 = ZOSMA TRANSFORM OF X_1068."""

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
    orthocenter_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01898(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1898 = ZOSMA TRANSFORM OF X_1068 on reference triangle ABC."""
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center"])
    X_1837 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - 2*cos(B)*cos(C)', ID="X_1837", classes=["center"])
    X_1898 = reflection_in_point(model, X_65, X_1837, ID="X_1898", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_4, X_65, 4, 65, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_90 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A))', ID="X_90", classes=["center", "incident"])
    central_line(model, X_3, X_90, 3, 90, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X_662", classes=["center", "incident"])
    central_line(model, X_21, X_662, 21, 662, incident=True)
    return promote_point_to_top(model, X_1898)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1898 on the given reference triangle."""
    model = create_model('X_1898 = ZOSMA TRANSFORM OF X_1068')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01898(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01898.json"))
    write_center_svg(
        model_acute,
        here / "x-01898.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
