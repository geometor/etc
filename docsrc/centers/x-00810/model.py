"""GEOMETOR construction model for X_810 = CROSSPOINT OF X_1 AND X_163."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00810(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_810 = CROSSPOINT OF X_1 AND X_163 on reference triangle ABC."""
    X_810 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X_810", classes=["selected", "target"])
    X_521 = eval_trilinear_point(model, A, B, C, '(sec(B) - sec(C))*(csc(A))', ID="X_521", classes=["center", "incident"])
    X_656 = eval_trilinear_point(model, A, B, C, 'tan(B) - tan(C)', ID="X_656", classes=["center", "incident"])
    central_line(model, X_521, X_656, 521, 656, incident=True)
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center", "incident"])
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X_663", classes=["center", "incident"])
    central_line(model, X_661, X_663, 661, 663, incident=True)
    X_667 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b - c)', ID="X_667", classes=["center", "incident"])
    X_788 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(3) - c**(3))', ID="X_788", classes=["center", "incident"])
    central_line(model, X_667, X_788, 667, 788, incident=True)
    return promote_point_to_top(model, X_810)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_810 on the given reference triangle."""
    model = create_model('X_810 = CROSSPOINT OF X_1 AND X_163')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00810(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00810.json"))
    write_center_svg(
        model_acute,
        here / "x-00810.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
