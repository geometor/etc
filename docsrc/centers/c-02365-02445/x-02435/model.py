"""GEOMETOR construction model for X_2435 = ISOGONAL CONJUGATE OF X_2409."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02435(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2435 = ISOGONAL CONJUGATE OF X_2409 on reference triangle ABC."""
    X_2409 = point_from_barycentrics(model, A, B, C, -0.074912795, 0.079939185, 0.99497361, ID="X_2409", classes=["center"])
    X_2435 = isogonal_conjugate(model, A, B, C, X_2409, ID="X_2435", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X_520", classes=["center", "incident"])
    central_line(model, X_6, X_520, 6, 520, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_4, X_525, 4, 525, incident=True)
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_64, X_512, 64, 512, incident=True)
    return promote_point_to_top(model, X_2435)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2435 on the given reference triangle."""
    model = create_model('X_2435 = ISOGONAL CONJUGATE OF X_2409')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02435(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02435.json"))
    write_center_svg(
        model_acute,
        here / "x-02435.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
