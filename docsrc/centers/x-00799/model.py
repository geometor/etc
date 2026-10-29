"""GEOMETOR construction model for X(799) = ISOGONAL CONJUGATE OF X(798)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00799(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(799) = ISOGONAL CONJUGATE OF X(798) on reference triangle ABC."""
    X_798 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))', ID="X(798)", classes=["center"])
    X_799 = isogonal_conjugate(model, A, B, C, X_798, ID="X(799)", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    central_line(model, X_99, X_100, 99, 100, incident=True)
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X(88)", classes=["center", "incident"])
    X_274 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c)', ID="X(274)", classes=["center", "incident"])
    central_line(model, X_88, X_274, 88, 274, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X(63)", classes=["center", "incident"])
    X_561 = eval_trilinear_point(model, A, B, C, 'a **(- 4)', ID="X(561)", classes=["center", "incident"])
    central_line(model, X_63, X_561, 63, 561, incident=True)
    return promote_point_to_top(model, X_799)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(799) on the given reference triangle."""
    model = create_model('X(799) = ISOGONAL CONJUGATE OF X(798)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00799(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00799.json"))
    write_center_svg(
        model_acute,
        here / "x-00799.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
