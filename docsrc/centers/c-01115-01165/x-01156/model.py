"""GEOMETOR construction model for X_1156 = ISOGONAL CONJUGATE OF X_1155."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    gergonne_point_of,
    midpoint,
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01156(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1156 = ISOGONAL CONJUGATE OF X_1155 on reference triangle ABC."""
    X_144 = eval_trilinear_point(model, A, B, C, '(csc(A))*(tan(B/2) + tan(C/2) - tan(A/2))', ID="X_144", classes=["center"])
    X_149 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(3) + c**(3) - a**(3) + (a**(2) - b*c)*(b + c) + a*(b*c - b**(2) - c**(2))))', ID="X_149", classes=["center"])
    X_1156 = midpoint(model, X_144, X_149, ID="X_1156", classes=["selected", "target"], guide=False)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_7, X_11, 7, 11, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_9, X_100, 9, 100, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_8, X_190, 8, 190, incident=True)
    return promote_point_to_top(model, X_1156)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1156 on the given reference triangle."""
    model = create_model('X_1156 = ISOGONAL CONJUGATE OF X_1155')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01156(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01156.json"))
    write_center_svg(
        model_acute,
        here / "x-01156.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
