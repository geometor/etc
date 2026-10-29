"""GEOMETOR construction model for X(96) = ISOGONAL CONJUGATE OF X(52)."""

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
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00096(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(96) = ISOGONAL CONJUGATE OF X(52) on reference triangle ABC."""
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X(52)", classes=["center"])
    X_96 = isogonal_conjugate(model, A, B, C, X_52, ID="X(96)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X(54)", classes=["center", "incident"])
    central_line(model, X_2, X_54, 2, 54, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X(95)", classes=["center", "incident"])
    central_line(model, X_76, X_95, 76, 95, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_231 = eval_barycentric_point(model, A, B, C, '2*a**(8) - 4*a**(6)*b**(2) + 3*a**(4)*b**(4) - 2*a**(2)*b**(6) + b**(8) - 4*a**(6)*c**(2) + 2*a**(2)*b**(4)*c**(2) - 4*b**(6)*c**(2) + 3*a**(4)*c**(4) + 2*a**(2)*b**(2)*c**(4) + 6*b**(4)*c**(4) - 2*a**(2)*c**(6) - 4*b**(2)*c**(6) + c**(8)', ID="X(231)", classes=["center", "incident"])
    central_line(model, X_4, X_231, 4, 231, incident=True)
    return promote_point_to_top(model, X_96)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(96) on the given reference triangle."""
    model = create_model('X(96) = ISOGONAL CONJUGATE OF X(52)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00096(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00096.json"))
    write_center_svg(
        model_acute,
        here / "x-00096.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
