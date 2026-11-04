"""GEOMETOR construction model for X_1851 = ZOSMA TRANSFORM OF X_200."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01851(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1851 = ZOSMA TRANSFORM OF X_200 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center"])
    central_line(model, X_4, X_8, 4, 8)
    central_line(model, X_25, X_105, 25, 105)
    X_1851 = intersect_lines(model, X_4, X_8, X_25, X_105, ID="X_1851", classes=["selected", "target"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    X_207 = eval_trilinear_point(model, A, B, C, '((1 - sec(A))*(sec(B) + sec(C) - sec(A) - 1))', ID="X_207", classes=["center", "incident"])
    central_line(model, X_34, X_207, 34, 207, incident=True)
    return promote_point_to_top(model, X_1851)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1851 on the given reference triangle."""
    model = create_model('X_1851 = ZOSMA TRANSFORM OF X_200')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01851(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01851.json"))
    write_center_svg(
        model_acute,
        here / "x-01851.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
