"""GEOMETOR construction model for X_2190 = X_2-ISOCONJUGATE OF X_216."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02190(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2190 = X_2-ISOCONJUGATE OF X_216 on reference triangle ABC."""
    X_2190 = eval_trilinear_point(model, A, B, C, 'sec(A)*sec(B - C)', ID="X_2190", classes=["selected", "target"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_54, X_65, 54, 65, incident=True)
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X_91", classes=["center", "incident"])
    central_line(model, X_47, X_91, 47, 91, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_158 = eval_trilinear_point(model, A, B, C, '(sec(A))**(2)', ID="X_158", classes=["center", "incident"])
    central_line(model, X_31, X_158, 31, 158, incident=True)
    return promote_point_to_top(model, X_2190)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2190 on the given reference triangle."""
    model = create_model('X_2190 = X_2-ISOCONJUGATE OF X_216')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02190(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02190.json"))
    write_center_svg(
        model_acute,
        here / "x-02190.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
