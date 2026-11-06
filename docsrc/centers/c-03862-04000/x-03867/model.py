"""GEOMETOR construction model for X_3867 = PERSPECTOR OF ABC AND T(a², a² + c²)."""

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
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03867(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3867 = PERSPECTOR OF ABC AND T(a², a² + c²) on reference triangle ABC."""
    X_3867 = eval_barycentric_point(model, A, B, C, '((b**(2) + c**(2))*(a**(2) + b**(2) - c**(2))*(a**(2) - b**(2) + c**(2))/(3*a**(2) + b**(2) + c**(2)))', ID="X_3867", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center", "incident"])
    X_427 = eval_trilinear_point(model, A, B, C, 'sec(A) + cos(B - C)', ID="X_427", classes=["center", "incident"])
    central_line(model, X_141, X_427, 141, 427, incident=True)
    X_428 = eval_trilinear_point(model, A, B, C, '3*sec(A) - csc(A)*tan(omega) ', ID="X_428", classes=["center", "incident"])
    X_597 = eval_trilinear_point(model, A, B, C, '(4*a**(2) + b**(2) + c**(2))/a', ID="X_597", classes=["center", "incident"])
    central_line(model, X_428, X_597, 428, 597, incident=True)
    return promote_point_to_top(model, X_3867)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3867 on the given reference triangle."""
    model = create_model('X_3867 = PERSPECTOR OF ABC AND T(a², a² + c²)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03867(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03867.json"))
    write_center_svg(
        model_acute,
        here / "x-03867.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
