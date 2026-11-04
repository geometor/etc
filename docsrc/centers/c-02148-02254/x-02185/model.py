"""GEOMETOR construction model for X_2185 = X_2-ISOCONJUGATE OF X_181."""

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


def construct_x_02185(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2185 = X_2-ISOCONJUGATE OF X_181 on reference triangle ABC."""
    X_2171 = eval_trilinear_point(model, A, B, C, '(b + c)**(2)/(b + c - a)', ID="X_2171", classes=["center"])
    X_2185 = isogonal_conjugate(model, A, B, C, X_2171, ID="X_2185", classes=["selected", "target"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_21, X_60, 21, 60, incident=True)
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    central_line(model, X_27, X_86, 27, 86, incident=True)
    X_261 = eval_trilinear_point(model, A, B, C, '(((csc(A))*(sec(B/2 - C/2)))**(2))', ID="X_261", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    central_line(model, X_261, X_284, 261, 284, incident=True)
    return promote_point_to_top(model, X_2185)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2185 on the given reference triangle."""
    model = create_model('X_2185 = X_2-ISOCONJUGATE OF X_181')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02185(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02185.json"))
    write_center_svg(
        model_acute,
        here / "x-02185.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
