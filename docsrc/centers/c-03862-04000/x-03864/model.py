"""GEOMETOR construction model for X_3864 = PERSPECTOR OF ABC AND T(bc, c²)."""

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
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03864(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3864 = PERSPECTOR OF ABC AND T(bc, c²) on reference triangle ABC."""
    X_3864 = eval_barycentric_point(model, A, B, C, '(a*(b**(2) - a*c)*(c**(2) - a*b)*(b**(2) + b*c + c**(2)))', ID="X_3864", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_1, X_39, 1, 39, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_257 = eval_trilinear_point(model, A, B, C, '1/(a**(3) + a*b*c)', ID="X_257", classes=["center", "incident"])
    central_line(model, X_10, X_257, 10, 257, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_334 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(a**(2) - b*c)', ID="X_334", classes=["center", "incident"])
    central_line(model, X_76, X_334, 76, 334, incident=True)
    return promote_point_to_top(model, X_3864)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3864 on the given reference triangle."""
    model = create_model('X_3864 = PERSPECTOR OF ABC AND T(bc, c²)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03864(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03864.json"))
    write_center_svg(
        model_acute,
        here / "x-03864.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
