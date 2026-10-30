"""GEOMETOR construction model for X(574) = HARMONIC OF X(187)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00574(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(574) = HARMONIC OF X(187) on reference triangle ABC."""
    X_574 = eval_trilinear_point(model, A, B, C, 'a*(a**(2) - 2*b**(2) - 2*c**(2))', ID="X(574)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_2, X_99, 2, 99, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_353 = point_from_barycentrics(model, A, B, C, 0.31964876, 0.38714151, 0.29320973, ID="X(353)", classes=["center", "incident"])
    central_line(model, X_110, X_353, 110, 353, incident=True)
    return promote_point_to_top(model, X_574)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(574) on the given reference triangle."""
    model = create_model('X(574) = HARMONIC OF X(187)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00574(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00574.json"))
    write_center_svg(
        model_acute,
        here / "x-00574.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
