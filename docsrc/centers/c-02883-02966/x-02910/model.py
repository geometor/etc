"""GEOMETOR construction model for X_2910 = ORTHIC-ISOGONAL CONJUGATE OF X_40."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02910(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2910 = ORTHIC-ISOGONAL CONJUGATE OF X_40 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center"])
    X_2910 = ceva_conjugate(model, A, B, C, X_4, X_40, ID="X_2910", classes=["selected", "target"])
    X_198 = eval_trilinear_point(model, A, B, C, '(a*(cos(B) + cos(C) - cos(A) - 1))', ID="X_198", classes=["center", "incident"])
    central_line(model, X_40, X_198, 40, 198, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_1181 = eval_trilinear_point(model, A, B, C, '((1 - cos(A)*sin(B)*sin(C))*cos(A))', ID="X_1181", classes=["center", "incident"])
    central_line(model, X_9, X_1181, 9, 1181, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_1753 = point_from_barycentrics(model, A, B, C, -0.10341592, 0.079954955, 1.023461, ID="X_1753", classes=["center", "incident"])
    central_line(model, X_101, X_1753, 101, 1753, incident=True)
    return promote_point_to_top(model, X_2910)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2910 on the given reference triangle."""
    model = create_model('X_2910 = ORTHIC-ISOGONAL CONJUGATE OF X_40')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02910(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02910.json"))
    write_center_svg(
        model_acute,
        here / "x-02910.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
