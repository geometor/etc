"""GEOMETOR construction model for X_923 = POINT ALBIREO."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00923(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_923 = POINT ALBIREO on reference triangle ABC."""
    X_923 = eval_trilinear_point(model, A, B, C, '(a**(2)/(b**(2) + c**(2) - 2*a**(2)))', ID="X_923", classes=["selected", "target"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_42, X_101, 42, 101, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    central_line(model, X_31, X_163, 31, 163, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X_662", classes=["center", "incident"])
    central_line(model, X_1, X_662, 1, 662, incident=True)
    return promote_point_to_top(model, X_923)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_923 on the given reference triangle."""
    model = create_model('X_923 = POINT ALBIREO')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00923(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00923.json"))
    write_center_svg(
        model_acute,
        here / "x-00923.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
