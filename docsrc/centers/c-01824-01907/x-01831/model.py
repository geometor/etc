"""GEOMETOR construction model for X_1831 = ZOSMA TRANSFORM OF X_12."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01831(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1831 = ZOSMA TRANSFORM OF X_12 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_270 = eval_trilinear_point(model, A, B, C, '(sec(A))/(1 + cos(B - C))', ID="X_270", classes=["center"])
    X_1831 = crosspoint(model, A, B, C, X_4, X_270, ID="X_1831", classes=["selected", "target"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_4, X_80, 4, 80, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_501 = eval_trilinear_point(model, A, B, C, '(a*(a**(3) - b**(3) - c**(3) - b*c*(a + b + c) + a*b*(a - b) + a*c*(a - c))/(b + c))', ID="X_501", classes=["center", "incident"])
    central_line(model, X_28, X_501, 28, 501, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_1697 = eval_trilinear_point(model, A, B, C, '-1 + sin(A/2)*cos(B/2)*cos(C/2)', ID="X_1697", classes=["center", "incident"])
    central_line(model, X_33, X_1697, 33, 1697, incident=True)
    return promote_point_to_top(model, X_1831)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1831 on the given reference triangle."""
    model = create_model('X_1831 = ZOSMA TRANSFORM OF X_12')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01831(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01831.json"))
    write_center_svg(
        model_acute,
        here / "x-01831.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
