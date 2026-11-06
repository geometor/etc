"""GEOMETOR construction model for X_3405 = COT(A + ω) POINT."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03405(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3405 = COT(A + ω) POINT on reference triangle ABC."""
    X_3404 = eval_trilinear_point(model, A, B, C, '(tan(A +  omega  ))', ID="X_3404", classes=["center"])
    X_3405 = isogonal_conjugate(model, A, B, C, X_3404, ID="X_3405", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center", "incident"])
    central_line(model, X_1, X_82, 1, 82, incident=True)
    X_798 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))', ID="X_798", classes=["center", "incident"])
    X_812 = eval_trilinear_point(model, A, B, C, 'a **(-2)*(b**(1) - c**(1)) + a**(0)*(b **(-1) - c **(-1))', ID="X_812", classes=["center", "incident"])
    central_line(model, X_798, X_812, 798, 812, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_1969 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2)*sin(2*B)*sin(2*C))', ID="X_1969", classes=["center", "incident"])
    central_line(model, X_19, X_1969, 19, 1969, incident=True)
    return promote_point_to_top(model, X_3405)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3405 on the given reference triangle."""
    model = create_model('X_3405 = COT(A + ω) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03405(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03405.json"))
    write_center_svg(
        model_acute,
        here / "x-03405.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
