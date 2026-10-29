"""GEOMETOR construction model for X(603) = X(58)-CEVA CONJUGATE OF X(56)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00603(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(603) = X(58)-CEVA CONJUGATE OF X(56) on reference triangle ABC."""
    X_318 = eval_trilinear_point(model, A, B, C, '(1 + sec(A))/a**(2)', ID="X(318)", classes=["center"])
    X_603 = isogonal_conjugate(model, A, B, C, X_318, ID="X(603)", classes=["selected", "target"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X(28)", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center", "incident"])
    central_line(model, X_28, X_34, 28, 34, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X(73)", classes=["center", "incident"])
    central_line(model, X_3, X_73, 3, 73, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X(36)", classes=["center", "incident"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X(47)", classes=["center", "incident"])
    central_line(model, X_36, X_47, 36, 47, incident=True)
    return promote_point_to_top(model, X_603)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(603) on the given reference triangle."""
    model = create_model('X(603) = X(58)-CEVA CONJUGATE OF X(56)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00603(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00603.json"))
    write_center_svg(
        model_acute,
        here / "x-00603.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
