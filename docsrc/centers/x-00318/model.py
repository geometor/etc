"""GEOMETOR construction model for X(318) = ISOTOMIC CONJUGATE OF X(77)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00318(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(318) = ISOTOMIC CONJUGATE OF X(77) on reference triangle ABC."""
    X_318 = eval_trilinear_point(model, A, B, C, '(1 + sec(A))/a**(2)', ID="X(318)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    central_line(model, X_4, X_8, 4, 8, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    central_line(model, X_29, X_33, 29, 33, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_158 = point_from_barycentrics(model, A, B, C, 0.04776757, 0.099240104, 0.85299233, ID="X(158)", classes=["center", "incident"])
    central_line(model, X_10, X_158, 10, 158, incident=True)
    return promote_point_to_top(model, X_318)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(318) on the given reference triangle."""
    model = create_model('X(318) = ISOTOMIC CONJUGATE OF X(77)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00318(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00318.json"))
    write_center_svg(
        model_acute,
        here / "x-00318.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
