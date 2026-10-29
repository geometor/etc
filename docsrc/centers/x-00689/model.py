"""GEOMETOR construction model for X(689) = TRILINEAR POLE OF LINE X(6)X(76)."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00689(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(689) = TRILINEAR POLE OF LINE X(6)X(76) on reference triangle ABC."""
    X_688 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(4)- c**(4))', ID="X(688)", classes=["center"])
    X_689 = isogonal_conjugate(model, A, B, C, X_688, ID="X(689)", classes=["selected", "target"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X(111)", classes=["center", "incident"])
    X_308 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b**(2) + c**(2))', ID="X(308)", classes=["center", "incident"])
    central_line(model, X_111, X_308, 111, 308, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_670 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(2) - c**(2)))', ID="X(670)", classes=["center", "incident"])
    central_line(model, X_110, X_670, 110, 670, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_703 = eval_trilinear_point(model, A, B, C, '1/(a**(-5)*(b**(0)+ c**(0)) - a**(-1)*(b**(-4)+ c**(-4)))', ID="X(703)", classes=["center", "incident"])
    central_line(model, X_6, X_703, 6, 703, incident=True)
    return promote_point_to_top(model, X_689)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(689) on the given reference triangle."""
    model = create_model('X(689) = TRILINEAR POLE OF LINE X(6)X(76)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00689(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00689.json"))
    write_center_svg(
        model_acute,
        here / "x-00689.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
