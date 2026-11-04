"""GEOMETOR construction model for X_2149 = X_2-ISOCONJUGATE OF X_11."""

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


def construct_x_02149(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2149 = X_2-ISOCONJUGATE OF X_11 on reference triangle ABC."""
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X_59", classes=["center"])
    X_1110 = eval_trilinear_point(model, A, B, C, '((a/(b - c))**(2))', ID="X_1110", classes=["center"])
    X_2149 = ceva_conjugate(model, A, B, C, X_59, X_1110, ID="X_2149", classes=["selected", "target"])
    X_672 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c))', ID="X_672", classes=["center", "incident"])
    central_line(model, X_59, X_672, 59, 672, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_652 = eval_trilinear_point(model, A, B, C, 'sec(B) - sec(C)', ID="X_652", classes=["center", "incident"])
    central_line(model, X_101, X_652, 101, 652, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center", "incident"])
    central_line(model, X_109, X_649, 109, 649, incident=True)
    return promote_point_to_top(model, X_2149)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2149 on the given reference triangle."""
    model = create_model('X_2149 = X_2-ISOCONJUGATE OF X_11')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02149(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02149.json"))
    write_center_svg(
        model_acute,
        here / "x-02149.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
