"""GEOMETOR construction model for X_2183 = X_2-ISOCONJUGATE OF X_104."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02183(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2183 = X_2-ISOCONJUGATE OF X_104 on reference triangle ABC."""
    X_2183 = eval_trilinear_point(model, A, B, C, '(a - c)*cos(B) + (a - b)*cos(C)', ID="X_2183", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_6, X_41, 6, 41, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_197 = eval_trilinear_point(model, A, B, C, 'a*(-a**(2)*tan(A/2) + b**(2)*tan(B/2) + c**(2)*tan(C/2))', ID="X_197", classes=["center", "incident"])
    central_line(model, X_31, X_197, 31, 197, incident=True)
    return promote_point_to_top(model, X_2183)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2183 on the given reference triangle."""
    model = create_model('X_2183 = X_2-ISOCONJUGATE OF X_104')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02183(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02183.json"))
    write_center_svg(
        model_acute,
        here / "x-02183.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
