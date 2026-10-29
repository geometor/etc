"""GEOMETOR construction model for X(531) = DIRECTION OF VECTOR AX + BX + CX, where X = X(14)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00531(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(531) = DIRECTION OF VECTOR AX + BX + CX, where X = X(14) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X(14)", classes=["center"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center"])
    X_298 = eval_barycentric_point(model, A, B, C, 'csc(A)*sin(A + pi /3)', ID="X(298)", classes=["center"])
    central_line(model, X_2, X_14, 2, 14)
    central_line(model, X_99, X_298, 99, 298)
    X_531 = intersect_lines(model, X_2, X_14, X_99, X_298, ID="X(531)", classes=["selected", "target"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center", "incident"])
    X_396 = eval_trilinear_point(model, A, B, C, 'cos(B - C) + 2*cos(A - pi /3)', ID="X(396)", classes=["center", "incident"])
    central_line(model, X_115, X_396, 115, 396, incident=True)
    return promote_point_to_top(model, X_531)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(531) on the given reference triangle."""
    model = create_model('X(531) = DIRECTION OF VECTOR AX + BX + CX, where X = X(14)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00531(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00531.json"))
    write_center_svg(
        model_acute,
        here / "x-00531.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
