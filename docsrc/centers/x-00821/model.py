"""GEOMETOR construction model for X(821) = ISOGONAL CONJUGATE OF X(820)."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00821(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(821) = ISOGONAL CONJUGATE OF X(820) on reference triangle ABC."""
    X_820 = point_from_barycentrics(model, A, B, C, 0.4160805, 0.47409113, 0.10982837, ID="X(820)", classes=["center"])
    X_821 = isogonal_conjugate(model, A, B, C, X_820, ID="X(821)", classes=["selected", "target"])
    X_158 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(2*A))', ID="X(158)", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '1 + cos(2*A)', ID="X(255)", classes=["center", "incident"])
    central_line(model, X_158, X_255, 158, 255, incident=True)
    X_243 = eval_barycentric_point(model, A, B, C, '(a - b - c)*(a**(4) - a**(2)*(b**(2) - b*c + c**(2)) - b*c*(b - c)**(2))/(a**(2) - b**(2) - c**(2))', ID="X(243)", classes=["center", "incident"])
    X_411 = eval_barycentric_point(model, A, B, C, 'a*(a**(6) - a**(5)*b - 2*a**(4)*b**(2) + 2*a**(3)*b**(3) + a**(2)*b**(4) - a*b**(5) - a**(5)*c - a**(4)*b*c + a*b**(4)*c + b**(5)*c - 2*a**(4)*c**(2) + 2*a**(2)*b**(2)*c**(2) + 2*a**(3)*c**(3) - 2*b**(3)*c**(3) + a**(2)*c**(4) + a*b*c**(4) - a*c**(5) + b*c**(5))', ID="X(411)", classes=["center", "incident"])
    central_line(model, X_243, X_411, 243, 411, incident=True)
    X_774 = eval_trilinear_point(model, A, B, C, '1 - cos(A)*cos(B - C)', ID="X(774)", classes=["center", "incident"])
    X_823 = eval_trilinear_point(model, A, B, C, '1/(csc(B/2) - csc(C/2))', ID="X(823)", classes=["center", "incident"])
    central_line(model, X_774, X_823, 774, 823, incident=True)
    return promote_point_to_top(model, X_821)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(821) on the given reference triangle."""
    model = create_model('X(821) = ISOGONAL CONJUGATE OF X(820)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00821(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00821.json"))
    write_center_svg(
        model_acute,
        here / "x-00821.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
