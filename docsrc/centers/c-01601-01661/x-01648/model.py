"""GEOMETOR construction model for X_1648 = TRIPOLAR CENTROID OF X_523."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01648(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1648 = TRIPOLAR CENTROID OF X_523 on reference triangle ABC."""
    X_1641 = point_from_barycentrics(model, A, B, C, -1.6171171, 0.22187902, 2.3952381, ID="X_1641", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_1648 = reflection_in_point(model, X_1641, X_2, ID="X_1648", classes=["selected", "target"], guide=False)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_115, X_125, 115, 125, incident=True)
    X_669 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(2) - c**(2))', ID="X_669", classes=["center", "incident"])
    X_865 = eval_trilinear_point(model, A, B, C, '(sin(2*B)*(csc(C))**(2)*sin(C - A)*csc(A - B) - sin(2*C)*(csc(B))**(2)*sin(B - A)*csc(A - C))', ID="X_865", classes=["center", "incident"])
    central_line(model, X_669, X_865, 669, 865, incident=True)
    return promote_point_to_top(model, X_1648)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1648 on the given reference triangle."""
    model = create_model('X_1648 = TRIPOLAR CENTROID OF X_523')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01648(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01648.json"))
    write_center_svg(
        model_acute,
        here / "x-01648.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
