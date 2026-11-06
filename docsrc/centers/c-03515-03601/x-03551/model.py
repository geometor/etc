"""GEOMETOR construction model for X_3551 = ISOGONAL CONJUGATE OF X_3550."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    mittenpunkt_of,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03551(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3551 = ISOGONAL CONJUGATE OF X_3550 on reference triangle ABC."""
    X_3550 = eval_trilinear_point(model, A, B, C, '(2*a**(2) + b*c - c*a - a*b)', ID="X_3550", classes=["center"])
    X_3551 = isogonal_conjugate(model, A, B, C, X_3550, ID="X_3551", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_726 = eval_trilinear_point(model, A, B, C, '(a **(-3)*(b **(-1) + c **(-1)) - a **(-2)*(b **(-2) + c **(-2)))', ID="X_726", classes=["center", "incident"])
    central_line(model, X_8, X_726, 8, 726, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1463 = point_from_barycentrics(model, A, B, C, -0.64021164, 0.2031746, 1.437037, ID="X_1463", classes=["center", "incident"])
    central_line(model, X_1, X_1463, 1, 1463, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_1575 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2)) - b*c*(b + c)', ID="X_1575", classes=["center", "incident"])
    central_line(model, X_9, X_1575, 9, 1575, incident=True)
    return promote_point_to_top(model, X_3551)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3551 on the given reference triangle."""
    model = create_model('X_3551 = ISOGONAL CONJUGATE OF X_3550')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03551(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03551.json"))
    write_center_svg(
        model_acute,
        here / "x-03551.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
