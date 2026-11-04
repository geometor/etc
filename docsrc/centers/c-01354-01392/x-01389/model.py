"""GEOMETOR construction model for X_1389 = ISOGONAL CONJUGATE OF X_1385."""

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
    nagel_point_of,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01389(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1389 = ISOGONAL CONJUGATE OF X_1385 on reference triangle ABC."""
    X_1385 = eval_trilinear_point(model, A, B, C, '16*( area )**(2) + a*(a + b + c)*(b**(2) + c**(2) - a**(2))', ID="X_1385", classes=["center"])
    X_1389 = isogonal_conjugate(model, A, B, C, X_1385, ID="X_1389", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    central_line(model, X_5, X_8, 5, 8, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_65, X_104, 65, 104, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_21, X_517, 21, 517, incident=True)
    return promote_point_to_top(model, X_1389)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1389 on the given reference triangle."""
    model = create_model('X_1389 = ISOGONAL CONJUGATE OF X_1385')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01389(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01389.json"))
    write_center_svg(
        model_acute,
        here / "x-01389.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
