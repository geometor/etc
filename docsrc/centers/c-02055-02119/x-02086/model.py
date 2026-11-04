"""GEOMETOR construction model for X_2086 = PK-TRANSFORM OF X_99."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02086(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2086 = PK-TRANSFORM OF X_99 on reference triangle ABC."""
    X_2086 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))**(2)*(a**(4) - b**(2)*c**(2)))', ID="X_2086", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_351 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(2) + c**(2) - 2*a**(2)))', ID="X_351", classes=["center", "incident"])
    X_865 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*(csc(C))**(2)*sin(C - A)*csc(A - B) - sin(2*C)*(csc(B))**(2)*sin(B - A)*csc(A - C))', ID="X_865", classes=["center", "incident"])
    central_line(model, X_351, X_865, 351, 865, incident=True)
    X_671 = eval_trilinear_point(model, A, B, C, '1/(a*(2*a**(2) - b**(2) - c**(2)))', ID="X_671", classes=["center", "incident"])
    X_729 = eval_trilinear_point(model, A, B, C, '1/(a**(-3)*(b**(0) + c**(0)) - a **(-1)*(b**(-2) + c **(-2)))', ID="X_729", classes=["center", "incident"])
    central_line(model, X_671, X_729, 671, 729, incident=True)
    return promote_point_to_top(model, X_2086)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2086 on the given reference triangle."""
    model = create_model('X_2086 = PK-TRANSFORM OF X_99')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02086(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02086.json"))
    write_center_svg(
        model_acute,
        here / "x-02086.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
