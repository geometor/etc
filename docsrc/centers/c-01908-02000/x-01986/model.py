"""GEOMETOR construction model for X_1986 = HATZIPOLAKIS REFLECTION POINT."""

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
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01986(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1986 = HATZIPOLAKIS REFLECTION POINT on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_403 = eval_trilinear_point(model, A, B, C, '(sec(A))*(1 + cos(2*B) + cos(2*C))', ID="X_403", classes=["center"])
    X_1986 = ceva_conjugate(model, A, B, C, X_4, X_403, ID="X_1986", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_6, X_74, 6, 74, incident=True)
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X_94", classes=["center", "incident"])
    central_line(model, X_4, X_94, 4, 94, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_24, X_110, 24, 110, incident=True)
    return promote_point_to_top(model, X_1986)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1986 on the given reference triangle."""
    model = create_model('X_1986 = HATZIPOLAKIS REFLECTION POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01986(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01986.json"))
    write_center_svg(
        model_acute,
        here / "x-01986.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
