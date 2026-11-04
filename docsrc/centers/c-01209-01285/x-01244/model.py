"""GEOMETOR construction model for X_1244 = ISOGONAL CONJUGATE OF X_1009."""

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


def construct_x_01244(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1244 = ISOGONAL CONJUGATE OF X_1009 on reference triangle ABC."""
    X_1009 = eval_trilinear_point(model, A, B, C, '(a**(4)*(b + c) + 2*a**(3)*b*c - a**(2)*(b**(3) + c**(3)) + b*c*(b + c)*(b**(2) + c**(2)))', ID="X_1009", classes=["center"])
    X_1244 = isogonal_conjugate(model, A, B, C, X_1009, ID="X_1244", classes=["selected", "target"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_71, X_238, 71, 238, incident=True)
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    central_line(model, X_72, X_239, 72, 239, incident=True)
    return promote_point_to_top(model, X_1244)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1244 on the given reference triangle."""
    model = create_model('X_1244 = ISOGONAL CONJUGATE OF X_1009')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01244(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01244.json"))
    write_center_svg(
        model_acute,
        here / "x-01244.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
