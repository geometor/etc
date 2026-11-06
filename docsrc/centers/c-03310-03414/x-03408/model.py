"""GEOMETOR construction model for X_3408 = TAN(A + 2ω) POINT."""

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


def construct_x_03408(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3408 = TAN(A + 2ω) POINT on reference triangle ABC."""
    X_3408 = eval_trilinear_point(model, A, B, C, '(tan(A + 2*omega  ))', ID="X_3408", classes=["selected", "target"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_1934 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2)/(a**(4) - b**(2)*c**(2)))', ID="X_1934", classes=["center", "incident"])
    central_line(model, X_63, X_1934, 63, 1934, incident=True)
    return promote_point_to_top(model, X_3408)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3408 on the given reference triangle."""
    model = create_model('X_3408 = TAN(A + 2ω) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03408(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03408.json"))
    write_center_svg(
        model_acute,
        here / "x-03408.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
