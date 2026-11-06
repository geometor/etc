"""GEOMETOR construction model for X_3788 = X_3053com[T(a², a² - b²)]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03788(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3788 = X_3053com[T(a², a² - b²)] on reference triangle ABC."""
    X_3767 = eval_barycentric_point(model, A, B, C, 'a**(4) + (b**(2) - c**(2))**(2)', ID="X_3767", classes=["center"])
    X_3788 = complement(model, A, B, C, X_3767, ID="X_3788", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_2, X_39, 2, 39, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    central_line(model, X_3, X_114, 3, 114, incident=True)
    X_140 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B - C)', ID="X_140", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center", "incident"])
    central_line(model, X_140, X_141, 140, 141, incident=True)
    return promote_point_to_top(model, X_3788)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3788 on the given reference triangle."""
    model = create_model('X_3788 = X_3053com[T(a², a² - b²)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03788(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03788.json"))
    write_center_svg(
        model_acute,
        here / "x-03788.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
