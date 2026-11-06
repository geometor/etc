"""GEOMETOR construction model for X_3903 = X_115com[INVERSE(n(3rd EULER TRIANGLE))]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03903(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3903 = X_115com[INVERSE(n(3rd EULER TRIANGLE))] on reference triangle ABC."""
    X_3903 = eval_barycentric_point(model, A, B, C, '(a*(a - b)*(a - c)*(b**(2) + a*c)*(c**(2) + a*b))', ID="X_3903", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_99, X_512, 99, 512, incident=True)
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center", "incident"])
    X_1320 = eval_trilinear_point(model, A, B, C, '((b + c - a)/ (b + c - 2*a))', ID="X_1320", classes=["center", "incident"])
    central_line(model, X_256, X_1320, 256, 1320, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1581 = eval_trilinear_point(model, A, B, C, '1/(a**(4) - b**(2)*c**(2))', ID="X_1581", classes=["center", "incident"])
    central_line(model, X_1, X_1581, 1, 1581, incident=True)
    return promote_point_to_top(model, X_3903)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3903 on the given reference triangle."""
    model = create_model('X_3903 = X_115com[INVERSE(n(3rd EULER TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03903(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03903.json"))
    write_center_svg(
        model_acute,
        here / "x-03903.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
