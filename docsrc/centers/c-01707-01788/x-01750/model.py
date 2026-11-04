"""GEOMETOR construction model for X_1750 = MIMOSA TRANSFORM OF X_268."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01750(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1750 = MIMOSA TRANSFORM OF X_268 on reference triangle ABC."""
    X_282 = eval_trilinear_point(model, A, B, C, '(cot(A/2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X_282", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1750 = ceva_conjugate(model, A, B, C, X_282, X_1, ID="X_1750", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_9, X_165, 9, 165, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    central_line(model, X_40, X_210, 40, 210, incident=True)
    return promote_point_to_top(model, X_1750)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1750 on the given reference triangle."""
    model = create_model('X_1750 = MIMOSA TRANSFORM OF X_268')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01750(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01750.json"))
    write_center_svg(
        model_acute,
        here / "x-01750.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
