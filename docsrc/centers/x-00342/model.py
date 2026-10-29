"""GEOMETOR construction model for X(342) = ISOTOMIC CONJUGATE OF X(271)."""

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


def construct_x_00342(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(342) = ISOTOMIC CONJUGATE OF X(271) on reference triangle ABC."""
    X_271 = eval_trilinear_point(model, A, B, C, '(cot(A)*cot(A/2))/(-1 - cos(A) + cos(B) + cos(C))', ID="X(271)", classes=["center"])
    X_342 = isotomic_conjugate(model, A, B, C, X_271, ID="X(342)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_4, X_7, 4, 7, incident=True)
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X(226)", classes=["center", "incident"])
    central_line(model, X_92, X_226, 92, 226, incident=True)
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X(85)", classes=["center", "incident"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X(264)", classes=["center", "incident"])
    central_line(model, X_85, X_264, 85, 264, incident=True)
    return promote_point_to_top(model, X_342)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(342) on the given reference triangle."""
    model = create_model('X(342) = ISOTOMIC CONJUGATE OF X(271)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00342(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00342.json"))
    write_center_svg(
        model_acute,
        here / "x-00342.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
