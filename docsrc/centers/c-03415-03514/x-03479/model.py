"""GEOMETOR construction model for X_3479 = ISOGONAL CONJUGATE OF X_1337."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03479(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3479 = ISOGONAL CONJUGATE OF X_1337 on reference triangle ABC."""
    X_1337 = eval_barycentric_point(model, A, B, C, '(a**(2)*(2*D*U - 3**(1/2)*V*W)/(4*D + 3**(1/2)*a**(2)))', ID="X_1337", classes=["center"])
    X_3479 = isogonal_conjugate(model, A, B, C, X_1337, ID="X_3479", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_298 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A +  pi  /3)', ID="X_298", classes=["center", "incident"])
    central_line(model, X_3, X_298, 3, 298, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    central_line(model, X_30, X_1337, 30, 1337, incident=True)
    X_3480 = point_from_barycentrics(model, A, B, C, -1.1796659, 0.33688479, 1.8427811, ID="X_3480", classes=["center", "incident"])
    X_3484 = point_from_barycentrics(model, A, B, C, 1.3028444, 1.5329065, -1.8357509, ID="X_3484", classes=["center", "incident"])
    central_line(model, X_3480, X_3484, 3480, 3484, incident=True)
    return promote_point_to_top(model, X_3479)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3479 on the given reference triangle."""
    model = create_model('X_3479 = ISOGONAL CONJUGATE OF X_1337')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03479(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03479.json"))
    write_center_svg(
        model_acute,
        here / "x-03479.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
