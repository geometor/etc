"""GEOMETOR construction model for X(775) = ISOGONAL CONJUGATE OF X(774)."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00775(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(775) = ISOGONAL CONJUGATE OF X(774) on reference triangle ABC."""
    X_774 = eval_trilinear_point(model, A, B, C, '1 - cos(A)*cos(B - C)', ID="X(774)", classes=["center"])
    X_775 = isogonal_conjugate(model, A, B, C, X_774, ID="X(775)", classes=["selected", "target"])
    X_158 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(2*A))', ID="X(158)", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '1 + cos(2*A)', ID="X(255)", classes=["center", "incident"])
    central_line(model, X_158, X_255, 158, 255, incident=True)
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X(225)", classes=["center", "incident"])
    X_412 = point_from_barycentrics(model, A, B, C, 0.035155518, 0.14825745, 0.81658703, ID="X(412)", classes=["center", "incident"])
    central_line(model, X_225, X_412, 225, 412, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_801 = eval_barycentric_point(model, A, B, C, '1/(a**(4)*(b**(2) + c**(2)) - 2*a**(2)*(b**(2) - c**(2))**(2) + (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X(801)", classes=["center", "incident"])
    central_line(model, X_10, X_801, 10, 801, incident=True)
    return promote_point_to_top(model, X_775)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(775) on the given reference triangle."""
    model = create_model('X(775) = ISOGONAL CONJUGATE OF X(774)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00775(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00775.json"))
    write_center_svg(
        model_acute,
        here / "x-00775.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
