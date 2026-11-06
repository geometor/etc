"""GEOMETOR construction model for X_3490 = ISOGONAL CONJUGATE OF X_628."""

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
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03490(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3490 = ISOGONAL CONJUGATE OF X_628 on reference triangle ABC."""
    X_628 = point_from_barycentrics(model, A, B, C, 0.057011511, 0.38206086, 0.56092763, ID="X_628", classes=["center"])
    X_3490 = isogonal_conjugate(model, A, B, C, X_628, ID="X_3490", classes=["selected", "target"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    X_62 = eval_trilinear_point(model, A, B, C, 'sin(A -  pi  /6)', ID="X_62", classes=["center", "incident"])
    central_line(model, X_51, X_62, 51, 62, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_303 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A -  pi  /6)', ID="X_303", classes=["center", "incident"])
    central_line(model, X_5, X_303, 5, 303, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_1338 = eval_barycentric_point(model, A, B, C, '(a**(2)*(2*D*U + 3**(1/2)*V*W)/(4*D - 3**(1/2)*a**(2)))', ID="X_1338", classes=["center", "incident"])
    central_line(model, X_3, X_1338, 3, 1338, incident=True)
    return promote_point_to_top(model, X_3490)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3490 on the given reference triangle."""
    model = create_model('X_3490 = ISOGONAL CONJUGATE OF X_628')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03490(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03490.json"))
    write_center_svg(
        model_acute,
        here / "x-03490.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
