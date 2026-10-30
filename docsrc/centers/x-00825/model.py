"""GEOMETOR construction model for X(825) = o-(0, 3) CIRCUMCIRCLE POINT."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00825(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(825) = o-(0, 3) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_824 = point_from_barycentrics(model, A, B, C, 0.47351813, -0.81281066, 0.33929252, ID="X(824)", classes=["center"])
    X_825 = isogonal_conjugate(model, A, B, C, X_824, ID="X(825)", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X(163)", classes=["center", "incident"])
    central_line(model, X_99, X_163, 99, 163, incident=True)
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X(103)", classes=["center", "incident"])
    X_572 = eval_trilinear_point(model, A, B, C, 's*cos(A) + r*sin(A)', ID="X(572)", classes=["center", "incident"])
    central_line(model, X_103, X_572, 103, 572, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_753 = point_from_barycentrics(model, A, B, C, 0.086173306, 1.0651021, -0.15127536, ID="X(753)", classes=["center", "incident"])
    central_line(model, X_6, X_753, 6, 753, incident=True)
    return promote_point_to_top(model, X_825)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(825) on the given reference triangle."""
    model = create_model('X(825) = o-(0, 3) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00825(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00825.json"))
    write_center_svg(
        model_acute,
        here / "x-00825.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
