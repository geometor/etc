"""GEOMETOR construction model for X_1947 = CROSSSUM OF PU(19)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_01947(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1947 = CROSSSUM OF PU(19) on reference triangle ABC."""
    X_1947 = eval_trilinear_point(model, A, B, C, '(((cos(A))**(2) + cos(B)*cos(C))*csc(2*A))', ID="X_1947", classes=["selected", "target"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center", "incident"])
    central_line(model, X_57, X_264, 57, 264, incident=True)
    X_278 = eval_trilinear_point(model, A, B, C, 'sec(A)*tan(A/2)', ID="X_278", classes=["center", "incident"])
    X_330 = eval_trilinear_point(model, A, B, C, 'b*c/(a*b + a*c - b*c)', ID="X_330", classes=["center", "incident"])
    central_line(model, X_278, X_330, 278, 330, incident=True)
    X_318 = eval_trilinear_point(model, A, B, C, '(1 + sec(A))/a**(2)', ID="X_318", classes=["center", "incident"])
    X_377 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) - 2*b**(2)*c**(2) - 2*a*b*c*(a + b + c)))', ID="X_377", classes=["center", "incident"])
    central_line(model, X_318, X_377, 318, 377, incident=True)
    return promote_point_to_top(model, X_1947)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1947 on the given reference triangle."""
    model = create_model('X_1947 = CROSSSUM OF PU(19)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01947(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01947.json"))
    write_center_svg(
        model_acute,
        here / "x-01947.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
