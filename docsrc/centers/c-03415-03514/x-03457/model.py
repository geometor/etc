"""GEOMETOR construction model for X_3457 = X_13-VERTEX CONJUGATE OF X_15."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03457(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3457 = X_13-VERTEX CONJUGATE OF X_15 on reference triangle ABC."""
    X_298 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A +  pi  /3)', ID="X_298", classes=["center"])
    X_3457 = isogonal_conjugate(model, A, B, C, X_298, ID="X_3457", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /3)', ID="X_13", classes=["center", "incident"])
    central_line(model, X_2, X_13, 2, 13, incident=True)
    X_62 = eval_trilinear_point(model, A, B, C, 'sin(A -  pi  /6)', ID="X_62", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_62, X_110, 62, 110, incident=True)
    X_300 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*csc(A +  pi  /3)', ID="X_300", classes=["center", "incident"])
    X_308 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b**(2) + c**(2))', ID="X_308", classes=["center", "incident"])
    central_line(model, X_300, X_308, 300, 308, incident=True)
    return promote_point_to_top(model, X_3457)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3457 on the given reference triangle."""
    model = create_model('X_3457 = X_13-VERTEX CONJUGATE OF X_15')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03457(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03457.json"))
    write_center_svg(
        model_acute,
        here / "x-03457.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
