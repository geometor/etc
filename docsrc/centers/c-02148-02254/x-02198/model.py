"""GEOMETOR construction model for X_2198 = X_2-ISOCONJUGATE OF X_272."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02198(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2198 = X_2-ISOCONJUGATE OF X_272 on reference triangle ABC."""
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center"])
    central_line(model, X_31, X_32, 31, 32)
    central_line(model, X_37, X_65, 37, 65)
    X_2198 = intersect_lines(model, X_31, X_32, X_37, X_65, ID="X_2198", classes=["selected", "target"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    X_672 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c))', ID="X_672", classes=["center", "incident"])
    central_line(model, X_72, X_672, 72, 672, incident=True)
    return promote_point_to_top(model, X_2198)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2198 on the given reference triangle."""
    model = create_model('X_2198 = X_2-ISOCONJUGATE OF X_272')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02198(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02198.json"))
    write_center_svg(
        model_acute,
        here / "x-02198.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
