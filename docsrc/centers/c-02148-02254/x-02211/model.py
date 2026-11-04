"""GEOMETOR construction model for X_2211 = X_2-ISOCONJUGATE OF X_336."""

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


def construct_x_02211(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2211 = X_2-ISOCONJUGATE OF X_336 on reference triangle ABC."""
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A +  omega  )', ID="X_232", classes=["center"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A +  omega  )', ID="X_237", classes=["center"])
    X_2211 = ceva_conjugate(model, A, B, C, X_232, X_237, ID="X_2211", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_263 = eval_trilinear_point(model, A, B, C, 'a**(2)*sec(A -  omega  )', ID="X_263", classes=["center", "incident"])
    central_line(model, X_25, X_263, 25, 263, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_682 = eval_trilinear_point(model, A, B, C, '(sec(B)*(csc(C))**(3) + sec(C)*(csc(B))**(3))', ID="X_682", classes=["center", "incident"])
    central_line(model, X_32, X_682, 32, 682, incident=True)
    return promote_point_to_top(model, X_2211)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2211 on the given reference triangle."""
    model = create_model('X_2211 = X_2-ISOCONJUGATE OF X_336')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02211(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02211.json"))
    write_center_svg(
        model_acute,
        here / "x-02211.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
