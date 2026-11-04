"""GEOMETOR construction model for X_1993 = ORTHOCORRESPONDENT OF X_3."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01993(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1993 = ORTHOCORRESPONDENT OF X_3 on reference triangle ABC."""
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center"])
    X_1993 = reflection_in_point(model, X_22, X_184, ID="X_1993", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_3, X_54, 3, 54, incident=True)
    X_26 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)*cos(2*B) + c**(2)*cos(2*C) - a**(2)*cos(2*A))', ID="X_26", classes=["center", "incident"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    central_line(model, X_26, X_49, 26, 49, incident=True)
    return promote_point_to_top(model, X_1993)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1993 on the given reference triangle."""
    model = create_model('X_1993 = ORTHOCORRESPONDENT OF X_3')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01993(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01993.json"))
    write_center_svg(
        model_acute,
        here / "x-01993.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
