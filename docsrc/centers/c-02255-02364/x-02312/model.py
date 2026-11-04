"""GEOMETOR construction model for X_2312 = X_2-ISOCONJUGATE OF X_1297."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02312(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2312 = X_2-ISOCONJUGATE OF X_1297 on reference triangle ABC."""
    X_293 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(A +  omega  )', ID="X_293", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_2312 = ceva_conjugate(model, A, B, C, X_293, X_31, ID="X_2312", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_19, X_31, 19, 31, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_38, X_48, 38, 48, incident=True)
    X_198 = eval_trilinear_point(model, A, B, C, '(a*(cos(B) + cos(C) - cos(A) - 1))', ID="X_198", classes=["center", "incident"])
    X_199 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) - a**(4) + (b**(2) + c**(2) - a**(2))*(b*c + c*a + a*b)))', ID="X_199", classes=["center", "incident"])
    central_line(model, X_198, X_199, 198, 199, incident=True)
    return promote_point_to_top(model, X_2312)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2312 on the given reference triangle."""
    model = create_model('X_2312 = X_2-ISOCONJUGATE OF X_1297')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02312(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02312.json"))
    write_center_svg(
        model_acute,
        here / "x-02312.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
