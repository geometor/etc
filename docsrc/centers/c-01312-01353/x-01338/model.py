"""GEOMETOR construction model for X_1338 = 2nd WERNAU POINT."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01338(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1338 = 2nd WERNAU POINT on reference triangle ABC."""
    X_1338 = eval_barycentric_point(model, A, B, C, '(a**(2)*(2*D*U + 3**(1/2)*V*W)/(4*D - 3**(1/2)*a**(2)))', ID="X_1338", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_617 = point_from_barycentrics(model, A, B, C, 0.67910401, -1.0602234, 1.3811194, ID="X_617", classes=["center", "incident"])
    central_line(model, X_4, X_617, 4, 617, incident=True)
    X_1157 = eval_trilinear_point(model, A, B, C, '4*cos(A) + cos(3*A)*sec(A)*sec(B - C)', ID="X_1157", classes=["center", "incident"])
    X_1337 = eval_barycentric_point(model, A, B, C, '(a**(2)*(2*D*U - 3**(1/2)*V*W)/(4*D + 3**(1/2)*a**(2)))', ID="X_1337", classes=["center", "incident"])
    central_line(model, X_1157, X_1337, 1157, 1337, incident=True)
    return promote_point_to_top(model, X_1338)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1338 on the given reference triangle."""
    model = create_model('X_1338 = 2nd WERNAU POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01338(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01338.json"))
    write_center_svg(
        model_acute,
        here / "x-01338.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
