"""GEOMETOR construction model for X(180) = 2nd AJIMA-MALFATTI POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00180(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(180) = 2nd AJIMA-MALFATTI POINT on reference triangle ABC."""
    X_180 = point_from_barycentrics(model, A, B, C, 0.24857469, 0.32040764, 0.43101767, ID="X(180)", classes=["selected", "target"])
    X_173 = eval_trilinear_point(model, A, B, C, 'cos(B/2) + cos(C/2) - cos(A/2)', ID="X(173)", classes=["center", "incident"])
    X_483 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(A/2))', ID="X(483)", classes=["center", "incident"])
    central_line(model, X_173, X_483, 173, 483, incident=True)
    return promote_point_to_top(model, X_180)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(180) on the given reference triangle."""
    model = create_model('X(180) = 2nd AJIMA-MALFATTI POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00180(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00180.json"))
    write_center_svg(
        model_acute,
        here / "x-00180.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
