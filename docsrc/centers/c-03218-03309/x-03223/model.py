"""GEOMETOR construction model for X_3223 = ISOGONAL CONJUGATE OF X_1740."""

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


def construct_x_03223(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3223 = ISOGONAL CONJUGATE OF X_1740 on reference triangle ABC."""
    X_1740 = eval_trilinear_point(model, A, B, C, '(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_1740", classes=["center"])
    X_3223 = isogonal_conjugate(model, A, B, C, X_1740, ID="X_3223", classes=["selected", "target"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X_192", classes=["center", "incident"])
    central_line(model, X_42, X_192, 42, 192, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    central_line(model, X_43, X_213, 43, 213, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_1582 = eval_trilinear_point(model, A, B, C, 'a**(4) + b**(2)*c**(2)', ID="X_1582", classes=["center", "incident"])
    central_line(model, X_31, X_1582, 31, 1582, incident=True)
    return promote_point_to_top(model, X_3223)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3223 on the given reference triangle."""
    model = create_model('X_3223 = ISOGONAL CONJUGATE OF X_1740')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03223(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03223.json"))
    write_center_svg(
        model_acute,
        here / "x-03223.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
