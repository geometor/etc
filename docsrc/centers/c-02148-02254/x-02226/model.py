"""GEOMETOR construction model for X_2226 = X_2-ISOCONJUGATE OF X_678."""

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


def construct_x_02226(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2226 = X_2-ISOCONJUGATE OF X_678 on reference triangle ABC."""
    X_679 = eval_trilinear_point(model, A, B, C, '(1/(b + c - 2*a)**(2))', ID="X_679", classes=["center"])
    X_1318 = eval_trilinear_point(model, A, B, C, '(a*(b + c - a)/(b + c - 2*a)**(2))', ID="X_1318", classes=["center"])
    X_2226 = ceva_conjugate(model, A, B, C, X_679, X_1318, ID="X_2226", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    central_line(model, X_44, X_88, 44, 88, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    central_line(model, X_36, X_106, 36, 106, incident=True)
    return promote_point_to_top(model, X_2226)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2226 on the given reference triangle."""
    model = create_model('X_2226 = X_2-ISOCONJUGATE OF X_678')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02226(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02226.json"))
    write_center_svg(
        model_acute,
        here / "x-02226.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
