"""GEOMETOR construction model for X_1903 = ZOSMA TRANSFORM OF X_1249."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01903(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1903 = ZOSMA TRANSFORM OF X_1249 on reference triangle ABC."""
    X_1817 = point_from_barycentrics(model, A, B, C, 0.57344373, 0.48236737, -0.055811101, ID="X_1817", classes=["center"])
    X_1903 = isogonal_conjugate(model, A, B, C, X_1817, ID="X_1903", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_3, X_9, 3, 9, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    central_line(model, X_6, X_33, 6, 33, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    central_line(model, X_19, X_64, 19, 64, incident=True)
    return promote_point_to_top(model, X_1903)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1903 on the given reference triangle."""
    model = create_model('X_1903 = ZOSMA TRANSFORM OF X_1249')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01903(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01903.json"))
    write_center_svg(
        model_acute,
        here / "x-01903.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
