"""GEOMETOR construction model for X_1429 = X_239-BETH CONJUGATE OF X_239."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01429(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1429 = X_239-BETH CONJUGATE OF X_239 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center"])
    central_line(model, X_1, X_3, 1, 3)
    central_line(model, X_83, X_226, 83, 226)
    X_1429 = intersect_lines(model, X_1, X_3, X_83, X_226, ID="X_1429", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_604 = eval_trilinear_point(model, A, B, C, 'a*(1 - cos(A))', ID="X_604", classes=["center", "incident"])
    central_line(model, X_7, X_604, 7, 604, incident=True)
    return promote_point_to_top(model, X_1429)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1429 on the given reference triangle."""
    model = create_model('X_1429 = X_239-BETH CONJUGATE OF X_239')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01429(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01429.json"))
    write_center_svg(
        model_acute,
        here / "x-01429.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
