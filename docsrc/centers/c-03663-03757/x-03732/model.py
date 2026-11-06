"""GEOMETOR construction model for X_3732 = X_3022com(EXCENTRAL TRIANGLE)."""

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


def construct_x_03732(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3732 = X_3022com(EXCENTRAL TRIANGLE) on reference triangle ABC."""
    X_3732 = eval_barycentric_point(model, A, B, C, '((a**(2) + b**(2) + c**(2) - 2*b*c)/(b - c))', ID="X_3732", classes=["selected", "target"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    X_169 = eval_trilinear_point(model, A, B, C, '- (sin(A))*(cos(A/2))**(2) + (sin(B))*(cos(B/2))**(2) + (sin(C))*(cos(C/2))**(2)', ID="X_169", classes=["center", "incident"])
    central_line(model, X_85, X_169, 85, 169, incident=True)
    X_144 = eval_trilinear_point(model, A, B, C, '(csc(A))*(tan(B/2) + tan(C/2) - tan(A/2))', ID="X_144", classes=["center", "incident"])
    X_153 = eval_barycentric_point(model, A, B, C, 'a**(7) - a**(6)*(b + c) - a**(5)*(b**(2) - 7*b*c + c**(2)) + a**(4)*(b + c)*(b**(2) - 6*b*c + c**(2)) - a**(3)*(b**(4) + 2*b**(3)*c - 10*b**(2)*c**(2) + 2*b*c**(3) + c**(4)) + a**(2)*(b - c)**(2)*(b + c)*(b**(2) + 6*b*c + c**(2)) + a*(b**(2) - c**(2))**(2)*(b**(2) - 5*b*c + c**(2)) - (b - c)**(4)*(b + c)**(3)', ID="X_153", classes=["center", "incident"])
    central_line(model, X_144, X_153, 144, 153, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_101, X_514, 101, 514, incident=True)
    return promote_point_to_top(model, X_3732)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3732 on the given reference triangle."""
    model = create_model('X_3732 = X_3022com(EXCENTRAL TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03732(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03732.json"))
    write_center_svg(
        model_acute,
        here / "x-03732.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
