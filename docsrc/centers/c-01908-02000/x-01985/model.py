"""GEOMETOR construction model for X_1985 = EULER LINE INTERCEPT OF LINE X_6X_11."""

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
    feuerbach_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01985(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1985 = EULER LINE INTERCEPT OF LINE X_6X_11 on reference triangle ABC."""
    X_1985 = eval_trilinear_point(model, A, B, C, '(sec(A) + sec(B) + sec(C))*csc(A) + (csc(A) + csc(B) + csc(C))*sec(A)', ID="X_1985", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_6, X_11, 6, 11, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_1837 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - 2*cos(B)*cos(C)', ID="X_1837", classes=["center", "incident"])
    central_line(model, X_42, X_1837, 42, 1837, incident=True)
    return promote_point_to_top(model, X_1985)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1985 on the given reference triangle."""
    model = create_model('X_1985 = EULER LINE INTERCEPT OF LINE X_6X_11')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01985(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01985.json"))
    write_center_svg(
        model_acute,
        here / "x-01985.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
