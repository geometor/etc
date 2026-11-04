"""GEOMETOR construction model for X_1075 = X_3-CEVA CONJUGATE OF X_4."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01075(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1075 = X_3-CEVA CONJUGATE OF X_4 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1075 = ceva_conjugate(model, A, B, C, X_3, X_4, ID="X_1075", classes=["selected", "target"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_4, X_51, 4, 51, incident=True)
    X_155 = eval_trilinear_point(model, A, B, C, '(cos(A))*((cos(B))**(2) + (cos(C))**(2) - (cos(A))**(2))', ID="X_155", classes=["center", "incident"])
    X_450 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(4) - (cos(B)*cos(C))**(2))', ID="X_450", classes=["center", "incident"])
    central_line(model, X_155, X_450, 155, 450, incident=True)
    X_216 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*cos(B - C)', ID="X_216", classes=["center", "incident"])
    X_631 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B)*cos(C)', ID="X_631", classes=["center", "incident"])
    central_line(model, X_216, X_631, 216, 631, incident=True)
    return promote_point_to_top(model, X_1075)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1075 on the given reference triangle."""
    model = create_model('X_1075 = X_3-CEVA CONJUGATE OF X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01075(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01075.json"))
    write_center_svg(
        model_acute,
        here / "x-01075.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
