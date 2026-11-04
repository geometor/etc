"""GEOMETOR construction model for X_2169 = X_2-ISOCONJUGATE OF X_53."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02169(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2169 = X_2-ISOCONJUGATE OF X_53 on reference triangle ABC."""
    X_2167 = eval_trilinear_point(model, A, B, C, '(1/(sin(2*B) + sin(2*C)))', ID="X_2167", classes=["center"])
    X_2148 = eval_trilinear_point(model, A, B, C, 'a*sec(B - C)', ID="X_2148", classes=["center"])
    X_2169 = ceva_conjugate(model, A, B, C, X_2167, X_2148, ID="X_2169", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_36, X_54, 36, 54, incident=True)
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_47, X_48, 47, 48, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1748 = eval_trilinear_point(model, A, B, C, 'cot(A) - tan(A)', ID="X_1748", classes=["center", "incident"])
    central_line(model, X_1, X_1748, 1, 1748, incident=True)
    return promote_point_to_top(model, X_2169)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2169 on the given reference triangle."""
    model = create_model('X_2169 = X_2-ISOCONJUGATE OF X_53')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02169(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02169.json"))
    write_center_svg(
        model_acute,
        here / "x-02169.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
