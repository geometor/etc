"""GEOMETOR construction model for X(587) = POINT ARCTURUS."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00587(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(587) = POINT ARCTURUS on reference triangle ABC."""
    X_587 = point_from_barycentrics(model, A, B, C, 0.25159642, 0.27841635, 0.46998723, ID="X(587)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center", "incident"])
    central_line(model, X_2, X_92, 2, 92, incident=True)
    return promote_point_to_top(model, X_587)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(587) on the given reference triangle."""
    model = create_model('X(587) = POINT ARCTURUS')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00587(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00587.json"))
    write_center_svg(
        model_acute,
        here / "x-00587.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
