"""GEOMETOR construction model for X_2858 = SM(X_98, X_111)."""

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


def construct_x_02858(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2858 = SM(X_98, X_111) on reference triangle ABC."""
    X_2858 = eval_trilinear_point(model, A, B, C, '(b*c/((b**(2) - c**(2))*(a**(4) + b**(4) + c**(4) - 3*b**(2)*c**(2))))', ID="X_2858", classes=["selected", "target"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    central_line(model, X_111, X_325, 111, 325, incident=True)
    X_323 = eval_trilinear_point(model, A, B, C, 'sin(3*A)*(csc(A))**(2)', ID="X_323", classes=["center", "incident"])
    X_729 = eval_trilinear_point(model, A, B, C, '1/(a**(-3)*(b**(0) + c**(0)) - a **(-1)*(b**(-2) + c **(-2)))', ID="X_729", classes=["center", "incident"])
    central_line(model, X_323, X_729, 323, 729, incident=True)
    X_691 = eval_trilinear_point(model, A, B, C, 'a/((b**(2) - c**(2))*(2*a**(2) - b**(2) - c**(2)))', ID="X_691", classes=["center", "incident"])
    X_2396 = eval_barycentric_point(model, A, B, C, '(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))/(b**(2) - c**(2))', ID="X_2396", classes=["center", "incident"])
    central_line(model, X_691, X_2396, 691, 2396, incident=True)
    return promote_point_to_top(model, X_2858)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2858 on the given reference triangle."""
    model = create_model('X_2858 = SM(X_98, X_111)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02858(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02858.json"))
    write_center_svg(
        model_acute,
        here / "x-02858.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
