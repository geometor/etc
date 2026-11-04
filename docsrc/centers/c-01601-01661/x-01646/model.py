"""GEOMETOR construction model for X_1646 = TRIPOLAR CENTROID OF X_513."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01646(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1646 = TRIPOLAR CENTROID OF X_513 on reference triangle ABC."""
    X_1646 = eval_trilinear_point(model, A, B, C, '(a*(b - c)**(2)*(2*b*c - a*b - a*c))', ID="X_1646", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_2, X_37, 2, 37, incident=True)
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    X_292 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) - b*c)', ID="X_292", classes=["center", "incident"])
    central_line(model, X_88, X_292, 88, 292, incident=True)
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X_665", classes=["center", "incident"])
    central_line(model, X_244, X_665, 244, 665, incident=True)
    return promote_point_to_top(model, X_1646)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1646 on the given reference triangle."""
    model = create_model('X_1646 = TRIPOLAR CENTROID OF X_513')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01646(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01646.json"))
    write_center_svg(
        model_acute,
        here / "x-01646.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
