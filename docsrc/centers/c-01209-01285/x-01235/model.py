"""GEOMETOR construction model for X_1235 = ISOTOMIC CONJUGATE OF X_1176."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01235(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1235 = ISOTOMIC CONJUGATE OF X_1176 on reference triangle ABC."""
    X_1176 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a**(2))/(b**(2) + c**(2))', ID="X_1176", classes=["center"])
    X_1235 = isotomic_conjugate(model, A, B, C, X_1176, ID="X_1235", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_4, X_69, 4, 69, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_183 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*cos(A-  omega  )', ID="X_183", classes=["center", "incident"])
    central_line(model, X_24, X_183, 24, 183, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_276 = eval_trilinear_point(model, A, B, C, '(csc(A))**(3)*sec(A)*sec(B - C)', ID="X_276", classes=["center", "incident"])
    central_line(model, X_54, X_276, 54, 276, incident=True)
    return promote_point_to_top(model, X_1235)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1235 on the given reference triangle."""
    model = create_model('X_1235 = ISOTOMIC CONJUGATE OF X_1176')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01235(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01235.json"))
    write_center_svg(
        model_acute,
        here / "x-01235.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
