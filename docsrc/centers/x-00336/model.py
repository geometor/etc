"""GEOMETOR construction model for X(336) = ISOTOMIC CONJUGATE OF X(240)."""

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
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00336(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(336) = ISOTOMIC CONJUGATE OF X(240) on reference triangle ABC."""
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A + omega )', ID="X(240)", classes=["center"])
    X_336 = isotomic_conjugate(model, A, B, C, X_240, ID="X(336)", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    central_line(model, X_48, X_75, 48, 75, incident=True)
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X(73)", classes=["center", "incident"])
    X_290 = eval_barycentric_point(model, A, B, C, 'csc(A)*sec(A + omega )', ID="X(290)", classes=["center", "incident"])
    central_line(model, X_73, X_290, 73, 290, incident=True)
    X_255 = eval_trilinear_point(model, A, B, C, '1 + cos(2*A)', ID="X(255)", classes=["center", "incident"])
    X_293 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(A + omega )', ID="X(293)", classes=["center", "incident"])
    central_line(model, X_255, X_293, 255, 293, incident=True)
    return promote_point_to_top(model, X_336)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(336) on the given reference triangle."""
    model = create_model('X(336) = ISOTOMIC CONJUGATE OF X(240)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00336(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00336.json"))
    write_center_svg(
        model_acute,
        here / "x-00336.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
