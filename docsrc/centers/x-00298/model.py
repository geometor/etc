"""GEOMETOR construction model for X(298) = ISOTOMIC CONJUGATE OF 1st ISOGONIC CENTER."""

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
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00298(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(298) = ISOTOMIC CONJUGATE OF 1st ISOGONIC CENTER on reference triangle ABC."""
    X_298 = eval_barycentric_point(model, A, B, C, 'csc(A)*sin(A + pi /3)', ID="X(298)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X(14)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_14, X_76, 14, 76, incident=True)
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center", "incident"])
    X_532 = point_from_barycentrics(model, A, B, C, -0.64045027, -0.11837216, 0.75882243, ID="X(532)", classes=["center", "incident"])
    central_line(model, X_13, X_532, 13, 532, incident=True)
    return promote_point_to_top(model, X_298)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(298) on the given reference triangle."""
    model = create_model('X(298) = ISOTOMIC CONJUGATE OF 1st ISOGONIC CENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00298(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00298.json"))
    write_center_svg(
        model_acute,
        here / "x-00298.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
