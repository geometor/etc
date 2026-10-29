"""GEOMETOR construction model for X(977) = ISOGONAL CONJUGATE OF X(976)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00977(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(977) = ISOGONAL CONJUGATE OF X(976) on reference triangle ABC."""
    X_976 = eval_trilinear_point(model, A, B, C, 'a**(3)+ (b + c)*(b**(2)+ c**(2))', ID="X(976)", classes=["center"])
    X_977 = isogonal_conjugate(model, A, B, C, X_976, ID="X(977)", classes=["selected", "target"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X(22)", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    central_line(model, X_22, X_56, 22, 56, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X(106)", classes=["center", "incident"])
    X_833 = eval_trilinear_point(model, A, B, C, '1/(a**(0)*(b**(4)- c**(4)) + a**(3)*(b**(1)- c**(1)))', ID="X(833)", classes=["center", "incident"])
    central_line(model, X_106, X_833, 106, 833, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    X_982 = eval_trilinear_point(model, A, B, C, 'b**(2)- b*c + c**(2)', ID="X(982)", classes=["center", "incident"])
    central_line(model, X_58, X_982, 58, 982, incident=True)
    return promote_point_to_top(model, X_977)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(977) on the given reference triangle."""
    model = create_model('X(977) = ISOGONAL CONJUGATE OF X(976)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00977(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00977.json"))
    write_center_svg(
        model_acute,
        here / "x-00977.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
