"""GEOMETOR construction model for X_2651 = CROSSDIFFERENCE OF PU(81)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02651(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2651 = CROSSDIFFERENCE OF PU(81) on reference triangle ABC."""
    X_2651 = eval_trilinear_point(model, A, B, C, '(1/((cos(A) + cos(B))*(cos(A) + cos(C))) - 1/(cos(B) + cos(C))**(2))', ID="X_2651", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_1, X_21, 1, 21, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_409 = eval_barycentric_point(model, A, B, C, 'a*(a + b) * (a + c) * (a**(4) - a**(3)*b + a*b**(3) - b**(4) - a**(3)*c + a**(2)*b*c + a*b**(2)*c + b**(3)*c + a*b*c**(2) + 4*b**(2)*c**(2) + a*c**(3) + b*c**(3) - c**(4))', ID="X_409", classes=["center", "incident"])
    central_line(model, X_65, X_409, 65, 409, incident=True)
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center", "incident"])
    X_411 = eval_trilinear_point(model, A, B, C, '(cos(B)*cos(C) - (cos(A) + cos(B) + cos(C))*cos(A))', ID="X_411", classes=["center", "incident"])
    central_line(model, X_185, X_411, 185, 411, incident=True)
    return promote_point_to_top(model, X_2651)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2651 on the given reference triangle."""
    model = create_model('X_2651 = CROSSDIFFERENCE OF PU(81)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02651(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02651.json"))
    write_center_svg(
        model_acute,
        here / "x-02651.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
