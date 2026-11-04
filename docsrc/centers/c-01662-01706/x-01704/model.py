"""GEOMETOR construction model for X_1704 = INSIMILICENTER(BEVAN CIRCLE, BROCARD CIRCLE)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01704(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1704 = INSIMILICENTER(BEVAN CIRCLE, BROCARD CIRCLE) on reference triangle ABC."""
    X_1704 = eval_trilinear_point(model, A, B, C, '(2*cos(A - omega ) + e*(1 + cos(A) - cos(B) - cos(C)))', ID="X_1704", classes=["selected", "target"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A- omega )', ID="X_182", classes=["center", "incident"])
    central_line(model, X_40, X_182, 40, 182, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1340 = point_from_barycentrics(model, A, B, C, 0.34709524, 0.36700624, 0.28589852, ID="X_1340", classes=["center", "incident"])
    central_line(model, X_1, X_1340, 1, 1340, incident=True)
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    X_1341 = point_from_barycentrics(model, A, B, C, 0.30653192, 0.35355532, 0.33991277, ID="X_1341", classes=["center", "incident"])
    central_line(model, X_165, X_1341, 165, 1341, incident=True)
    return promote_point_to_top(model, X_1704)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1704 on the given reference triangle."""
    model = create_model('X_1704 = INSIMILICENTER(BEVAN CIRCLE, BROCARD CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01704(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01704.json"))
    write_center_svg(
        model_acute,
        here / "x-01704.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
