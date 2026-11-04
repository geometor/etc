"""GEOMETOR construction model for X_2255 = X_2-ISOCONJUGATE OF X_923."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02255(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2255 = X_2-ISOCONJUGATE OF X_923 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_198 = eval_trilinear_point(model, A, B, C, '(a*(cos(B) + cos(C) - cos(A) - 1))', ID="X_198", classes=["center"])
    central_line(model, X_6, X_40, 6, 40)
    central_line(model, X_31, X_198, 31, 198)
    X_2255 = intersect_lines(model, X_6, X_40, X_31, X_198, ID="X_2255", classes=["selected", "target"])
    X_208 = eval_trilinear_point(model, A, B, C, '((1 - sec(A))*(cos(B) + cos(C) - cos(A) - 1))', ID="X_208", classes=["center", "incident"])
    X_608 = eval_trilinear_point(model, A, B, C, 'a*(1 - sec(A))', ID="X_608", classes=["center", "incident"])
    central_line(model, X_208, X_608, 208, 608, incident=True)
    return promote_point_to_top(model, X_2255)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2255 on the given reference triangle."""
    model = create_model('X_2255 = X_2-ISOCONJUGATE OF X_923')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02255(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02255.json"))
    write_center_svg(
        model_acute,
        here / "x-02255.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
