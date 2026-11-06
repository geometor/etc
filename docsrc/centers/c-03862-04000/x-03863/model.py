"""GEOMETOR construction model for X_3863 = PERSPECTOR OF ABC AND T(-bc, b²)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03863(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3863 = PERSPECTOR OF ABC AND T(-bc, b²) on reference triangle ABC."""
    X_3863 = eval_barycentric_point(model, A, B, C, '(a**(2)*(b**(2) + a*c)*(c**(2) + a*b)*(b**(2) - b*c + c**(2)))', ID="X_3863", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center", "incident"])
    central_line(model, X_37, X_256, 37, 256, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_257 = eval_trilinear_point(model, A, B, C, '1/(a**(3) + a*b*c)', ID="X_257", classes=["center", "incident"])
    central_line(model, X_75, X_257, 75, 257, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_893 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) + b*c)', ID="X_893", classes=["center", "incident"])
    central_line(model, X_6, X_893, 6, 893, incident=True)
    return promote_point_to_top(model, X_3863)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3863 on the given reference triangle."""
    model = create_model('X_3863 = PERSPECTOR OF ABC AND T(-bc, b²)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03863(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03863.json"))
    write_center_svg(
        model_acute,
        here / "x-03863.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
