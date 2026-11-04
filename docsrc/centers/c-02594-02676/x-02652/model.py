"""GEOMETOR construction model for X_2652 = TRILINEAR POLE OF PU(81)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02652(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2652 = TRILINEAR POLE OF PU(81) on reference triangle ABC."""
    X_2651 = eval_trilinear_point(model, A, B, C, '(1/((cos(A) + cos(B))*(cos(A) + cos(C))) - 1/(cos(B) + cos(C))**(2))', ID="X_2651", classes=["center"])
    X_2652 = isogonal_conjugate(model, A, B, C, X_2651, ID="X_2652", classes=["selected", "target"])
    X_243 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(2) - cos(B)*cos(C))', ID="X_243", classes=["center", "incident"])
    X_415 = eval_barycentric_point(model, A, B, C, '(a + b) * (a + c) * (a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2)) * (a**(3) - 2*a**(2)*b + b**(3) - 2*a**(2)*c + a*b*c + c**(3))', ID="X_415", classes=["center", "incident"])
    central_line(model, X_243, X_415, 243, 415, incident=True)
    X_409 = eval_barycentric_point(model, A, B, C, 'a*(a + b) * (a + c) * (a**(4) - a**(3)*b + a*b**(3) - b**(4) - a**(3)*c + a**(2)*b*c + a*b**(2)*c + b**(3)*c + a*b*c**(2) + 4*b**(2)*c**(2) + a*c**(3) + b*c**(3) - c**(4))', ID="X_409", classes=["center", "incident"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X_662", classes=["center", "incident"])
    central_line(model, X_409, X_662, 409, 662, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_1247 = point_from_barycentrics(model, A, B, C, 0.47979502, 0.29838347, 0.22182151, ID="X_1247", classes=["center", "incident"])
    central_line(model, X_3, X_1247, 3, 1247, incident=True)
    return promote_point_to_top(model, X_2652)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2652 on the given reference triangle."""
    model = create_model('X_2652 = TRILINEAR POLE OF PU(81)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02652(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02652.json"))
    write_center_svg(
        model_acute,
        here / "x-02652.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
