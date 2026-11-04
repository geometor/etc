"""GEOMETOR construction model for X_1902 = ZOSMA TRANSFORM OF X_1210."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01902(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1902 = ZOSMA TRANSFORM OF X_1210 on reference triangle ABC."""
    X_1829 = point_from_barycentrics(model, A, B, C, 0.10770975, 0.19863946, 0.69365079, ID="X_1829", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1902 = reflection_in_point(model, X_1829, X_4, ID="X_1902", classes=["selected", "target"], guide=False)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    central_line(model, X_4, X_8, 4, 8, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    central_line(model, X_25, X_40, 25, 40, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    central_line(model, X_33, X_64, 33, 64, incident=True)
    return promote_point_to_top(model, X_1902)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1902 on the given reference triangle."""
    model = create_model('X_1902 = ZOSMA TRANSFORM OF X_1210')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01902(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01902.json"))
    write_center_svg(
        model_acute,
        here / "x-01902.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
