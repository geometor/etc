"""GEOMETOR construction model for X_3466 = ISOGONAL CONJUGATE OF X_3465."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03466(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3466 = ISOGONAL CONJUGATE OF X_3465 on reference triangle ABC."""
    X_3465 = point_from_barycentrics(model, A, B, C, 2.7525253, 2.4545455, -4.2070707, ID="X_3465", classes=["center"])
    X_3466 = isogonal_conjugate(model, A, B, C, X_3465, ID="X_3466", classes=["selected", "target"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    X_1330 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2)/(a + c) + c**(2)/(a + b) - a**(2)/(b + c)))', ID="X_1330", classes=["center", "incident"])
    central_line(model, X_78, X_1330, 78, 1330, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_1807 = eval_trilinear_point(model, A, B, C, '1/(2 - sec(A))', ID="X_1807", classes=["center", "incident"])
    central_line(model, X_30, X_1807, 30, 1807, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_1794 = point_from_barycentrics(model, A, B, C, 0.46882064, 0.38927507, 0.14190429, ID="X_1794", classes=["center", "incident"])
    central_line(model, X_109, X_1794, 109, 1794, incident=True)
    return promote_point_to_top(model, X_3466)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3466 on the given reference triangle."""
    model = create_model('X_3466 = ISOGONAL CONJUGATE OF X_3465')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03466(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03466.json"))
    write_center_svg(
        model_acute,
        here / "x-03466.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
