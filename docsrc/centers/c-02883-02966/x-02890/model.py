"""GEOMETOR construction model for X_2890 = ANTICOMPLEMENTARY CONJUGATE OF X_9."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02890(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2890 = ANTICOMPLEMENTARY CONJUGATE OF X_9 on reference triangle ABC."""
    X_1174 = point_from_barycentrics(model, A, B, C, 0.24963675, 0.33833122, 0.41203203, ID="X_1174", classes=["center"])
    X_2890 = anticomplement(model, A, B, C, X_1174, ID="X_2890", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_1174, 2, 1174, incident=True)
    return promote_point_to_top(model, X_2890)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2890 on the given reference triangle."""
    model = create_model('X_2890 = ANTICOMPLEMENTARY CONJUGATE OF X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02890(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02890.json"))
    write_center_svg(
        model_acute,
        here / "x-02890.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
