"""GEOMETOR construction model for X_1576 = ISOGONAL CONJUGATE OF X_850."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01576(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1576 = ISOGONAL CONJUGATE OF X_850 on reference triangle ABC."""
    X_1576 = eval_trilinear_point(model, A, B, C, 'a**(3)/(b**(2) - c**(2))', ID="X_1576", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_157 = eval_trilinear_point(model, A, B, C, '(a*(b**(3)*cos(B) + c**(3)*cos(C) - a**(3)*cos(A)))', ID="X_157", classes=["center", "incident"])
    central_line(model, X_6, X_157, 6, 157, incident=True)
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X_50", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X_237", classes=["center", "incident"])
    central_line(model, X_50, X_237, 50, 237, incident=True)
    X_160 = eval_trilinear_point(model, A, B, C, '(a*((b**(2) + c**(2))*sin(2*A) + (c**(2) - a**(2))*sin(2*B) + (b**(2) - a**(2))*sin(2*C)))', ID="X_160", classes=["center", "incident"])
    X_206 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(4) + c**(4) - a**(4))', ID="X_206", classes=["center", "incident"])
    central_line(model, X_160, X_206, 160, 206, incident=True)
    return promote_point_to_top(model, X_1576)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1576 on the given reference triangle."""
    model = create_model('X_1576 = ISOGONAL CONJUGATE OF X_850')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01576(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01576.json"))
    write_center_svg(
        model_acute,
        here / "x-01576.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
