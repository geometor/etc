"""GEOMETOR construction model for X_1847 = ZOSMA TRANSFORM OF X_170."""

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
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01847(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1847 = ZOSMA TRANSFORM OF X_170 on reference triangle ABC."""
    X_1802 = eval_trilinear_point(model, A, B, C, '(1 + cos(A))**(2)*cot(A)', ID="X_1802", classes=["center"])
    X_1847 = isogonal_conjugate(model, A, B, C, X_1802, ID="X_1847", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_4, X_7, 4, 7, incident=True)
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    central_line(model, X_85, X_92, 85, 92, incident=True)
    X_278 = eval_trilinear_point(model, A, B, C, 'sec(A)*tan(A/2)', ID="X_278", classes=["center", "incident"])
    X_279 = eval_trilinear_point(model, A, B, C, 'csc(A)*(tan(A/2))**(2)', ID="X_279", classes=["center", "incident"])
    central_line(model, X_278, X_279, 278, 279, incident=True)
    return promote_point_to_top(model, X_1847)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1847 on the given reference triangle."""
    model = create_model('X_1847 = ZOSMA TRANSFORM OF X_170')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01847(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01847.json"))
    write_center_svg(
        model_acute,
        here / "x-01847.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
