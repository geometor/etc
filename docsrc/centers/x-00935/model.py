"""GEOMETOR construction model for X(935) = POINT ALCOR."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00935(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(935) = POINT ALCOR on reference triangle ABC."""
    X_935 = eval_barycentric_point(model, A, B, C, '1/((b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2)))', ID="X(935)", classes=["selected", "target"])
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(67)", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X(74)", classes=["center", "incident"])
    central_line(model, X_67, X_74, 67, 74, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X(98)", classes=["center", "incident"])
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X(186)", classes=["center", "incident"])
    central_line(model, X_98, X_186, 98, 186, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X(111)", classes=["center", "incident"])
    X_468 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cot(B) + cot(C) - 2*cot(A))', ID="X(468)", classes=["center", "incident"])
    central_line(model, X_111, X_468, 111, 468, incident=True)
    return promote_point_to_top(model, X_935)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(935) on the given reference triangle."""
    model = create_model('X(935) = POINT ALCOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00935(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00935.json"))
    write_center_svg(
        model_acute,
        here / "x-00935.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
