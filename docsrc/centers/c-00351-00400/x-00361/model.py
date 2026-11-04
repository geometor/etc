"""GEOMETOR construction model for X_361 = X_266-CEVA CONJUGATE OF X_1."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00361(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_361 = X_266-CEVA CONJUGATE OF X_1 on reference triangle ABC."""
    X_266 = eval_trilinear_point(model, A, B, C, 'sin(A/2)', ID="X_266", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_361 = ceva_conjugate(model, A, B, C, X_266, X_1, ID="X_361", classes=["selected", "target"])
    X_188 = eval_trilinear_point(model, A, B, C, 'csc(A/2)', ID="X_188", classes=["center", "incident"])
    central_line(model, X_1, X_188, 1, 188, incident=True)
    X_164 = eval_trilinear_point(model, A, B, C, 'sin(B/2) + sin(C/2) - sin(A/2)', ID="X_164", classes=["center", "incident"])
    X_503 = eval_trilinear_point(model, A, B, C, '(sec(B/2) + sec(C/2) - sec(A/2))', ID="X_503", classes=["center", "incident"])
    central_line(model, X_164, X_503, 164, 503, incident=True)
    X_978 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c) + a*(b**(2) - b*c + c**(2)) - b*c*(b + c)', ID="X_978", classes=["center", "incident"])
    central_line(model, X_266, X_978, 266, 978, incident=True)
    return promote_point_to_top(model, X_361)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_361 on the given reference triangle."""
    model = create_model('X_361 = X_266-CEVA CONJUGATE OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00361(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00361.json"))
    write_center_svg(
        model_acute,
        here / "x-00361.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
