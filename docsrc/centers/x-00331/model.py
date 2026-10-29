"""GEOMETOR construction model for X(331) = ISOTOMIC CONJUGATE OF X(219)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    isotomic_conjugate,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00331(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(331) = ISOTOMIC CONJUGATE OF X(219) on reference triangle ABC."""
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X(219)", classes=["center"])
    X_331 = isotomic_conjugate(model, A, B, C, X_219, ID="X(331)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_150 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4)+ c**(4)- a**(4)+ a*(b*c**(2)+c*b**(2)- b**(3)- c**(3)) - b*c*(a**(2)+ b**(2)+ c**(2)) + (b + c)*a**(3))', ID="X(150)", classes=["center", "incident"])
    central_line(model, X_4, X_150, 4, 150, incident=True)
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X(85)", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center", "incident"])
    central_line(model, X_85, X_92, 85, 92, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_286 = eval_trilinear_point(model, A, B, C, '(csc(2*A))/(sin(B) + sin(C))', ID="X(286)", classes=["center", "incident"])
    central_line(model, X_7, X_286, 7, 286, incident=True)
    return promote_point_to_top(model, X_331)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(331) on the given reference triangle."""
    model = create_model('X(331) = ISOTOMIC CONJUGATE OF X(219)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00331(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00331.json"))
    write_center_svg(
        model_acute,
        here / "x-00331.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
