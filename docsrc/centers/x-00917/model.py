"""GEOMETOR construction model for X(917) = X(516)-CROSS CONJUGATE OF X(4)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00917(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(917) = X(516)-CROSS CONJUGATE OF X(4) on reference triangle ABC."""
    X_916 = point_from_barycentrics(model, A, B, C, 0.80066716, -0.26177284, -0.53889432, ID="X(916)", classes=["center"])
    X_917 = isogonal_conjugate(model, A, B, C, X_916, ID="X(917)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_4, X_101, 4, 101, incident=True)
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X(27)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_27, X_110, 27, 110, incident=True)
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    central_line(model, X_92, X_100, 92, 100, incident=True)
    return promote_point_to_top(model, X_917)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(917) on the given reference triangle."""
    model = create_model('X(917) = X(516)-CROSS CONJUGATE OF X(4)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00917(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00917.json"))
    write_center_svg(
        model_acute,
        here / "x-00917.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
