"""GEOMETOR construction model for X_1995 = ORTHOCORRESPONDENT OF X_6."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01995(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1995 = ORTHOCORRESPONDENT OF X_6 on reference triangle ABC."""
    X_598 = eval_trilinear_point(model, A, B, C, 'b*c/(a**(2) - 2*b**(2) - 2*c**(2))', ID="X_598", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1995 = ceva_conjugate(model, A, B, C, X_598, X_6, ID="X_1995", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_6, X_110, 6, 110, incident=True)
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center", "incident"])
    central_line(model, X_107, X_264, 107, 264, incident=True)
    return promote_point_to_top(model, X_1995)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1995 on the given reference triangle."""
    model = create_model('X_1995 = ORTHOCORRESPONDENT OF X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01995(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01995.json"))
    write_center_svg(
        model_acute,
        here / "x-01995.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
