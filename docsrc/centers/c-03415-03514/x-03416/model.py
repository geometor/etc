"""GEOMETOR construction model for X_3416 = ISOGONAL CONJUGATE OF X_3415."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    midpoint,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03416(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3416 = ISOGONAL CONJUGATE OF X_3415 on reference triangle ABC."""
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center"])
    X_3416 = midpoint(model, X_8, X_69, ID="X_3416", classes=["selected", "target"], guide=False)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_7, X_8, 7, 8, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_6, X_10, 6, 10, incident=True)
    X_66 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4))', ID="X_66", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    central_line(model, X_66, X_72, 66, 72, incident=True)
    return promote_point_to_top(model, X_3416)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3416 on the given reference triangle."""
    model = create_model('X_3416 = ISOGONAL CONJUGATE OF X_3415')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03416(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03416.json"))
    write_center_svg(
        model_acute,
        here / "x-03416.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
