"""GEOMETOR construction model for X_2127 = ISOGONAL CONJUGATE OF X_2126."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02127(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2127 = ISOGONAL CONJUGATE OF X_2126 on reference triangle ABC."""
    X_2126 = point_from_barycentrics(model, A, B, C, 0.26468766, 0.32505588, 0.41025647, ID="X_2126", classes=["center"])
    X_2127 = isogonal_conjugate(model, A, B, C, X_2126, ID="X_2127", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_10, X_2126, 10, 2126, incident=True)
    return promote_point_to_top(model, X_2127)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2127 on the given reference triangle."""
    model = create_model('X_2127 = ISOGONAL CONJUGATE OF X_2126')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02127(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02127.json"))
    write_center_svg(
        model_acute,
        here / "x-02127.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
