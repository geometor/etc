"""GEOMETOR construction model for X_2350 = X_2-ISOCONJUGATE OF X_1621."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02350(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2350 = X_2-ISOCONJUGATE OF X_1621 on reference triangle ABC."""
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center"])
    central_line(model, X_37, X_38, 37, 38)
    central_line(model, X_39, X_42, 39, 42)
    X_2350 = intersect_lines(model, X_37, X_38, X_39, X_42, ID="X_2350", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_251 = eval_trilinear_point(model, A, B, C, 'a**(2)*csc(A +  omega  )', ID="X_251", classes=["center", "incident"])
    central_line(model, X_58, X_251, 58, 251, incident=True)
    return promote_point_to_top(model, X_2350)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2350 on the given reference triangle."""
    model = create_model('X_2350 = X_2-ISOCONJUGATE OF X_1621')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02350(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02350.json"))
    write_center_svg(
        model_acute,
        here / "x-02350.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
