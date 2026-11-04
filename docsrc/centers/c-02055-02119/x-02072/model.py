"""GEOMETOR construction model for X_2072 = INVERSE-IN-CIRCUMCIRCLE OF X_26."""

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
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02072(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2072 = INVERSE-IN-CIRCUMCIRCLE OF X_26 on reference triangle ABC."""
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X_186", classes=["center"])
    X_2072 = complement(model, A, B, C, X_186, ID="X_2072", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    X_339 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A))/a**(4)', ID="X_339", classes=["center", "incident"])
    central_line(model, X_325, X_339, 325, 339, incident=True)
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X_127", classes=["center", "incident"])
    X_625 = eval_trilinear_point(model, A, B, C, '(2*(b**(4) + c**(4) - b**(2)*c**(2)) - a**(2)*(b**(2) + c**(2)))/a', ID="X_625", classes=["center", "incident"])
    central_line(model, X_127, X_625, 127, 625, incident=True)
    return promote_point_to_top(model, X_2072)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2072 on the given reference triangle."""
    model = create_model('X_2072 = INVERSE-IN-CIRCUMCIRCLE OF X_26')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02072(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02072.json"))
    write_center_svg(
        model_acute,
        here / "x-02072.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
