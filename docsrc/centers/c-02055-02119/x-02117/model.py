"""GEOMETOR construction model for X_2117 = X_2-ISOCONJUGATE OF X_2116."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02117(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2117 = X_2-ISOCONJUGATE OF X_2116 on reference triangle ABC."""
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center"])
    X_2116 = point_from_barycentrics(model, A, B, C, 0.43264106, -0.77002375, 1.3373827, ID="X_2116", classes=["center"])
    X_672 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c))', ID="X_672", classes=["center"])
    X_2110 = eval_trilinear_point(model, A, B, C, '(a*((b**(2) + b*c + c**(2))*a**(3) - (b + c)*(b**(2) + c**(2))*a**(2) - b*c*(b**(2) - b*c + c**(2))*a + b**(2)*c**(2)*(b + c)))', ID="X_2110", classes=["center"])
    central_line(model, X_238, X_2116, 238, 2116)
    central_line(model, X_672, X_2110, 672, 2110)
    X_2117 = intersect_lines(model, X_238, X_2116, X_672, X_2110, ID="X_2117", classes=["selected", "target"])
    X_2106 = eval_trilinear_point(model, A, B, C, '((a + b)*(a + c)*(b**(2)*c**(2) - a**(2)*b**(2) - a**(2)*c**(2) + a*b*c*(b + c - a)))', ID="X_2106", classes=["center", "incident"])
    X_2114 = point_from_barycentrics(model, A, B, C, 0.30214425, -0.63937622, 1.337232, ID="X_2114", classes=["center", "incident"])
    central_line(model, X_2106, X_2114, 2106, 2114, incident=True)
    return promote_point_to_top(model, X_2117)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2117 on the given reference triangle."""
    model = create_model('X_2117 = X_2-ISOCONJUGATE OF X_2116')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02117(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02117.json"))
    write_center_svg(
        model_acute,
        here / "x-02117.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
