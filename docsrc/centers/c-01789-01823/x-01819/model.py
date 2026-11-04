"""GEOMETOR construction model for X_1819 = INVERSE MIMOSA TRANSFORM OF X_1498."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01819(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1819 = INVERSE MIMOSA TRANSFORM OF X_1498 on reference triangle ABC."""
    X_1792 = point_from_barycentrics(model, A, B, C, 0.64689234, 0.29959202, 0.053515639, ID="X_1792", classes=["center"])
    X_283 = eval_trilinear_point(model, A, B, C, '(cos(A))/(cos(B) + cos(C))', ID="X_283", classes=["center"])
    X_1819 = ceva_conjugate(model, A, B, C, X_1792, X_283, ID="X_1819", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_9, X_21, 9, 21, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    central_line(model, X_3, X_49, 3, 49, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_1167 = point_from_barycentrics(model, A, B, C, 0.35929716, 0.32223282, 0.31847002, ID="X_1167", classes=["center", "incident"])
    central_line(model, X_58, X_1167, 58, 1167, incident=True)
    return promote_point_to_top(model, X_1819)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1819 on the given reference triangle."""
    model = create_model('X_1819 = INVERSE MIMOSA TRANSFORM OF X_1498')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01819(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01819.json"))
    write_center_svg(
        model_acute,
        here / "x-01819.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
