"""GEOMETOR construction model for X_2052 = ISOGONAL CONJUGATE OF X_577."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02052(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2052 = ISOGONAL CONJUGATE OF X_577 on reference triangle ABC."""
    X_577 = eval_trilinear_point(model, A, B, C, 'sin(A)*(cos(A))**(2)', ID="X_577", classes=["center"])
    X_2052 = isogonal_conjugate(model, A, B, C, X_577, ID="X_2052", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_4, X_51, 4, 51, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_96 = eval_trilinear_point(model, A, B, C, 'sec(2*A)*sec(B - C)', ID="X_96", classes=["center", "incident"])
    central_line(model, X_24, X_96, 24, 96, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_25, X_98, 25, 98, incident=True)
    return promote_point_to_top(model, X_2052)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2052 on the given reference triangle."""
    model = create_model('X_2052 = ISOGONAL CONJUGATE OF X_577')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02052(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02052.json"))
    write_center_svg(
        model_acute,
        here / "x-02052.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
