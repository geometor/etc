"""GEOMETOR construction model for X(914) = ISOGONAL CONJUGATE OF X(913)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00914(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(914) = ISOGONAL CONJUGATE OF X(913) on reference triangle ABC."""
    X_913 = point_from_barycentrics(model, A, B, C, -0.12730133, 0.53064554, 0.59665579, ID="X(913)", classes=["center"])
    X_914 = isogonal_conjugate(model, A, B, C, X_913, ID="X(914)", classes=["selected", "target"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X(63)", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    central_line(model, X_63, X_69, 63, 69, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_224 = eval_trilinear_point(model, A, B, C, '(cot(B)*(cos(B/2))**(2) + cot(C)*(cos(C/2))**(2) - cot(A)*(cos(A/2))**(2))*cot(A)', ID="X(224)", classes=["center", "incident"])
    central_line(model, X_8, X_224, 8, 224, incident=True)
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X(514)", classes=["center", "incident"])
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X(661)", classes=["center", "incident"])
    central_line(model, X_514, X_661, 514, 661, incident=True)
    return promote_point_to_top(model, X_914)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(914) on the given reference triangle."""
    model = create_model('X(914) = ISOGONAL CONJUGATE OF X(913)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00914(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00914.json"))
    write_center_svg(
        model_acute,
        here / "x-00914.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
