"""GEOMETOR construction model for X_2167 = X_2-ISOCONJUGATE OF X_51."""

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


def construct_x_02167(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2167 = X_2-ISOCONJUGATE OF X_51 on reference triangle ABC."""
    X_1953 = eval_trilinear_point(model, A, B, C, 'sin(2*B) + sin(2*C)', ID="X_1953", classes=["center"])
    X_2167 = isogonal_conjugate(model, A, B, C, X_1953, ID="X_2167", classes=["selected", "target"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    central_line(model, X_54, X_72, 54, 72, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    central_line(model, X_48, X_92, 48, 92, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_293 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(A +  omega  )', ID="X_293", classes=["center", "incident"])
    central_line(model, X_38, X_293, 38, 293, incident=True)
    return promote_point_to_top(model, X_2167)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2167 on the given reference triangle."""
    model = create_model('X_2167 = X_2-ISOCONJUGATE OF X_51')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02167(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02167.json"))
    write_center_svg(
        model_acute,
        here / "x-02167.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
