"""GEOMETOR construction model for X_2393 = ISOGONAL CONJUGATE OF X_2373."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02393(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2393 = ISOGONAL CONJUGATE OF X_2373 on reference triangle ABC."""
    X_2373 = point_from_barycentrics(model, A, B, C, 0.69246829, 0.98040184, -0.67287013, ID="X_2373", classes=["center"])
    X_2393 = isogonal_conjugate(model, A, B, C, X_2373, ID="X_2393", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_6, X_25, 6, 25, incident=True)
    X_66 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4))', ID="X_66", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_66, X_69, 66, 69, incident=True)
    X_160 = eval_trilinear_point(model, A, B, C, '(a*((b**(2) + c**(2))*sin(2*A) + (c**(2) - a**(2))*sin(2*B) + (b**(2) - a**(2))*sin(2*C)))', ID="X_160", classes=["center", "incident"])
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X_216", classes=["center", "incident"])
    central_line(model, X_160, X_216, 160, 216, incident=True)
    return promote_point_to_top(model, X_2393)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2393 on the given reference triangle."""
    model = create_model('X_2393 = ISOGONAL CONJUGATE OF X_2373')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02393(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02393.json"))
    write_center_svg(
        model_acute,
        here / "x-02393.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
