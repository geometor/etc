"""GEOMETOR construction model for X_2113 = X_2-ISOCONJUGATE OF X_2112."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02113(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2113 = X_2-ISOCONJUGATE OF X_2112 on reference triangle ABC."""
    X_2113 = eval_trilinear_point(model, A, B, C, '(1/(a**(4) - b*c*a**(2) - (b**(3) + c**(3))*a + 2*b**(2)*c**(2)))', ID="X_2113", classes=["selected", "target"])
    X_672 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c))', ID="X_672", classes=["center", "incident"])
    X_1282 = point_from_barycentrics(model, A, B, C, 0.61507937, -0.97619048, 1.3611111, ID="X_1282", classes=["center", "incident"])
    central_line(model, X_672, X_1282, 672, 1282, incident=True)
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    X_2112 = eval_trilinear_point(model, A, B, C, '(a*(a**(4) - b*c*a**(2) - (b**(3) + c**(3))*a + 2*b**(2)*c**(2)))', ID="X_2112", classes=["center", "incident"])
    central_line(model, X_238, X_2112, 238, 2112, incident=True)
    X_1931 = eval_trilinear_point(model, A, B, C, '(((b + c)**(2) - (a + b)*(a + c))/(b + c))', ID="X_1931", classes=["center", "incident"])
    X_2110 = eval_trilinear_point(model, A, B, C, '(a*((b**(2) + b*c + c**(2))*a**(3) - (b + c)*(b**(2) + c**(2))*a**(2) - b*c*(b**(2) - b*c + c**(2))*a + b**(2)*c**(2)*(b + c)))', ID="X_2110", classes=["center", "incident"])
    central_line(model, X_1931, X_2110, 1931, 2110, incident=True)
    return promote_point_to_top(model, X_2113)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2113 on the given reference triangle."""
    model = create_model('X_2113 = X_2-ISOCONJUGATE OF X_2112')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02113(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02113.json"))
    write_center_svg(
        model_acute,
        here / "x-02113.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
