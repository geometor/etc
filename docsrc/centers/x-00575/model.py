"""GEOMETOR construction model for X(575) = ORTHOGONAL OF X(187)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00575(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(575) = ORTHOGONAL OF X(187) on reference triangle ABC."""
    X_575 = eval_barycentric_point(model, A, B, C, 'a**(2)*(2*a**(4) + b**(4) + c**(4) - 3*a**(2)*b**(2) - 3*a**(2)*c**(2) - 4*b**(2)*c**(2))', ID="X(575)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(23)", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center", "incident"])
    central_line(model, X_23, X_51, 23, 51, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_373 = point_from_barycentrics(model, A, B, C, 0.28382464, 0.3169161, 0.39925926, ID="X(373)", classes=["center", "incident"])
    central_line(model, X_110, X_373, 110, 373, incident=True)
    return promote_point_to_top(model, X_575)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(575) on the given reference triangle."""
    model = create_model('X(575) = ORTHOGONAL OF X(187)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00575(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00575.json"))
    write_center_svg(
        model_acute,
        here / "x-00575.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
