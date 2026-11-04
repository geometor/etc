"""GEOMETOR construction model for X_2930 = TANGENTIAL-ISOGONAL CONJUGATE OF X_23."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02930(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2930 = TANGENTIAL-ISOGONAL CONJUGATE OF X_23 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center"])
    X_2930 = reflection_in_point(model, X_6, X_110, ID="X_2930", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_67", classes=["center", "incident"])
    central_line(model, X_3, X_67, 3, 67, incident=True)
    central_line(model, X_6, X_110, 6, 110, incident=True)
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_23", classes=["center", "incident"])
    X_524 = eval_trilinear_point(model, A, B, C, '(2*a**(2) - b**(2) - c**(2))/a', ID="X_524", classes=["center", "incident"])
    central_line(model, X_23, X_524, 23, 524, incident=True)
    return promote_point_to_top(model, X_2930)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2930 on the given reference triangle."""
    model = create_model('X_2930 = TANGENTIAL-ISOGONAL CONJUGATE OF X_23')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02930(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02930.json"))
    write_center_svg(
        model_acute,
        here / "x-02930.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
