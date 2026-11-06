"""GEOMETOR construction model for X_3315 = INTERSECTION OF LINES X_1X_88 AND X_105X_110."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03315(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3315 = INTERSECTION OF LINES X_1X_88 AND X_105X_110 on reference triangle ABC."""
    X_3315 = eval_trilinear_point(model, A, B, C, '((a - b)*(a - c) + 2*(b - c)**(2))', ID="X_3315", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    central_line(model, X_1, X_88, 1, 88, incident=True)
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_105, X_110, 105, 110, incident=True)
    X_149 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(3) + c**(3) - a**(3) + (a**(2) - b*c)*(b + c) + a*(b*c - b**(2) - c**(2))))', ID="X_149", classes=["center", "incident"])
    X_1086 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)**(2))', ID="X_1086", classes=["center", "incident"])
    central_line(model, X_149, X_1086, 149, 1086, incident=True)
    return promote_point_to_top(model, X_3315)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3315 on the given reference triangle."""
    model = create_model('X_3315 = INTERSECTION OF LINES X_1X_88 AND X_105X_110')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03315(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03315.json"))
    write_center_svg(
        model_acute,
        here / "x-03315.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
