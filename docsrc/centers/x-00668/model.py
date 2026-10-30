"""GEOMETOR construction model for X(668) = TRILINEAR POLE OF LINE X(2)X(37)."""

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
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00668(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(668) = TRILINEAR POLE OF LINE X(2)X(37) on reference triangle ABC."""
    X_667 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b - c)', ID="X(667)", classes=["center"])
    X_668 = isogonal_conjugate(model, A, B, C, X_667, ID="X(668)", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_8, X_76, 8, 76, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    central_line(model, X_99, X_100, 99, 100, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_150 = point_from_barycentrics(model, A, B, C, 0.10714286, 1.6428571, -0.75, ID="X(150)", classes=["center", "incident"])
    central_line(model, X_69, X_150, 69, 150, incident=True)
    return promote_point_to_top(model, X_668)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(668) on the given reference triangle."""
    model = create_model('X(668) = TRILINEAR POLE OF LINE X(2)X(37)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00668(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00668.json"))
    write_center_svg(
        model_acute,
        here / "x-00668.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
