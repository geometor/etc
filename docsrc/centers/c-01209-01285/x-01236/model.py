"""GEOMETOR construction model for X_1236 = ISOTOMIC CONJUGATE OF X_1177."""

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


def construct_x_01236(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1236 = ISOTOMIC CONJUGATE OF X_1177 on reference triangle ABC."""
    X_1177 = eval_trilinear_point(model, A, B, C, '(a/(b**(6) + c**(6) - a**(4)*b**(2) - a**(4)*c**(2) + 2*a**(2)*b**(2)*c**(2) - b**(4)*c**(2) - b**(2)*c**(4)))', ID="X_1177", classes=["center"])
    X_1236 = isotomic_conjugate(model, A, B, C, X_1177, ID="X_1236", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_4, X_69, 4, 69, incident=True)
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    X_339 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A))/a**(4)', ID="X_339", classes=["center", "incident"])
    central_line(model, X_325, X_339, 325, 339, incident=True)
    X_826 = eval_trilinear_point(model, A, B, C, 'a **(-1)*(b**(4) - c**(4)) + a**(3)*(b**(0) - c**(0))', ID="X_826", classes=["center", "incident"])
    X_850 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))/a**(3)', ID="X_850", classes=["center", "incident"])
    central_line(model, X_826, X_850, 826, 850, incident=True)
    return promote_point_to_top(model, X_1236)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1236 on the given reference triangle."""
    model = create_model('X_1236 = ISOTOMIC CONJUGATE OF X_1177')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01236(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01236.json"))
    write_center_svg(
        model_acute,
        here / "x-01236.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
