"""GEOMETOR construction model for X_1229 = ISOTOMIC CONJUGATE OF X_1170."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01229(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1229 = ISOTOMIC CONJUGATE OF X_1170 on reference triangle ABC."""
    X_1170 = eval_trilinear_point(model, A, B, C, '1/((a - b - c)*(a*(b + c) - (b - c)**(2)))', ID="X_1170", classes=["center"])
    X_1229 = isotomic_conjugate(model, A, B, C, X_1170, ID="X_1229", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_2, X_37, 2, 37, incident=True)
    X_294 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b**(2) + c**(2) - a*b - a*c))', ID="X_294", classes=["center", "incident"])
    X_314 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2)*(b + c - a)/(b + c))', ID="X_314", classes=["center", "incident"])
    central_line(model, X_294, X_314, 294, 314, incident=True)
    X_1089 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2)*(b + c)**(2))', ID="X_1089", classes=["center", "incident"])
    X_1210 = eval_barycentric_point(model, A, B, C, 'a**(3)*(b + c) - a**(2)*(b - c)**(2) - a*(b - c)**(2)*(b + c) + (b**(2) - c**(2))**(2)', ID="X_1210", classes=["center", "incident"])
    central_line(model, X_1089, X_1210, 1089, 1210, incident=True)
    return promote_point_to_top(model, X_1229)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1229 on the given reference triangle."""
    model = create_model('X_1229 = ISOTOMIC CONJUGATE OF X_1170')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01229(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01229.json"))
    write_center_svg(
        model_acute,
        here / "x-01229.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
