"""GEOMETOR construction model for X_3197 = X_40-CEVA CONJUGATE OF X_55."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03197(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3197 = X_40-CEVA CONJUGATE OF X_55 on reference triangle ABC."""
    X_3197 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(6) - 2*a**(5)*b - a**(4)*b**(2) + 4*a**(3)*b**(3) - a**(2)*b**(4) - 2*a*b**(5) + b**(6) - 2*a**(5)*c - 2*a**(4)*b*c + 2*a*b**(4)*c + 2*b**(5)*c - a**(4)*c**(2) + 2*a**(2)*b**(2)*c**(2) - b**(4)*c**(2) + 4*a**(3)*c**(3) - 4*b**(3)*c**(3) - a**(2)*c**(4) + 2*a*b*c**(4) - b**(2)*c**(4) - 2*a*c**(5) + 2*b*c**(5) + c**(6))', ID="X_3197", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_6, X_19, 6, 19, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_48, X_55, 48, 55, incident=True)
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    central_line(model, X_64, X_71, 64, 71, incident=True)
    return promote_point_to_top(model, X_3197)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3197 on the given reference triangle."""
    model = create_model('X_3197 = X_40-CEVA CONJUGATE OF X_55')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03197(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03197.json"))
    write_center_svg(
        model_acute,
        here / "x-03197.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
