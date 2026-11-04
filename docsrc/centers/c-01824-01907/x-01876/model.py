"""GEOMETOR construction model for X_1876 = ZOSMA TRANSFORM OF X_516."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    midpoint,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01876(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1876 = ZOSMA TRANSFORM OF X_516 on reference triangle ABC."""
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center"])
    X_1456 = point_from_barycentrics(model, A, B, C, -0.40740741, -0.35555556, 1.762963, ID="X_1456", classes=["center"])
    X_1876 = midpoint(model, X_65, X_1456, ID="X_1876", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_4, X_7, 4, 7, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_6, X_19, 6, 19, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_25, X_57, 25, 57, incident=True)
    return promote_point_to_top(model, X_1876)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1876 on the given reference triangle."""
    model = create_model('X_1876 = ZOSMA TRANSFORM OF X_516')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01876(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01876.json"))
    write_center_svg(
        model_acute,
        here / "x-01876.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
