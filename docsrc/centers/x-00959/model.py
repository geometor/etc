"""GEOMETOR construction model for X(959) = ISOGONAL CONJUGATE OF X(958)."""

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
    isogonal_conjugate,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00959(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(959) = ISOGONAL CONJUGATE OF X(958) on reference triangle ABC."""
    X_958 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(a**(2) + a*b + a*c + 2*b*c)', ID="X(958)", classes=["center"])
    X_959 = isogonal_conjugate(model, A, B, C, X_958, ID="X(959)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center", "incident"])
    central_line(model, X_2, X_65, 2, 65, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X(81)", classes=["center", "incident"])
    central_line(model, X_56, X_81, 56, 81, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_181 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)/(b + c - a)', ID="X(181)", classes=["center", "incident"])
    central_line(model, X_8, X_181, 8, 181, incident=True)
    return promote_point_to_top(model, X_959)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(959) on the given reference triangle."""
    model = create_model('X(959) = ISOGONAL CONJUGATE OF X(958)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00959(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00959.json"))
    write_center_svg(
        model_acute,
        here / "x-00959.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
