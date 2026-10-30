"""GEOMETOR construction model for X(440) = COMPLEMENT OF X(27)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00440(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(440) = COMPLEMENT OF X(27) on reference triangle ABC."""
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X(27)", classes=["center"])
    X_440 = complement(model, A, B, C, X_27, ID="X(440)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X(118)", classes=["center", "incident"])
    X_122 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(a**(2) - b**(2) - c**(2))**(2)*(3*a**(4) - 2*a**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2))', ID="X(122)", classes=["center", "incident"])
    central_line(model, X_118, X_122, 118, 122, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X(226)", classes=["center", "incident"])
    central_line(model, X_37, X_226, 37, 226, incident=True)
    return promote_point_to_top(model, X_440)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(440) on the given reference triangle."""
    model = create_model('X(440) = COMPLEMENT OF X(27)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00440(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00440.json"))
    write_center_svg(
        model_acute,
        here / "x-00440.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
