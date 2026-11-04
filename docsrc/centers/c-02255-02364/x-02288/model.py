"""GEOMETOR construction model for X_2288 = X_2-ISOCONJUGATE OF X_1065."""

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
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02288(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2288 = X_2-ISOCONJUGATE OF X_1065 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    central_line(model, X_6, X_19, 6, 19)
    central_line(model, X_32, X_48, 32, 48)
    X_2288 = intersect_lines(model, X_6, X_19, X_32, X_48, ID="X_2288", classes=["selected", "target"])
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X_216", classes=["center", "incident"])
    X_1195 = point_from_barycentrics(model, A, B, C, 0.19476988, 0.33920828, 0.46602184, ID="X_1195", classes=["center", "incident"])
    central_line(model, X_216, X_1195, 216, 1195, incident=True)
    return promote_point_to_top(model, X_2288)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2288 on the given reference triangle."""
    model = create_model('X_2288 = X_2-ISOCONJUGATE OF X_1065')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02288(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02288.json"))
    write_center_svg(
        model_acute,
        here / "x-02288.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
