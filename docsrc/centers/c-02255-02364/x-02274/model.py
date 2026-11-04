"""GEOMETOR construction model for X_2274 = X_2-ISOCONJUGATE OF X_981."""

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
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02274(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2274 = X_2-ISOCONJUGATE OF X_981 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    central_line(model, X_6, X_41, 6, 41)
    central_line(model, X_1, X_75, 1, 75)
    X_2274 = intersect_lines(model, X_6, X_41, X_1, X_75, ID="X_2274", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_560 = eval_trilinear_point(model, A, B, C, 'a**(4)', ID="X_560", classes=["center", "incident"])
    central_line(model, X_58, X_560, 58, 560, incident=True)
    return promote_point_to_top(model, X_2274)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2274 on the given reference triangle."""
    model = create_model('X_2274 = X_2-ISOCONJUGATE OF X_981')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02274(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02274.json"))
    write_center_svg(
        model_acute,
        here / "x-02274.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
