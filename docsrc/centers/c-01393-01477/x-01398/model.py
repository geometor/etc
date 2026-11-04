"""GEOMETOR construction model for X_1398 = X_34-BETH CONJUGATE OF X_34."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01398(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1398 = X_34-BETH CONJUGATE OF X_34 on reference triangle ABC."""
    X_1265 = eval_trilinear_point(model, A, B, C, '((cos(A))*((csc(A/2))**(4)))', ID="X_1265", classes=["center"])
    X_1398 = isogonal_conjugate(model, A, B, C, X_1265, ID="X_1398", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_25, X_34, 25, 34, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_279 = eval_trilinear_point(model, A, B, C, 'csc(A)*(tan(A/2))**(2)', ID="X_279", classes=["center", "incident"])
    central_line(model, X_28, X_279, 28, 279, incident=True)
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    X_221 = eval_trilinear_point(model, A, B, C, '((sin(A/2))**(2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_221", classes=["center", "incident"])
    central_line(model, X_184, X_221, 184, 221, incident=True)
    return promote_point_to_top(model, X_1398)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1398 on the given reference triangle."""
    model = create_model('X_1398 = X_34-BETH CONJUGATE OF X_34')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01398(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01398.json"))
    write_center_svg(
        model_acute,
        here / "x-01398.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
