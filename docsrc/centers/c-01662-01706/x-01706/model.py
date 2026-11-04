"""GEOMETOR construction model for X_1706 = EXSIMILICENTER(BEVAN CIRCLE, SPIEKER CIRCLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01706(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1706 = EXSIMILICENTER(BEVAN CIRCLE, SPIEKER CIRCLE) on reference triangle ABC."""
    X_1706 = eval_trilinear_point(model, A, B, C, '(b*c*(2*(b + c) - a*(cos(A) - cos(B) - cos(C) + 1)))', ID="X_1706", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_8, X_57, 8, 57, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_200 = eval_trilinear_point(model, A, B, C, '(cot(A/2))**(2)', ID="X_200", classes=["center", "incident"])
    central_line(model, X_65, X_200, 65, 200, incident=True)
    return promote_point_to_top(model, X_1706)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1706 on the given reference triangle."""
    model = create_model('X_1706 = EXSIMILICENTER(BEVAN CIRCLE, SPIEKER CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01706(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01706.json"))
    write_center_svg(
        model_acute,
        here / "x-01706.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
