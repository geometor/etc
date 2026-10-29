"""GEOMETOR construction model for X(257) = ISOGONAL CONJUGATE OF X(172)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00257(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(257) = ISOGONAL CONJUGATE OF X(172) on reference triangle ABC."""
    X_172 = eval_trilinear_point(model, A, B, C, 'a**(3) + a*b*c', ID="X(172)", classes=["center"])
    X_257 = isogonal_conjugate(model, A, B, C, X_172, ID="X(257)", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X(192)", classes=["center", "incident"])
    central_line(model, X_8, X_192, 8, 192, incident=True)
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center", "incident"])
    X_242 = point_from_barycentrics(model, A, B, C, -0.21362434, 0.01984127, 1.1937831, ID="X(242)", classes=["center", "incident"])
    central_line(model, X_29, X_242, 29, 242, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X(385)", classes=["center", "incident"])
    central_line(model, X_1, X_385, 1, 385, incident=True)
    return promote_point_to_top(model, X_257)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(257) on the given reference triangle."""
    model = create_model('X(257) = ISOGONAL CONJUGATE OF X(172)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00257(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00257.json"))
    write_center_svg(
        model_acute,
        here / "x-00257.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
