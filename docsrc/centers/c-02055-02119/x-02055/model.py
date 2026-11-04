"""GEOMETOR construction model for X_2055 = ORION TRANSFORM OF X_3."""

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
    nine_point_center_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02055(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2055 = ORION TRANSFORM OF X_3 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_275 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*sec(B - C)', ID="X_275", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    central_line(model, X_5, X_275, 5, 275)
    X_2055 = intersect_lines(model, X_3, X_6, X_5, X_275, ID="X_2055", classes=["selected", "target"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_418 = eval_trilinear_point(model, A, B, C, '(cos(A))*(csc(2*B) + csc(2*C))', ID="X_418", classes=["center", "incident"])
    central_line(model, X_54, X_418, 54, 418, incident=True)
    return promote_point_to_top(model, X_2055)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2055 on the given reference triangle."""
    model = create_model('X_2055 = ORION TRANSFORM OF X_3')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02055(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02055.json"))
    write_center_svg(
        model_acute,
        here / "x-02055.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
