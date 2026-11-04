"""GEOMETOR construction model for X_2310 = X_2-ISOCONJUGATE OF X_1262."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02310(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2310 = X_2-ISOCONJUGATE OF X_1262 on reference triangle ABC."""
    X_2310 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))**(2)', ID="X_2310", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    central_line(model, X_31, X_33, 31, 33, incident=True)
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X_45", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_45, X_55, 45, 55, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_11, X_244, 11, 244, incident=True)
    return promote_point_to_top(model, X_2310)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2310 on the given reference triangle."""
    model = create_model('X_2310 = X_2-ISOCONJUGATE OF X_1262')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02310(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02310.json"))
    write_center_svg(
        model_acute,
        here / "x-02310.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
