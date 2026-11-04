"""GEOMETOR construction model for X_2279 = X_2-ISOCONJUGATE OF X_1001."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02279(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2279 = X_2-ISOCONJUGATE OF X_1001 on reference triangle ABC."""
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center"])
    central_line(model, X_9, X_86, 9, 86)
    central_line(model, X_41, X_58, 41, 58)
    X_2279 = intersect_lines(model, X_9, X_86, X_41, X_58, ID="X_2279", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    central_line(model, X_56, X_213, 56, 213, incident=True)
    return promote_point_to_top(model, X_2279)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2279 on the given reference triangle."""
    model = create_model('X_2279 = X_2-ISOCONJUGATE OF X_1001')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02279(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02279.json"))
    write_center_svg(
        model_acute,
        here / "x-02279.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
