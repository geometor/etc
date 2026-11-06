"""GEOMETOR construction model for X_3942 = X_2310com[INVERSE(n(INTANGENTS TRIANGLE))]."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03942(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3942 = X_2310com[INVERSE(n(INTANGENTS TRIANGLE))] on reference triangle ABC."""
    X_3942 = eval_barycentric_point(model, A, B, C, '(a*(b - c)**(2)*(b**(2) + c**(2) - a**(2)))', ID="X_3942", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_48, X_77, 48, 77, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_269 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)', ID="X_269", classes=["center", "incident"])
    central_line(model, X_19, X_269, 19, 269, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_337 = eval_trilinear_point(model, A, B, C, '(csc(A)*cot(A))/(a**(2) - b*c)', ID="X_337", classes=["center", "incident"])
    central_line(model, X_69, X_337, 69, 337, incident=True)
    return promote_point_to_top(model, X_3942)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3942 on the given reference triangle."""
    model = create_model('X_3942 = X_2310com[INVERSE(n(INTANGENTS TRIANGLE))]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03942(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03942.json"))
    write_center_svg(
        model_acute,
        here / "x-03942.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
