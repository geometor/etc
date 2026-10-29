"""GEOMETOR construction model for X(19) = CLAWSON POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcircle,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    orthic_triangle,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00019(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(19) = CLAWSON POINT on reference triangle ABC."""
    orthic_triangle(model, A, B, C)
    circumcircle(model, A, B, C)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    central_line(model, X_4, X_9, 4, 9)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X(28)", classes=["center"])
    central_line(model, X_1, X_28, 1, 28)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center"])
    central_line(model, X_6, X_34, 6, 34)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["selected", "target"])
    return promote_point_to_top(model, X_19)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(19) on the given reference triangle."""
    model = create_model('X(19) = CLAWSON POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00019(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00019.json"))
    write_center_svg(
        model_acute,
        here / "x-00019.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
