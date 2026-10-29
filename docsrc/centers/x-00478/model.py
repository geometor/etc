"""GEOMETOR construction model for X(478) = CENTER OF YIU CONIC."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00478(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(478) = CENTER OF YIU CONIC on reference triangle ABC."""
    X_478 = eval_trilinear_point(model, A, B, C, 'a*(a**(4) - 2*a*b*c*(b + c - a) - (b**(2) - c**(2))**(2))/(b + c - a)', ID="X(478)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    central_line(model, X_6, X_19, 6, 19, incident=True)
    X_222 = eval_trilinear_point(model, A, B, C, 'cos(A)*tan(A/2)', ID="X(222)", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X(226)", classes=["center", "incident"])
    central_line(model, X_222, X_226, 222, 226, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X(109)", classes=["center", "incident"])
    X_573 = eval_trilinear_point(model, A, B, C, '(c - a)*cos(B)*sin(A - B) - (a - b)*cos(C)*sin(C - A)', ID="X(573)", classes=["center", "incident"])
    central_line(model, X_109, X_573, 109, 573, incident=True)
    return promote_point_to_top(model, X_478)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(478) on the given reference triangle."""
    model = create_model('X(478) = CENTER OF YIU CONIC')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00478(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00478.json"))
    write_center_svg(
        model_acute,
        here / "x-00478.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
