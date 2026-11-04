"""GEOMETOR construction model for X_2800 = ISOGONAL CONJUGATE OF X_2716."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02800(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2800 = ISOGONAL CONJUGATE OF X_2716 on reference triangle ABC."""
    X_2716 = point_from_barycentrics(model, A, B, C, 1.0195707, 0.064393939, -0.083964646, ID="X_2716", classes=["center"])
    X_2800 = isogonal_conjugate(model, A, B, C, X_2716, ID="X_2800", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_11, X_65, 11, 65, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_4, X_80, 4, 80, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_1, X_104, 1, 104, incident=True)
    return promote_point_to_top(model, X_2800)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2800 on the given reference triangle."""
    model = create_model('X_2800 = ISOGONAL CONJUGATE OF X_2716')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02800(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02800.json"))
    write_center_svg(
        model_acute,
        here / "x-02800.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
