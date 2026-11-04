"""GEOMETOR construction model for X_2953 = EXCENTRAL-ISOGONAL CONJUGATE OF X_62."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02953(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2953 = EXCENTRAL-ISOGONAL CONJUGATE OF X_62 on reference triangle ABC."""
    X_191 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(b*c + c*a + a*b) + b**(3) + c**(3) - a**(3)', ID="X_191", classes=["center"])
    X_1277 = eval_trilinear_point(model, A, B, C, '- sqrt(3/4) - cos(A +  pi  /6) + cos(B +  pi  /6) + cos(C +  pi  /6)', ID="X_1277", classes=["center"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center"])
    X_2945 = point_from_barycentrics(model, A, B, C, 0.54021963, 0.41139336, 0.048387008, ID="X_2945", classes=["center"])
    central_line(model, X_191, X_1277, 191, 1277)
    central_line(model, X_40, X_2945, 40, 2945)
    X_2953 = intersect_lines(model, X_191, X_1277, X_40, X_2945, ID="X_2953", classes=["selected", "target"])
    X_1761 = point_from_barycentrics(model, A, B, C, 0.54015296, 0.3957935, 0.064053537, ID="X_1761", classes=["center", "incident"])
    X_2321 = point_from_barycentrics(model, A, B, C, 0.47272727, 0.32727273, 0.2, ID="X_2321", classes=["center", "incident"])
    central_line(model, X_1761, X_2321, 1761, 2321, incident=True)
    return promote_point_to_top(model, X_2953)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2953 on the given reference triangle."""
    model = create_model('X_2953 = EXCENTRAL-ISOGONAL CONJUGATE OF X_62')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02953(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02953.json"))
    write_center_svg(
        model_acute,
        here / "x-02953.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
