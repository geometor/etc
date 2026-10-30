"""GEOMETOR construction model for X(831) = o-(1, 3) CIRCUMCIRCLE POINT."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00831(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(831) = o-(1, 3) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_830 = point_from_barycentrics(model, A, B, C, 0.54558558, 0.25327972, -0.7988653, ID="X(830)", classes=["center"])
    X_831 = isogonal_conjugate(model, A, B, C, X_830, ID="X(831)", classes=["selected", "target"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X(662)", classes=["center", "incident"])
    X_827 = eval_trilinear_point(model, A, B, C, '1/(a**(-1)*(b**(4) - c**(4)) + a**(3)*(b**(0) - c**(0)))', ID="X(827)", classes=["center", "incident"])
    central_line(model, X_662, X_827, 662, 827, incident=True)
    return promote_point_to_top(model, X_831)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(831) on the given reference triangle."""
    model = create_model('X(831) = o-(1, 3) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00831(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00831.json"))
    write_center_svg(
        model_acute,
        here / "x-00831.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
