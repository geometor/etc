"""GEOMETOR construction model for X_2197 = X_2-ISOCONJUGATE OF X_270."""

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


def construct_x_02197(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2197 = X_2-ISOCONJUGATE OF X_270 on reference triangle ABC."""
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X_73", classes=["center"])
    central_line(model, X_12, X_37, 12, 37)
    central_line(model, X_71, X_73, 71, 73)
    X_2197 = intersect_lines(model, X_12, X_37, X_71, X_73, ID="X_2197", classes=["selected", "target"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X_181", classes=["center", "incident"])
    central_line(model, X_42, X_181, 42, 181, incident=True)
    return promote_point_to_top(model, X_2197)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2197 on the given reference triangle."""
    model = create_model('X_2197 = X_2-ISOCONJUGATE OF X_270')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02197(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02197.json"))
    write_center_svg(
        model_acute,
        here / "x-02197.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
