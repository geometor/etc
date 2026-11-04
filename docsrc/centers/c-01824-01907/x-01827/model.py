"""GEOMETOR construction model for X_1827 = ZOSMA TRANSFORM OF X_7."""

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
    gergonne_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01827(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1827 = ZOSMA TRANSFORM OF X_7 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center"])
    X_1827 = crosspoint(model, A, B, C, X_4, X_33, ID="X_1827", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_4, X_7, 4, 7, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_19, X_25, 19, 25, incident=True)
    X_294 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b**(2) + c**(2) - a*b - a*c))', ID="X_294", classes=["center", "incident"])
    X_1172 = point_from_barycentrics(model, A, B, C, 0.14979394, 0.23060383, 0.61960222, ID="X_1172", classes=["center", "incident"])
    central_line(model, X_294, X_1172, 294, 1172, incident=True)
    return promote_point_to_top(model, X_1827)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1827 on the given reference triangle."""
    model = create_model('X_1827 = ZOSMA TRANSFORM OF X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01827(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01827.json"))
    write_center_svg(
        model_acute,
        here / "x-01827.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
