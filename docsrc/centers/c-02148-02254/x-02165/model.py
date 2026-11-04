"""GEOMETOR construction model for X_2165 = X_2-ISOCONJUGATE OF X_47."""

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
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02165(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2165 = X_2-ISOCONJUGATE OF X_47 on reference triangle ABC."""
    X_1993 = eval_trilinear_point(model, A, B, C, 'csc(A)*cos(2*A)', ID="X_1993", classes=["center"])
    X_2165 = isogonal_conjugate(model, A, B, C, X_1993, ID="X_2165", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_5, X_6, 5, 6, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    central_line(model, X_25, X_53, 25, 53, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_96 = eval_trilinear_point(model, A, B, C, 'sec(2*A)*sec(B - C)', ID="X_96", classes=["center", "incident"])
    central_line(model, X_4, X_96, 4, 96, incident=True)
    return promote_point_to_top(model, X_2165)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2165 on the given reference triangle."""
    model = create_model('X_2165 = X_2-ISOCONJUGATE OF X_47')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02165(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02165.json"))
    write_center_svg(
        model_acute,
        here / "x-02165.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
