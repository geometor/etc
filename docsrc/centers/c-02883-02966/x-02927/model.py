"""GEOMETOR construction model for X_2927 = TANGENTIAL-ISOGONAL CONJUGATE OF X_17."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02927(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2927 = TANGENTIAL-ISOGONAL CONJUGATE OF X_17 on reference triangle ABC."""
    X_2927 = point_from_barycentrics(model, A, B, C, 0.60598844, 0.51555187, -0.12154031, ID="X_2927", classes=["selected", "target"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    X_2937 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(8) - 2*a**(6)*(b**(2) + c**(2)) - a**(4)*b**(2)*c**(2) + a**(2)*(2*b**(6) + b**(4)*c**(2) + b**(2)*c**(4) + 2*c**(6)) - (b**(2) - c**(2))**(2)*(b**(4) + c**(4)))', ID="X_2937", classes=["center", "incident"])
    central_line(model, X_15, X_2937, 15, 2937, incident=True)
    return promote_point_to_top(model, X_2927)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2927 on the given reference triangle."""
    model = create_model('X_2927 = TANGENTIAL-ISOGONAL CONJUGATE OF X_17')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02927(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02927.json"))
    write_center_svg(
        model_acute,
        here / "x-02927.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
