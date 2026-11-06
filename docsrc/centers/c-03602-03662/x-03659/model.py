"""GEOMETOR construction model for X_3659 = FEUERBACH POINT OF EXCENTRAL TRIANGLE."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_03659(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3659 = FEUERBACH POINT OF EXCENTRAL TRIANGLE on reference triangle ABC."""
    X_3659 = eval_trilinear_point(model, A, B, C, '((cos(A/2))/(sin(B/2) - sin(C/2)))', ID="X_3659", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_164 = eval_trilinear_point(model, A, B, C, 'sin(B/2) + sin(C/2) - sin(A/2)', ID="X_164", classes=["center", "incident"])
    central_line(model, X_3, X_164, 3, 164, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_258 = eval_trilinear_point(model, A, B, C, '1/(cos(B/2) + cos(C/2) - cos(A/2))', ID="X_258", classes=["center", "incident"])
    central_line(model, X_55, X_258, 55, 258, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    X_1130 = eval_trilinear_point(model, A, B, C, '(sin(( pi  + 3*A)/4)/sin(( pi  - A)/4))', ID="X_1130", classes=["center", "incident"])
    central_line(model, X_106, X_1130, 106, 1130, incident=True)
    return promote_point_to_top(model, X_3659)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3659 on the given reference triangle."""
    model = create_model('X_3659 = FEUERBACH POINT OF EXCENTRAL TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03659(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03659.json"))
    write_center_svg(
        model_acute,
        here / "x-03659.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
