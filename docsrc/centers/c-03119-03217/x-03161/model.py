"""GEOMETOR construction model for X_3161 = X_2-CEVA CONJUGATE OF X_8."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03161(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3161 = X_2-CEVA CONJUGATE OF X_8 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center"])
    X_3161 = crosspoint(model, A, B, C, X_2, X_145, ID="X_3161", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_8, X_9, 8, 9, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    X_344 = eval_trilinear_point(model, A, B, C, '((csc(A/2))**(2))*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4))', ID="X_344", classes=["center", "incident"])
    central_line(model, X_190, X_344, 190, 344, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_644 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b - c))', ID="X_644", classes=["center", "incident"])
    central_line(model, X_6, X_644, 6, 644, incident=True)
    return promote_point_to_top(model, X_3161)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3161 on the given reference triangle."""
    model = create_model('X_3161 = X_2-CEVA CONJUGATE OF X_8')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03161(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03161.json"))
    write_center_svg(
        model_acute,
        here / "x-03161.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
