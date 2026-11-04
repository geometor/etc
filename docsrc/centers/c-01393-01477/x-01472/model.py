"""GEOMETOR construction model for X_1472 = X_1036-BETH CONJUGATE OF X_1036."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01472(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1472 = X_1036-BETH CONJUGATE OF X_1036 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    central_line(model, X_3, X_31, 3, 31)
    central_line(model, X_32, X_48, 32, 48)
    X_1472 = intersect_lines(model, X_3, X_31, X_32, X_48, ID="X_1472", classes=["selected", "target"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_614 = eval_trilinear_point(model, A, B, C, 'a**(2) + b**(2) + c**(2) - 2*b*c', ID="X_614", classes=["center", "incident"])
    central_line(model, X_28, X_614, 28, 614, incident=True)
    return promote_point_to_top(model, X_1472)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1472 on the given reference triangle."""
    model = create_model('X_1472 = X_1036-BETH CONJUGATE OF X_1036')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01472(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01472.json"))
    write_center_svg(
        model_acute,
        here / "x-01472.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
