"""GEOMETOR construction model for X_2175 = X_2-ISOCONJUGATE OF X_85."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02175(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2175 = X_2-ISOCONJUGATE OF X_85 on reference triangle ABC."""
    X_2175 = eval_trilinear_point(model, A, B, C, '(cot(A/2)*(sin(A))**(3))', ID="X_2175", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X_181", classes=["center", "incident"])
    central_line(model, X_25, X_181, 25, 181, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_31, X_184, 31, 184, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X_219", classes=["center", "incident"])
    central_line(model, X_55, X_219, 55, 219, incident=True)
    return promote_point_to_top(model, X_2175)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2175 on the given reference triangle."""
    model = create_model('X_2175 = X_2-ISOCONJUGATE OF X_85')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02175(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02175.json"))
    write_center_svg(
        model_acute,
        here / "x-02175.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
