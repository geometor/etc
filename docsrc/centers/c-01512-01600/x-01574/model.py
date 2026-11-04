"""GEOMETOR construction model for X_1574 = EXSIMILICENTER OF SPIEKER AND MOSES CIRCLES."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01574(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1574 = EXSIMILICENTER OF SPIEKER AND MOSES CIRCLES on reference triangle ABC."""
    X_1574 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2)) - 2*b*c*(b + c)', ID="X_1574", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_10, X_39, 10, 39, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_762 = eval_trilinear_point(model, A, B, C, '(b + c)**(3)', ID="X_762", classes=["center", "incident"])
    central_line(model, X_38, X_762, 38, 762, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_1015 = eval_trilinear_point(model, A, B, C, 'a*(b - c)**(2)', ID="X_1015", classes=["center", "incident"])
    central_line(model, X_8, X_1015, 8, 1015, incident=True)
    return promote_point_to_top(model, X_1574)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1574 on the given reference triangle."""
    model = create_model('X_1574 = EXSIMILICENTER OF SPIEKER AND MOSES CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01574(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01574.json"))
    write_center_svg(
        model_acute,
        here / "x-01574.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
