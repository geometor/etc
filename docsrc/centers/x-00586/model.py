"""GEOMETOR construction model for X(586) = 2nd CONGRUENT SHRUNK INSQUARES POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00586(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(586) = 2nd CONGRUENT SHRUNK INSQUARES POINT on reference triangle ABC."""
    X_586 = eval_trilinear_point(model, A, B, C, '(2*area*(1/b + 1/c - 1/a) + a - b - c)/a', ID="X(586)", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X(192)", classes=["center", "incident"])
    central_line(model, X_8, X_192, 8, 192, incident=True)
    return promote_point_to_top(model, X_586)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(586) on the given reference triangle."""
    model = create_model('X(586) = 2nd CONGRUENT SHRUNK INSQUARES POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00586(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00586.json"))
    write_center_svg(
        model_acute,
        here / "x-00586.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
