"""GEOMETOR construction model for X_2139 = ISOGONAL CONJUGATE OF X_2138."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02139(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2139 = ISOGONAL CONJUGATE OF X_2138 on reference triangle ABC."""
    X_2138 = point_from_barycentrics(model, A, B, C, -0.18550485, -0.37942939, 1.5649342, ID="X_2138", classes=["center"])
    X_2139 = isogonal_conjugate(model, A, B, C, X_2138, ID="X_2139", classes=["selected", "target"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_159 = eval_trilinear_point(model, A, B, C, '(a*((a**(2) + b**(2) + c**(2))*sin(2*A) + (c**(2) - b**(2) - a**(2))*sin(2*B) + (b**(2) - c**(2) - a**(2))*sin(2*C)))', ID="X_159", classes=["center", "incident"])
    central_line(model, X_20, X_159, 20, 159, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_69, X_2138, 69, 2138, incident=True)
    return promote_point_to_top(model, X_2139)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2139 on the given reference triangle."""
    model = create_model('X_2139 = ISOGONAL CONJUGATE OF X_2138')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02139(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02139.json"))
    write_center_svg(
        model_acute,
        here / "x-02139.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
