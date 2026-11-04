"""GEOMETOR construction model for X_1877 = ZOSMA TRANSFORM OF X_517."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01877(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1877 = ZOSMA TRANSFORM OF X_517 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1846 = point_from_barycentrics(model, A, B, C, 0.090909091, -1.5936216e-17, 0.90909091, ID="X_1846", classes=["center"])
    X_1877 = ceva_conjugate(model, A, B, C, X_4, X_1846, ID="X_1877", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_51, X_65, 51, 65, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_1455 = point_from_barycentrics(model, A, B, C, -0.35353535, -0.48484848, 1.8383838, ID="X_1455", classes=["center", "incident"])
    central_line(model, X_11, X_1455, 11, 1455, incident=True)
    return promote_point_to_top(model, X_1877)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1877 on the given reference triangle."""
    model = create_model('X_1877 = ZOSMA TRANSFORM OF X_517')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01877(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01877.json"))
    write_center_svg(
        model_acute,
        here / "x-01877.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
