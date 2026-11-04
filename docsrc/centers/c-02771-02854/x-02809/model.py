"""GEOMETOR construction model for X_2809 = ISOGONAL CONJUGATE OF X_2725."""

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
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02809(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2809 = ISOGONAL CONJUGATE OF X_2725 on reference triangle ABC."""
    X_2725 = point_from_barycentrics(model, A, B, C, 0.76388889, -0.28333333, 0.51944444, ID="X_2725", classes=["center"])
    X_2809 = isogonal_conjugate(model, A, B, C, X_2725, ID="X_2809", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_1, X_41, 1, 41, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X_116", classes=["center", "incident"])
    central_line(model, X_10, X_116, 10, 116, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    central_line(model, X_40, X_103, 40, 103, incident=True)
    return promote_point_to_top(model, X_2809)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2809 on the given reference triangle."""
    model = create_model('X_2809 = ISOGONAL CONJUGATE OF X_2725')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02809(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02809.json"))
    write_center_svg(
        model_acute,
        here / "x-02809.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
