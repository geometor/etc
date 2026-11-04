"""GEOMETOR construction model for X_1304 = COLLINGS TRANSFORM OF X_403."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01304(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1304 = COLLINGS TRANSFORM OF X_403 on reference triangle ABC."""
    X_403 = eval_trilinear_point(model, A, B, C, '(sec(A))*(1 + cos(2*B) + cos(2*C))', ID="X_403", classes=["center"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center"])
    X_1304 = cevapoint(model, A, B, C, X_403, X_523, ID="X_1304", classes=["selected", "target"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X_186", classes=["center", "incident"])
    central_line(model, X_74, X_186, 74, 186, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A + omega )', ID="X_232", classes=["center", "incident"])
    central_line(model, X_111, X_232, 111, 232, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X_250", classes=["center", "incident"])
    central_line(model, X_110, X_250, 110, 250, incident=True)
    return promote_point_to_top(model, X_1304)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1304 on the given reference triangle."""
    model = create_model('X_1304 = COLLINGS TRANSFORM OF X_403')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01304(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01304.json"))
    write_center_svg(
        model_acute,
        here / "x-01304.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
