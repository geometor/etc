"""GEOMETOR construction model for X_2103 = REFLECTION OF X_1114 IN X_1."""

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
    intersect_lines,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02103(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2103 = REFLECTION OF X_1114 IN X_1 on reference triangle ABC."""
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center"])
    X_944 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a**(4) - 2*a**(3)*(b + c) + (b - c)**(2)*(2*a*b + 2*a*c - 2*b*c - b**(2) - c**(2) - 2*a**(2)))', ID="X_944", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1114 = eval_trilinear_point(model, A, B, C, '(R + d)*cos(A) - 2*R*cos(B)*cos(C)', ID="X_1114", classes=["center"])
    central_line(model, X_30, X_944, 30, 944)
    central_line(model, X_1, X_1114, 1, 1114)
    X_2103 = intersect_lines(model, X_30, X_944, X_1, X_1114, ID="X_2103", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_1312 = eval_trilinear_point(model, A, B, C, '((J - 1)*cos(A) + 2*(J + 1)*cos(B)*cos(C))', ID="X_1312", classes=["center", "incident"])
    central_line(model, X_8, X_1312, 8, 1312, incident=True)
    return promote_point_to_top(model, X_2103)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2103 on the given reference triangle."""
    model = create_model('X_2103 = REFLECTION OF X_1114 IN X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02103(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02103.json"))
    write_center_svg(
        model_acute,
        here / "x-02103.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
