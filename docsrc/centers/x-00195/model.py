"""GEOMETOR construction model for X(195) = X(5)-CEVA CONJUGATE OF X(3)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00195(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(195) = X(5)-CEVA CONJUGATE OF X(3) on reference triangle ABC."""
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_195 = ceva_conjugate(model, A, B, C, X_5, X_3, ID="X(195)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /6)', ID="X(17)", classes=["center", "incident"])
    central_line(model, X_6, X_17, 6, 17, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    central_line(model, X_3, X_54, 3, 54, incident=True)
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X(49)", classes=["center", "incident"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X(52)", classes=["center", "incident"])
    central_line(model, X_49, X_52, 49, 52, incident=True)
    return promote_point_to_top(model, X_195)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(195) on the given reference triangle."""
    model = create_model('X(195) = X(5)-CEVA CONJUGATE OF X(3)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00195(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00195.json"))
    write_center_svg(
        model_acute,
        here / "x-00195.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
