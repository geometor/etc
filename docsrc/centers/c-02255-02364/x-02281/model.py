"""GEOMETOR construction model for X_2281 = X_2-ISOCONJUGATE OF X_1010."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02281(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2281 = X_2-ISOCONJUGATE OF X_1010 on reference triangle ABC."""
    X_2221 = point_from_barycentrics(model, A, B, C, 0.20882469, 0.32409591, 0.4670794, ID="X_2221", classes=["center"])
    X_1245 = point_from_barycentrics(model, A, B, C, 0.2312025, 0.33122426, 0.43757323, ID="X_1245", classes=["center"])
    X_2281 = ceva_conjugate(model, A, B, C, X_2221, X_1245, ID="X_2281", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_6, X_63, 6, 63, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_32, X_48, 32, 48, incident=True)
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    central_line(model, X_71, X_213, 71, 213, incident=True)
    return promote_point_to_top(model, X_2281)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2281 on the given reference triangle."""
    model = create_model('X_2281 = X_2-ISOCONJUGATE OF X_1010')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02281(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02281.json"))
    write_center_svg(
        model_acute,
        here / "x-02281.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
