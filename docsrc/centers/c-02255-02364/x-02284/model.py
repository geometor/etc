"""GEOMETOR construction model for X_2284 = X_2-ISOCONJUGATE OF X_1027."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02284(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2284 = X_2-ISOCONJUGATE OF X_1027 on reference triangle ABC."""
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X_665", classes=["center"])
    X_672 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c))', ID="X_672", classes=["center"])
    X_2284 = cevapoint(model, A, B, C, X_665, X_672, ID="X_2284", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_692 = eval_trilinear_point(model, A, B, C, 'a**(2)/(b - c)', ID="X_692", classes=["center", "incident"])
    central_line(model, X_101, X_692, 101, 692, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    X_644 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b - c))', ID="X_644", classes=["center", "incident"])
    central_line(model, X_190, X_644, 190, 644, incident=True)
    return promote_point_to_top(model, X_2284)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2284 on the given reference triangle."""
    model = create_model('X_2284 = X_2-ISOCONJUGATE OF X_1027')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02284(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02284.json"))
    write_center_svg(
        model_acute,
        here / "x-02284.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
