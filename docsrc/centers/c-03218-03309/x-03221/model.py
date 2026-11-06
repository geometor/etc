"""GEOMETOR construction model for X_3221 = SS(a → bc) OF X_647."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03221(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3221 = SS(a → bc) OF X_647 on reference triangle ABC."""
    X_3221 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(c**(2)*a**(2) + a**(2)*b**(2) - b**(2)*c**(2)))', ID="X_3221", classes=["selected", "target"])
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    central_line(model, X_30, X_511, 30, 511, incident=True)
    X_882 = point_from_barycentrics(model, A, B, C, 0.023590899, 1.0060979, -0.02968882, ID="X_882", classes=["center", "incident"])
    X_1843 = eval_trilinear_point(model, A, B, C, 'tan(A)*sin(A +  omega  )', ID="X_1843", classes=["center", "incident"])
    central_line(model, X_882, X_1843, 882, 1843, incident=True)
    X_669 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(2) - c**(2))', ID="X_669", classes=["center", "incident"])
    X_2451 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(a**(4) + 2*b**(2)*c**(2) - a**(2)*b**(2)- a**(2)*c**(2)))', ID="X_2451", classes=["center", "incident"])
    central_line(model, X_669, X_2451, 669, 2451, incident=True)
    return promote_point_to_top(model, X_3221)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3221 on the given reference triangle."""
    model = create_model('X_3221 = SS(a → bc) OF X_647')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03221(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03221.json"))
    write_center_svg(
        model_acute,
        here / "x-03221.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
