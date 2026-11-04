"""GEOMETOR construction model for X_1403 = X_43-BETH CONJUGATE OF X_43."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01403(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1403 = X_43-BETH CONJUGATE OF X_43 on reference triangle ABC."""
    X_604 = eval_trilinear_point(model, A, B, C, 'a*(1 - cos(A))', ID="X_604", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_1403 = ceva_conjugate(model, A, B, C, X_604, X_56, ID="X_1403", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_183 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*cos(A- omega )', ID="X_183", classes=["center", "incident"])
    central_line(model, X_75, X_183, 75, 183, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_727 = eval_trilinear_point(model, A, B, C, '(1/(a **(-3)*(b **(-1) + c **(-1)) - a **(-2)*(b **(-2) + c **(-2))))', ID="X_727", classes=["center", "incident"])
    central_line(model, X_109, X_727, 109, 727, incident=True)
    return promote_point_to_top(model, X_1403)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1403 on the given reference triangle."""
    model = create_model('X_1403 = X_43-BETH CONJUGATE OF X_43')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01403(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01403.json"))
    write_center_svg(
        model_acute,
        here / "x-01403.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
