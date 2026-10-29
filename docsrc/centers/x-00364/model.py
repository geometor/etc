"""GEOMETOR construction model for X(364) = WABASH CENTER."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00364(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(364) = WABASH CENTER on reference triangle ABC."""
    X_364 = eval_trilinear_point(model, A, B, C, 'b**(1/2) + c**(1/2) - a**(1/2)', ID="X(364)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_365 = eval_trilinear_point(model, A, B, C, 'a**(1/2)', ID="X(365)", classes=["center", "incident"])
    central_line(model, X_1, X_365, 1, 365, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_366 = eval_trilinear_point(model, A, B, C, 'a**(-1/2)', ID="X(366)", classes=["center", "incident"])
    central_line(model, X_9, X_366, 9, 366, incident=True)
    return promote_point_to_top(model, X_364)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(364) on the given reference triangle."""
    model = create_model('X(364) = WABASH CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00364(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00364.json"))
    write_center_svg(
        model_acute,
        here / "x-00364.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
