"""GEOMETOR construction model for X(348) = ISOTOMIC CONJUGATE OF X(281)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00348(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(348) = ISOTOMIC CONJUGATE OF X(281) on reference triangle ABC."""
    X_348 = eval_trilinear_point(model, A, B, C, 'cot(A)*(sec(A/2))**(2)', ID="X(348)", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    central_line(model, X_7, X_21, 7, 21, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X(85)", classes=["center", "incident"])
    central_line(model, X_2, X_85, 2, 85, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X(73)", classes=["center", "incident"])
    central_line(model, X_69, X_73, 69, 73, incident=True)
    return promote_point_to_top(model, X_348)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(348) on the given reference triangle."""
    model = create_model('X(348) = ISOTOMIC CONJUGATE OF X(281)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00348(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00348.json"))
    write_center_svg(
        model_acute,
        here / "x-00348.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
