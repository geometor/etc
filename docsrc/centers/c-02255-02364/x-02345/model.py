"""GEOMETOR construction model for X_2345 = X_2-ISOCONJUGATE OF X_1472."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    mittenpunkt_of,
    nagel_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02345(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2345 = X_2-ISOCONJUGATE OF X_1472 on reference triangle ABC."""
    X_2221 = point_from_barycentrics(model, A, B, C, 0.20882469, 0.32409591, 0.4670794, ID="X_2221", classes=["center"])
    X_2345 = isogonal_conjugate(model, A, B, C, X_2221, ID="X_2345", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    central_line(model, X_6, X_8, 6, 8, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_2, X_37, 2, 37, incident=True)
    return promote_point_to_top(model, X_2345)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2345 on the given reference triangle."""
    model = create_model('X_2345 = X_2-ISOCONJUGATE OF X_1472')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02345(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02345.json"))
    write_center_svg(
        model_acute,
        here / "x-02345.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
