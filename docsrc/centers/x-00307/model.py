"""GEOMETOR construction model for X(307) = ISOTOMIC CONJUGATE OF X(29)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    gergonne_point_of,
    isotomic_conjugate,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00307(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(307) = ISOTOMIC CONJUGATE OF X(29) on reference triangle ABC."""
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center"])
    X_307 = isotomic_conjugate(model, A, B, C, X_29, ID="X(307)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X(73)", classes=["center", "incident"])
    central_line(model, X_69, X_73, 69, 73, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_253 = eval_barycentric_point(model, A, B, C, '1/(3*a**(4) - 2*a**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2))', ID="X(253)", classes=["center", "incident"])
    central_line(model, X_8, X_253, 8, 253, incident=True)
    return promote_point_to_top(model, X_307)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(307) on the given reference triangle."""
    model = create_model('X(307) = ISOTOMIC CONJUGATE OF X(29)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00307(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00307.json"))
    write_center_svg(
        model_acute,
        here / "x-00307.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
