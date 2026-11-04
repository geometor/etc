"""GEOMETOR construction model for X_1957 = CROSSSUM OF PU(22)."""

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


def construct_x_01957(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1957 = CROSSSUM OF PU(22) on reference triangle ABC."""
    X_1910 = eval_trilinear_point(model, A, B, C, '(a/(a**(2)*cos(B)*cos(C) - b*c*(cos(A))**(2)))', ID="X_1910", classes=["center"])
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A +  omega  )', ID="X_240", classes=["center"])
    X_1957 = ceva_conjugate(model, A, B, C, X_1910, X_240, ID="X_1957", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    central_line(model, X_31, X_92, 31, 92, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_204 = eval_trilinear_point(model, A, B, C, '((tan(A))*(tan(B) + tan(C) - tan(A)))', ID="X_204", classes=["center", "incident"])
    central_line(model, X_1, X_204, 1, 204, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_63, X_240, 63, 240, incident=True)
    return promote_point_to_top(model, X_1957)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1957 on the given reference triangle."""
    model = create_model('X_1957 = CROSSSUM OF PU(22)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01957(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01957.json"))
    write_center_svg(
        model_acute,
        here / "x-01957.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
