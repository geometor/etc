"""GEOMETOR construction model for X(491) = CEVAPOINT OF X(2) AND X(487)."""

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
    isotomic_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00491(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(491) = CEVAPOINT OF X(2) AND X(487) on reference triangle ABC."""
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A + pi /4)', ID="X(486)", classes=["center"])
    X_491 = isotomic_conjugate(model, A, B, C, X_486, ID="X(491)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_487 = point_from_barycentrics(model, A, B, C, -1.1839423, 1.1273575, 1.0565848, ID="X(487)", classes=["center", "incident"])
    central_line(model, X_4, X_487, 4, 487, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_490 = point_from_barycentrics(model, A, B, C, 0.61185907, 0.42830629, -0.040165363, ID="X(490)", classes=["center", "incident"])
    central_line(model, X_3, X_490, 3, 490, incident=True)
    return promote_point_to_top(model, X_491)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(491) on the given reference triangle."""
    model = create_model('X(491) = CEVAPOINT OF X(2) AND X(487)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00491(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00491.json"))
    write_center_svg(
        model_acute,
        here / "x-00491.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
