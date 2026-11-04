"""GEOMETOR construction model for X_2958 = EXCENTRAL-ISOGONAL CONJUGATE OF X_101."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02958(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2958 = EXCENTRAL-ISOGONAL CONJUGATE OF X_101 on reference triangle ABC."""
    X_1146 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)*(b + c - a))**(2)', ID="X_1146", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2958 = ceva_conjugate(model, A, B, C, X_1146, X_1, ID="X_2958", classes=["selected", "target"])
    X_484 = eval_trilinear_point(model, A, B, C, '1 + 2*(cos(A) - cos(B) - cos(C))', ID="X_484", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    central_line(model, X_484, X_516, 484, 516, incident=True)
    X_1262 = point_from_barycentrics(model, A, B, C, 0.10548523, 0.067510549, 0.82700422, ID="X_1262", classes=["center", "incident"])
    central_line(model, X_1, X_1262, 1, 1262, incident=True)
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    X_1768 = eval_trilinear_point(model, A, B, C, 'a**(5) - a**(4)*(b + c) - a**(3)*(2*b**(2) - 5*b*c + 2*c**(2)) + 2*a**(2)*(b - c)**(2)*(b + c) + a*(b - c)**(2)*(b**(2) - b*c + c**(2)) - b**(5) + b**(4)*c + b*c**(4) - c**(5)', ID="X_1768", classes=["center", "incident"])
    central_line(model, X_514, X_1768, 514, 1768, incident=True)
    return promote_point_to_top(model, X_2958)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2958 on the given reference triangle."""
    model = create_model('X_2958 = EXCENTRAL-ISOGONAL CONJUGATE OF X_101')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02958(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02958.json"))
    write_center_svg(
        model_acute,
        here / "x-02958.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
