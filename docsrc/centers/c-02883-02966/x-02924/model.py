"""GEOMETOR construction model for X_2924 = TANGENTIAL-ISOGONAL CONJUGATE OF X_14."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02924(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2924 = TANGENTIAL-ISOGONAL CONJUGATE OF X_14 on reference triangle ABC."""
    X_2924 = point_from_barycentrics(model, A, B, C, 0.63692502, -0.69094425, 1.0540192, ID="X_2924", classes=["selected", "target"])
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A-  pi  /3)', ID="X_16", classes=["center", "incident"])
    X_2070 = eval_trilinear_point(model, A, B, C, '(J**(2) - 2)*cos(A) + 4*cos(B)*cos(C)', ID="X_2070", classes=["center", "incident"])
    central_line(model, X_16, X_2070, 16, 2070, incident=True)
    return promote_point_to_top(model, X_2924)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2924 on the given reference triangle."""
    model = create_model('X_2924 = TANGENTIAL-ISOGONAL CONJUGATE OF X_14')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02924(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02924.json"))
    write_center_svg(
        model_acute,
        here / "x-02924.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
