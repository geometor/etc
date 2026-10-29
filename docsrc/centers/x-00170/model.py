"""GEOMETOR construction model for X(170) = X(9)-ALEPH CONJUGATE OF X(9)."""

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


def construct_x_00170(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(170) = X(9)-ALEPH CONJUGATE OF X(9) on reference triangle ABC."""
    X_170 = eval_trilinear_point(model, A, B, C, '- (tan(A/2))*(sec(A/2))**(2) + (tan(B/2))*(sec(B/2))**(2) + (tan(C/2))*(sec(C/2))**(2)', ID="X(170)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X(43)", classes=["center", "incident"])
    X_218 = eval_trilinear_point(model, A, B, C, '(cos(A/2))**(2)*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4))', ID="X(218)", classes=["center", "incident"])
    central_line(model, X_43, X_218, 43, 218, incident=True)
    return promote_point_to_top(model, X_170)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(170) on the given reference triangle."""
    model = create_model('X(170) = X(9)-ALEPH CONJUGATE OF X(9)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00170(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00170.json"))
    write_center_svg(
        model_acute,
        here / "x-00170.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
