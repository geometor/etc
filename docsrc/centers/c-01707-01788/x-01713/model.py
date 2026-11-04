"""GEOMETOR construction model for X_1713 = MIMOSA TRANSFORM OF X_27."""

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
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01713(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1713 = MIMOSA TRANSFORM OF X_27 on reference triangle ABC."""
    X_765 = eval_trilinear_point(model, A, B, C, '(b - c) **(-2)', ID="X_765", classes=["center"])
    X_823 = eval_trilinear_point(model, A, B, C, '1/((sec(B))**(2) - (sec(C))**(2))', ID="X_823", classes=["center"])
    X_1713 = crosspoint(model, A, B, C, X_765, X_823, ID="X_1713", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_579 = eval_trilinear_point(model, A, B, C, '(a*(a**(2)*b + a**(2)*c + a*b*c - b**(3) - c**(3)))', ID="X_579", classes=["center", "incident"])
    central_line(model, X_4, X_579, 4, 579, incident=True)
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_950 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)*(2*a**(3) + (b + c)*(a**(2) + (b - c)**(2)))', ID="X_950", classes=["center", "incident"])
    central_line(model, X_71, X_950, 71, 950, incident=True)
    return promote_point_to_top(model, X_1713)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1713 on the given reference triangle."""
    model = create_model('X_1713 = MIMOSA TRANSFORM OF X_27')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01713(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01713.json"))
    write_center_svg(
        model_acute,
        here / "x-01713.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
