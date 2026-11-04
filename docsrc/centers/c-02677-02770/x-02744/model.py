"""GEOMETOR construction model for X_2744 = SR(X_104, X_107)."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02744(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2744 = SR(X_104, X_107) on reference triangle ABC."""
    X_2719 = point_from_barycentrics(model, A, B, C, -0.16730342, 0.437479, 0.72982443, ID="X_2719", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2744 = reflection_in_point(model, X_2719, X_3, ID="X_2744", classes=["selected", "target"], guide=False)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X_520", classes=["center", "incident"])
    central_line(model, X_104, X_520, 104, 520, incident=True)
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_107, X_517, 107, 517, incident=True)
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    X_1309 = eval_trilinear_point(model, A, B, C, '(csc(2*A))/(4*((sin(B))**(2) - (sin(C))**(2))*cos(B)*cos(C) + (sin(B))**(2)*cos(B) - (sin(C))**(2)*cos(C))', ID="X_1309", classes=["center", "incident"])
    central_line(model, X_72, X_1309, 72, 1309, incident=True)
    return promote_point_to_top(model, X_2744)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2744 on the given reference triangle."""
    model = create_model('X_2744 = SR(X_104, X_107)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02744(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02744.json"))
    write_center_svg(
        model_acute,
        here / "x-02744.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
