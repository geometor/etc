"""GEOMETOR construction model for X_2180 = X_2-ISOCONJUGATE OF X_96."""

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


def construct_x_02180(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2180 = X_2-ISOCONJUGATE OF X_96 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_1953 = eval_trilinear_point(model, A, B, C, 'sin(2*B) + sin(2*C)', ID="X_1953", classes=["center"])
    X_2180 = ceva_conjugate(model, A, B, C, X_19, X_1953, ID="X_2180", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_31, X_48, 31, 48, incident=True)
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X_91", classes=["center", "incident"])
    central_line(model, X_19, X_91, 19, 91, incident=True)
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    X_563 = eval_trilinear_point(model, A, B, C, 'sin(4*A)', ID="X_563", classes=["center", "incident"])
    central_line(model, X_47, X_563, 47, 563, incident=True)
    return promote_point_to_top(model, X_2180)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2180 on the given reference triangle."""
    model = create_model('X_2180 = X_2-ISOCONJUGATE OF X_96')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02180(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02180.json"))
    write_center_svg(
        model_acute,
        here / "x-02180.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
