"""GEOMETOR construction model for X_1260 = ISOGONAL CONJUGATE OF X_1119."""

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
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01260(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1260 = ISOGONAL CONJUGATE OF X_1119 on reference triangle ABC."""
    X_1119 = eval_trilinear_point(model, A, B, C, '((1 - sec(A))/(1 + cos(A)))', ID="X_1119", classes=["center"])
    X_1260 = isogonal_conjugate(model, A, B, C, X_1119, ID="X_1260", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_9, X_55, 9, 55, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_3, X_63, 3, 63, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_218 = eval_trilinear_point(model, A, B, C, '((cos(A/2))**(2)*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4)))', ID="X_218", classes=["center", "incident"])
    central_line(model, X_31, X_218, 31, 218, incident=True)
    return promote_point_to_top(model, X_1260)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1260 on the given reference triangle."""
    model = create_model('X_1260 = ISOGONAL CONJUGATE OF X_1119')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01260(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01260.json"))
    write_center_svg(
        model_acute,
        here / "x-01260.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
