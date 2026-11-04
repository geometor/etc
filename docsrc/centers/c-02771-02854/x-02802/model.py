"""GEOMETOR construction model for X_2802 = ISOGONAL CONJUGATE OF X_2718."""

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
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02802(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2802 = ISOGONAL CONJUGATE OF X_2718 on reference triangle ABC."""
    X_2718 = eval_trilinear_point(model, A, B, C, '(1/(b**(3) + c**(3) - a**(2)*b - a**(2)*c - 2*b**(2)*c - 2*b*c**(2) + 4*a*b*c))', ID="X_2718", classes=["center"])
    X_2802 = isogonal_conjugate(model, A, B, C, X_2718, ID="X_2802", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_10, X_11, 10, 11, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center", "incident"])
    central_line(model, X_8, X_80, 8, 80, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    central_line(model, X_1, X_88, 1, 88, incident=True)
    return promote_point_to_top(model, X_2802)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2802 on the given reference triangle."""
    model = create_model('X_2802 = ISOGONAL CONJUGATE OF X_2718')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02802(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02802.json"))
    write_center_svg(
        model_acute,
        here / "x-02802.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
