"""GEOMETOR construction model for X(629) = COMPLEMENT OF X(17)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    midpoint,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00629(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(629) = COMPLEMENT OF X(17) on reference triangle ABC."""
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /6)', ID="X(17)", classes=["center"])
    X_627 = point_from_barycentrics(model, A, B, C, 0.44119208, 0.35326848, 0.20553943, ID="X(627)", classes=["center"])
    X_629 = midpoint(model, X_17, X_627, ID="X(629)", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_2, X_17, 2, 17, incident=True)
    X_61 = eval_trilinear_point(model, A, B, C, 'sin(A + pi /6)', ID="X(61)", classes=["center", "incident"])
    X_302 = eval_barycentric_point(model, A, B, C, 'csc(A)*sin(A + pi /6)', ID="X(302)", classes=["center", "incident"])
    central_line(model, X_61, X_302, 61, 302, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_618 = point_from_barycentrics(model, A, B, C, 0.38507388, 0.34992883, 0.26499729, ID="X(618)", classes=["center", "incident"])
    central_line(model, X_5, X_618, 5, 618, incident=True)
    return promote_point_to_top(model, X_629)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(629) on the given reference triangle."""
    model = create_model('X(629) = COMPLEMENT OF X(17)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00629(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00629.json"))
    write_center_svg(
        model_acute,
        here / "x-00629.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
