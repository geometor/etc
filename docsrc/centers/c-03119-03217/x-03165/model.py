"""GEOMETOR construction model for X_3165 = X_3-CEVA CONJUGATE OF X_15."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03165(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3165 = X_3-CEVA CONJUGATE OF X_15 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_15 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /3)', ID="X_15", classes=["center"])
    X_3165 = ceva_conjugate(model, A, B, C, X_3, X_15, ID="X_3165", classes=["selected", "target"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_62 = eval_trilinear_point(model, A, B, C, 'sin(A -  pi  /6)', ID="X_62", classes=["center", "incident"])
    central_line(model, X_54, X_62, 54, 62, incident=True)
    X_16 = eval_trilinear_point(model, A, B, C, 'sin(A-  pi  /3)', ID="X_16", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_16, X_184, 16, 184, incident=True)
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X_186", classes=["center", "incident"])
    central_line(model, X_15, X_186, 15, 186, incident=True)
    return promote_point_to_top(model, X_3165)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3165 on the given reference triangle."""
    model = create_model('X_3165 = X_3-CEVA CONJUGATE OF X_15')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03165(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03165.json"))
    write_center_svg(
        model_acute,
        here / "x-03165.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
