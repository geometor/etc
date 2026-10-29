"""GEOMETOR construction model for X(295) = ISOGONAL CONJUGATE OF X(242)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00295(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(295) = ISOGONAL CONJUGATE OF X(242) on reference triangle ABC."""
    X_242 = point_from_barycentrics(model, A, B, C, -0.21362434, 0.01984127, 1.1937831, ID="X(242)", classes=["center"])
    X_295 = isogonal_conjugate(model, A, B, C, X_242, ID="X(295)", classes=["selected", "target"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X(43)", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    central_line(model, X_43, X_57, 43, 57, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X(101)", classes=["center", "incident"])
    central_line(model, X_58, X_101, 58, 101, incident=True)
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X(27)", classes=["center", "incident"])
    X_335 = eval_trilinear_point(model, A, B, C, 'b*c/(a**(2) - b*c)', ID="X(335)", classes=["center", "incident"])
    central_line(model, X_27, X_335, 27, 335, incident=True)
    return promote_point_to_top(model, X_295)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(295) on the given reference triangle."""
    model = create_model('X(295) = ISOGONAL CONJUGATE OF X(242)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00295(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00295.json"))
    write_center_svg(
        model_acute,
        here / "x-00295.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
