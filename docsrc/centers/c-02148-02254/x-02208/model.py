"""GEOMETOR construction model for X_2208 = X_2-ISOCONJUGATE OF X_329."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02208(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2208 = X_2-ISOCONJUGATE OF X_329 on reference triangle ABC."""
    X_322 = eval_trilinear_point(model, A, B, C, '((-1 - cos(A) + cos(B) + cos(C))*(csc(A))**(2))', ID="X_322", classes=["center"])
    X_2208 = isogonal_conjugate(model, A, B, C, X_322, ID="X_2208", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_48, X_55, 48, 55, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center", "incident"])
    central_line(model, X_21, X_84, 21, 84, incident=True)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_41, X_184, 41, 184, incident=True)
    return promote_point_to_top(model, X_2208)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2208 on the given reference triangle."""
    model = create_model('X_2208 = X_2-ISOCONJUGATE OF X_329')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02208(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02208.json"))
    write_center_svg(
        model_acute,
        here / "x-02208.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
