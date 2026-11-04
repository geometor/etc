"""GEOMETOR construction model for X_2639 = CROSSSUM OF PU(77)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02639(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2639 = CROSSSUM OF PU(77) on reference triangle ABC."""
    X_2639 = eval_trilinear_point(model, A, B, C, '(1/((sec(A) - sec(B))*(sec(A) - sec(C))) - 1/(sec(B) - sec(C))**(2))', ID="X_2639", classes=["selected", "target"])
    X_652 = eval_trilinear_point(model, A, B, C, 'sec(B) - sec(C)', ID="X_652", classes=["center", "incident"])
    X_653 = eval_trilinear_point(model, A, B, C, '1/(sec(B) - sec(C))', ID="X_653", classes=["center", "incident"])
    central_line(model, X_652, X_653, 652, 653, incident=True)
    return promote_point_to_top(model, X_2639)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2639 on the given reference triangle."""
    model = create_model('X_2639 = CROSSSUM OF PU(77)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02639(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02639.json"))
    write_center_svg(
        model_acute,
        here / "x-02639.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
