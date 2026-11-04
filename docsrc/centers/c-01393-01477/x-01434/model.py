"""GEOMETOR construction model for X_1434 = X_274-BETH CONJUGATE OF X_274."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01434(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1434 = X_274-BETH CONJUGATE OF X_274 on reference triangle ABC."""
    X_1334 = eval_trilinear_point(model, A, B, C, '(a*(b + c)*(b + c - a))', ID="X_1334", classes=["center"])
    X_1434 = isogonal_conjugate(model, A, B, C, X_1334, ID="X_1434", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_7, X_21, 7, 21, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    central_line(model, X_57, X_85, 57, 85, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_279 = eval_trilinear_point(model, A, B, C, 'csc(A)*(tan(A/2))**(2)', ID="X_279", classes=["center", "incident"])
    central_line(model, X_81, X_279, 81, 279, incident=True)
    return promote_point_to_top(model, X_1434)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1434 on the given reference triangle."""
    model = create_model('X_1434 = X_274-BETH CONJUGATE OF X_274')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01434(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01434.json"))
    write_center_svg(
        model_acute,
        here / "x-01434.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
