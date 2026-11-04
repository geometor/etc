"""GEOMETOR construction model for X_1861 = ZOSMA TRANSFORM OF X_238."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    mittenpunkt_of,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01861(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1861 = ZOSMA TRANSFORM OF X_238 on reference triangle ABC."""
    X_1861 = eval_barycentric_point(model, A, B, C, '(b**(2) + c**(2) - a*(b + c))/(a**(2) - b**(2) - c**(2))', ID="X_1861", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    central_line(model, X_2, X_33, 2, 33, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_8, X_34, 8, 34, incident=True)
    return promote_point_to_top(model, X_1861)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1861 on the given reference triangle."""
    model = create_model('X_1861 = ZOSMA TRANSFORM OF X_238')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01861(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01861.json"))
    write_center_svg(
        model_acute,
        here / "x-01861.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
