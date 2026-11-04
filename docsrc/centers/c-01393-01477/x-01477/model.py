"""GEOMETOR construction model for X_1477 = X_1280-BETH CONJUGATE OF X_1280."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01477(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1477 = X_1280-BETH CONJUGATE OF X_1280 on reference triangle ABC."""
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_1458 = eval_barycentric_point(model, A, B, C, 'a**(2)*(b**(2) + c**(2) - a*b - a*c)/(a - b - c)', ID="X_1458", classes=["center"])
    X_1477 = cevapoint(model, A, B, C, X_56, X_1458, ID="X_1477", classes=["selected", "target"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_56, X_101, 56, 101, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_57, X_100, 57, 100, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1292 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(a**(2) + b**(2) + c**(2) - 2*a*b - 2*a*c))', ID="X_1292", classes=["center", "incident"])
    central_line(model, X_1, X_1292, 1, 1292, incident=True)
    return promote_point_to_top(model, X_1477)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1477 on the given reference triangle."""
    model = create_model('X_1477 = X_1280-BETH CONJUGATE OF X_1280')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01477(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01477.json"))
    write_center_svg(
        model_acute,
        here / "x-01477.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
