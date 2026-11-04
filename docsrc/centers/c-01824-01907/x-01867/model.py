"""GEOMETOR construction model for X_1867 = ZOSMA TRANSFORM OF X_386."""

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
    nagel_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01867(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1867 = ZOSMA TRANSFORM OF X_386 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    central_line(model, X_4, X_8, 4, 8)
    central_line(model, X_12, X_37, 12, 37)
    X_1867 = intersect_lines(model, X_4, X_8, X_12, X_37, ID="X_1867", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_407 = point_from_barycentrics(model, A, B, C, 0.10813862, 0.19355731, 0.69830407, ID="X_407", classes=["center", "incident"])
    central_line(model, X_10, X_407, 10, 407, incident=True)
    return promote_point_to_top(model, X_1867)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1867 on the given reference triangle."""
    model = create_model('X_1867 = ZOSMA TRANSFORM OF X_386')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01867(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01867.json"))
    write_center_svg(
        model_acute,
        here / "x-01867.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
