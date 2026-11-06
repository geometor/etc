"""GEOMETOR construction model for X_3174 = X_7-CEVA CONJUGATE OF X_9."""

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
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03174(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3174 = X_7-CEVA CONJUGATE OF X_9 on reference triangle ABC."""
    X_3174 = eval_barycentric_point(model, A, B, C, '(a*( b + c - a)*(a**(3) - 3*a**(2)*b - 3*a**(2)*c + a*(3*b**(2) - 2*b*c + 3*c**(2)) - (b + c)*(b - c)**(2)))', ID="X_3174", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_9, X_55, 9, 55, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center", "incident"])
    central_line(model, X_1, X_142, 1, 142, incident=True)
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    X_390 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)*(3*a**(2) + (b - c)**(2))', ID="X_390", classes=["center", "incident"])
    central_line(model, X_78, X_390, 78, 390, incident=True)
    return promote_point_to_top(model, X_3174)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3174 on the given reference triangle."""
    model = create_model('X_3174 = X_7-CEVA CONJUGATE OF X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03174(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03174.json"))
    write_center_svg(
        model_acute,
        here / "x-03174.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
