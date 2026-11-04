"""GEOMETOR construction model for X_1049 = TRILINEAR PURE ANGLES CENTER."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01049(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1049 = TRILINEAR PURE ANGLES CENTER on reference triangle ABC."""
    X_1049 = eval_trilinear_point(model, A, B, C, 'A', ID="X_1049", classes=["selected", "target"])
    return promote_point_to_top(model, X_1049)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1049 on the given reference triangle."""
    model = create_model('X_1049 = TRILINEAR PURE ANGLES CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01049(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01049.json"))
    write_center_svg(
        model_acute,
        here / "x-01049.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
