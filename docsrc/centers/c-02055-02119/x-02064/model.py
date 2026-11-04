"""GEOMETOR construction model for X_2064 = ORION TRANSFORM OF X_75."""

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


def construct_x_02064(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2064 = ORION TRANSFORM OF X_75 on reference triangle ABC."""
    X_2064 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2)*(a**(4) - b**(4) - c**(4) + a**(2)*b*c - b**(3)*c - b*c**(3)))', ID="X_2064", classes=["selected", "target"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    central_line(model, X_76, X_85, 76, 85, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_314 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2)*(b + c - a)/(b + c))', ID="X_314", classes=["center", "incident"])
    central_line(model, X_81, X_314, 81, 314, incident=True)
    X_278 = eval_trilinear_point(model, A, B, C, 'sec(A)*tan(A/2)', ID="X_278", classes=["center", "incident"])
    X_345 = eval_trilinear_point(model, A, B, C, '(csc(A))/(1 - sec(A))', ID="X_345", classes=["center", "incident"])
    central_line(model, X_278, X_345, 278, 345, incident=True)
    return promote_point_to_top(model, X_2064)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2064 on the given reference triangle."""
    model = create_model('X_2064 = ORION TRANSFORM OF X_75')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02064(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02064.json"))
    write_center_svg(
        model_acute,
        here / "x-02064.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
