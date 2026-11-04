"""GEOMETOR construction model for X_1065 = ISOGONAL CONJUGATE OF X_1064."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01065(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1065 = ISOGONAL CONJUGATE OF X_1064 on reference triangle ABC."""
    X_1064 = eval_trilinear_point(model, A, B, C, '(1 + cos(A)*(cos(B) + cos(C)))', ID="X_1064", classes=["center"])
    X_1065 = isogonal_conjugate(model, A, B, C, X_1064, ID="X_1065", classes=["selected", "target"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_102, X_226, 102, 226, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_388 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) + (b + c)**(2))/(b + c - a)', ID="X_388", classes=["center", "incident"])
    central_line(model, X_3, X_388, 3, 388, incident=True)
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center", "incident"])
    central_line(model, X_284, X_515, 284, 515, incident=True)
    return promote_point_to_top(model, X_1065)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1065 on the given reference triangle."""
    model = create_model('X_1065 = ISOGONAL CONJUGATE OF X_1064')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01065(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01065.json"))
    write_center_svg(
        model_acute,
        here / "x-01065.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
