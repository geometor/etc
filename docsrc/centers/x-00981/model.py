"""GEOMETOR construction model for X(981) = ISOGONAL CONJUGATE OF X(980)."""

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
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00981(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(981) = ISOGONAL CONJUGATE OF X(980) on reference triangle ABC."""
    X_980 = point_from_barycentrics(model, A, B, C, 0.29311432, 0.33946795, 0.36741773, ID="X(980)", classes=["center"])
    X_981 = isogonal_conjugate(model, A, B, C, X_980, ID="X(981)", classes=["selected", "target"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    central_line(model, X_21, X_32, 21, 32, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X(213)", classes=["center", "incident"])
    central_line(model, X_8, X_213, 8, 213, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_314 = point_from_barycentrics(model, A, B, C, 0.47638074, 0.32254946, 0.20106979, ID="X(314)", classes=["center", "incident"])
    central_line(model, X_6, X_314, 6, 314, incident=True)
    return promote_point_to_top(model, X_981)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(981) on the given reference triangle."""
    model = create_model('X(981) = ISOGONAL CONJUGATE OF X(980)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00981(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00981.json"))
    write_center_svg(
        model_acute,
        here / "x-00981.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
