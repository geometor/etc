"""GEOMETOR construction model for X_3423 = X_1-VERTEX CONJUGATE OF X_57."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03423(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3423 = X_1-VERTEX CONJUGATE OF X_57 on reference triangle ABC."""
    X_2550 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c + a*cos(B)*cos(C)))', ID="X_2550", classes=["center"])
    X_3423 = isogonal_conjugate(model, A, B, C, X_2550, ID="X_3423", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_3, X_41, 3, 41, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_25, X_57, 25, 57, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_7, X_105, 7, 105, incident=True)
    return promote_point_to_top(model, X_3423)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3423 on the given reference triangle."""
    model = create_model('X_3423 = X_1-VERTEX CONJUGATE OF X_57')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03423(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03423.json"))
    write_center_svg(
        model_acute,
        here / "x-03423.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
