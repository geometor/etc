"""GEOMETOR construction model for X_871 = ISOTOMIC CONJUGATE OF X_869."""

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
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00871(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_871 = ISOTOMIC CONJUGATE OF X_869 on reference triangle ABC."""
    X_869 = point_from_barycentrics(model, A, B, C, 0.22475648, 0.33333333, 0.44191018, ID="X_869", classes=["center"])
    X_871 = isotomic_conjugate(model, A, B, C, X_869, ID="X_871", classes=["selected", "target"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_335 = eval_trilinear_point(model, A, B, C, 'b*c/(a**(2) - b*c)', ID="X_335", classes=["center", "incident"])
    central_line(model, X_76, X_335, 76, 335, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_561 = eval_trilinear_point(model, A, B, C, 'a **(- 4)', ID="X_561", classes=["center", "incident"])
    central_line(model, X_2, X_561, 2, 561, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_700 = point_from_barycentrics(model, A, B, C, 0.79085004, -0.21959226, -0.57125778, ID="X_700", classes=["center", "incident"])
    central_line(model, X_75, X_700, 75, 700, incident=True)
    return promote_point_to_top(model, X_871)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_871 on the given reference triangle."""
    model = create_model('X_871 = ISOTOMIC CONJUGATE OF X_869')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00871(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00871.json"))
    write_center_svg(
        model_acute,
        here / "x-00871.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
