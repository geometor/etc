"""GEOMETOR construction model for X(276) = ISOGONAL CONJUGATE OF X(217)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00276(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(276) = ISOGONAL CONJUGATE OF X(217) on reference triangle ABC."""
    X_217 = point_from_barycentrics(model, A, B, C, 0.28340965, 0.39731376, 0.31927659, ID="X(217)", classes=["center"])
    X_276 = isogonal_conjugate(model, A, B, C, X_217, ID="X(276)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X(95)", classes=["center", "incident"])
    central_line(model, X_3, X_95, 3, 95, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    X_275 = eval_trilinear_point(model, A, B, C, 'csc(2*A)*sec(B - C)', ID="X(275)", classes=["center", "incident"])
    central_line(model, X_76, X_275, 76, 275, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_327 = eval_trilinear_point(model, A, B, C, 'sin(A)*csc(2*A - 2*omega )', ID="X(327)", classes=["center", "incident"])
    central_line(model, X_4, X_327, 4, 327, incident=True)
    return promote_point_to_top(model, X_276)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(276) on the given reference triangle."""
    model = create_model('X(276) = ISOGONAL CONJUGATE OF X(217)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00276(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00276.json"))
    write_center_svg(
        model_acute,
        here / "x-00276.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
