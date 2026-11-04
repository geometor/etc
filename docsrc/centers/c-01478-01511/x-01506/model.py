"""GEOMETOR construction model for X_1506 = INSIMILICENTER OF MOSES AND NINE-POINT CIRCLES."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01506(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1506 = INSIMILICENTER OF MOSES AND NINE-POINT CIRCLES on reference triangle ABC."""
    X_1078 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2)*c**(2) + c**(2)*a**(2) + a**(2)*b**(2) - a**(4)))', ID="X_1078", classes=["center"])
    X_1506 = complement(model, A, B, C, X_1078, ID="X_1506", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /6)', ID="X_17", classes=["center", "incident"])
    central_line(model, X_6, X_17, 6, 17, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_2, X_32, 2, 32, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_5, X_39, 5, 39, incident=True)
    return promote_point_to_top(model, X_1506)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1506 on the given reference triangle."""
    model = create_model('X_1506 = INSIMILICENTER OF MOSES AND NINE-POINT CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01506(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01506.json"))
    write_center_svg(
        model_acute,
        here / "x-01506.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
