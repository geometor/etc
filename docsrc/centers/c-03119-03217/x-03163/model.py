"""GEOMETOR construction model for X_3163 = X_2-CEVA CONJUGATE OF X_30."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03163(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3163 = X_2-CEVA CONJUGATE OF X_30 on reference triangle ABC."""
    X_1494 = eval_trilinear_point(model, A, B, C, '(b*c/((b**(2) - c**(2))**(2) + a**(2)*(b**(2) + c**(2) - 2*a**(2))))', ID="X_1494", classes=["center"])
    X_3163 = complement(model, A, B, C, X_1494, ID="X_3163", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_6, X_13, 6, 13, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_648 = eval_trilinear_point(model, A, B, C, '1/(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2)))', ID="X_648", classes=["center", "incident"])
    central_line(model, X_2, X_648, 2, 648, incident=True)
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X_216", classes=["center", "incident"])
    X_549 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 4*cos(A)', ID="X_549", classes=["center", "incident"])
    central_line(model, X_216, X_549, 216, 549, incident=True)
    return promote_point_to_top(model, X_3163)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3163 on the given reference triangle."""
    model = create_model('X_3163 = X_2-CEVA CONJUGATE OF X_30')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03163(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03163.json"))
    write_center_svg(
        model_acute,
        here / "x-03163.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
