"""GEOMETOR construction model for X_2118 = POINT KEPLER VII."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02118(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2118 = POINT KEPLER VII on reference triangle ABC."""
    X_2118 = eval_trilinear_point(model, A, B, C, '(a*(a + b + c)*(b*c)**(1/2) + (b*c + c*a + a*b)*(a - (a*b)**(1/2) - (a*c)**(1/2)))', ID="X_2118", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_365 = eval_trilinear_point(model, A, B, C, 'a**(1/2)', ID="X_365", classes=["center", "incident"])
    central_line(model, X_6, X_365, 6, 365, incident=True)
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    X_2119 = eval_trilinear_point(model, A, B, C, '(a**(1/2)/((a + b + c)*(a*b*c)**(1/2) + (b*c + c*a + a*b)*(a**(1/2) - b**(1/2) - c**(1/2))))', ID="X_2119", classes=["center", "incident"])
    central_line(model, X_238, X_2119, 238, 2119, incident=True)
    X_2108 = eval_trilinear_point(model, A, B, C, '((b + c)*a**(3) - (b**(2) - b*c + c**(2))*a**(2) - (b + c)*(b**(2) + c**(2))*a + b*c*(b**(2) + b*c + c**(2)))', ID="X_2108", classes=["center", "incident"])
    X_2147 = point_from_barycentrics(model, A, B, C, 0.6235198, -0.91312312, 1.2896033, ID="X_2147", classes=["center", "incident"])
    central_line(model, X_2108, X_2147, 2108, 2147, incident=True)
    return promote_point_to_top(model, X_2118)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2118 on the given reference triangle."""
    model = create_model('X_2118 = POINT KEPLER VII')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02118(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02118.json"))
    write_center_svg(
        model_acute,
        here / "x-02118.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
