"""GEOMETOR construction model for X_3144 = X_225-CEVA CONJUGATE OF X_4."""

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
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03144(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3144 = X_225-CEVA CONJUGATE OF X_4 on reference triangle ABC."""
    X_3144 = eval_barycentric_point(model, A, B, C, '((a**(3) + 2*a**(2)*(b + c) + a*b*c - b**(3) - c**(3))/(b**(2) + c**(2) - a**(2)))', ID="X_3144", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    X_978 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c) + a*(b**(2) - b*c + c**(2)) - b*c*(b + c)', ID="X_978", classes=["center", "incident"])
    central_line(model, X_34, X_978, 34, 978, incident=True)
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    X_1247 = point_from_barycentrics(model, A, B, C, 0.47979502, 0.29838347, 0.22182151, ID="X_1247", classes=["center", "incident"])
    central_line(model, X_225, X_1247, 225, 1247, incident=True)
    return promote_point_to_top(model, X_3144)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3144 on the given reference triangle."""
    model = create_model('X_3144 = X_225-CEVA CONJUGATE OF X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03144(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03144.json"))
    write_center_svg(
        model_acute,
        here / "x-03144.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
