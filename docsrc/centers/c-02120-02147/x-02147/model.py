"""GEOMETOR construction model for X_2147 = X_2-ISOCONJUGATE OF X_2146."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02147(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2147 = X_2-ISOCONJUGATE OF X_2146 on reference triangle ABC."""
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center"])
    X_2146 = point_from_barycentrics(model, A, B, C, 0.87201907, -1.0289414, 1.1569223, ID="X_2146", classes=["center"])
    X_365 = eval_trilinear_point(model, A, B, C, 'a**(1/2)', ID="X_365", classes=["center"])
    X_2144 = point_from_barycentrics(model, A, B, C, 0.042427957, 1.0319255, -0.074353432, ID="X_2144", classes=["center"])
    central_line(model, X_238, X_2146, 238, 2146)
    central_line(model, X_365, X_2144, 365, 2144)
    X_2147 = intersect_lines(model, X_238, X_2146, X_365, X_2144, ID="X_2147", classes=["selected", "target"])
    X_2108 = eval_trilinear_point(model, A, B, C, '((b + c)*a**(3) - (b**(2) - b*c + c**(2))*a**(2) - (b + c)*(b**(2) + c**(2))*a + b*c*(b**(2) + b*c + c**(2)))', ID="X_2108", classes=["center", "incident"])
    X_2118 = eval_trilinear_point(model, A, B, C, '(a*(a + b + c)*(b*c)**(1/2) + (b*c + c*a + a*b)*(a - (a*b)**(1/2) - (a*c)**(1/2)))', ID="X_2118", classes=["center", "incident"])
    central_line(model, X_2108, X_2118, 2108, 2118, incident=True)
    return promote_point_to_top(model, X_2147)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2147 on the given reference triangle."""
    model = create_model('X_2147 = X_2-ISOCONJUGATE OF X_2146')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02147(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02147.json"))
    write_center_svg(
        model_acute,
        here / "x-02147.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
