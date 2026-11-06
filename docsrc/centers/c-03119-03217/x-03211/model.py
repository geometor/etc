"""GEOMETOR construction model for X_3211 = X_57-CEVA CONJUGATE OF X_3."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03211(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3211 = X_57-CEVA CONJUGATE OF X_3 on reference triangle ABC."""
    X_3211 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - a**(2))*(a**(4) - 2*a**(3)*(b + c) - 2*a**(2)*b*c + 2*a*(b**(3) + c**(3)) - (b**(2) - c**(2))**(2)))', ID="X_3211", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_3, X_48, 3, 48, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_169 = eval_trilinear_point(model, A, B, C, '- (sin(A))*(cos(A/2))**(2) + (sin(B))*(cos(B/2))**(2) + (sin(C))*(cos(C/2))**(2)', ID="X_169", classes=["center", "incident"])
    central_line(model, X_6, X_169, 6, 169, incident=True)
    X_155 = eval_trilinear_point(model, A, B, C, '(cos(A))*((cos(B))**(2) + (cos(C))**(2) - (cos(A))**(2))', ID="X_155", classes=["center", "incident"])
    X_610 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C) - tan(A)', ID="X_610", classes=["center", "incident"])
    central_line(model, X_155, X_610, 155, 610, incident=True)
    return promote_point_to_top(model, X_3211)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3211 on the given reference triangle."""
    model = create_model('X_3211 = X_57-CEVA CONJUGATE OF X_3')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03211(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03211.json"))
    write_center_svg(
        model_acute,
        here / "x-03211.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
