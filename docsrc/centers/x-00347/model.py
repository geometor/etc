"""GEOMETOR construction model for X(347) = ISOTOMIC CONJUGATE OF X(280)."""

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
    gergonne_point_of,
    incenter_of,
    isotomic_conjugate,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00347(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(347) = ISOTOMIC CONJUGATE OF X(280) on reference triangle ABC."""
    X_280 = point_from_barycentrics(model, A, B, C, -0.15770609, -0.1827957, 1.3405018, ID="X(280)", classes=["center"])
    X_347 = isotomic_conjugate(model, A, B, C, X_280, ID="X(347)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center", "incident"])
    central_line(model, X_2, X_92, 2, 92, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_253 = point_from_barycentrics(model, A, B, C, -23.560976, -29.731707, 54.292683, ID="X(253)", classes=["center", "incident"])
    central_line(model, X_8, X_253, 8, 253, incident=True)
    return promote_point_to_top(model, X_347)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(347) on the given reference triangle."""
    model = create_model('X(347) = ISOTOMIC CONJUGATE OF X(280)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00347(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00347.json"))
    write_center_svg(
        model_acute,
        here / "x-00347.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
