"""GEOMETOR construction model for X(50) = X(74)-CEVA CONJUGATE OF X(184)."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00050(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(50) = X(74)-CEVA CONJUGATE OF X(184) on reference triangle ABC."""
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X(50)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(67)", classes=["center", "incident"])
    X_248 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*sec(A + omega )', ID="X(248)", classes=["center", "incident"])
    central_line(model, X_67, X_248, 67, 248, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center", "incident"])
    X_231 = eval_barycentric_point(model, A, B, C, '2*a**(8) - 4*a**(6)*b**(2) + 3*a**(4)*b**(4) - 2*a**(2)*b**(6) + b**(8) - 4*a**(6)*c**(2) + 2*a**(2)*b**(4)*c**(2) - 4*b**(6)*c**(2) + 3*a**(4)*c**(4) + 2*a**(2)*b**(2)*c**(4) + 6*b**(4)*c**(4) - 2*a**(2)*c**(6) - 4*b**(2)*c**(6) + c**(8)', ID="X(231)", classes=["center", "incident"])
    central_line(model, X_115, X_231, 115, 231, incident=True)
    return promote_point_to_top(model, X_50)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(50) on the given reference triangle."""
    model = create_model('X(50) = X(74)-CEVA CONJUGATE OF X(184)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00050(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00050.json"))
    write_center_svg(
        model_acute,
        here / "x-00050.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
