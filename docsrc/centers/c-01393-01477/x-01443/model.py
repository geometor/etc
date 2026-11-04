"""GEOMETOR construction model for X_1443 = X_320-BETH CONJUGATE OF X_320."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01443(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1443 = X_320-BETH CONJUGATE OF X_320 on reference triangle ABC."""
    X_1443 = eval_trilinear_point(model, A, B, C, '((1 - 2*cos(A))/(1 + cos(A)))', ID="X_1443", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_89 = eval_trilinear_point(model, A, B, C, '1/(2*b + 2*c - a)', ID="X_89", classes=["center", "incident"])
    central_line(model, X_57, X_89, 57, 89, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_241 = eval_trilinear_point(model, A, B, C, '(cos(B/2))**(4) - ((cos(A/2))**(2))*((cos(B/2))**(2) +(cos(C/2))**(2)) + (cos(C/2))**(4)', ID="X_241", classes=["center", "incident"])
    central_line(model, X_44, X_241, 44, 241, incident=True)
    return promote_point_to_top(model, X_1443)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1443 on the given reference triangle."""
    model = create_model('X_1443 = X_320-BETH CONJUGATE OF X_320')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01443(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01443.json"))
    write_center_svg(
        model_acute,
        here / "x-01443.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
