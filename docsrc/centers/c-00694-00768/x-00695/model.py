"""GEOMETOR construction model for X_695 = ISOGONAL CONJUGATE OF X_384."""

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


def construct_x_00695(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_695 = ISOGONAL CONJUGATE OF X_384 on reference triangle ABC."""
    X_384 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) + b**(2)*c**(2))', ID="X_384", classes=["center"])
    X_695 = isogonal_conjugate(model, A, B, C, X_384, ID="X_695", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center", "incident"])
    central_line(model, X_69, X_194, 69, 194, incident=True)
    X_248 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*sec(A +  omega  )', ID="X_248", classes=["center", "incident"])
    X_682 = eval_trilinear_point(model, A, B, C, '(sec(B)*(csc(C))**(3) + sec(C)*(csc(B))**(3))', ID="X_682", classes=["center", "incident"])
    central_line(model, X_248, X_682, 248, 682, incident=True)
    X_694 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) - b**(2)*c**(2))', ID="X_694", classes=["center", "incident"])
    central_line(model, X_384, X_694, 384, 694, incident=True)
    return promote_point_to_top(model, X_695)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_695 on the given reference triangle."""
    model = create_model('X_695 = ISOGONAL CONJUGATE OF X_384')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00695(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00695.json"))
    write_center_svg(
        model_acute,
        here / "x-00695.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
