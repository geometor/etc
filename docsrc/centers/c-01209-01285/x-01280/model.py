"""GEOMETOR construction model for X_1280 = ISOGONAL CONJUGATE OF X_1279."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    nagel_point_of,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01280(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1280 = ISOGONAL CONJUGATE OF X_1279 on reference triangle ABC."""
    X_644 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(b - c))', ID="X_644", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1280 = reflection_in_point(model, X_644, X_1, ID="X_1280", classes=["selected", "target"], guide=False)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_57, X_100, 57, 100, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_277 = eval_trilinear_point(model, A, B, C, '(((sec(A/2))**(2))/(- (cos(A/2))**(4) + (cos(B/2))**(4) + (cos(C/2))**(4)))', ID="X_277", classes=["center", "incident"])
    central_line(model, X_8, X_277, 8, 277, incident=True)
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    X_279 = eval_trilinear_point(model, A, B, C, 'csc(A)*(tan(A/2))**(2)', ID="X_279", classes=["center", "incident"])
    central_line(model, X_145, X_279, 145, 279, incident=True)
    return promote_point_to_top(model, X_1280)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1280 on the given reference triangle."""
    model = create_model('X_1280 = ISOGONAL CONJUGATE OF X_1279')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01280(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01280.json"))
    write_center_svg(
        model_acute,
        here / "x-01280.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
