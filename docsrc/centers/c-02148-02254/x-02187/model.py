"""GEOMETOR construction model for X_2187 = X_2-ISOCONJUGATE OF X_189."""

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


def construct_x_02187(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2187 = X_2-ISOCONJUGATE OF X_189 on reference triangle ABC."""
    X_309 = eval_trilinear_point(model, A, B, C, '((csc(A))**(2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X_309", classes=["center"])
    X_2187 = isogonal_conjugate(model, A, B, C, X_309, ID="X_2187", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_25, X_41, 25, 41, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_48, X_55, 48, 55, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_31, X_184, 31, 184, incident=True)
    return promote_point_to_top(model, X_2187)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2187 on the given reference triangle."""
    model = create_model('X_2187 = X_2-ISOCONJUGATE OF X_189')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02187(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02187.json"))
    write_center_svg(
        model_acute,
        here / "x-02187.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
