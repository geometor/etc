"""GEOMETOR construction model for X_2152 = X_2-ISOCONJUGATE OF X_14."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02152(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2152 = X_2-ISOCONJUGATE OF X_14 on reference triangle ABC."""
    X_2152 = eval_trilinear_point(model, A, B, C, 'sin(A)*sin(A -  pi  /3)', ID="X_2152", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_31, X_48, 31, 48, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1094 = eval_trilinear_point(model, A, B, C, '((sin(A +  pi  /3))**(2))', ID="X_1094", classes=["center", "incident"])
    central_line(model, X_1, X_1094, 1, 1094, incident=True)
    X_2154 = eval_trilinear_point(model, A, B, C, '(sin(A)*csc(A -  pi  /3))', ID="X_2154", classes=["center", "incident"])
    X_2173 = eval_trilinear_point(model, A, B, C, 'a*(cos(A) - 2*cos(B)*cos(C))', ID="X_2173", classes=["center", "incident"])
    central_line(model, X_2154, X_2173, 2154, 2173, incident=True)
    return promote_point_to_top(model, X_2152)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2152 on the given reference triangle."""
    model = create_model('X_2152 = X_2-ISOCONJUGATE OF X_14')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02152(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02152.json"))
    write_center_svg(
        model_acute,
        here / "x-02152.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
