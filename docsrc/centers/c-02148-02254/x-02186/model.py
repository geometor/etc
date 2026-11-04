"""GEOMETOR construction model for X_2186 = X_2-ISOCONJUGATE OF X_182."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02186(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2186 = X_2-ISOCONJUGATE OF X_182 on reference triangle ABC."""
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center"])
    X_262 = eval_trilinear_point(model, A, B, C, 'sec(A -  omega  )', ID="X_262", classes=["center"])
    central_line(model, X_48, X_82, 48, 82)
    central_line(model, X_10, X_262, 10, 262)
    X_2186 = intersect_lines(model, X_48, X_82, X_10, X_262, ID="X_2186", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_263 = eval_trilinear_point(model, A, B, C, 'a**(2)*sec(A -  omega  )', ID="X_263", classes=["center", "incident"])
    central_line(model, X_37, X_263, 37, 263, incident=True)
    return promote_point_to_top(model, X_2186)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2186 on the given reference triangle."""
    model = create_model('X_2186 = X_2-ISOCONJUGATE OF X_182')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02186(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02186.json"))
    write_center_svg(
        model_acute,
        here / "x-02186.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
