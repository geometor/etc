"""GEOMETOR construction model for X_2453 = REFLECTION OF X_6 IN X_1316."""

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
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02453(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2453 = REFLECTION OF X_6 IN X_1316 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1316 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(B - C))**(2) + a**(2)*sin(A - B)*sin(A - C)', ID="X_1316", classes=["center"])
    X_2453 = reflection_in_point(model, X_6, X_1316, ID="X_2453", classes=["selected", "target"], guide=False)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_183 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*cos(A-  omega  )', ID="X_183", classes=["center", "incident"])
    central_line(model, X_23, X_183, 23, 183, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_338 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)/a**(3)', ID="X_338", classes=["center", "incident"])
    central_line(model, X_98, X_338, 98, 338, incident=True)
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_6, X_523, 6, 523, incident=True)
    return promote_point_to_top(model, X_2453)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2453 on the given reference triangle."""
    model = create_model('X_2453 = REFLECTION OF X_6 IN X_1316')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02453(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02453.json"))
    write_center_svg(
        model_acute,
        here / "x-02453.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
