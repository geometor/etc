"""GEOMETOR construction model for X(4) = ORTHOCENTER."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00004(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(4) = ORTHOCENTER on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["selected", "target"], draw_altitudes=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    central_line(model, X_9, X_10, 9, 10, incident=True)
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A + pi /3)', ID="X(15)", classes=["center", "incident"])
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /6)', ID="X(17)", classes=["center", "incident"])
    central_line(model, X_15, X_17, 15, 17, incident=True)
    return promote_point_to_top(model, X_4)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(4) on the given reference triangle."""
    model = create_model('X(4) = ORTHOCENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00004(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00004.json"))
    write_center_svg(
        model_acute,
        here / "x-00004.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
