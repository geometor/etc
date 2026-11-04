"""GEOMETOR construction model for X_2981 = DC(X_13)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02981(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2981 = DC(X_13) on reference triangle ABC."""
    X_396 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 2*cos(A -  pi  /3)', ID="X_396", classes=["center"])
    X_2981 = isogonal_conjugate(model, A, B, C, X_396, ID="X_2981", classes=["selected", "target"])
    X_61 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /6)', ID="X_61", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_61, X_110, 61, 110, incident=True)
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center", "incident"])
    X_1337 = eval_barycentric_point(model, A, B, C, '(a**(2)*(2*D*U - 3**(1/2)*V*W)/(4*D + 3**(1/2)*a**(2)))', ID="X_1337", classes=["center", "incident"])
    central_line(model, X_15, X_1337, 15, 1337, incident=True)
    X_1989 = eval_trilinear_point(model, A, B, C, '(sin(A))**(2)*csc(3*A)', ID="X_1989", classes=["center", "incident"])
    central_line(model, X_396, X_1989, 396, 1989, incident=True)
    return promote_point_to_top(model, X_2981)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2981 on the given reference triangle."""
    model = create_model('X_2981 = DC(X_13)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02981(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02981.json"))
    write_center_svg(
        model_acute,
        here / "x-02981.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
