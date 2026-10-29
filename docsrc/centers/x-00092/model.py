"""GEOMETOR construction model for X(92) = CEVAPOINT OF INCENTER AND CLAWSON POINT."""

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
    incircle,
    isogonal_conjugate,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00092(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(92) = CEVAPOINT OF INCENTER AND CLAWSON POINT on reference triangle ABC."""
    incircle(model, A, B, C)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center"])
    central_line(model, X_4, X_8, 4, 8)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center"])
    central_line(model, X_1, X_29, 1, 29)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X(27)", classes=["center"])
    central_line(model, X_19, X_27, 19, 27)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center"])
    X_92 = isogonal_conjugate(model, A, B, C, X_48, ID="X(92)", classes=["selected", "target"])
    return promote_point_to_top(model, X_92)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(92) on the given reference triangle."""
    model = create_model('X(92) = CEVAPOINT OF INCENTER AND CLAWSON POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00092(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00092.json"))
    write_center_svg(
        model_acute,
        here / "x-00092.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
