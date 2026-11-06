"""GEOMETOR construction model for X_1305 = COLLINGS TRANSFORM OF X_440."""

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
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01305(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1305 = COLLINGS TRANSFORM OF X_440 on reference triangle ABC."""
    X_917 = eval_trilinear_point(model, A, B, C, '(sec(A))/((a - b)*sin(2*B) + (a - c)*sin(2*C))', ID="X_917", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_1305 = reflection_in_point(model, X_917, X_3, ID="X_1305", classes=["selected", "target"], guide=False)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    central_line(model, X_20, X_103, 20, 103, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    X_347 = eval_trilinear_point(model, A, B, C, '((-1 - cos(A) + cos(B) + cos(C))*(sec(A/2))**(2))', ID="X_347", classes=["center", "incident"])
    central_line(model, X_106, X_347, 106, 347, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_675 = eval_trilinear_point(model, A, B, C, '(b*c/(b**(3) + c**(3) - a*(b**(2) + c**(2))))', ID="X_675", classes=["center", "incident"])
    central_line(model, X_22, X_675, 22, 675, incident=True)
    return promote_point_to_top(model, X_1305)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1305 on the given reference triangle."""
    model = create_model('X_1305 = COLLINGS TRANSFORM OF X_440')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01305(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01305.json"))
    write_center_svg(
        model_acute,
        here / "x-01305.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
