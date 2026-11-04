"""GEOMETOR construction model for X_1241 = ISOTOMIC CONJUGATE OF X_1194."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01241(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1241 = ISOTOMIC CONJUGATE OF X_1194 on reference triangle ABC."""
    X_1194 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) + a**(2)*b**(2) + a**(2)*c**(2)))', ID="X_1194", classes=["center"])
    X_1241 = isotomic_conjugate(model, A, B, C, X_1194, ID="X_1241", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_25, X_76, 25, 76, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_305 = eval_trilinear_point(model, A, B, C, 'b**(4)*c**(4)*cos(A)', ID="X_305", classes=["center", "incident"])
    central_line(model, X_6, X_305, 6, 305, incident=True)
    X_251 = eval_trilinear_point(model, A, B, C, 'a**(2)*csc(A +  omega  )', ID="X_251", classes=["center", "incident"])
    X_384 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) + b**(2)*c**(2))', ID="X_384", classes=["center", "incident"])
    central_line(model, X_251, X_384, 251, 384, incident=True)
    return promote_point_to_top(model, X_1241)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1241 on the given reference triangle."""
    model = create_model('X_1241 = ISOTOMIC CONJUGATE OF X_1194')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01241(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01241.json"))
    write_center_svg(
        model_acute,
        here / "x-01241.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
