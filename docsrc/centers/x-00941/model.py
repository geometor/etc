"""GEOMETOR construction model for X(941) = ISOGONAL CONJUGATE OF X(940)."""

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
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00941(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(941) = ISOGONAL CONJUGATE OF X(940) on reference triangle ABC."""
    X_940 = eval_trilinear_point(model, A, B, C, 'a*s + b*c', ID="X(940)", classes=["center"])
    X_941 = isogonal_conjugate(model, A, B, C, X_940, ID="X(941)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    central_line(model, X_6, X_21, 6, 21, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    central_line(model, X_8, X_37, 8, 37, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X(42)", classes=["center", "incident"])
    central_line(model, X_9, X_42, 9, 42, incident=True)
    return promote_point_to_top(model, X_941)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(941) on the given reference triangle."""
    model = create_model('X(941) = ISOGONAL CONJUGATE OF X(940)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00941(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00941.json"))
    write_center_svg(
        model_acute,
        here / "x-00941.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
