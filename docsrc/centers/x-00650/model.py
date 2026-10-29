"""GEOMETOR construction model for X(650) = CROSSDIFFERENCE OF X(1) AND X(3)."""

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


def construct_x_00650(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(650) = CROSSDIFFERENCE OF X(1) AND X(3) on reference triangle ABC."""
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X(650)", classes=["selected", "target"])
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X(230)", classes=["center", "incident"])
    X_231 = eval_barycentric_point(model, A, B, C, '2*a**(8) - 4*a**(6)*b**(2) + 3*a**(4)*b**(4) - 2*a**(2)*b**(6) + b**(8) - 4*a**(6)*c**(2) + 2*a**(2)*b**(4)*c**(2) - 4*b**(6)*c**(2) + 3*a**(4)*c**(4) + 2*a**(2)*b**(2)*c**(4) + 6*b**(4)*c**(4) - 2*a**(2)*c**(6) - 4*b**(2)*c**(6) + c**(8)', ID="X(231)", classes=["center", "incident"])
    central_line(model, X_230, X_231, 230, 231, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_241 = eval_trilinear_point(model, A, B, C, '(b**(2) + c**(2) - a*b - a*c)/(a - b - c)', ID="X(241)", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X(514)", classes=["center", "incident"])
    central_line(model, X_241, X_514, 241, 514, incident=True)
    return promote_point_to_top(model, X_650)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(650) on the given reference triangle."""
    model = create_model('X(650) = CROSSDIFFERENCE OF X(1) AND X(3)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00650(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00650.json"))
    write_center_svg(
        model_acute,
        here / "x-00650.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
