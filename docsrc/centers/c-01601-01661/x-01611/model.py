"""GEOMETOR construction model for X_1611 = TCC-PERSPECTOR OF X_25."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01611(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1611 = TCC-PERSPECTOR OF X_25 on reference triangle ABC."""
    X_1611 = eval_trilinear_point(model, A, B, C, '(a*((a**(2) + b**(2) + c**(2))**(2) - 8*b**(2)*c**(2)))', ID="X_1611", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_1196 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) + a**(2)*b**(2) + a**(2)*c**(2) - 2*b**(2)*c**(2)))', ID="X_1196", classes=["center", "incident"])
    central_line(model, X_3, X_1196, 3, 1196, incident=True)
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A + omega )', ID="X_232", classes=["center", "incident"])
    X_1033 = point_from_barycentrics(model, A, B, C, -0.20250392, -0.4085329, 1.6110368, ID="X_1033", classes=["center", "incident"])
    central_line(model, X_232, X_1033, 232, 1033, incident=True)
    return promote_point_to_top(model, X_1611)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1611 on the given reference triangle."""
    model = create_model('X_1611 = TCC-PERSPECTOR OF X_25')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01611(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01611.json"))
    write_center_svg(
        model_acute,
        here / "x-01611.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
