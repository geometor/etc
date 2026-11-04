"""GEOMETOR construction model for X_1126 = ISOGONAL CONJUGATE OF X_1125."""

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
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01126(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1126 = ISOGONAL CONJUGATE OF X_1125 on reference triangle ABC."""
    X_1125 = eval_trilinear_point(model, A, B, C, '(2*a+b+c)/a', ID="X_1125", classes=["center"])
    X_1126 = isogonal_conjugate(model, A, B, C, X_1125, ID="X_1126", classes=["selected", "target"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    central_line(model, X_35, X_42, 35, 42, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    central_line(model, X_10, X_86, 10, 86, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X_181", classes=["center", "incident"])
    central_line(model, X_56, X_181, 56, 181, incident=True)
    return promote_point_to_top(model, X_1126)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1126 on the given reference triangle."""
    model = create_model('X_1126 = ISOGONAL CONJUGATE OF X_1125')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01126(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01126.json"))
    write_center_svg(
        model_acute,
        here / "x-01126.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
