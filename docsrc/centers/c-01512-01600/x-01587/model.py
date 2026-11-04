"""GEOMETOR construction model for X_1587 = POINT CASTOR I."""

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
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01587(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1587 = POINT CASTOR I on reference triangle ABC."""
    X_1587 = eval_trilinear_point(model, A, B, C, '(sin(A) + cos(B)*cos(C))', ID="X_1587", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A +  pi  /4)', ID="X_372", classes=["center", "incident"])
    central_line(model, X_2, X_372, 2, 372, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_371 = eval_trilinear_point(model, A, B, C, 'cos(A -  pi  /4)', ID="X_371", classes=["center", "incident"])
    central_line(model, X_20, X_371, 20, 371, incident=True)
    return promote_point_to_top(model, X_1587)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1587 on the given reference triangle."""
    model = create_model('X_1587 = POINT CASTOR I')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01587(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01587.json"))
    write_center_svg(
        model_acute,
        here / "x-01587.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
