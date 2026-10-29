"""GEOMETOR construction model for X(444) = EULER LINE INTERCEPT OF LINE X(19)X(232)."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00444(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(444) = EULER LINE INTERCEPT OF LINE X(19)X(232) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center"])
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A + omega )', ID="X(232)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_19, X_232, 19, 232)
    X_444 = intersect_lines(model, X_2, X_3, X_19, X_232, ID="X(444)", classes=["selected", "target"])
    return promote_point_to_top(model, X_444)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(444) on the given reference triangle."""
    model = create_model('X(444) = EULER LINE INTERCEPT OF LINE X(19)X(232)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00444(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00444.json"))
    write_center_svg(
        model_acute,
        here / "x-00444.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
