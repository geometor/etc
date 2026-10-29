"""GEOMETOR construction model for X(626) = COMPLEMENT OF X(32)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00626(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(626) = COMPLEMENT OF X(32) on reference triangle ABC."""
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center"])
    X_626 = complement(model, A, B, C, X_32, ID="X(626)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_2, X_32, 2, 32, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_114 = point_from_barycentrics(model, A, B, C, 0.37082211, -0.060960354, 0.69013825, ID="X(114)", classes=["center", "incident"])
    central_line(model, X_3, X_114, 3, 114, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_5, X_141, 5, 141, incident=True)
    return promote_point_to_top(model, X_626)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(626) on the given reference triangle."""
    model = create_model('X(626) = COMPLEMENT OF X(32)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00626(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00626.json"))
    write_center_svg(
        model_acute,
        here / "x-00626.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
