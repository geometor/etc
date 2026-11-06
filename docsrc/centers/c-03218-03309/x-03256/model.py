"""GEOMETOR construction model for X_3256 = ISOGONAL CONJUGATE OF X_3255."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03256(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3256 = ISOGONAL CONJUGATE OF X_3255 on reference triangle ABC."""
    X_3255 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - a)/(b*c + (b + c - a)**(2)))', ID="X_3255", classes=["center"])
    X_3256 = isogonal_conjugate(model, A, B, C, X_3255, ID="X_3256", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_42, X_109, 42, 109, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_100, X_226, 100, 226, incident=True)
    return promote_point_to_top(model, X_3256)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3256 on the given reference triangle."""
    model = create_model('X_3256 = ISOGONAL CONJUGATE OF X_3255')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03256(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03256.json"))
    write_center_svg(
        model_acute,
        here / "x-03256.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
