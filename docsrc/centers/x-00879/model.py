"""GEOMETOR construction model for X(879) = ISOTOMIC CONJUGATE OF X(877)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00879(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(879) = ISOTOMIC CONJUGATE OF X(877) on reference triangle ABC."""
    X_877 = point_from_barycentrics(model, A, B, C, -0.31137873, 0.061326014, 1.2500527, ID="X(877)", classes=["center"])
    X_879 = isotomic_conjugate(model, A, B, C, X_877, ID="X(879)", classes=["selected", "target"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    central_line(model, X_74, X_98, 74, 98, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X(512)", classes=["center", "incident"])
    central_line(model, X_4, X_512, 4, 512, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X(525)", classes=["center", "incident"])
    central_line(model, X_3, X_525, 3, 525, incident=True)
    return promote_point_to_top(model, X_879)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(879) on the given reference triangle."""
    model = create_model('X(879) = ISOTOMIC CONJUGATE OF X(877)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00879(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00879.json"))
    write_center_svg(
        model_acute,
        here / "x-00879.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
