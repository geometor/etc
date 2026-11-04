"""GEOMETOR construction model for X_1043 = CEVAPOINT OF X_1 AND X_20."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01043(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1043 = CEVAPOINT OF X_1 AND X_20 on reference triangle ABC."""
    X_1042 = eval_trilinear_point(model, A, B, C, '((1 - cos(A))*(cos(B) + cos(C)))', ID="X_1042", classes=["center"])
    X_1043 = isogonal_conjugate(model, A, B, C, X_1042, ID="X_1043", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_8, X_21, 8, 21, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    central_line(model, X_29, X_33, 29, 33, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_1, X_75, 1, 75, incident=True)
    return promote_point_to_top(model, X_1043)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1043 on the given reference triangle."""
    model = create_model('X_1043 = CEVAPOINT OF X_1 AND X_20')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01043(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01043.json"))
    write_center_svg(
        model_acute,
        here / "x-01043.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
