"""GEOMETOR construction model for X_961 = ISOGONAL CONJUGATE OF X_960."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00961(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_961 = ISOGONAL CONJUGATE OF X_960 on reference triangle ABC."""
    X_960 = eval_trilinear_point(model, A, B, C, '((b + c - a)*(b**(2) + c**(2) + a*b + a*c))', ID="X_960", classes=["center"])
    X_961 = isogonal_conjugate(model, A, B, C, X_960, ID="X_961", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    central_line(model, X_2, X_12, 2, 12, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    central_line(model, X_65, X_81, 65, 81, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_429 = eval_barycentric_point(model, A, B, C, '(b + c) * (-a**(2) + b**(2) - c**(2)) * (a**(2) + b**(2) - c**(2)) * (a*b + b**(2) + a*c + c**(2))', ID="X_429", classes=["center", "incident"])
    central_line(model, X_108, X_429, 108, 429, incident=True)
    return promote_point_to_top(model, X_961)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_961 on the given reference triangle."""
    model = create_model('X_961 = ISOGONAL CONJUGATE OF X_960')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00961(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00961.json"))
    write_center_svg(
        model_acute,
        here / "x-00961.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
