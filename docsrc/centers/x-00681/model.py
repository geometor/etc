"""GEOMETOR construction model for X(681) = TRILINEAR POLE OF LINE X(6)X(158)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00681(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(681) = TRILINEAR POLE OF LINE X(6)X(158) on reference triangle ABC."""
    X_680 = point_from_barycentrics(model, A, B, C, 0.54558558, 0.25327972, -0.7988653, ID="X(680)", classes=["center"])
    X_681 = isogonal_conjugate(model, A, B, C, X_680, ID="X(681)", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_823 = eval_trilinear_point(model, A, B, C, '1/(csc(B/2) - csc(C/2))', ID="X(823)", classes=["center", "incident"])
    central_line(model, X_110, X_823, 110, 823, incident=True)
    return promote_point_to_top(model, X_681)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(681) on the given reference triangle."""
    model = create_model('X(681) = TRILINEAR POLE OF LINE X(6)X(158)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00681(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00681.json"))
    write_center_svg(
        model_acute,
        here / "x-00681.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
