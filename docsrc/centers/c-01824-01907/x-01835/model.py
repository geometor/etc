"""GEOMETOR construction model for X_1835 = ZOSMA TRANSFORM OF X_30."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01835(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1835 = ZOSMA TRANSFORM OF X_30 on reference triangle ABC."""
    X_1793 = point_from_barycentrics(model, A, B, C, 0.22028637, 0.81616101, -0.036447382, ID="X_1793", classes=["center"])
    X_1835 = isogonal_conjugate(model, A, B, C, X_1793, ID="X_1835", classes=["selected", "target"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_28, X_34, 28, 34, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center", "incident"])
    central_line(model, X_4, X_79, 4, 79, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X_186", classes=["center", "incident"])
    central_line(model, X_36, X_186, 36, 186, incident=True)
    return promote_point_to_top(model, X_1835)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1835 on the given reference triangle."""
    model = create_model('X_1835 = ZOSMA TRANSFORM OF X_30')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01835(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01835.json"))
    write_center_svg(
        model_acute,
        here / "x-01835.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
