"""GEOMETOR construction model for X(261) = ISOTOMIC CONJUGATE OF X(12)."""

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


def construct_x_00261(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(261) = ISOTOMIC CONJUGATE OF X(12) on reference triangle ABC."""
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X(181)", classes=["center"])
    X_261 = isogonal_conjugate(model, A, B, C, X_181, ID="X(261)", classes=["selected", "target"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X(86)", classes=["center", "incident"])
    central_line(model, X_58, X_86, 58, 86, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_75, X_99, 75, 99, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X(28)", classes=["center", "incident"])
    X_242 = point_from_barycentrics(model, A, B, C, -0.21362434, 0.01984127, 1.1937831, ID="X(242)", classes=["center", "incident"])
    central_line(model, X_28, X_242, 28, 242, incident=True)
    return promote_point_to_top(model, X_261)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(261) on the given reference triangle."""
    model = create_model('X(261) = ISOTOMIC CONJUGATE OF X(12)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00261(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00261.json"))
    write_center_svg(
        model_acute,
        here / "x-00261.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
