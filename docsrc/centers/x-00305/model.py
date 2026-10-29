"""GEOMETOR construction model for X(305) = ISOTOMIC CONJUGATE OF X(25)."""

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
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00305(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(305) = ISOTOMIC CONJUGATE OF X(25) on reference triangle ABC."""
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center"])
    X_305 = isotomic_conjugate(model, A, B, C, X_25, ID="X(305)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    central_line(model, X_2, X_39, 2, 39, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X(22)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_22, X_99, 22, 99, incident=True)
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X(95)", classes=["center", "incident"])
    X_183 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*cos(A- omega )', ID="X(183)", classes=["center", "incident"])
    central_line(model, X_95, X_183, 95, 183, incident=True)
    return promote_point_to_top(model, X_305)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(305) on the given reference triangle."""
    model = create_model('X(305) = ISOTOMIC CONJUGATE OF X(25)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00305(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00305.json"))
    write_center_svg(
        model_acute,
        here / "x-00305.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
