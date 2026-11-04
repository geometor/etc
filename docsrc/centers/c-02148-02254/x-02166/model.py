"""GEOMETOR construction model for X_2166 = X_2-ISOCONJUGATE OF X_50."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02166(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2166 = X_2-ISOCONJUGATE OF X_50 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1749 = eval_trilinear_point(model, A, B, C, 'a**(6) - 3*a**(4)*(b**(2) + c**(2)) + a**(2)*(3*b**(4) - b**(2)*c**(2) + 3*c**(4)) - (b**(2) - c**(2))**(2)*(b**(2) + c**(2))', ID="X_1749", classes=["center"])
    X_2166 = cevapoint(model, A, B, C, X_1, X_1749, ID="X_2166", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X_94", classes=["center", "incident"])
    central_line(model, X_10, X_94, 10, 94, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_79 = eval_trilinear_point(model, A, B, C, '1/(1 + 2*cos(A))', ID="X_79", classes=["center", "incident"])
    central_line(model, X_65, X_79, 65, 79, incident=True)
    X_564 = eval_trilinear_point(model, A, B, C, 'cos(2*B - 2*C)', ID="X_564", classes=["center", "incident"])
    central_line(model, X_1, X_564, 1, 564, incident=True)
    return promote_point_to_top(model, X_2166)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2166 on the given reference triangle."""
    model = create_model('X_2166 = X_2-ISOCONJUGATE OF X_50')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02166(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02166.json"))
    write_center_svg(
        model_acute,
        here / "x-02166.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
