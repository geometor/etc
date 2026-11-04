"""GEOMETOR construction model for X_2955 = EXCENTRAL-ISOGONAL CONJUGATE OF X_72."""

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
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02955(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2955 = EXCENTRAL-ISOGONAL CONJUGATE OF X_72 on reference triangle ABC."""
    X_950 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)*(2*a**(3) + (b + c)*(a**(2) + (b - c)**(2)))', ID="X_950", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2955 = ceva_conjugate(model, A, B, C, X_950, X_1, ID="X_2955", classes=["selected", "target"])
    X_951 = eval_trilinear_point(model, A, B, C, '(a/((b + c - a)*(2*a**(3) + (b + c)*(a**(2) + (b - c)**(2)))))', ID="X_951", classes=["center", "incident"])
    central_line(model, X_1, X_951, 1, 951, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_1718 = point_from_barycentrics(model, A, B, C, 0.43333333, -0.6, 1.1666667, ID="X_1718", classes=["center", "incident"])
    central_line(model, X_35, X_1718, 35, 1718, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_1723 = point_from_barycentrics(model, A, B, C, -0.12103506, 0.28547579, 0.83555927, ID="X_1723", classes=["center", "incident"])
    central_line(model, X_40, X_1723, 40, 1723, incident=True)
    return promote_point_to_top(model, X_2955)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2955 on the given reference triangle."""
    model = create_model('X_2955 = EXCENTRAL-ISOGONAL CONJUGATE OF X_72')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02955(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02955.json"))
    write_center_svg(
        model_acute,
        here / "x-02955.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
