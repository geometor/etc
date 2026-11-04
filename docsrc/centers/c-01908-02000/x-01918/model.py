"""GEOMETOR construction model for X_1918 = BICENTRIC SUM OF PU(12)."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01918(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1918 = BICENTRIC SUM OF PU(12) on reference triangle ABC."""
    X_310 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b + c)', ID="X_310", classes=["center"])
    X_1918 = isogonal_conjugate(model, A, B, C, X_310, ID="X_1918", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_6, X_31, 6, 31, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center", "incident"])
    central_line(model, X_10, X_82, 10, 82, incident=True)
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    central_line(model, X_86, X_171, 86, 171, incident=True)
    return promote_point_to_top(model, X_1918)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1918 on the given reference triangle."""
    model = create_model('X_1918 = BICENTRIC SUM OF PU(12)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01918(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01918.json"))
    write_center_svg(
        model_acute,
        here / "x-01918.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
