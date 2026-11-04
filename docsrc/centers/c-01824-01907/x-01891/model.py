"""GEOMETOR construction model for X_1891 = ZOSMA TRANSFORM OF X_986."""

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
    intersect_lines,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01891(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1891 = ZOSMA TRANSFORM OF X_986 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    central_line(model, X_1, X_4, 1, 4)
    central_line(model, X_8, X_19, 8, 19)
    X_1891 = intersect_lines(model, X_1, X_4, X_8, X_19, ID="X_1891", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    central_line(model, X_10, X_28, 10, 28, incident=True)
    return promote_point_to_top(model, X_1891)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1891 on the given reference triangle."""
    model = create_model('X_1891 = ZOSMA TRANSFORM OF X_986')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01891(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01891.json"))
    write_center_svg(
        model_acute,
        here / "x-01891.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
