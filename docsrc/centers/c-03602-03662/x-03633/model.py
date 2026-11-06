"""GEOMETOR construction model for X_3633 = H⁻¹(X_8; M, -1/2)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03633(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3633 = H⁻¹(X_8; M, -1/2) on reference triangle ABC."""
    X_3633 = eval_trilinear_point(model, A, B, C, 'b*c*(5*a - 2*b - 2*c)', ID="X_3633", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_548 = eval_trilinear_point(model, A, B, C, '- cos(B - C) + 6*cos(A)', ID="X_548", classes=["center", "incident"])
    central_line(model, X_40, X_548, 40, 548, incident=True)
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    X_1357 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)*(b - c)**(2)*(a**(2) - (b - c)**(2))**(2)', ID="X_1357", classes=["center", "incident"])
    central_line(model, X_210, X_1357, 210, 1357, incident=True)
    return promote_point_to_top(model, X_3633)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3633 on the given reference triangle."""
    model = create_model('X_3633 = H⁻¹(X_8; M, -1/2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03633(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03633.json"))
    write_center_svg(
        model_acute,
        here / "x-03633.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
