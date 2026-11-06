"""GEOMETOR construction model for X_3425 = X_2-VERTEX CONJUGATE OF X_4."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03425(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3425 = X_2-VERTEX CONJUGATE OF X_4 on reference triangle ABC."""
    X_1352 = eval_trilinear_point(model, A, B, C, 'a - 2*R*cos(B-C)*cot(omega) ', ID="X_1352", classes=["center"])
    X_3425 = isogonal_conjugate(model, A, B, C, X_1352, ID="X_3425", classes=["selected", "target"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_22, X_184, 22, 184, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A +  omega  )', ID="X_232", classes=["center", "incident"])
    central_line(model, X_32, X_232, 32, 232, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_315 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) - a**(4))', ID="X_315", classes=["center", "incident"])
    central_line(model, X_3, X_315, 3, 315, incident=True)
    return promote_point_to_top(model, X_3425)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3425 on the given reference triangle."""
    model = create_model('X_3425 = X_2-VERTEX CONJUGATE OF X_4')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03425(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03425.json"))
    write_center_svg(
        model_acute,
        here / "x-03425.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
