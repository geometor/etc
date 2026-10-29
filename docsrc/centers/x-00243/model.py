"""GEOMETOR construction model for X(243) = X(4)-LINE CONJUGATE OF X(73)."""

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
    incenter_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00243(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(243) = X(4)-LINE CONJUGATE OF X(73) on reference triangle ABC."""
    X_243 = eval_barycentric_point(model, A, B, C, '(a - b - c)*(a**(4) - a**(2)*(b**(2) - b*c + c**(2)) - b*c*(b - c)**(2))/(a**(2) - b**(2) - c**(2))', ID="X(243)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center", "incident"])
    central_line(model, X_55, X_92, 55, 92, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_158 = point_from_barycentrics(model, A, B, C, 0.04776757, 0.099240104, 0.85299233, ID="X(158)", classes=["center", "incident"])
    central_line(model, X_3, X_158, 3, 158, incident=True)
    return promote_point_to_top(model, X_243)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(243) on the given reference triangle."""
    model = create_model('X(243) = X(4)-LINE CONJUGATE OF X(73)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00243(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00243.json"))
    write_center_svg(
        model_acute,
        here / "x-00243.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
