"""GEOMETOR construction model for X_1926 = CROSSDIFFERENCE OF PU(13)."""

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


def construct_x_01926(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1926 = CROSSDIFFERENCE OF PU(13) on reference triangle ABC."""
    X_1926 = eval_trilinear_point(model, A, B, C, '(1 - b**(2)*c**(2)/a**(4))', ID="X_1926", classes=["selected", "target"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_38, X_75, 38, 75, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_257 = eval_trilinear_point(model, A, B, C, '1/(a**(3) + a*b*c)', ID="X_257", classes=["center", "incident"])
    central_line(model, X_76, X_257, 76, 257, incident=True)
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center", "incident"])
    X_786 = eval_trilinear_point(model, A, B, C, '(a **(-4)*(b **(-1) - c **(-1)) + a **(-2)*(b **(-3) - c **(-3)))', ID="X_786", classes=["center", "incident"])
    central_line(model, X_661, X_786, 661, 786, incident=True)
    return promote_point_to_top(model, X_1926)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1926 on the given reference triangle."""
    model = create_model('X_1926 = CROSSDIFFERENCE OF PU(13)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01926(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01926.json"))
    write_center_svg(
        model_acute,
        here / "x-01926.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
