"""GEOMETOR construction model for X_3613 = ISOTOMIC CONJUGATE OF X_1078."""

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
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03613(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3613 = ISOTOMIC CONJUGATE OF X_1078 on reference triangle ABC."""
    X_1078 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2)*c**(2) + c**(2)*a**(2) + a**(2)*b**(2) - a**(4)))', ID="X_1078", classes=["center"])
    X_3613 = isotomic_conjugate(model, A, B, C, X_1078, ID="X_3613", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center", "incident"])
    central_line(model, X_5, X_141, 5, 141, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_160 = eval_trilinear_point(model, A, B, C, '(a*((b**(2) + c**(2))*sin(2*A) + (c**(2) - a**(2))*sin(2*B) + (b**(2) - a**(2))*sin(2*C)))', ID="X_160", classes=["center", "incident"])
    central_line(model, X_4, X_160, 4, 160, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A +  omega  )', ID="X_232", classes=["center", "incident"])
    central_line(model, X_53, X_232, 53, 232, incident=True)
    return promote_point_to_top(model, X_3613)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3613 on the given reference triangle."""
    model = create_model('X_3613 = ISOTOMIC CONJUGATE OF X_1078')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03613(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03613.json"))
    write_center_svg(
        model_acute,
        here / "x-03613.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
