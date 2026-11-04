"""GEOMETOR construction model for X_2258 = X_2-ISOCONJUGATE OF X_940."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02258(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2258 = X_2-ISOCONJUGATE OF X_940 on reference triangle ABC."""
    X_941 = eval_trilinear_point(model, A, B, C, '(1/(a**(2) + a*(b + c) + 2*b*c))', ID="X_941", classes=["center"])
    X_959 = eval_trilinear_point(model, A, B, C, '(1/((b + c - a)*(a**(2) + a*b + a*c + 2*b*c)))', ID="X_959", classes=["center"])
    X_2258 = crosspoint(model, A, B, C, X_941, X_959, ID="X_2258", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    central_line(model, X_9, X_42, 9, 42, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    central_line(model, X_55, X_213, 55, 213, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    central_line(model, X_31, X_284, 31, 284, incident=True)
    return promote_point_to_top(model, X_2258)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2258 on the given reference triangle."""
    model = create_model('X_2258 = X_2-ISOCONJUGATE OF X_940')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02258(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02258.json"))
    write_center_svg(
        model_acute,
        here / "x-02258.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
