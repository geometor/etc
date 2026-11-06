"""GEOMETOR construction model for X_3437 = X_10-VERTEX CONJUGATE OF X_10."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03437(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3437 = X_10-VERTEX CONJUGATE OF X_10 on reference triangle ABC."""
    X_1330 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2)/(a + c) + c**(2)/(a + b) - a**(2)/(b + c)))', ID="X_1330", classes=["center"])
    X_3437 = isogonal_conjugate(model, A, B, C, X_1330, ID="X_3437", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_199 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) - a**(4) + (b**(2) + c**(2) - a**(2))*(b*c + c*a + a*b)))', ID="X_199", classes=["center", "incident"])
    central_line(model, X_10, X_199, 10, 199, incident=True)
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_228 = eval_trilinear_point(model, A, B, C, '(sin(2*A))*(sin(B) + sin(C))', ID="X_228", classes=["center", "incident"])
    central_line(model, X_35, X_228, 35, 228, incident=True)
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    X_386 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_386", classes=["center", "incident"])
    central_line(model, X_184, X_386, 184, 386, incident=True)
    return promote_point_to_top(model, X_3437)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3437 on the given reference triangle."""
    model = create_model('X_3437 = X_10-VERTEX CONJUGATE OF X_10')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03437(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03437.json"))
    write_center_svg(
        model_acute,
        here / "x-03437.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
