"""GEOMETOR construction model for X_1460 = X_612-BETH CONJUGATE OF X_612."""

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
    incenter_of,
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01460(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1460 = X_612-BETH CONJUGATE OF X_612 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    central_line(model, X_1, X_3, 1, 3)
    central_line(model, X_25, X_31, 25, 31)
    X_1460 = intersect_lines(model, X_1, X_3, X_25, X_31, ID="X_1460", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X_181", classes=["center", "incident"])
    central_line(model, X_6, X_181, 6, 181, incident=True)
    return promote_point_to_top(model, X_1460)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1460 on the given reference triangle."""
    model = create_model('X_1460 = X_612-BETH CONJUGATE OF X_612')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01460(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01460.json"))
    write_center_svg(
        model_acute,
        here / "x-01460.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
