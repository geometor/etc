"""GEOMETOR construction model for X_1573 = INSIMILICENTER OF SPIEKER AND MOSES CIRCLES."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01573(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1573 = INSIMILICENTER OF SPIEKER AND MOSES CIRCLES on reference triangle ABC."""
    X_1573 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2)) + 2*b*c*(b + c)', ID="X_1573", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_10, X_39, 10, 39, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_37, X_519, 37, 519, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_538 = point_from_barycentrics(model, A, B, C, -0.75777793, 0.11558409, 0.64219384, ID="X_538", classes=["center", "incident"])
    central_line(model, X_75, X_538, 75, 538, incident=True)
    return promote_point_to_top(model, X_1573)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1573 on the given reference triangle."""
    model = create_model('X_1573 = INSIMILICENTER OF SPIEKER AND MOSES CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01573(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01573.json"))
    write_center_svg(
        model_acute,
        here / "x-01573.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
