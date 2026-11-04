"""GEOMETOR construction model for X_1233 = ISOTOMIC CONJUGATE OF X_1174."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01233(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1233 = ISOTOMIC CONJUGATE OF X_1174 on reference triangle ABC."""
    X_1174 = point_from_barycentrics(model, A, B, C, 0.24963675, 0.33833122, 0.41203203, ID="X_1174", classes=["center"])
    X_1233 = isotomic_conjugate(model, A, B, C, X_1174, ID="X_1233", classes=["selected", "target"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    central_line(model, X_76, X_85, 76, 85, incident=True)
    X_310 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b + c)', ID="X_310", classes=["center", "incident"])
    X_333 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)/(b + c)', ID="X_333", classes=["center", "incident"])
    central_line(model, X_310, X_333, 310, 333, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_674 = eval_trilinear_point(model, A, B, C, '(a*(b**(3) + c**(3) - a*(b**(2) + c**(2))))', ID="X_674", classes=["center", "incident"])
    central_line(model, X_69, X_674, 69, 674, incident=True)
    return promote_point_to_top(model, X_1233)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1233 on the given reference triangle."""
    model = create_model('X_1233 = ISOTOMIC CONJUGATE OF X_1174')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01233(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01233.json"))
    write_center_svg(
        model_acute,
        here / "x-01233.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
