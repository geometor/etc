"""GEOMETOR construction model for X(309) = ISOTOMIC CONJUGATE OF X(40)."""

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


def construct_x_00309(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(309) = ISOTOMIC CONJUGATE OF X(40) on reference triangle ABC."""
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X(40)", classes=["center"])
    X_309 = isotomic_conjugate(model, A, B, C, X_40, ID="X(309)", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_189 = eval_trilinear_point(model, A, B, C, 'b*c/(cos(B) + cos(C) - cos(A) - 1)', ID="X(189)", classes=["center", "incident"])
    central_line(model, X_69, X_189, 69, 189, incident=True)
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X(85)", classes=["center", "incident"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X(264)", classes=["center", "incident"])
    central_line(model, X_85, X_264, 85, 264, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    X_280 = point_from_barycentrics(model, A, B, C, -0.15770609, -0.1827957, 1.3405018, ID="X(280)", classes=["center", "incident"])
    central_line(model, X_75, X_280, 75, 280, incident=True)
    return promote_point_to_top(model, X_309)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(309) on the given reference triangle."""
    model = create_model('X(309) = ISOTOMIC CONJUGATE OF X(40)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00309(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00309.json"))
    write_center_svg(
        model_acute,
        here / "x-00309.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
