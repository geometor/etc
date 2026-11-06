"""GEOMETOR construction model for X_3690 = X_1746com(EXTOUCH TRIANGLE)."""

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


def construct_x_03690(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3690 = X_1746com(EXTOUCH TRIANGLE) on reference triangle ABC."""
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center"])
    X_3690 = crosspoint(model, A, B, C, X_71, X_72, ID="X_3690", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_9, X_51, 9, 51, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_220 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)**(2)', ID="X_220", classes=["center", "incident"])
    central_line(model, X_25, X_220, 25, 220, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_209 = eval_trilinear_point(model, A, B, C, '((sin(B) + sin(C))*(sin(A) + sin(A - B) + sin(A - C)))', ID="X_209", classes=["center", "incident"])
    central_line(model, X_37, X_209, 37, 209, incident=True)
    return promote_point_to_top(model, X_3690)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3690 on the given reference triangle."""
    model = create_model('X_3690 = X_1746com(EXTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03690(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03690.json"))
    write_center_svg(
        model_acute,
        here / "x-03690.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
