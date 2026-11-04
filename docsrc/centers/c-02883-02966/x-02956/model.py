"""GEOMETOR construction model for X_2956 = EXCENTRAL-ISOGONAL CONJUGATE OF X_84."""

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
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02956(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2956 = EXCENTRAL-ISOGONAL CONJUGATE OF X_84 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1394 = eval_trilinear_point(model, A, B, C, '(3*a**(4) - b**(4) - c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) + 2*b**(2)*c**(2))/(a - b - c)', ID="X_1394", classes=["center"])
    X_2956 = reflection_in_point(model, X_1, X_1394, ID="X_2956", classes=["selected", "target"], guide=False)
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center", "incident"])
    central_line(model, X_1, X_84, 1, 84, incident=True)
    X_266 = eval_trilinear_point(model, A, B, C, 'sin(A/2)', ID="X_266", classes=["center", "incident"])
    X_505 = eval_trilinear_point(model, A, B, C, '(1/(sin(B/2) + sin(C/2) - sin(A/2)))', ID="X_505", classes=["center", "incident"])
    central_line(model, X_266, X_505, 266, 505, incident=True)
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_223", classes=["center", "incident"])
    X_1158 = eval_trilinear_point(model, A, B, C, 'a**(6) - b**(6) - c**(6) + b**(2)*c**(2)*(b**(2) + c**(2)) + 3*a**(2)*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2)) + 2*a*b*c*(a**(3) - b**(3) - c**(3) - a*b*c + (a**(2) + b*c)*(b + c) - a*b**(2) - a*c**(2))', ID="X_1158", classes=["center", "incident"])
    central_line(model, X_223, X_1158, 223, 1158, incident=True)
    return promote_point_to_top(model, X_2956)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2956 on the given reference triangle."""
    model = create_model('X_2956 = EXCENTRAL-ISOGONAL CONJUGATE OF X_84')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02956(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02956.json"))
    write_center_svg(
        model_acute,
        here / "x-02956.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
