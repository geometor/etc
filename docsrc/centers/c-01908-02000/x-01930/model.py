"""GEOMETOR construction model for X_1930 = BICENTRIC SUM OF PU(14)."""

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
    isotomic_conjugate,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01930(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1930 = BICENTRIC SUM OF PU(14) on reference triangle ABC."""
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center"])
    X_1930 = isotomic_conjugate(model, A, B, C, X_82, ID="X_1930", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_1, X_75, 1, 75, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_150 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) + a*(b*c**(2) +c*b**(2) - b**(3) - c**(3)) - b*c*(a**(2) + b**(2) + c**(2)) + (b + c)*a**(3)))', ID="X_150", classes=["center", "incident"])
    central_line(model, X_8, X_150, 8, 150, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_334 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(a**(2) - b*c)', ID="X_334", classes=["center", "incident"])
    central_line(model, X_76, X_334, 76, 334, incident=True)
    return promote_point_to_top(model, X_1930)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1930 on the given reference triangle."""
    model = create_model('X_1930 = BICENTRIC SUM OF PU(14)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01930(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01930.json"))
    write_center_svg(
        model_acute,
        here / "x-01930.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
