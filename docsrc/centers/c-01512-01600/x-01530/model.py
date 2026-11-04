"""GEOMETOR construction model for X_1530 = ORTHOJOIN OF X_31."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    nagel_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01530(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1530 = ORTHOJOIN OF X_31 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_118 = point_from_barycentrics(model, A, B, C, 0.28918651, -0.056547619, 0.76736111, ID="X_118", classes=["center"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center"])
    central_line(model, X_4, X_8, 4, 8)
    central_line(model, X_118, X_516, 118, 516)
    X_1530 = intersect_lines(model, X_4, X_8, X_118, X_516, ID="X_1530", classes=["selected", "target"])
    X_152 = eval_barycentric_point(model, A, B, C, 'a**(8) - a**(7)*(b + c) + a**(6)*(2*b**(2) + b*c + 2*c**(2)) - a**(5)*(5*b**(3) - b**(2)*c - b*c**(2) + 5*c**(3)) - a**(4)*b*c*(b**(2) - 6*b*c + c**(2)) + a**(3)*(5*b**(5) + b**(4)*c - 6*b**(3)*c**(2) - 6*b**(2)*c**(3) + b*c**(4) + 5*c**(5)) - a**(2)*(2*b**(6) + b**(5)*c + 2*b**(4)*c**(2) - 10*b**(3)*c**(3) + 2*b**(2)*c**(4) + b*c**(5) + 2*c**(6)) + a*(b**(7) - b**(6)*c - 3*b**(5)*c**(2) + 3*b**(4)*c**(3) + 3*b**(3)*c**(4) - 3*b**(2)*c**(5) - b*c**(6) + c**(7)) - b**(8) + b**(7)*c + 2*b**(6)*c**(2) - b**(5)*c**(3) - 2*b**(4)*c**(4) - b**(3)*c**(5) + 2*b**(2)*c**(6) + b*c**(7) - c**(8)', ID="X_152", classes=["center", "incident"])
    X_971 = eval_trilinear_point(model, A, B, C, 'a**(4)*(b + c) - 2*a**(3)*(b**(2) + c**(2) - b*c) + 2*a*(b - c)**(2)*(b**(2) + c**(2) + b*c) - (b - c)**(2)*(b + c)**(3)', ID="X_971", classes=["center", "incident"])
    central_line(model, X_152, X_971, 152, 971, incident=True)
    return promote_point_to_top(model, X_1530)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1530 on the given reference triangle."""
    model = create_model('X_1530 = ORTHOJOIN OF X_31')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01530(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01530.json"))
    write_center_svg(
        model_acute,
        here / "x-01530.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
